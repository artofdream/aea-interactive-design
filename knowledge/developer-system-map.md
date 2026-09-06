---
title: Developer system map
nav: Quantic
---

# Café Fausse — developer system map

Plain-English map of the restaurant app a software developer needs to orient fast.  
**Live tip (MSAIE staging):** `cafe.artof.link` @ `73d202d` · same React → Flask → Postgres design locally and on staging.

**Honesty locks:** on-box Postgres (not shared RDS) · no `/api/gallery` · newsletter store-only unless SES env is set · fail-closed if DB is down · on camera say **MSAIE staging**.

---

## 1. Stack, versions, rationale

| Layer | What | Version (pinned / observed) | Why |
| --- | --- | --- | --- |
| Frontend | React + JSX | React/ReactDOM **^18.3.1** | SPA pages for SRS surface |
| Routing | react-router-dom | **^6.28.0** | Client routes |
| Build | Vite + @vitejs/plugin-react | Vite **^5.4.11**, plugin **^4.3.4** | Fast local FE; production build served by Flask/Caddy |
| Backend | Flask + gunicorn | Flask **3.1.3** (range ≥3&lt;4), gunicorn **23.0.0** (≥22&lt;24) | Thin HTTP API + static SPA |
| DB driver | psycopg2-binary | **2.9.12** (≥2.9&lt;3) | Postgres access |
| CORS | flask-cors | **5.0.1** (≥4&lt;6) | Vite localhost in local dev; staging same-origin via Caddy |
| Optional mail | boto3 | **1.43.89** (≥1.34&lt;2) | Present; unused when SES env unset |
| Runtime | Python | **3.12.14** on staging box | App runtime |
| Staging edge | Caddy | **Caddy:2** | TLS + reverse proxy |
| Database | PostgreSQL | **postgres:16** compose service | On-box data store |

**Rationale (short):** one freeze file for official copy; React for the public UX; Flask in the middle; Postgres for bookings/customers with fail-closed writes; staging proves the same design over HTTPS without claiming forever hosting.

---

## 2. Frontend / backend segmentation

```
Browser (React SPA)
  ├── Pages from freeze.json (Home, Menu, About, Gallery static images)
  ├── Reservations / Newsletter forms → fetch API
  └── /operator → read-only demo snapshot
         │
         ▼
Flask API (+ built SPA assets)
  ├── /api/* JSON
  ├── /images/<file> allowlisted gallery assets
  └── /unsubscribe HTML
         │
         ▼
PostgreSQL (on-box)
  ├── customers
  └── reservations  UNIQUE(time_slot, table_number)
```

| Side | Owns | Does not own |
| --- | --- | --- |
| **Frontend** | Routes, forms, freeze display, gallery lightbox UI | Business rules for capacity / DB honesty |
| **Backend** | Slots, reservations, newsletter store, fail-closed, freeze JSON APIs | Inventing menu/gallery copy outside freeze |
| **DB** | Customers + reservations integrity | Frontend state |

**SPA routes:** `/` · `/menu` · `/reservations` · `/about` · `/gallery` · `/operator`  
Gallery = FE page + static `/images/…` — **not** an API resource.

---

## 3. API endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/health` | Liveness; DB ping → `{ok:true}` |
| GET | `/api/menu` | Official menu from freeze |
| GET | `/api/site` | Site/awards/reviews/… from freeze |
| GET | `/api/slots?date=YYYY-MM-DD` | Slots for date (400 without date) |
| GET | `/api/availability?time_slot=` | Remaining tables / fully_booked |
| POST | `/api/reservations` | Create booking (GET → 404) |
| POST | `/api/newsletter` | Store signup FR-15/16 (GET → 404) |
| GET/POST | `/api/newsletter/unsubscribe` | Future unsubscribe |
| GET | `/unsubscribe` | HTML unsubscribe page |
| GET | `/api/operator` | Demo snapshot only — **not** a product FR |
| GET | `/images/<file>` | Basename-allowlisted images |
| — | `/api/gallery` | **Does not exist (404)** |

---

## 4. DB schema (`backend/schema.sql`)

### `customers`
- `customer_id`, `customer_name`, `email_address` **UNIQUE**, `phone_number`
- `newsletter_signup`, `created_at` / `updated_at`

### `reservations`
- `reservation_id`, `customer_id` FK → customers
- `time_slot` TIMESTAMPTZ, `table_number` 1–30, `guest_count` 1–20, `created_at`
- **UNIQUE** `(time_slot, table_number)` — one table per slot (capacity honesty)

---

## 5. Methods / modules overview (developer map)

Not every helper — the map:

| Area | Where to look | Role |
| --- | --- | --- |
| Freeze source | `shared/freeze.json` | Menu, hours, awards, reviews, site copy |
| FE pages | `frontend/src/…` (route pages) | Render freeze + forms |
| HTTP client calls | FE reservation/newsletter forms | `fetch` to `/api/*` |
| Flask app / routes | `backend/` app factory + blueprints/routes | Wire HTTP → services |
| Slot / booking logic | backend reservation/slot modules | Random table 1–30, uniqueness, full-slot errors |
| Newsletter store | backend newsletter path | Validate/normalize email; store; skip SES if unset |
| Fail-closed | DB access + tests | Missing/unreachable DB → honest error, no fake success |
| Operator snapshot | `/api/operator` | Read-only recording helper |
| CI freeze lock | `test_freeze.py` (and related) | Fail if freeze copy drifts |

---

## 6. Event / listener map (runtime)

**There is no app event bus, WebSocket, or server-sent event stream.**

Runtime is classic **request/response**:

| Actor | “Event” | What happens |
| --- | --- | --- |
| User | Click nav / open page | React Router renders; freeze data from FE bundle and/or `/api/menu` `/api/site` |
| User | Pick date on reservations | `GET /api/slots?date=` |
| User | Check / submit booking | `GET /api/availability` · `POST /api/reservations` |
| User | Newsletter submit | `POST /api/newsletter` → store; email delivery skipped if SES unset |
| User | Gallery | Client UI + `GET /images/…` only |
| Browser | Page load | Same-origin to staging via Caddy; local Vite may use CORS to Flask |

Staging CORS: same-origin behind Caddy. Local: CORS allows Vite localhost in code.

---

## 7. Local (dev) vs MSAIE staging (same design)

| | Local (dev) | MSAIE staging |
| --- | --- | --- |
| URL | Vite + local Flask on developer machine | `https://cafe.artof.link/` |
| FE | Vite hot reload | Built SPA |
| Edge | — | Caddy:2 TLS |
| DB | Local Postgres | Compose **postgres:16** on the instance |
| Purpose | Iterate without touching the shared demo | Shared HTTPS proof for graders/team |

---

## 8. Gotchas checklist

1. **No `/api/gallery`** — gallery is SPA + `/images/…`.
2. **Newsletter grade floor = store-only** until SES env is set (`email_delivery.status=skipped` when unset).
3. **On-box Postgres only** — not shared RDS.
4. **Fail-closed** if DB missing/unreachable (no pretend writes).
5. **No event-bus** — HTTP only.
6. `/api/operator` is demo/recording helper, not a new FR.
7. On camera: **MSAIE staging**, not Lightsail jargon.

---

*Sources: App inventory tip `73d202d`; `backend/schema.sql`; frontend routes; Flask API routes; compose stack. Unknown until probed stays labeled if anything drifts after tip.*

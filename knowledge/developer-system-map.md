# Café Fausse — developer system map

Plain-English map of the restaurant app a software developer needs to orient fast.  
**Inventory tip:** App `73d202d` (New Bot stack / API / schema / FE/BE cut). Same React → Flask → Postgres design locally and on staging.

**Related:** [Stack](stack.md) · [Local vs AWS](part3-local-vs-aws.md) · [Part 4 coding overview](part4-coding-overview.md) · [Quantic](quantic.md) · [Honesty](honesty.md) · [SRS freeze](srs.md)

**Honesty locks:** **Local (dev)** + **Docker** `cafe-pg` (`postgres:16`) · **on-box Postgres** on MSAIE staging (not a shared RDS; no AEA RDS / florist) · no `/api/gallery` · newsletter **store-only** unless SES env is set · **fail-closed** if DB is down · on camera say **MSAIE staging** · **HTTP only** (no event bus).

---

## 1. Stack, versions, rationale

New Bot inventory at tip `73d202d` (pinned range + observed install). Do not treat a hostname as a version probe.

| Layer | What | Version (pinned / observed) | Why |
| --- | --- | --- | --- |
| Frontend | React + JSX | React/ReactDOM **^18.3.1** | SPA pages for SRS surface |
| Routing | react-router-dom | **^6.28.0** | Client routes |
| Build | Vite + @vitejs/plugin-react | Vite **^5.4.11**, plugin **^4.3.4** | Fast local FE; production build served by Flask/Caddy |
| Backend | Flask + gunicorn | Flask **3.1.3** (range ≥3&lt;4), gunicorn **23.0.0** (≥22&lt;24) | Thin HTTP API + static SPA |
| DB driver | psycopg2-binary | **2.9.12** (≥2.9&lt;3) | Postgres access |
| CORS | flask-cors | **5.0.1** (≥4&lt;6) | Vite `5173` → Flask when not same-origin; staging same-origin via Caddy |
| Optional mail | boto3 | **1.43.89** (≥1.34&lt;2) | Present; unused when SES env unset |
| Runtime | Python | **3.12.14** on staging box | App runtime |
| Staging edge | Caddy | **Caddy:2** | TLS + reverse proxy |
| Database | PostgreSQL | **postgres:16** | On-box data store (Docker locally; on-box on staging) |

**Rationale (short):** one freeze file for official copy; React for the public UX; Flask in the middle; Postgres for bookings/customers with fail-closed writes; staging proves the same design over HTTPS without claiming forever hosting.

---

## 2. Frontend / backend segmentation

```
Browser (React SPA)
  ├── Home / Menu / About / Gallery — import shared/freeze.json (not GET /api/menu)
  ├── Reservations / Newsletter forms → fetch /api/*
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
Gallery = FE page + static `/images/…` — **not** an API resource. **`/api/gallery` does not exist.**

---

## 3. API endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/health` | Liveness; DB ping → `{ok:true}` |
| GET | `/api/menu` | Official menu from freeze (exposed; public pages import freeze) |
| GET | `/api/site` | Site/awards/reviews/… from freeze (exposed; public pages import freeze) |
| GET | `/api/slots?date=YYYY-MM-DD` | Slots for date (400 without date) |
| GET | `/api/availability?time_slot=` | Remaining tables / fully_booked |
| POST | `/api/reservations` | Create booking (GET → 404) |
| POST | `/api/newsletter` | Store signup **FR-15** / **FR-16** (GET → 404) |
| GET/POST | `/api/newsletter/unsubscribe` | Future [#135](https://github.com/artofdream/aea-interactive-design/issues/135) unsubscribe — not a new FR |
| GET | `/unsubscribe` | HTML unsubscribe page |
| GET | `/api/operator` | Demo snapshot only — **not** a product FR / **not FR-19** |
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

No AEA RDS schema. No florist tables. Staging DB is **on-box Postgres (MSAIE staging)** — not a shared RDS.

---

## 5. Methods / modules overview (developer map)

Not every helper — the map:

| Area | Where to look | Role |
| --- | --- | --- |
| Freeze source | `shared/freeze.json` | Menu, hours, awards, reviews, site copy |
| FE pages | `frontend/src/pages/` | Render freeze + forms |
| HTTP client calls | Reservations + `NewsletterForm` | `fetch` to `/api/slots` then `/api/reservations`; `POST /api/newsletter` |
| Flask app / routes | `backend/cafe_fausse/__init__.py` | Wire HTTP → services |
| Slot / booking logic | `slots.py` · `reservations.py` | Random table 1–30, uniqueness, full-slot errors |
| Newsletter store | `newsletter.py` | Validate/normalize email; store; skip SES if unset |
| Fail-closed | `db.py` + `test_fail_closed.py` | Missing/unreachable DB → honest error, no fake success |
| Operator snapshot | `/api/operator` | Read-only recording helper |
| CI freeze lock | `test_freeze.py` (and related) | Fail if freeze copy drifts |

---

## 6. Event / listener map (runtime)

**There is no app event bus, WebSocket, or server-sent event stream.** Runtime is classic **HTTP request/response** only.

| Actor | “Event” | What happens |
| --- | --- | --- |
| User | Click nav / open page | React Router renders; static pages import `freeze.json` |
| User | Pick date on reservations | `GET /api/slots?date=` |
| User | Check / submit booking | `GET /api/availability` · `POST /api/reservations` |
| User | Newsletter submit | `POST /api/newsletter` → store; `email_delivery.status=skipped` if SES unset |
| User | Gallery | Client UI + `GET /images/…` only — no `/api/gallery` |
| Browser | Page load | Staging: same-origin behind Caddy. Local (dev): Vite proxies `/api` and `/images` to Flask (`:5000`); CORS also allows `5173` |

---

## 7. Local (dev) + Docker vs MSAIE staging (same design)

Do **not** call the product “cts-ai”. That name is a developer box, not the stack.

| | **Local (dev)** | **Docker (local Postgres)** | **MSAIE staging** |
| --- | --- | --- | --- |
| URL | Vite `http://127.0.0.1:5173` + Flask `:5000` | `cafe-pg` on `127.0.0.1:5432` | `https://cafe.artof.link/` |
| FE | Vite hot reload (proxies `/api` + `/images`) | — | Built SPA |
| Edge | — | — | Caddy:2 TLS |
| DB | App points at `DATABASE_URL` | `docker run … postgres:16` (`cafe-pg`) **or** a local Postgres install | **On-box Postgres (MSAIE staging)** — not a shared RDS |
| Purpose | Iterate without touching the shared demo | Give local Flask a real Postgres | Shared HTTPS proof for graders/team |

Same design on both deploy targets: **React + JSX → Flask → PostgreSQL**. Fail-closed without a database. Newsletter is **store-only** until SES env is set. On camera: **cafe.artof.link** = **MSAIE staging** (temporary — not production forever). Deploy table: [Local vs AWS](part3-local-vs-aws.md).

---

## 8. Gotchas checklist

1. **No `/api/gallery`** — gallery is SPA + `/images/…`.
2. **Newsletter grade floor = store-only** until SES env is set (`email_delivery.status=skipped` when unset). Not a Coverage send claim.
3. **On-box Postgres only** on staging — not a shared RDS; no AEA RDS / florist.
4. **Fail-closed** if DB missing/unreachable (no pretend writes). Full slot (30 tables) → honest error (**FR-9**).
5. **No event bus** — HTTP only.
6. `/api/operator` is a demo/recording helper, **not FR-19**.
7. On camera: **MSAIE staging**, not Lightsail jargon.
8. **Local (dev) + Docker** — Docker here is `postgres:16` as `cafe-pg` (or a local install). Not the product name.

---

*Sources: New Bot App inventory tip `73d202d`; `backend/schema.sql`; `frontend/src/pages/`; Flask routes in `backend/cafe_fausse/`; README Docker `cafe-pg`. Unknown until probed stays labeled if anything drifts after tip. [Parts 3–5 materials](parts-345-materials.md) · [Handoff mapping](parts-345-handoff-mapping.md) (not spoken on camera).*

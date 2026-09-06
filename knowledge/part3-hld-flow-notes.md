# Part 3 — HLD + Meghna FE/BE flow (architect cut)

**Audience:** Architecture talk (Part 3 NATURAL) · on-camera slides.  
**Palette:** match `hld-as-is.svg` — bg `#f6f1e8`, panels `#fffdf8`, accent `#7a2e1f`, muted `#5e574d`, box `#efeae1`, Georgia + ui-monospace.  
**Label:** PROTOTYPE visuals · not Quantic submit.  
**Routes:** from `aea-interactive-design` `main` Flask factory (`backend/cafe_fausse/__init__.py`).

These three **replace / augment** older `hld-as-is` / `hld-aws-staging` for the architect cut (local vs MSAIE staging + Meghna FE/BE path). Older SVGs kept for probe history.

---

## Index

| # | File | Title | Spoken cue (one line) |
| ---: | --- | --- | --- |
| 1 | `hld-local.svg` · `hld-local-720.png` | **Local setup (dev) — HLD** | “Local on the developer machine — Vite, Flask, Postgres — iterate without touching the shared demo.” |
| 2 | `hld-aws-msaie.svg` · `hld-aws-msaie-720.png` | **MSAIE staging — HLD** (`cafe.artof.link`) | “MSAIE staging at cafe.artof.link — same design, shared HTTPS proof. Knowledge is a separate hostname.” |
| 3 | `flow-meghna-fe-be.svg` · `flow-meghna-fe-be-720.png` | **Meghna demo path — frontend / backend** | “What Meghna clicks vs what hits Flask — static pages from freeze; booking through slots and reservations.” |
| 4 | `flow-coding-overview.svg` · `flow-coding-overview-720.png` | **Coding overview** (Part 4) | “Forms → API → modules → Postgres. Freeze for static pages; booking through slots + reservations.” |

---

## Diagram 1 — Local (`hld-local`)

- **cts-ai** box: Frontend (Vite / React+JSX) → Backend (Flask `:5000`) → Data (local PostgreSQL).
- **freeze.json** shared config under both FE + API.
- Backend box lists key routes: `/api/health`, `/api/menu`, `/api/site`, `/api/slots`, `/api/availability`, `POST /api/reservations`, `POST /api/newsletter`, `GET /api/operator` (helper).
- Fail-closed without DB; full book → 409.
- Label: coding & iteration — **not** the shared demo URL.

---

## Diagram 2 — MSAIE staging (`hld-aws-msaie`)

- Speakable title: **MSAIE staging** (not “weekend Lightsail”).
- App path: Browser → DNS/TLS → Flask+built SPA → **on-box Postgres (not AEA RDS)**.
- Knowledge Pages column: `knowledge.cafe.artof.link` — two hostnames, two jobs.
- Backend box lists the same key API routes as local.
- Small ops line (off-camera-honest): DNS → TLS → Flask+SPA → on-box PG · tip `73d202d`.
- Out of cut (dashed): AEA RDS · ELB wildcard · permanent hosting Future.
- Newsletter: store-only.

---

## Diagram 3 — Meghna FE / BE (`flow-meghna-fe-be`)

**Click path:** Home → Gallery → Menu → Reservations (+ newsletter optional).

| Step | Frontend | Hits Flask? | Data |
| --- | --- | --- | --- |
| Home / Gallery / Menu | React pages | **No** `/api/menu` from FE — `@shared/freeze.json` (+ menu-presentation) at build | freeze · images via `GET /images/…` |
| Reservations | Booking form | **GET** `/api/slots?date=` → **POST** `/api/reservations` | Postgres customers/reservations · 409 if full |
| Newsletter (optional) | Footer form | **POST** `/api/newsletter` | Postgres store-only |
| Operator | not Meghna path | **GET** `/api/operator` | read-only helper |

**Legend on diagram:** full Flask surface (`/api/health`, `/api/menu`, `/api/site`, …) so Architecture can point at exposed routes without inventing FE arrows.

Ends with **Handoff → Architecture (Part 3)**.

---

## Flask routes (main) — quick legend

| Method | Path | Role |
| --- | --- | --- |
| GET | `/api/health` | DB ping |
| GET | `/api/menu` | freeze menu (API; FE Menu page imports freeze) |
| GET | `/api/site` | freeze site fields |
| GET | `/api/slots?date=` | reservation slots |
| GET | `/api/availability` | remaining tables |
| POST | `/api/reservations` | create · 409 full · fail-closed |
| POST | `/api/newsletter` | store-only until SES |
| GET\|POST | `/api/newsletter/unsubscribe` | unsubscribe API |
| GET | `/unsubscribe` | unsubscribe page |
| GET | `/api/operator` | read-only helper |
| GET | `/images/<path>` | allowlisted images |
| GET | `/` · `/<path>` | SPA catch-all |

No FR/NFR IDs on the diagrams.

---

## Related docs

- [`PART3-LOCAL-VS-AWS.md`](PART3-LOCAL-VS-AWS.md) — local vs MSAIE staging table  
- [`PART3-VARIANT-B-SCRIPT-NATURAL.md`](PART3-VARIANT-B-SCRIPT-NATURAL.md) — diagram callouts  
- [`PARTS-345-MATERIALS.md`](PARTS-345-MATERIALS.md) — pack index  
- Older: `hld-as-is.svg`, `hld-aws-staging.svg` (probe / history)

---

---

## Part 4 companion — coding overview

| File | Title | Spoken cue |
| --- | --- | --- |
| `flow-coding-overview.svg` · `flow-coding-overview-720.png` | **Coding overview** — forms · functions · FE · BE · API · DB | “Pages/forms → Flask → modules → Postgres. Freeze for static pages; slots + reservations for booking.” |

Detail: [`PART4-CODING-OVERVIEW.md`](PART4-CODING-OVERVIEW.md). Maps to the Architecture flow (Part 3) with coding-layer labels.


*Packed 2026-09-06 Europe/Oslo · PROTOTYPE · architect cut HLD trio + Meghna FE/BE honesty (freeze vs API).*

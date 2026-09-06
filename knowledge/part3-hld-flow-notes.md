# Part 3 — HLD + Meghna FE/BE flow (architect cut)

**Audience:** Architecture talk (Part 3 NATURAL) · on-camera slides.  
**Label:** **PROTOTYPE** visuals · not Quantic submit. No FR/NFR IDs on the diagrams.  
**On camera:** **cafe.artof.link** = **MSAIE staging** (temporary — not production forever). Avoid “weekend Lightsail.”  
**Prefer these** for the architect dual-env cut. Older [as-is HLD](assets/hld-as-is.svg) / [AWS staging HLD](assets/hld-aws-staging.svg) stay on [Stack](stack.md) as **history / probe archive**.

Folded into [Stack](stack.md). Deploy table: [Local vs AWS](part3-local-vs-aws.md). Pack index: [Parts 3–5 materials](parts-345-materials.md). Part 4 companion: [Coding overview](part4-coding-overview.md). ID map: [Handoff mapping](parts-345-handoff-mapping.md) — **not spoken on camera**.

---

## Honesty (diagrams)

- **MSAIE staging** at `cafe.artof.link` on camera. Off-camera ops (Lightsail / Caddy / tip `73d202d`) live on [Local vs AWS](part3-local-vs-aws.md).
- **Home / Gallery / Menu** read the **freeze** at build (`@shared/freeze.json`). They do **not** call `GET /api/menu` from the frontend.
- **Booking** = `GET /api/slots?date=` then `POST /api/reservations`. Full book → 409. Fail-closed without Postgres.
- **Newsletter** = `POST /api/newsletter` **store-only** (do not claim outbound SES).
- Staging database is **on-box Postgres**, not AEA RDS.
- These SVGs are **PROTOTYPE** visuals — not the Quantic submit film.

---

## Index

| # | Visual | Title | Spoken cue (one line) |
| ---: | --- | --- | --- |
| 1 | [SVG](assets/hld-local.svg) · [720 PNG](assets/hld-local-720.png) | **Local setup (dev) — HLD** | “Local on the developer machine — Vite, Flask, Postgres — iterate without touching the shared demo.” |
| 2 | [SVG](assets/hld-aws-msaie.svg) · [720 PNG](assets/hld-aws-msaie-720.png) | **MSAIE staging — HLD** (`cafe.artof.link`) | “MSAIE staging at cafe.artof.link — same design, shared HTTPS proof. Knowledge is a separate hostname.” |
| 3 | [SVG](assets/flow-meghna-fe-be.svg) · [720 PNG](assets/flow-meghna-fe-be-720.png) | **Meghna demo path — frontend / backend** | “What Meghna clicks vs what hits Flask — static pages from freeze; booking through slots and reservations.” |
| 4 | [SVG](assets/flow-coding-overview.svg) · [720 PNG](assets/flow-coding-overview-720.png) | **Coding overview** (Part 4) | “Forms → API → modules → Postgres. Freeze for static pages; booking through slots + reservations.” |

---

## 1. Local (`hld-local`)

cts-ai box: Frontend (Vite / React+JSX) → Backend (Flask `:5000`) → Data (local PostgreSQL). `freeze.json` sits under both FE and API. Fail-closed without DB; full book → 409. Coding and iteration — **not** the shared demo URL.

![Local setup (dev): Vite React frontend, Flask API with key routes, local PostgreSQL, shared freeze.json. Fail-closed without DB. Not the shared demo URL.](assets/hld-local.svg)

Fallback raster: [hld-local-720.png](assets/hld-local-720.png).

---

## 2. MSAIE staging (`hld-aws-msaie`)

Speakable title: **MSAIE staging** at `cafe.artof.link`. Browser → DNS/TLS → Flask + built SPA → **on-box Postgres (not AEA RDS)**. Knowledge Pages (`knowledge.cafe.artof.link`) is a separate column — two hostnames, two jobs. Same key API routes as local. Newsletter **store-only**. Dashed / out of cut: AEA RDS · ELB wildcard · permanent hosting (Future). Off-camera ops line: tip `73d202d`.

![MSAIE staging at cafe.artof.link: Knowledge Pages separate; browser to DNS/TLS to Flask+SPA to on-box Postgres. AEA RDS and ELB wildcard out of cut. Newsletter store-only.](assets/hld-aws-msaie.svg)

Fallback raster: [hld-aws-msaie-720.png](assets/hld-aws-msaie-720.png).

---

## 3. Meghna FE / BE (`flow-meghna-fe-be`)

**Click path:** Home → Gallery → Menu → Reservations (+ newsletter optional). Ends with a handoff to Architecture (Part 3).

![Meghna demo path: Home Gallery Menu from freeze at build (no /api/menu). Reservations GET /api/slots then POST /api/reservations. Newsletter optional POST /api/newsletter store-only.](assets/flow-meghna-fe-be.svg)

Fallback raster: [flow-meghna-fe-be-720.png](assets/flow-meghna-fe-be-720.png).

| Step | Frontend | Hits Flask? | Data |
| --- | --- | --- | --- |
| Home / Gallery / Menu | React pages | **No** `/api/menu` from FE — `@shared/freeze.json` (+ menu-presentation) at build | freeze · images via `GET /images/…` |
| Reservations | Booking form | **GET** `/api/slots?date=` → **POST** `/api/reservations` | Postgres customers/reservations · 409 if full |
| Newsletter (optional) | Footer form | **POST** `/api/newsletter` | Postgres store-only |
| Operator | not Meghna path | **GET** `/api/operator` | read-only helper |

The diagram also lists the full Flask surface (`/api/health`, `/api/menu`, `/api/site`, …) so Architecture can point at exposed routes without inventing FE arrows.

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

## Related

- [Local vs AWS](part3-local-vs-aws.md) — local vs MSAIE staging table
- [Part 3 natural script](part3-variant-b-script-natural.md) — diagram callouts
- [Parts 3–5 materials](parts-345-materials.md) — pack index
- [Part 4 coding overview](part4-coding-overview.md) — forms · functions · FE · BE · API · DB
- [Stack](stack.md) — four new diagrams + older HLDs as history
- History / probe archive: [as-is SVG](assets/hld-as-is.svg), [AWS staging SVG](assets/hld-aws-staging.svg)

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE · architect cut HLD trio + Meghna FE/BE honesty (freeze vs API).*

---
title: Teammate HLD (Hiren)
nav: Quantic
---

# Teammate HLD — Hiren’s Café Fausse cut

**Label:** teammate architecture / code sample — **not** our MSAIE staging map.

| | Ours (Claude / this repo) | Hiren (teammate) |
| --- | --- | --- |
| Live demo truth | `https://cafe.artof.link/` tip `73d202d` | His repo — not our host |
| Repo | [artofdream/aea-interactive-design](https://github.com/artofdream/aea-interactive-design) | [vadaliah/Quantic_Cafe_Fausse_Application](https://github.com/vadaliah/Quantic_Cafe_Fausse_Application) |
| Database | **On-box Postgres** (`postgres:16`) on MSAIE staging | **Aurora Postgres Serverless v2** via CDK (`us-east-2`, IAM auth, VPC) |
| Edge / deploy | Caddy → Flask → on-box Postgres | CDK / AWS-shaped deploy (his design) |
| Flask style | App factory `@app.get` / `@app.post` | **Flask Blueprints** |
| Menu / site copy | `shared/freeze.json` via `/api/menu` · `/api/site` | **Menu in DB tables** (CRUD) |
| Reservations | One-shot create · UNIQUE `(time_slot, table_number)` · guest 1–20 | Lifecycle **PENDING → ASSIGNED → RELEASED** · guest **1–10** |
| FE stack | React **18** · Vite **5** | React **19** · Vite **8** |
| Extra APIs on ours | `/api/slots` · `/api/site` · `/api/newsletter` · `/api/operator` | Those routes **not** in his tree (as assessed) |

## On camera (honesty)

1. Show **our** MSAIE HLD / `cafe.artof.link` for Part 3 architecture.
2. If referring to Hiren: call it **teammate HLD** — Aurora/CDK + multi-state bookings — a different valid design for the same SRS shape.
3. Do **not** present Hiren’s Aurora diagram as `cafe.artof.link`.

## Related (ours)

- [Part 3 present](part3-present.md) · [MSAIE HLD SVG](assets/hld-aws-msaie.svg) · [Developer system map](developer-system-map.md) · [Stack](stack.md)
- Honesty still: [slide-p3-07-teammate.svg](assets/slide-p3-07-teammate.svg)

*Sources: App inventory of Hiren’s public repo vs tip `73d202d`. Unknown until probed if his remote drifts.*

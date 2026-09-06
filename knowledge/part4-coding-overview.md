# Part 4 — Coding overview diagram

**Who:** Hiren Part 4.  
**Visual:** [SVG](assets/flow-coding-overview.svg) · [720 PNG](assets/flow-coding-overview-720.png)  
**Job:** On-camera map of **forms · functions · frontend · backend · API · DB** — coding why/how that maps to the Part 3 architecture flow.  
**Label:** **PROTOTYPE** visual · not Quantic submit. No FR/NFR IDs on the diagram.  
**Honesty:** wiring from `aea-interactive-design` `main`. Folded into [Stack](stack.md). Architecture trio: [Part 3 HLD + flow](part3-hld-flow-notes.md).

---

## Spoken cue (one line)

“Coding map — pages and forms up top, Flask routes in the middle, modules under that, Postgres at the bottom. Static pages read the freeze; booking goes through slots and reservations.”

---

## Diagram

![Part 4 coding overview: Home Menu Gallery About import freeze.json (not /api/menu). Reservations form GET /api/slots then POST /api/reservations to Postgres. NewsletterForm POST /api/newsletter store-only. Backend modules under Flask. Fail-closed without DB.](assets/flow-coding-overview.svg)

Fallback raster: [flow-coding-overview-720.png](assets/flow-coding-overview-720.png).

---

## Honest wiring

| Layer | What | Connects how |
| --- | --- | --- |
| **Frontend pages** | Home / Menu / Gallery / About | `import @shared/freeze.json` (+ menu-presentation) — **not** `/api/menu` |
| **Images** | Gallery / menu photos | `GET /images/…` |
| **Reservations form** | booking fields | **GET** `/api/slots?date=` → **POST** `/api/reservations` → Postgres |
| **NewsletterForm** | footer email | **POST** `/api/newsletter` → store-only |
| **API** | Flask routes | health · menu/site (exposed; FE uses freeze) · slots/reservations · newsletter · operator helper |
| **Backend modules** | `reservations.py` · `newsletter.py` · `content`/`slots` · `db.py` · `validate.py` | functions behind routes |
| **DB** | `customers` · `reservations` | unique slot+table · fail-closed without DB · full book → 409 |

**On camera:** **cafe.artof.link** = **MSAIE staging** (temporary). Staging Postgres is **on-box**, not AEA RDS. Newsletter is **store-only**.

---

## Related

- Architecture trio: [Part 3 HLD + Meghna FE/BE](part3-hld-flow-notes.md)
- Part 4 NATURAL callouts: [Part 4 natural script](part4-variant-c-script-natural.md)
- Meghna FE/BE: [flow-meghna-fe-be.svg](assets/flow-meghna-fe-be.svg)
- [Stack](stack.md) · [Parts 3–5 materials](parts-345-materials.md) · [Local vs AWS](part3-local-vs-aws.md)
- ID map: [Handoff mapping](parts-345-handoff-mapping.md) — **not spoken on camera**

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE · Part 4 coding overview.*

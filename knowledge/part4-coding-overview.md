# Part 4 — Coding overview diagram

**Visual:** `flow-coding-overview.svg` · `flow-coding-overview-720.png`  
**Job:** On-camera map of **forms · functions · frontend · backend · API · DB** — coding why/how that maps to the Part 3 architecture flow.  
**Honesty:** wiring from `aea-interactive-design` `main`.

---

## Spoken cue (one line)

“Coding map — pages and forms up top, Flask routes in the middle, modules under that, Postgres at the bottom. Static pages read the freeze; booking goes through slots and reservations.”

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

---

## Related

- Architecture trio: [`PART3-HLD-FLOW-NOTES.md`](PART3-HLD-FLOW-NOTES.md)  
- Part 4 NATURAL callouts: [`PART4-VARIANT-C-SCRIPT-NATURAL.md`](PART4-VARIANT-C-SCRIPT-NATURAL.md)  
- Meghna FE/BE: `flow-meghna-fe-be.svg`

---

*Packed 2026-09-06 Europe/Oslo · PROTOTYPE · Part 4 coding overview.*

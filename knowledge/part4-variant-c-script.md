# Part 4 — Coding rationale / Variant C (~3 min)

**Who:** **Hiren** (owner lock 2026-09-06) — Coding Part 4.  
**Job:** Why these implementations — freeze + CI, table/fail-closed, timezone/modules/tooling — then hand to Shared close.  
**Picture:** freeze/CI cards → table/index/fail-closed → timezone/NFR-9/tooling → close handoff.  
**Label:** **PROTOTYPE** — not Quantic submit.  
**Talk lock:** #97. Room clock ≈ **6:30–9:30**.

FR/NFR IDs OK in speech. Plain-English VO twin: [Part 4 VO](part4-variant-c-voiceover.md). Pack index: [Parts 3–5 materials](parts-345-materials.md). Talk cuts: [Presentation](presentation.md). Silent rehearsal clip: [`clips/part4-variant-c-prototype-silent.mp4`](clips/part4-variant-c-prototype-silent.mp4) (**PROTOTYPE**).

---

## 1. Timed beat sheet (~180s)

| Clock | Dur | Beat | Show | Say |
| ---: | ---: | --- | --- | --- |
| **0:00–0:15** | 15s | Open | Title card | “Coding rationale — we implemented the freeze; we did not invent a second menu.” |
| **0:15–1:00** | 45s | Freeze + CI | Freeze card (+ forms slide optional) | “Menu, address, hours, awards, reviews live in `shared/freeze.json`. Pages and `GET /api/menu` display that file. `test_freeze.py` fails if copy drifts. Do not improve prices. That locks FR-2, FR-5, FR-10, FR-11, FR-14.” |
| **1:00–2:00** | 60s | Table + fail-closed | Table / NFR-5/6 cards · data slides | “FR-8: random table from thirty — `ORDER BY random()` with `table_number` between 1 and 30. NFR-5: unique index `reservations_slot_table` on `(time_slot, table_number)` — same table cannot land twice in one slot. Full slot → FR-9 error, no thirty-first table. `test_fail_closed.py` covers missing DB, unreachable DB, timeout, and the 31st table. A write is only a write if Postgres accepts it — NFR-6. Email goes through validate, strip, lower before store — not a new FR; verbatim-case Future #37 stays parked.” |
| **2:00–2:45** | 45s | TZ + modules + tooling | Timezone / NFR-9 card | “Hours are Washington, DC. Slots use `America/New_York` from the freeze (`slots.py`, PR #12) so a browser elsewhere cannot invent Sunday hours — FR-2, FR-7. Packages under `backend/cafe_fausse/` and pages under `frontend/src/pages/` are the NFR-9 cut. Tooling log: `docs/ai-tooling.md` — Cursor, GitHub Actions, pytest; student app repos were not copied.” |
| **2:45–3:00** | 15s | Handoff | Handoff card | “That’s the coding why. Shared close next — shipped picture and the honesty lines, including NFR-1 and NFR-2 met with probes. Over to the close.” |

**Room tip:** If short on time, keep freeze (30s) + table/fail-closed (45s) + one timezone sentence + handoff.

---

## 2. Diagram / card callouts

| Visual | Point at | One line |
| --- | --- | --- |
| Freeze card | `shared/freeze.json` | “Single SoT — CI fails on drift.” |
| Table card | random 1–30 + unique index | “FR-8 + NFR-5 together.” |
| Fail-closed | missing DB / 31st table | “Honest no beats fake success.” |
| TZ / modules | America/New_York · package layout | “NFR-9 cut + slot honesty.” |

---

## 3. Supporting ID map

| Beat | Freeze IDs |
| --- | --- |
| Freeze + CI | FR-2, FR-5, FR-10, FR-11, FR-14 |
| Table + fail-closed | FR-8, FR-9, FR-15 (email normalize note), NFR-5, NFR-6 |
| Timezone / modules / tooling | FR-2, FR-7, NFR-9 |
| Parked | Future #37 (verbatim email case); #22 / #34–#38 stay parked |

---

## 4. What not to say

- Do not claim four-browser NFR-7 complete.
- Do not call `/operator` FR-19 or an admin console.
- Do not call `cafe.artof.link` production forever.
- Do not treat Future #22 / #34–#38 as missing grade rows.
- Leave the full NFR-1/2 probe numbers for Shared close (or one short pointer).

---

## 5. Handoff line (Shared close)

> “Coding rationale done. Shared close: what we shipped, and honesty — NFR-1 and NFR-2 met on the recorded probes, NFR-7 still Partial, staging not forever.”

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE sample · talk #97.*

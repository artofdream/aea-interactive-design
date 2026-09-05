# Part 4 — Variant C voice-over (ready to record)

**Length:** ~3 minutes  
**Picture:** silent `part4-variant-c-prototype-silent.mp4`  
**IDs:** OK in technical take · plain twin below  
**Status:** draft — **PROTOTYPE**, not Quantic submit.

---

## Timed lines (technical — IDs OK)

### Open (0:00–0:15)

“Coding rationale — we implemented the freeze; we did not invent a second menu.”

### Freeze + CI (0:15–1:00)

“Menu, address, hours, awards, and reviews live in shared slash freeze.json. Pages and GET slash api slash menu display that file. test-freeze fails if copy drifts. Do not improve prices. That locks FR-2, FR-5, FR-10, FR-11, and FR-14.”

### Table + fail-closed (1:00–2:00)

“FR-8: random table from thirty — order by random, table number one through thirty. NFR-5: unique index on time-slot and table-number — same table cannot land twice in one slot. Full slot gives the FR-9 error — no thirty-first table. test-fail-closed covers missing database, unreachable database, timeout, and the thirty-first table. A write counts only if Postgres accepts it — NFR-6. Email is validated, stripped, and lowercased before store — not a new FR; verbatim-case Future thirty-seven stays parked.”

### Timezone + modules + tooling (2:00–2:45)

“Hours are Washington, D.C. Slots use America slash New-York from the freeze — slots.py, PR twelve — so a browser elsewhere cannot invent Sunday hours. That supports FR-2 and FR-7. Packages under backend slash cafe-fausse and pages under frontend slash src slash pages are the NFR-9 cut. Tooling log: docs slash ai-tooling.md — Cursor, GitHub Actions, pytest; student app repos were not copied.”

### Handoff (2:45–3:00)

“That’s the coding why. Shared close next — shipped picture and honesty, including NFR-1 and NFR-2 met with probes. Over to the close.”

---

## Plain-English twin (optional)

### Open

“Why we coded it this way — we followed the freeze file; we did not invent another menu.”

### Freeze

“One freeze file owns menu, address, hours, awards, and reviews. The site and the menu API only show that file. Tests fail if someone edits copy out of band. We do not ‘improve’ prices.”

### Table

“A successful book picks a random table from one to thirty. The database unique rule blocks two bookings on the same table in the same slot. If the slot is full, we say no — we do not invent a thirty-first table. If the database is down or times out, we fail closed instead of faking success.”

### Timezone / modules

“Restaurant hours are Eastern Time for Washington, D.C., so a traveler’s browser cannot invent Sunday hours. Code is split into clear backend packages and page components. We logged Cursor, Actions, and pytest — we did not copy other student apps.”

### Handoff

“Coding done. Close next — what shipped, and the honesty lines.”

---

*End VO draft · recorded teammate audio: Unknown until Claude/Hiren records.*

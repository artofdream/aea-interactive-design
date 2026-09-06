> **NATURAL spoken track** — coding rationale (why/how) · no FR-/NFR- IDs on camera. Technical originals kept for post-mortem. ID map: [Parts 3–5 handoff mapping](parts-345-handoff-mapping.md).

# Part 4 — Variant C voice-over (ready to record) — coding rationale

**Length:** ~3 minutes  
**Picture:** silent `part4-variant-c-prototype-silent.mp4`  
**Spoken:** natural demo language — lead with **why**, then **how** — **no FR-/NFR- IDs, issue numbers, SHA, or CI job names**  
**Talk spine:** Part 2 UX/business · Part 3 architecture why/how · **Part 4 coding why/how** · Part 5 honesty/close  
**Who:** **Hiren** (owner lock 2026-09-06) — Coding Part 4.  
**IDs:** [Parts 3–5 handoff mapping](parts-345-handoff-mapping.md) only  
**Status:** draft for Hiren — **PROTOTYPE**, not Quantic submit.

---

## Timed lines (natural — for TTS / live VO)

### Open — coding why (0:00–0:15)

“Coding rationale — why these implementations, then how. We implemented the freeze; we did not invent a second menu.”

### Why freeze + how CI locks it (0:15–1:00)

“Why a freeze: menu, address, hours, awards, and reviews must have one source of truth. How: they live in one freeze file. The pages and the menu API only show that file. If someone edits copy out of band, the tests fail. We do not improve prices.”

### Why fail-closed + how table integrity (1:00–2:00)

“Why fail-closed and a hard table rule: honest no beats fake success. How: a successful book picks a random table from one to thirty. The database unique rule blocks two bookings on the same table in the same slot. If the slot is full, we say no — we do not invent a thirty-first table. If the database is missing, unreachable, or times out, we fail closed instead of faking success. A write counts only if Postgres accepts it. Email is validated, stripped, and lowercased before we store it. Keeping the original letter-case is a future item — parked, not a grade gap.”

### Why Eastern hours + how modules/tooling (2:00–2:45)

“Why Eastern Time: the restaurant is Washington, D.C. How: slot times come from the freeze, so a traveler’s browser cannot invent Sunday hours. Code is split into clear backend packages and page components. We logged Cursor, GitHub Actions, and pytest in the tooling note — we did not copy other student apps.”

### Handoff → honesty close (2:45–3:00)

“That’s the coding why and how. Shared close next — what we shipped, and honesty: load and submit timings met on the phone broadband probe, browser support still partial. Over to the close.”

---

## Tight cut (if late)

“Coding why and how. Why freeze: one file owns menu, address, hours, awards, reviews; how: tests fail on drift. Why fail-closed: honest no; how: random table one through thirty, unique rule blocks doubles, full slot says no, DB down fails closed. Why Eastern hours for D.C.; how: freeze slots, clear packages, tooling logged. Close next.”

---

*End VO draft · PROTOTYPE TTS uses Timed lines above · coding rationale (why/how) · MSAIE staging wording lock.*

> **NATURAL spoken track** — no FR-/NFR- IDs on camera. Technical originals kept for post-mortem. ID map: [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md).

# Part 4 — Variant C voice-over (ready to record)

**Length:** ~3 minutes  
**Picture:** silent `part4-variant-c-prototype-silent.mp4`  
**Spoken:** natural demo language — **no FR-/NFR- IDs, issue numbers, SHA, or CI job names**  
**IDs:** [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md) only  
**Status:** draft — **PROTOTYPE**, not Quantic submit.

---

## Timed lines (natural — for TTS / live VO)

### Open (0:00–0:15)

“Coding rationale — we implemented the freeze; we did not invent a second menu.”

### Freeze + CI (0:15–1:00)

“Menu, address, hours, awards, and reviews live in one freeze file. The pages and the menu API only show that file. If someone edits copy out of band, the tests fail. We do not improve prices.”

### Table + fail-closed (1:00–2:00)

“A successful book picks a random table from one to thirty. The database unique rule blocks two bookings on the same table in the same slot. If the slot is full, we say no — we do not invent a thirty-first table. If the database is missing, unreachable, or times out, we fail closed instead of faking success. A write counts only if Postgres accepts it. Email is validated, stripped, and lowercased before we store it. Keeping the original letter-case is a future item — parked, not a grade gap.”

### Timezone + modules + tooling (2:00–2:45)

“Restaurant hours are Eastern Time for Washington, D.C. Slot times come from the freeze, so a traveler’s browser cannot invent Sunday hours. Code is split into clear backend packages and page components. We logged Cursor, GitHub Actions, and pytest in the tooling note — we did not copy other student apps.”

### Handoff (2:45–3:00)

“That’s the coding why. Shared close next — what we shipped, and honesty: load and submit timings met on the phone broadband probe, browser support still partial. Over to the close.”

---

## Tight cut (if late)

“We followed the freeze — one file owns menu, address, hours, awards, and reviews; tests fail on drift. Booking picks a random table one through thirty; the unique rule blocks doubles; a full slot says no. Database down means fail closed. Hours are Eastern for D.C. Clear packages and pages; tooling logged. Close next.”

---

*End VO draft · PROTOTYPE TTS uses Timed lines above · recorded teammate audio: Unknown until Claude/Hiren records.*

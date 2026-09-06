> **NATURAL spoken track** — coding rationale (why/how) · no FR-/NFR- IDs on camera. Technical originals kept for post-mortem. ID map: [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md).

# Part 4 — Coding rationale / Variant C (~3 min)

**Talk spine:** Part 2 = UX/business rationale (Meghna) · Part 3 = architecture why/how · **Part 4 = coding why/how** · Part 5 = honesty/close.  
**Who:** Claude or Hiren (the one not doing Architecture).  
**Job:** Why these implementations / how they work — freeze + CI, table + fail-closed, timezone/modules — then hand to Shared close.  
**Picture:** freeze/CI cards → table/index/fail-closed → timezone/modules/tooling → close handoff.  
**Label:** **PROTOTYPE** — not Quantic submit.  
**Talk lock:** #97. Room clock ≈ **6:30–9:30**.

**Speaking rule:** Spoken / VO = clear, natural demo language — lead with **why**, then **how**. **No FR-/NFR- IDs, issue numbers, SHA, or CI job names on camera.** Demo focus: **cafe.artof.link** as MSAIE staging (temporary — not production forever). Mapping: [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md).

---

## 1. Timed beat sheet (~180s)

| Clock | Dur | Beat (why/how) | Show | Say |
| ---: | ---: | --- | --- | --- |
| **0:00–0:15** | 15s | **Open — coding why** | Title card | “Coding rationale — why these implementations, then how. We implemented the freeze; we did not invent a second menu.” |
| **0:15–1:00** | 45s | **Why freeze + how CI locks it** | Freeze card (+ forms slide optional) | “Why a freeze: menu, address, hours, awards, and reviews must have one source of truth. How: they live in one freeze file. The pages and the menu API only show that file. If someone edits copy out of band, the tests fail. We do not improve prices.” |
| **1:00–2:00** | 60s | **Why fail-closed + how table integrity** | Table / fail-closed cards · data slides | “Why fail-closed and a hard table rule: honest no beats fake success. How: a successful book picks a random table from one to thirty. The database unique rule blocks two bookings on the same table in the same slot. If the slot is full, we say no — we do not invent a thirty-first table. If the database is missing, unreachable, or times out, we fail closed instead of faking success. A write counts only if Postgres accepts it. Email is validated, stripped, and lowercased before we store it. Keeping the original letter-case is a future item — parked, not a grade gap.” |
| **2:00–2:45** | 45s | **Why Eastern hours + how modules/tooling** | Timezone / modules card | “Why Eastern Time: the restaurant is Washington, D.C. How: slot times come from the freeze, so a traveler’s browser cannot invent Sunday hours. Code is split into clear backend packages and page components. We logged Cursor, GitHub Actions, and pytest in the tooling note — we did not copy other student apps.” |
| **2:45–3:00** | 15s | **Handoff → honesty close** | Handoff card | “That’s the coding why and how. Shared close next — what we shipped, and honesty: load and submit timings met on the phone broadband probe, browser support still partial. Over to the close.” |

**Room tip:** If short on time, keep freeze why/how (30s) + table/fail-closed why/how (45s) + one timezone sentence + handoff.

---

## 2. Diagram / card callouts

| Visual | Point at | One line |
| --- | --- | --- |
| Freeze card | freeze file | “Why one source of truth — how CI fails on drift.” |
| Table card | random 1–30 + unique index | “How random table plus unique slot rule.” |
| Fail-closed | missing DB / 31st table | “Why honest no beats fake success.” |
| TZ / modules | America/New_York · package layout | “Why Eastern hours — how clear module cut.” |

---

## 3. Supporting ID map (off-camera)

See **[`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md)** — Part 4 table. Do not read IDs on camera.

---

## 4. What not to say

- Do not claim four-browser support complete.
- Do not call `/operator` an admin console or a graded admin feature.
- Do not call `cafe.artof.link` production forever — it is the **staging environment for the MSAIE project** (temporary).
- Do not treat parked Future items as missing grade rows.
- Leave the full probe numbers for Shared close (or one short pointer, as in the handoff line).
- Do not put SES outbound in the spoken grade story (Future / optional only).

---

## 5. Handoff line (Shared close)

> “That’s the coding why and how. Shared close: what we shipped, and honesty — load and submit timings met on the recorded probes, browser support still partial, cafe.artof.link MSAIE staging not forever.”

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE · talk #97 · coding rationale (why/how) · MSAIE staging wording lock.*

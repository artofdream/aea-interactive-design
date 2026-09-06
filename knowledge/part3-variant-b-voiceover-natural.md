> **NATURAL spoken track** — architecture rationale (why/how) · no FR-/NFR- IDs on camera. Technical originals kept for post-mortem. ID map: [Parts 3–5 handoff mapping](parts-345-handoff-mapping.md). Comparison table: [Local vs AWS](part3-local-vs-aws.md).

# Part 3 — Variant B voice-over (ready to record) — architecture rationale

**Length:** ~3 minutes  
**Picture:** silent `part3-variant-b-prototype-silent.mp4` or live diagrams  
**Spoken:** natural architect language — lead with **why**, then **how** — **no FR-/NFR- IDs, issue numbers, SHA, or CI job names**  
**Lens:** architecture rationale — why this design / how it hangs together — not a feature tour, not an ops dump  
**Talk spine:** Part 2 UX/business · **Part 3 architecture why/how** · Part 4 coding why/how · Part 5 honesty/close  
**Demo focus:** **cafe.artof.link** = **staging environment for the MSAIE project**; **Local vs AWS MSAIE staging** as deploy decision  
**IDs:** [Parts 3–5 handoff mapping](parts-345-handoff-mapping.md) only  
**Status:** draft for Claude/Hiren — **PROTOTYPE**, not Quantic submit.

---

## How to use

1. Open the silent prototype (or Stack + staging SVG tabs).
2. Read timed lines; ~1s breath between beats.
3. Stop at the Coding handoff — do not start Variant C.

---

## Timed lines (natural — for TTS / live VO)

### Why these boundaries (0:00–0:25)

“Architecture rationale — why this design hangs together. First, why the boundaries: two sites, two jobs. Knowledge on GitHub Pages is documentation and maps. The restaurant app at cafe.artof.link is our staging environment for the MSAIE project — not one shared shop, and not production forever. We grade only the official SRS. The operator path is a read-only helper, not an admin console we invent as product.”

### How the request flows (0:25–0:55)

“How it hangs together logically: React for the public UX, Flask API in the middle, PostgreSQL underneath. A booking or newsletter signup leaves the browser, hits the API, and lands in Postgres — customers and reservations for booking; newsletter stays store-only until outbound mail is wired. That is the path behind Meghna’s screen.”

### Why two deploy targets (0:55–1:35)

“Why two deploy targets, same design. Local — Vite, Flask, and local Postgres on the developer machine — so we iterate fast without touching the shared demo. MSAIE staging at cafe.artof.link — shared HTTPS — so graders and the team hit one URL and prove the high-level design holds across environments. Staging is temporary — not forever hosting.”

### How quality is encoded (1:35–2:10)

“How quality shows up in the design. Without a database the app fails closed — it does not pretend to book. Slot-plus-table uniqueness stops double-booking the same table in the same slot. The freeze file is the single source of truth: CI locks drift so menu copy and fail-closed rules cannot quietly change.”

### Why these tradeoffs (2:10–2:45)

“Why these tradeoffs. Two targets instead of one: speed locally, shared proof on staging. Knowledge is not the App — no shared load balancer, two hostnames, two jobs. Outbound SES is parked; newsletter stays store-only. Longer-term hosting stays a future item.”

### Handoff → coding why/how (2:45–3:00)

“That’s the architecture why and how. Coding next owns freeze, table assignment, and timezone — the implementation why and how. Over to you.”

---

## Tight cut (if late)

“Architecture why and how. Why boundaries: Knowledge on Pages; app at cafe.artof.link — MSAIE staging, not forever; grade floor is the official SRS; operator read-only. How it flows: React to Flask to Postgres. Why two targets: local Vite/Flask/Postgres for speed; cafe.artof.link for shared HTTPS proof. How quality: fail-closed, unique slot and table, freeze locks drift. Why tradeoffs: Knowledge is not the App; SES parked. Coding owns freeze, tables, timezone.”

---

*End VO draft · PROTOTYPE TTS uses Timed lines above · architecture rationale (why/how) · MSAIE staging lock · Local vs AWS as deploy decision.*

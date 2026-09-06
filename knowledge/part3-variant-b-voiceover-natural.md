> **NATURAL spoken track** — no FR-/NFR- IDs on camera. Technical originals kept for post-mortem. ID map: [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md).

# Part 3 — Variant B voice-over (ready to record)

**Length:** ~3 minutes  
**Picture:** silent `part3-variant-b-prototype-silent.mp4` or live diagrams  
**Spoken:** natural demo language — **no FR-/NFR- IDs, issue numbers, SHA, or CI job names**  
**IDs:** [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md) only  
**Status:** draft for Claude/Hiren — **PROTOTYPE**, not Quantic submit.

---

## How to use

1. Open the silent prototype (or Stack + staging SVG tabs).
2. Read timed lines; ~1s breath between beats.
3. Stop at the Coding handoff — do not start Variant C.

---

## Timed lines (natural — for TTS / live VO)

### Takeover (0:00–0:20)

“Taking Architecture from the booking screen. Two sites, two jobs: the knowledge map on GitHub Pages, and the restaurant app on weekend Lightsail staging — not one shared shop, and not production forever.”

### HLD staging (0:20–1:00)

“Here’s the as-is path: DNS points at a small Lightsail box with HTTPS, the Flask API, the built React app, and Postgres on that same box. Our shared company database is left alone. The wildcard load balancer on artof.link is not Café Fausse. Longer-term hosting stays a future item — parked for now.”

### As-is picture (1:00–1:50)

“Knowledge markdown builds to Pages. The app on main is React, Flask, and Postgres. This weekend’s share is cafe.artof.link — healthy and reachable — until the owner tears it down. Temporary demo window, not forever hosting.”

### Boxes (1:50–2:40)

“Front-end pages cover the public site — home, menu, gallery, about, reservations, and newsletter. The API covers booking and signup. The database stores customers and reservations with a unique rule: one table cannot be booked twice in the same time slot. We only grade the official requirement list. The operator view is a read-only helper — not an admin console.”

### Sensors + handoff (2:40–3:00)

“CI refuses a missing freeze file or a missing PDF fingerprint. Automated tests lock the menu copy and the fail-closed behavior — including a missing database and a fake thirty-first table. The author does not merge their own work. Over to Coding — freeze, tables, and timezone.”

---

## Tight cut (if late)

“Architecture from the booking screen. Knowledge on Pages; restaurant on weekend staging — not forever. Lightsail box runs HTTPS, Flask, React, and Postgres; company database untouched. Front-end covers the public site; API covers booking; database enforces one table per slot. Operator is read-only. CI locks the freeze and fail-closed. Coding next.”

---

*End VO draft · PROTOTYPE TTS uses Timed lines above · recorded teammate audio: Unknown until Claude/Hiren records.*

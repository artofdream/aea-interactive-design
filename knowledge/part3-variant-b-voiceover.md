# Part 3 — Variant B voice-over (ready to record)

**Length:** ~3 minutes  
**Picture:** silent [`clips/part3-variant-b-prototype-silent.mp4`](clips/part3-variant-b-prototype-silent.mp4) or live diagrams  
**IDs:** OK in technical take · plain twin below  
**Who:** **Claude** (owner lock 2026-09-06) — Architecture Part 3.  
**Status:** draft for Claude — **PROTOTYPE**, not Quantic submit.  
**Sister pages:** [Part 3 script](part3-variant-b-script.md) · [Parts 3–5 materials](parts-345-materials.md) · [Talk cuts](presentation.md)

---

## How to use

1. Open the silent prototype on [Parts 3–5 materials](parts-345-materials.md) (or Stack + staging SVG tabs).
2. Read timed lines; ~1s breath between beats.
3. Stop at the Coding handoff — do not start Variant C.

---

## Timed lines (technical — IDs OK)

### Takeover (0:00–0:20)

“Taking Architecture from Reservations. Two hostnames: Knowledge on GitHub Pages, App on Lightsail staging number fifty-seven — not one shop, and not production forever.”

### HLD staging (0:20–1:00)

“As-is path: Route fifty-three A to Lightsail cafe-fausse-staging, Caddy and Let’s Encrypt, Flask plus the built SPA, on-box Postgres on the instance — not a shared RDS. The star-dot-artof-dot-link ELB wildcard is not Café Fausse. Longer-term hosting remains Future twenty-two.”

### As-is picture (1:00–1:50)

“Knowledge markdown builds to Pages. App on main is React, Flask, and Postgres. This weekend’s share is cafe.artof.link — GET two hundred — weekend window until the owner tears it down, not forever.”

### Boxes → IDs (1:50–2:40)

“React pages map to FR-1 through FR-5 and FR-10 through FR-14, plus NFR-3, NFR-4, and NFR-8. Flask APIs: FR-6 through FR-9 and FR-15 through FR-18, with NFR-5 and NFR-6. Postgres is FR-17 — unique time-slot and table-number. Grade floor only: FR-1 through 18, NFR-1 through 9. Operator is a read-only helper — not FR-19.”

### Sensors + handoff (2:40–3:00)

“Outer harness: Actions require the freeze file and the PDF SHA-256; test-freeze locks copy; test-fail-closed locks missing database and the thirty-first table. Author does not merge. Over to Coding — freeze, tables, timezone.”

---

## Plain-English twin (optional)

### Takeover

“Architecture from the booking screen. Two websites: the knowledge map on Pages, the restaurant on weekend staging — temporary, not forever.”

### Staging

“DNS points at a small Lightsail box with HTTPS, the Flask API, the React app, and Postgres on that same box. Our shared company database is left alone. Long-term hosting is still a future item.”

### Boxes

“Front-end pages cover the public site requirements. The API covers booking and newsletter. The database stores customers and reservations with a unique slot-and-table rule. We only grade the official requirement list — operator view is just a read-only helper.”

### Sensors + handoff

“CI refuses a missing freeze or PDF fingerprint, and tests lock menu copy and fail-closed behavior. Coding next.”

---

*End VO draft · recorded teammate audio: Unknown until Claude/Hiren records.*

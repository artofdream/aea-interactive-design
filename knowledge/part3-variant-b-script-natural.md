> **NATURAL spoken track** — no FR-/NFR- IDs on camera. Technical originals kept for post-mortem. ID map: [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md).

# Part 3 — Architecture / Variant B (~3 min)

**Who:** Claude or Hiren (Hiren picks B vs C; Claude takes the other).  
**Job:** Take over from Meghna’s reservation screen → diagrams → Coverage boxes → sensors → hand off to Coding.  
**Picture:** live Reservations (or clip/still) → Stack + AWS staging SVG → coverage cards → CI sensors.  
**Label:** **PROTOTYPE** — not Quantic submit.  
**Talk lock:** #97 five-part VIDEO. Room clock ≈ **3:30–6:30**.

**Speaking rule:** Spoken / VO = clear, natural demo language. **No FR-/NFR- IDs, issue numbers, SHA, or CI job names on camera.** ID / freeze / probe mapping lives in [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md) (appendix below points there).

---

## 1. Timed beat sheet (~180s)

| Clock | Dur | Beat | Show | Say |
| ---: | ---: | --- | --- | --- |
| **0:00–0:20** | 20s | Takeover | Reservations still / live form on `cafe.artof.link` | “Taking Architecture from the booking screen. Two sites, two jobs: the knowledge map on GitHub Pages, and the restaurant app on weekend Lightsail staging — not one shared shop, and not production forever.” |
| **0:20–1:00** | 40s | HLD staging | `hld-aws-staging` SVG (+ Stack slide) | “Here’s the as-is path: DNS points at a small Lightsail box with HTTPS, the Flask API, the built React app, and Postgres on that same box. Our shared company database is left alone. The wildcard load balancer on artof.link is not Café Fausse. Longer-term hosting stays a future item — parked for now.” |
| **1:00–1:50** | 50s | As-is picture | `hld-as-is` SVG | “Knowledge markdown builds to Pages. The app on main is React, Flask, and Postgres. This weekend’s share is cafe.artof.link — healthy and reachable — until the owner tears it down. Temporary demo window, not forever hosting.” |
| **1:50–2:40** | 50s | Boxes | Coverage / boxes card | “Front-end pages cover the public site — home, menu, gallery, about, reservations, and newsletter. The API covers booking and signup. The database stores customers and reservations with a unique rule: one table cannot be booked twice in the same time slot. We only grade the official requirement list. The operator view is a read-only helper — not an admin console.” |
| **2:40–3:00** | 20s | Sensors + handoff | Sensors / CI card | “CI refuses a missing freeze file or a missing PDF fingerprint. Automated tests lock the menu copy and the fail-closed behavior — including a missing database and a fake thirty-first table. The author does not merge their own work. Over to Coding — freeze, tables, and timezone.” |

**Room tip:** If late at 2:30, skip as-is deep dive; keep staging SVG + boxes + handoff.

---

## 2. Diagram callouts (what to point at)

| Visual | Point at | One line |
| --- | --- | --- |
| Reservations start | Form fields / Reserve | “Product surface we just walked — now the boxes behind it.” |
| AWS staging SVG | Route53 → Lightsail → Caddy → Flask/SPA → PG | “Weekend staging path; company RDS untouched.” |
| As-is SVG | Knowledge Pages vs App staging vs local MVP | “Two hostnames, two jobs.” |
| Boxes card | Three coverage clusters | “Coverage is the grade map — not a second product.” |
| Sensors card | freeze / fail-closed / no self-merge | “Harness proves the freeze; not new grade rows.” |

Static assets in this pack: `hld-aws-staging-720.png`, `hld-as-is-720.png`, `fit-02-stack.png`, cards under `card-p3-*.png`.

---

## 3. Supporting ID map (off-camera)

See **[`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md)** — Part 3 table. Do not read IDs on camera.

---

## 4. Honesty (Architecture segment)

- Prefer `https://cafe.artof.link/` as **weekend Lightsail staging** — not production forever.
- Knowledge ≠ App (no shared LB).
- Do **not** invent an admin / graded operator feature.
- Leave full load / submit / browser honesty lines for **Shared close**. One breath here is enough: “speed and browser honesty are in the close.”

---

## 5. Handoff line (Coding)

> “That’s the as-is picture and the coverage map. Coding next: freeze file and CI, random table plus fail-closed, timezone and the module cut. Over to you.”

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE sample · talk #97 · natural spoken rewrite.*

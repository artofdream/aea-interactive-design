> **NATURAL spoken track** — architecture rationale (why/how) · no FR-/NFR- IDs on camera. Technical originals kept for post-mortem. ID map: [Parts 3–5 handoff mapping](parts-345-handoff-mapping.md). Local vs AWS table: [Local vs AWS](part3-local-vs-aws.md).

# Part 3 — Architecture rationale / Variant B (~3 min)

**Talk spine:** Part 2 = UX/business rationale (Meghna) · **Part 3 = architecture why/how** · Part 4 = coding why/how · Part 5 = honesty/close.  
**Who:** Claude or Hiren (Hiren picks B vs C; Claude takes the other).  
**Job:** Answer what a **software architect** wants — why this design / how it hangs together (boundaries, flow, deploy targets, quality attributes, tradeoffs) — then hand off to Coding. **Not a feature tour. Not an ops dump.**  
**Picture:** live Reservations (or clip/still) → Stack + AWS staging SVG → as-is / boxes → sensors → handoff.  
**Label:** **PROTOTYPE** — not Quantic submit.  
**Talk lock:** #97 five-part VIDEO. Room clock ≈ **3:30–6:30**.

**Speaking rule:** Spoken / VO = clear, natural architect language — lead with **why**, then **how**. **No FR-/NFR- IDs, issue numbers, SHA, or CI job names on camera.** Focus **cafe.artof.link** = **staging environment for the MSAIE project**. Cover **Local (dev) vs AWS MSAIE staging** as an architect **deploy decision** (what / explanation / rationale / implementation — see [Local vs AWS](part3-local-vs-aws.md)). Avoid on camera: “weekend Lightsail staging” and heavy Lightsail / Route53 / Caddy ops jargon. Temporary staging / not production forever is fine in plain words. ID mapping: [Parts 3–5 handoff mapping](parts-345-handoff-mapping.md).

---

## 1. Timed beat sheet (~180s)

| Clock | Dur | Beat (why/how) | Show | Say |
| ---: | ---: | --- | --- | --- |
| **0:00–0:25** | 25s | **Why these boundaries** | Reservations still / live form on `cafe.artof.link` | “Architecture rationale — why this design hangs together. First, why the boundaries: two sites, two jobs. Knowledge on GitHub Pages is documentation and maps. The restaurant app at cafe.artof.link is our staging environment for the MSAIE project — not one shared shop, and not production forever. We grade only the official SRS. The operator path is a read-only helper, not an admin console we invent as product.” |
| **0:25–0:55** | 30s | **How the request flows** | Stack slide / request path | “How it hangs together logically: React for the public UX, Flask API in the middle, PostgreSQL underneath. A booking or newsletter signup leaves the browser, hits the API, and lands in Postgres — customers and reservations for booking; newsletter stays store-only until outbound mail is wired. That is the path behind Meghna’s screen.” |
| **0:55–1:35** | 40s | **Why two deploy targets** | `hld-aws-staging` + `hld-as-is` SVG | “Why two deploy targets, same design. Local — Vite, Flask, and local Postgres on the developer machine — so we iterate fast without touching the shared demo. MSAIE staging at cafe.artof.link — shared HTTPS — so graders and the team hit one URL and prove the high-level design holds across environments. Staging is temporary — not forever hosting.” |
| **1:35–2:10** | 35s | **How quality is encoded** | Coverage / boxes + sensors cards | “How quality shows up in the design. Without a database the app fails closed — it does not pretend to book. Slot-plus-table uniqueness stops double-booking the same table in the same slot. The freeze file is the single source of truth: CI locks drift so menu copy and fail-closed rules cannot quietly change.” |
| **2:10–2:45** | 35s | **Why these tradeoffs** | As-is SVG / staging honesty | “Why these tradeoffs. Two targets instead of one: speed locally, shared proof on staging. Knowledge is not the App — no shared load balancer, two hostnames, two jobs. Outbound SES is parked; newsletter stays store-only. Longer-term hosting stays a future item.” |
| **2:45–3:00** | 15s | **Handoff → coding why/how** | Sensors / handoff card | “That’s the architecture why and how. Coding next owns freeze, table assignment, and timezone — the implementation why and how. Over to you.” |

**Room tip:** If late at 2:30, keep **Why these boundaries** + **Why two deploy targets** + **How quality is encoded** + **Handoff**.

---

## 2. Diagram callouts (what to point at)

| Visual | Point at | One line |
| --- | --- | --- |
| Reservations start | Form fields / Reserve | “Product surface — Architecture answers why/how behind it.” |
| Stack / logical path | React → Flask → Postgres | “How the request flows for booking and newsletter.” |
| AWS staging SVG | App host → HTTPS → Flask/SPA → PG | “Why staging exists: shared HTTPS proof at cafe.artof.link.” |
| As-is SVG | Local MVP vs AWS MSAIE staging vs Knowledge Pages | “Why two targets: local speed; cafe.artof.link shared proof — same HLD.” |
| Boxes / sensors cards | Fail-closed · unique slot+table · freeze/CI | “How quality is encoded — not a feature tour.” |
| Handoff card | Coding owns freeze / table / timezone | “Architecture why/how → Coding why/how.” |

Static assets in this pack: `hld-aws-staging-720.png`, `hld-as-is-720.png`, `fit-02-stack.png`, cards under `card-p3-*.png`. Full deploy comparison: [Local vs AWS](part3-local-vs-aws.md).

---

## 3. Supporting ID map (off-camera)

See **[Parts 3–5 handoff mapping](parts-345-handoff-mapping.md)** — Part 3 table. Do not read IDs on camera.

---

## 4. Honesty (Architecture segment)

- Prefer `https://cafe.artof.link/` as the **staging environment for the MSAIE project** — temporary staging, not production forever.
- **Local vs staging:** same React + Flask + PostgreSQL; local Vite + Flask + Postgres for coding speed; AWS MSAIE staging at cafe.artof.link for shared HTTPS demo — **same design, two deploy targets** (architect deploy decision). Ops detail — Lightsail/Caddy/on-box PG — off-camera in [Local vs AWS](part3-local-vs-aws.md).
- Knowledge ≠ App (no shared LB).
- Grade floor = official SRS only; do **not** invent an admin / graded operator feature (`/operator` is read-only helper).
- SES outbound parked (store-only newsletter).
- Leave full load / submit / browser honesty lines for **Shared close**.

---

## 5. Handoff line (Coding)

> “That’s the architecture why and how. Coding next owns freeze, table assignment, and timezone — the implementation why and how. Over to you.”

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE · talk #97 · architecture rationale (why/how) · MSAIE staging lock · Local vs AWS as deploy decision.*

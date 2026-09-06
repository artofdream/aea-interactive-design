# Local (dev) vs AWS MSAIE staging — architecture comparison

**Audience:** Architecture talk (Part 3 NATURAL) + Knowledge Stack/HLD fold-in.  
**On camera:** use the natural spoken beats in [Part 3 natural script](part3-variant-b-script-natural.md) / [Part 3 natural VO](part3-variant-b-voiceover-natural.md) (**architect lens**). Prefer **MSAIE staging** / **cafe.artof.link** language. Frame local vs AWS as an architect **deploy decision**, not an ops tour. Also folded into [Stack](stack.md).  
**Off camera / Knowledge / deliverable handoff:** this table — may name Lightsail, Caddy, on-box Postgres, host tip. No FR/NFR IDs required here.

**Demo focus:** [cafe.artof.link](https://cafe.artof.link/) = **staging environment for the MSAIE project** (temporary — not production forever). Presentation host.

---

## Same architecture (both sides)

**React + JSX frontend → Flask API → PostgreSQL** (FR/NFR MVP). **Fail-closed without DB.**

| | **Local (dev)** | **AWS MSAIE staging** |
| --- | --- | --- |
| **What was used** | Clone on **cts-ai** at `C:\projects\code\aea-interactive-design` | Deployed staging at **cafe.artof.link** — MSAIE project staging on **Lightsail** |
| **Explanation — what it is for** | Coding, iteration, and CI-adjacent work without touching the shared demo | Shared public HTTPS host graders (and the team) can open; same product surface Meghna walks |
| **Rationale — why both** | Fast local iterate | Prove the **same stack** on a public HTTPS host; one URL for the talk |
| **Implementation — how stood up** | Flask + **local Postgres**; Vite/dev frontend | **Caddy (TLS)** → Flask container → **on-box Postgres (MSAIE staging)** — not a shared RDS |
| **Stack** | React+JSX → Flask → PostgreSQL; fail-closed without DB | Same design: React+JSX → Flask → on-box PostgreSQL; fail-closed without DB |
| **Host tip (current)** | Developer box (cts-ai) | Lightsail instance tip **`73d202d`** (presentation host) |
| **Newsletter** | Store-only until SES env wired | Store-only until SES env wired (do not claim outbound SES) |
| **Honesty** | Not the public demo URL | Temporary MSAIE staging — **not production forever**; not a shared RDS |

---

## Architecture point (one line)

**Same design, two deploy targets** — local (cts-ai) for iterate; cafe.artof.link (MSAIE Lightsail staging) to prove the same React→Flask→Postgres stack on a public HTTPS host — so the HLD holds across environments.

---

## Architect questions (why/how — on-camera answers live in NATURAL VO)

Talk spine: Part 2 UX/business · **Part 3 architecture why/how** · Part 4 coding why/how · Part 5 honesty/close. Ops detail stays in the table above.

| Architect question (why/how) | Short answer |
| --- | --- |
| **Why these boundaries?** | Knowledge site (GitHub Pages) ≠ restaurant app (`cafe.artof.link`). Grade floor = official SRS only. `/operator` is a read-only helper, not an admin console. |
| **How does the request flow?** | React (public UX) → Flask API → PostgreSQL. Booking and newsletter follow that path (newsletter store-only until SES). |
| **Why two deploy targets?** | Same design: local (cts-ai Vite + Flask + local PG) for iterate; MSAIE staging at cafe.artof.link for shared HTTPS demo. Temporary staging — not production forever. |
| **How is quality encoded?** | Fail-closed without DB; unique slot+table integrity; freeze as single source of truth (CI locks drift). |
| **Why these tradeoffs?** | Two deploy targets (speed vs shared proof); Knowledge ≠ App (no shared LB); SES outbound parked (store-only). |
| **What does Coding own next (why/how)?** | Freeze file / CI, table assignment, timezone — implementation rationale. |

**On camera avoid:** “weekend Lightsail staging”, heavy Lightsail / Route53 / Caddy ops jargon.  
**Off camera / this table OK:** Lightsail, Caddy (TLS), on-box Postgres (MSAIE staging), not a shared RDS, host tip `73d202d`.

---

## Related assets

| Asset | Role |
| --- | --- |
| [Local HLD](assets/hld-local.svg) · [720 PNG](assets/hld-local-720.png) | **Architect cut** — Vite / Flask / local PG on cts-ai |
| [MSAIE staging HLD](assets/hld-aws-msaie.svg) · [720 PNG](assets/hld-aws-msaie-720.png) | **Architect cut** — `cafe.artof.link` · on-box Postgres (MSAIE staging) |
| [Meghna FE↔BE](assets/flow-meghna-fe-be.svg) | Click path vs Flask (freeze vs `GET /api/slots` + `POST /api/reservations`) |
| [Part 3 notes](part3-hld-flow-notes.md) · [Part 4 coding overview](part4-coding-overview.md) | Site pages for the four diagrams |
| `hld-as-is` / `hld-aws-staging` | **History / probe archive** (keep; do not prefer for the architect cut) |
| [Stack](stack.md) | Dual-env table + four new diagrams + archive HLDs |
| Live staging | https://cafe.artof.link/ |

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE · Honest cut: cts-ai local + Lightsail/Caddy/on-box PG staging · NATURAL track architect lens (MSAIE / cafe.artof.link on camera; local vs AWS as deploy decision).*

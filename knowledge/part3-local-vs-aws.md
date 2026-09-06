# Local (dev) vs AWS MSAIE staging — architecture comparison

**Audience:** Architecture talk (Part 3 NATURAL) + Knowledge Stack/HLD fold-in.  
**On camera:** use the natural spoken beats in `PART3-VARIANT-B-SCRIPT-NATURAL.md` / `PART3-VARIANT-B-VOICEOVER-NATURAL.md`. Prefer **MSAIE staging** / **cafe.artof.link** language.  
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
| **Implementation — how stood up** | Flask + **local Postgres**; Vite/dev frontend | **Caddy (TLS)** → Flask container → **on-box Postgres** (not AEA RDS) |
| **Stack** | React+JSX → Flask → PostgreSQL; fail-closed without DB | Same design: React+JSX → Flask → on-box PostgreSQL; fail-closed without DB |
| **Host tip (current)** | Developer box (cts-ai) | Lightsail instance tip **`73d202d`** (presentation host) |
| **Newsletter** | Store-only until SES env wired | Store-only until SES env wired (do not claim outbound SES) |
| **Honesty** | Not the public demo URL | Temporary MSAIE staging — **not production forever**; not AEA RDS |

---

## Architecture point (one line)

**Same design, two deploy targets** — local (cts-ai) for iterate; cafe.artof.link (MSAIE Lightsail staging) to prove the same React→Flask→Postgres stack on a public HTTPS host — so the HLD holds across environments.

---

## Related assets

| Asset | Role |
| --- | --- |
| `hld-as-is` SVG / `hld-as-is-720.png` | Local MVP vs app staging vs Knowledge Pages |
| `hld-aws-staging` SVG / `hld-aws-staging-720.png` | AWS MSAIE staging path (speak MSAIE / cafe.artof.link; put Lightsail/Caddy/on-box PG in this table) |
| Stack page | https://knowledge.cafe.artof.link/stack.html |
| Live staging | https://cafe.artof.link/ |

**On camera avoid:** “weekend Lightsail staging”, heavy Lightsail / Route53 / Caddy ops jargon.  
**Off camera / this table OK:** Lightsail, Caddy (TLS), on-box Postgres (not AEA RDS), host tip `73d202d`.

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE · Honest cut: cts-ai local + Lightsail/Caddy/on-box PG staging · NATURAL track wording lock (MSAIE / cafe.artof.link on camera).*

# Honesty

Status words are claims. They need a **probe**.

A probe is a command, an HTTP GET, a CI log, or a **committed** file that exists **now**, **this session**. Remembering a previous session, uncommitted files, publishing a hostname, or closing a PR is not a probe.

If evidence is missing, write **Unknown**.

**Probe date for the live rows below:** 2026-09-02 Europe/Berlin (this session).

## This repo, this session

| Claim | Status |
|---|---|
| Knowledge site `knowledge.cafe.artof.link` | HTTPS **GET 200** (`curl` this session). HTTP `http://knowledge.cafe.artof.link/` → **301** `Location: https://knowledge.cafe.artof.link/`. TLS VERIFY_OK. Certificate CN/SAN `knowledge.cafe.artof.link`, Let’s Encrypt YR1, `notAfter=2026-11-30`. DNS CNAME `artofdream.github.io`. Pages API: `cname=knowledge.cafe.artof.link`, cert state **approved**, **`https_enforced=true`**. |
| Restaurant hostname `cafe.artof.link` | **Not Café Fausse App.** `dig` CNAME → AWS ELB `aaafeaf0606ec43f5ad23cfe94d6273e-1de430975830beed.elb.eu-north-1.amazonaws.com.` (`eu-north-1`). Do not claim this hostname is live Café Fausse. Hosting remains future. |
| Restaurant MVP in-repo | **On `main`** (PRs #9 + timezone #12). React + JSX, Flask, PostgreSQL. Local path: Vite `127.0.0.1:5173`, Flask `:5000`, `cafe-pg`. App this session (cts-ai): Journey **J1–J8 PASS** (DB up); **J9 / NFR-3 / NFR-8 PASS** (Vite-only Edge `probe-nfr/` screenshots + theme.css; not Flask+Postgres). This Knowledge VM did not reach Vite. Tunnel / Flask not live (Docker Engine still coming). After the J1–J8 handoff, App reported `cafe-pg` unreachable. |
| Official SRS PDF at `docs/official/…SRS.pdf` | Committed freeze file; working copy `docs/srs.md`; CI fails closed if missing or SHA256 mismatches. |
| AWS / `cafe.artof.link` hosting | **Not in the restaurant MVP cut.** Owner skipped AWS re-auth. Hosting remains future. |
| NFR-1 / NFR-2 timings (3s page load, 2s form submit) | **Unknown** as an SRS-budget claim. Local Vite notes on [Coverage](coverage.md) / [#40](https://github.com/artofdream/aea-interactive-design/issues/40): home **56 ms**, `GET /api/site` **32 ms**. Do not say NFR-1 / NFR-2 **met**. |
| NFR-7 (Chrome, Firefox, Safari, Edge) | **Partial** — Edge **PASS** all routes with screenshots; Firefox **PASS** home; Chrome **Unknown** (not installed on cts-ai); Safari **Unknown** (not reported). Vite-only `:5173`. Not a four-browser claim. [#44](https://github.com/artofdream/aea-interactive-design/issues/44). |
| Journey 1–9 pass/fail | **J1–J8 PASS** (cts-ai local UX, DB up). **J9 / NFR-3 / NFR-8 PASS** (Vite-only Edge `probe-nfr/` screenshots + theme.css; not Flask+Postgres). Recorded on [Coverage](coverage.md). Tunnel / Flask not live (Docker Engine still coming). Do not treat J1–J8 as a public-host probe. |
| System is antifragile | **Do not claim this.** Use ratchet: failures add guides/sensors. |

## Live vs local vs Future

Three labels. Mixing them is a false claim.

| Label | What it is | What it is not |
|---|---|---|
| **Live** | This knowledge map at `knowledge.cafe.artof.link` (HTTPS GET **200** this session; HTTP **301** to HTTPS). | Not the restaurant. Not a reservation host. |
| **Local / tunnel** | Café Fausse App on `main` (Vite / Flask / `cafe-pg`). Demo on localhost or a tunnel after a GET this session. Silent clips are a **look**. | Not proof that a public restaurant host works. |
| **Future** | Intended restaurant hostname `cafe.artof.link` ([#22](https://github.com/artofdream/aea-interactive-design/issues/22)); FS extras [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38). | Not missing grade rows. That hostname is an AWS ELB today, **not** Café Fausse App. |

Picture: [Friday plan](friday-plan.md) mermaid. Same rule on the [Brief](brief.md) Friday section.

## Fail closed (restaurant MVP)

Missing PostgreSQL / no connection / timeout → honest **no** on reservation and newsletter writes. Time slot at 30 tables → **FR-9**; no table assigned. Red CI, missing checks, or checks not probed this session → do not merge. Unreviewed PR (no MRC **COMMENT** role-approve, and no non-author merge path) → do not merge. Author does not merge.

## What this site is not

Florist Path B, Lily’s Florist, 14 hats, Kafka, BFF, 3DX Lab, GitLab Pages/CI. Public repo. GitHub only.

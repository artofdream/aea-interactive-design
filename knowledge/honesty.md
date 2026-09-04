# Honesty

Status words are claims. They need a **probe**.

A probe is a command, an HTTP GET, a CI log, or a **committed** file that exists **now**, **this session**. Remembering a previous session, uncommitted files, publishing a hostname, or closing a PR is not a probe.

If evidence is missing, write **Unknown**.

**Probe date for the live rows below:** 2026-09-04 Europe/Berlin (this session). Journey / NFR evidence rows stay the 2026-09-02 records on [Coverage](coverage.md) — not re-probed tonight.

## This repo, this session

| Claim | Status |
|---|---|
| Knowledge site `knowledge.cafe.artof.link` | HTTPS **GET 200** (`curl` this session, 2026-09-04). HTTP `http://knowledge.cafe.artof.link/` → **301** `Location: https://knowledge.cafe.artof.link/`. TLS VERIFY_OK. Certificate CN/SAN `knowledge.cafe.artof.link`, Let’s Encrypt, `notAfter=2026-11-30`. DNS CNAME `artofdream.github.io`. Pages API enforce/cert: **Unknown** this session (last recorded 2026-09-02). |
| Restaurant hostname `cafe.artof.link` | **Not Café Fausse App.** `dig` CNAME → AWS ELB `aaafeaf0606ec43f5ad23cfe94d6273e-1de430975830beed.elb.eu-north-1.amazonaws.com.` (`eu-north-1`). Do not claim this hostname is live Café Fausse. Hosting remains future. |
| Restaurant MVP in-repo | **On `main`** (PRs #9 + timezone #12). React + JSX, Flask, PostgreSQL. Local path: Vite `127.0.0.1:5173`, Flask `:5000`, `cafe-pg`. App 2026-09-02 (cts-ai): Journey **J1–J8 PASS** (DB up); **J9 / NFR-3 / NFR-8 PASS** (Vite-only Edge `probe-nfr/` screenshots + theme.css; not Flask+Postgres). This Knowledge VM did not reach Vite on `:5173`. **Tunnel this session:** `https://real-goats-shop.loca.lt/` GET **200** (SPA + `/api/health`). Knowledge GET **200** this session. **Can be slow** (~11–18s); interstitial possible. Temporary localtunnel to Flask on cts-ai. **Not** an instant public host. **Not** `cafe.artof.link`. After the J1–J8 handoff, App reported `cafe-pg` unreachable — do not claim writes from the health GET. Old `https://tender-rings-kick.loca.lt/` is stale — do not keep as the live share URL. |
| Official SRS PDF at `docs/official/…SRS.pdf` | Committed freeze file; working copy `docs/srs.md`; CI fails closed if missing or SHA256 mismatches. |
| AWS / `cafe.artof.link` hosting | **Not in the restaurant MVP cut.** Owner skipped AWS re-auth. Hosting remains future. |
| NFR-1 / NFR-2 timings (3s page load, 2s form submit) | **Unknown** as an SRS-budget claim. Local Vite notes on [Coverage](coverage.md) / [#40](https://github.com/artofdream/aea-interactive-design/issues/40): home **56 ms**, `GET /api/site` **32 ms**. Do not say NFR-1 / NFR-2 **met**. |
| NFR-7 (Chrome, Firefox, Safari, Edge) | **Partial** — Edge **PASS** all routes with screenshots; Firefox **PASS** home; Chrome **Unknown** (not installed on cts-ai); Safari **Unknown** (not reported). Vite-only `:5173`. Not a four-browser claim. [#44](https://github.com/artofdream/aea-interactive-design/issues/44). |
| Journey 1–9 pass/fail | **J1–J8 PASS** (cts-ai local UX, DB up). **J9 / NFR-3 / NFR-8 PASS** (Vite-only Edge `probe-nfr/` screenshots + theme.css; not Flask+Postgres). Recorded on [Coverage](coverage.md). Do not treat J1–J8 as a public-host probe. |
| App tunnel tonight | `https://real-goats-shop.loca.lt/` GET **200** this session (SPA HTML, title Café Fausse). `/api/health` GET **200** `{"ok":true}`. Knowledge GET **200** this session (SPA + `/api/health`). **Can be slow** (~11–18s); localtunnel **interstitial possible**. Agent VMs with short timeouts can see 000/TLS fail even when App sees 200. Temporary localtunnel to Flask on cts-ai. **Not** an instant public host. **Not** `cafe.artof.link`. Clips stay fallback. Old `https://tender-rings-kick.loca.lt/` is stale — do not keep as the live share URL. |
| System is antifragile | **Do not claim this.** Use ratchet: failures add guides/sensors. |

## Live vs local vs Future

Three labels. Mixing them is a false claim.

| Label | What it is | What it is not |
|---|---|---|
| **Live** | This knowledge map at `knowledge.cafe.artof.link` (HTTPS GET **200** this session; HTTP **301** to HTTPS). | Not the restaurant. Not a reservation host. |
| **Local / tunnel** | Café Fausse App on `main`. Tunnel this session: `https://real-goats-shop.loca.lt/` GET **200** (SPA + `/api/health`; **slow** / interstitial-possible — not an instant public host). Temporary localtunnel to Flask on cts-ai. Silent clips are the **fallback** look. | Not proof that reservations work on a public host. Not `cafe.artof.link`. |
| **Future** | Intended restaurant hostname `cafe.artof.link` ([#22](https://github.com/artofdream/aea-interactive-design/issues/22)); FS extras [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38). | Not missing grade rows. That hostname is an AWS ELB today, **not** Café Fausse App. |

Picture: [Friday plan](friday-plan.md) mermaid. Same rule on the [Brief](brief.md) Friday section.

## Fail closed (restaurant MVP)

Missing PostgreSQL / no connection / timeout → honest **no** on reservation and newsletter writes. Time slot at 30 tables → **FR-9**; no table assigned. Red CI, missing checks, or checks not probed this session → do not merge. Unreviewed PR (no MRC **COMMENT** role-approve, and no non-author merge path) → do not merge. Author does not merge.

## What this site is not

Florist Path B, Lily’s Florist, 14 hats, Kafka, BFF, 3DX Lab, GitLab Pages/CI. Public repo. GitHub only.

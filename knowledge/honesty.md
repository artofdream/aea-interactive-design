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
| Restaurant MVP in-repo | **On `main`** (PRs #9 + timezone #12). React + JSX, Flask, PostgreSQL. Local path: Vite `127.0.0.1:5173`, Flask `:5000`, `cafe-pg`. Journey 1–9 pass/fail: **Unknown** (not probed this session; this agent cannot reach cts-ai). |
| Official SRS PDF at `docs/official/…SRS.pdf` | Committed freeze file; working copy `docs/srs.md`; CI fails closed if missing or SHA256 mismatches. |
| AWS / `cafe.artof.link` hosting | **Not in the restaurant MVP cut.** Owner skipped AWS re-auth. Hosting remains future. |
| NFR-1 / NFR-2 timings (3s page load, 2s form submit) | **Unknown** — no measured timing probe this session. |
| System is antifragile | **Do not claim this.** Use ratchet: failures add guides/sensors. |

## Fail closed (restaurant MVP)

Missing PostgreSQL / no connection / timeout → honest **no** on reservation and newsletter writes. Time slot at 30 tables → **FR-9**; no table assigned. Red CI, missing checks, or checks not probed this session → do not merge. Unreviewed PR (no GitHub `APPROVE` from a login other than the author) → do not merge.

## What this site is not

Florist Path B, Lily’s Florist, 14 hats, Kafka, BFF, 3DX Lab, GitLab Pages/CI. Public repo. GitHub only.

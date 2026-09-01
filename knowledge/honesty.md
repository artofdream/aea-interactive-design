# Honesty

Status words are claims. They need a **probe**.

A probe is a command, an HTTP GET, a CI log, or a **committed** file that exists **now**, **this session**. Remembering a previous session, uncommitted files, publishing a hostname, or closing a PR is not a probe.

If evidence is missing, write **Unknown**.

## This repo, this session (2026-09-01)

| Claim | Status |
|---|---|
| Knowledge site `https://knowledge.cafe.artof.link/` | **HTTPS GET 200** this session. TLS CN / SAN `knowledge.cafe.artof.link` (Let’s Encrypt YR1; notBefore 2026-09-01, notAfter 2026-11-30). Body is this knowledge map. |
| GitHub Pages `https_enforced` | **false** (`gh api repos/artofdream/aea-interactive-design/pages`). Certificate `state`: `approved`, domains `knowledge.cafe.artof.link`, `expires_at` 2026-11-30. HTTP GET also 200 (no HTTPS redirect). Owner can tick Enforce HTTPS. |
| Restaurant intended hostname `cafe.artof.link` | **Not our live app.** This session: CNAME to `aaafeaf0606ec43f5ad23cfe94d6273e-1de430975830beed.elb.eu-north-1.amazonaws.com`; that hostname did not resolve; `curl` GET failed (code 6). Do not present it as Café Fausse App. Hosting remains future. |
| Restaurant MVP in-repo | **On `main`.** Merged PRs #9 and #12 (`gh pr view`). Local intended: Vite `127.0.0.1:5173`, Flask `:5000`, `cafe-pg`. **This session local GET:** `:5173` and `:5000` connection refused; Docker unavailable. |
| Official SRS PDF at `docs/official/…SRS.pdf` | Committed freeze file present; CI job `srs-present` **success** on `main` `dc42ece` this session |
| AWS / `cafe.artof.link` hosting | **Not in the restaurant MVP.** Hosting remains future |
| CI on `main` | Workflows `CI` and `Knowledge site` **success** on `dc42ece` (probed `gh run list` this session) |
| Assignment collaborator `quantic-grader` | **Unknown / not listed** — `gh` collaborators this session: `artofdream` only. Owner must add; agent must not. |
| Restaurant reservations “work” on a public host | **Unknown** — no public app GET; local API not running here |
| UX journeys 1–9 | **Unknown** — no journey files in this repo; no local GET this session |
| System is antifragile | **Do not claim this.** Use ratchet: failures add guides/sensors |

## Fail closed (restaurant MVP)

Missing PostgreSQL / no connection / timeout → do not accept a booking or newsletter write; return an honest error. Time slot at 30 tables → **FR-9**; no table assigned.

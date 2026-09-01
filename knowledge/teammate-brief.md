# Teammate brief — Wed 2026-09-02 19:00 CET

Thin handoff for the teammate meeting. Not the restaurant. Not a second product.

**When:** Wednesday 2026-09-02, 19:00 CET (Europe/Berlin).  
**What to walk:** this page, then the [FR/NFR coverage matrix](coverage.md). Live claims below were probed **this session** (2026-09-01).

## Where we are

- **MVP = official SRS only.** Working freeze [`docs/srs.md`](srs.md) (FR-1..FR-18, NFR-1..NFR-9). SoT = official PDF in `docs/official/`. Do not invent `FR-19` / `NFR-10`. Do not “improve” freeze prices, address, hours, owners, awards, or reviews.
- **Tracker and CI are GitHub only.** No GitLab, no `glab`, no GitLab Pages. Loop: one finding → one GitHub issue → one branch → one PR against `main`. **Author does not merge their own PR.** Merge gate is GitHub review `APPROVE` from a login that is not the author (`cursor[bot]` for owner-authored PRs). Bugbot comments are a signal, not the gate.
- **Restaurant MVP is on `main`.** Merged GitHub PRs [#9](https://github.com/artofdream/aea-interactive-design/pull/9) (app) and [#12](https://github.com/artofdream/aea-interactive-design/pull/12) (America/New_York date/slot labels). Stack: React + JSX, Flask, PostgreSQL.
- **Local run (documented in README; not running in this cloud session):** Vite `http://127.0.0.1:5173`, Flask `http://127.0.0.1:5000`, Postgres container name `cafe-pg`. This session: GET `:5173` and `:5000` failed (connection refused); Docker was unavailable here. Journey results: **Unknown** (no `journey` files in-repo; no local GET this session).
- **Do not claim this harness is antifragile.** Failures add a tighter guide or sensor (ratchet). Missing DB / full slot (30 tables, FR-9) / timeout = honest **no**.

## Two public surfaces

| Team | Owns | Intended hostname | This session |
|---|---|---|---|
| Café Fausse Knowledge | This thin map (GitHub Actions → GitHub Pages) | `knowledge.cafe.artof.link` | **HTTPS GET 200** at `https://knowledge.cafe.artof.link/` — TLS CN / SAN `knowledge.cafe.artof.link` (Let’s Encrypt). Pages API: `https_enforced` **false**, certificate `approved` (expires 2026-11-30). HTTP also 200 (no force-HTTPS redirect). |
| Café Fausse App | Restaurant MVP in-repo | `cafe.artof.link` | **Not our live app.** DNS CNAME points at an AWS ELB hostname in `eu-north-1`; that target did **not** resolve (GET failed). Hosting remains Future. AWS is not in the restaurant MVP. |

Do not invent other domains. Do not configure DNS from an agent.

## Freeze vs Future

- **Freeze / assignment floor:** FR-1..FR-18 and NFR-1..NFR-9. Home, Menu, Reservations, About Us, Gallery, newsletter, 30-table random assignment, fail-closed writes.
- **Future / not-MVP:** `cafe.artof.link` hosting, AWS, knowledge-site depth beyond this map, GitHub E2E beyond the assignment, florist Path B, 14 hats, GitLab. Park extras on [Future](future.md).

## What to decide at 19:00

1. **Pages HTTPS enforce** — owner can tick GitHub Pages “Enforce HTTPS”. This session `https_enforced` is still **false** (HTTP and HTTPS both 200). Agent must not change that setting.
2. **Assignment collaborator** — `quantic-grader` is required. This session `gh` collaborators listed **only** `artofdream`. **Owner must add** the collaborator; an agent must not.
3. **Presentation honesty** — use the [coverage matrix](coverage.md). Cells marked **Unknown** stay Unknown (no 3s load probe, no four-browser matrix, no local Vite/Flask GET this session, no UX journeys in-repo).
4. **Do not demo `cafe.artof.link` as Café Fausse App.** Wildcard/dangling ELB CNAME is not our host. Demo is local (`127.0.0.1:5173` + `:5000` + `cafe-pg`) when those processes are actually up.
5. **PR discipline stays:** COMMENT or distinct `cursor[bot]` `APPROVE`; author does not merge own PR. Do not batch unrelated findings.

## Nested map (for the hour)

- Surfaces
  - Knowledge: live HTTPS GET 200 this session; `https_enforced` still false
  - App: in-repo on `main`; public hostname not ours
- Evidence
  - Code + GitHub Actions on `main` (CI + Knowledge site **success** on `dc42ece`, probed this session)
  - Local GET and journey runs: Unknown here
- Out of the meeting
  - New FR/NFR IDs
  - Florist / 14 hats / GitLab
  - Claiming the system is antifragile

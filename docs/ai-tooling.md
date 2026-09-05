# AI tooling log

Required for the Quantic assignment. Record of tools used for the Café Fausse restaurant MVP (issue #7). Do not invent FR/NFR IDs in this log.

## Tools

| Tool | Role |
|---|---|
| Cursor Grok 4.6 (cloud agent) | Implementation agent: read `AGENTS.md` / `docs/srs.md` / official PDF path, write React+JSX / Flask / PostgreSQL, tests, GitHub Actions ratchet |
| GitHub (issues, PRs, Actions) | Tracker and CI. No GitLab. Issue #7 is this restaurant cut. |
| pytest | Backend fail-closed tests (missing DB, unreachable DB, 30-table slot) |
| Vite / React 18 (JSX) | Front-end build |
| Flask + psycopg2 | REST API and PostgreSQL access |
| PostgreSQL 16 | Customers + Reservations (FR-17) |

## Prompts / instructions used

- Session SOP: `AGENTS.md`
- Working freeze: `docs/srs.md` (SoT = official PDF in `docs/official/`)
- Engineer / PR procedure: `.cursor/skills/engineer/SKILL.md`, `.cursor/skills/pr-coordinator/SKILL.md`
- Constraint: MVP is FR-1..FR-18 and NFR-1..NFR-9 only; extra ideas stay in `knowledge/future.md`
- Constraint: official images are the four webps in `assets/images/` only; Menu may serve an allowlisted subset of student-recovered extras as labeled presentation aids (not Quantic-official)
- Constraint: author does not merge their own PR

## Usage notes

AI drafted modular Flask packages and React pages from the freeze file `shared/freeze.json`. Menu prices, address, hours, awards, and reviews were copied from the SRS, not rewritten. Student application repositories were not used as a code source.

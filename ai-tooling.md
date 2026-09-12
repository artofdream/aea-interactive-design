# AI tooling log

Required for the Quantic assignment (root `ai-tooling.md`). Same record as `docs/ai-tooling.md`. Tools used for the Café Fausse restaurant MVP (issue #7). Do not invent FR/NFR IDs in this log.

## Tools

| Tool | Role |
|---|---|
| Cursor Grok 4.6 (cloud agent) | Implementation agent: read `AGENTS.md` / `docs/srs.md` / official PDF path, write React+JSX / Flask / PostgreSQL, tests, GitHub Actions ratchet |
| GitHub (issues, PRs, Actions) | Tracker and CI. No GitLab. Issue #7 is this restaurant cut. |
| pytest | Backend fail-closed tests (missing DB, unreachable DB, 30-table slot) |
| Vite / React 18 (JSX) | Front-end build |
| Flask + psycopg2 | REST API and PostgreSQL access |
| PostgreSQL 16 | Customers + Reservations (FR-17) |
| boto3 / Amazon SES v2 | Future #135 optional confirmation after newsletter store. Not a new FR. |

## Prompts / instructions used

- Session SOP: `AGENTS.md`
- Working freeze: `docs/srs.md` (SoT = official PDF in `docs/official/`)
- Engineer / PR procedure: `.cursor/skills/engineer/SKILL.md`, `.cursor/skills/pr-coordinator/SKILL.md`
- Constraint: MVP is FR-1..FR-18 and NFR-1..NFR-9 only; extra ideas stay in `knowledge/future.md`
- Constraint: official images are the four webps in `assets/images/` only; Menu may serve an allowlisted subset of student-recovered extras as labeled presentation aids (not Quantic-official)
- Constraint: author does not merge their own PR
- Future #135: optional SES send after FR-15/16 store; fail soft if unset; not FR-19

## Usage notes

AI drafted modular Flask packages and React pages from the freeze file `shared/freeze.json`. Menu prices, address, hours, awards, and reviews were copied from the SRS, not rewritten. Student application repositories were not used as a code source.

What worked well: freeze-first generation (SRS PDF / `docs/srs.md` → code), CI fail-closed on missing official PDF hash, and keeping Future extras out of the MVP cut.

What did not: treating teammate sample architecture as our staging map; claiming production-forever hosting for temporary MSAIE staging.

Skills / process (Grok + Café): Knowledge Honesty lists which shared Grok skills this lane adopts (PR train rebase, honesty ledger gate, companion plain docs, persona journey validation), the Café-specific Pages ratchet (`knowledge-pages-ratchet`), and AEA **Keep learning and apply** ([AEA #434](https://gitlab.com/artof-group/adaptive-experience-architecture/-/work_items/434); Café [#213](https://github.com/artofdream/aea-interactive-design/issues/213)): when the build teaches something, write it into the harness before the next loop. A skill is process memory — it does not prove Live or a freeze ID without a this-session probe. The #434 row is **Documented** / **Planned** until Pages-probed. See [Honesty](knowledge/honesty.md) (section **Skills / process (Grok + Café)**) and issue [#203](https://github.com/artofdream/aea-interactive-design/issues/203). This log does not close [#204](https://github.com/artofdream/aea-interactive-design/issues/204) (Pages ratchet skill body).

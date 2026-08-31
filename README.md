# aea-interactive-design

Quantic MSAIE **Café Fausse** project, and a transfer of the AEA outer harness onto GitHub (issues, PRs, Actions, knowledge site). Private repository.

**MVP = reconstructed SRS** (`docs/srs.md`, FR-1..FR-18 and NFR-1..NFR-9).  
**Future** = knowledge-site depth, GitHub E2E beyond the assignment, AEA prove / disprove / adjust. Extra restaurant features go in that future plan, not in the first app cut.

This foundation does **not** implement the restaurant. There is nothing to run for React / Flask / PostgreSQL yet.

## Two public surfaces

Documented names only. DNS and Pages enablement are **owner steps**. Do not invent other domains.

| Surface | Intended hostname | What | Live URL |
|---|---|---|---|
| Knowledge | `knowledge.cafe.artof.link` | Thin map (formula, stack, SRS freeze, honesty, Future). GitHub Actions → GitHub Pages. | **Unknown** until a GET probe after Pages + DNS |
| Implementation | `cafe.artof.link` | Restaurant (React + JSX, Flask, PostgreSQL). MVP = SRS. | **Unknown** — not built; no GET probe |

This knowledge site is not the restaurant and not a CMS.

## How to build the knowledge site

From the repo root (Python 3 stdlib; no pip packages):

```bash
python3 knowledge/build.py
```

Output: `knowledge/_site/`. Open `knowledge/_site/index.html`. GitHub Actions runs the same command and, on `main`, deploys GitHub Pages **after the owner sets Pages source to GitHub Actions**. Until that probe, the public URL stays Unknown.

CI also **fails closed** if `docs/srs.md` is missing. Tracker and CI are GitHub only (no GitLab).

## Restaurant app (later)

Not in this cut. When it is implemented:

- Stack: React + JSX, Flask, PostgreSQL.
- Scope: SRS only as MVP. Cite FR/NFR from `docs/srs.md`. Do not invent IDs.
- Fail closed: missing DB / full book (30 tables) / timeout = honest no.
- Intended hostname: `cafe.artof.link` (Unknown until probed).

Course images for that later UI live in `assets/images/` (filenames recovered; see `assets/images/PROVENANCE.md`). Student application code was not copied.

## Required later file

- `docs/ai-tooling.md` — stub present; fill in during implementation (assignment requirement).

## Collaborator

Assignment requires GitHub collaborator **`quantic-grader`**. The **owner** must add that collaborator. Agents must not.

## Honesty

Status words need a probe. Do not claim Pages or `cafe.artof.link` is live without a GET. Do not claim this harness is antifragile.

Read `AGENTS.md` at session start.

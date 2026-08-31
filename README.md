# aea-interactive-design

Quantic MSAIE **Café Fausse** project, and a transfer of the AEA outer harness onto GitHub (issues, PRs, Actions, knowledge site). Private repository.

**MVP = official SRS** (`docs/srs.md`, FR-1..FR-18 and NFR-1..NFR-9; SoT = official PDF in `docs/official/`).  
**Future** = knowledge-site depth, GitHub E2E beyond the assignment, AEA prove / disprove / adjust. Extra restaurant features go in that future plan, not in the first app cut.

This foundation does **not** implement the restaurant. There is nothing to run for React / Flask / PostgreSQL yet. **AWS is not in this PR.** Knowledge site = GitHub Pages. `cafe.artof.link` hosting remains future.

## Teams and two public surfaces

Documented names only. DNS and Pages enablement are **owner steps**. Do not invent other domains.

| Team | Intended hostname | What | Live URL |
|---|---|---|---|
| Café Fausse Knowledge | `knowledge.cafe.artof.link` | Thin map (formula, stack, SRS freeze, honesty, Future). GitHub Actions → GitHub Pages. | **Unknown** until a GET **this session** after Pages + DNS |
| Café Fausse App | `cafe.artof.link` | Restaurant (React + JSX, Flask, PostgreSQL). MVP = SRS. | **Unknown** — not built; hosting future; no GET this session |

This knowledge site is not the restaurant and not a CMS.

## How to build the knowledge site

From the repo root (Python 3 stdlib; no pip packages):

```bash
python3 knowledge/build.py
```

Output: `knowledge/_site/`. Open `knowledge/_site/index.html`. GitHub Actions runs the same command and, on `main`, deploys GitHub Pages **after the owner sets Pages source to GitHub Actions**. Until that probe, the public URL stays Unknown.

CI **fails closed** if `docs/srs.md` is missing or if the official PDF/zip SHA256 does not match the freeze. Tracker and CI are GitHub only (no GitLab). **Author does not merge their own PR.**

## Restaurant app (later — Café Fausse App)

Not in this cut. When it is implemented:

- Stack: React + JSX, Flask, PostgreSQL.
- Scope: SRS only as MVP. Cite FR/NFR from `docs/srs.md`. Do not invent IDs.
- Fail closed: missing DB / full book (30 tables) / timeout = honest no.
- Intended hostname: `cafe.artof.link` (Unknown until probed). Hosting is future (not AWS in this PR).

Course images: Quantic-official pack is **four** webps only (`assets/images/`, zip SHA256 in `docs/official/PROVENANCE.md`). Seventeen student-recovered files are in `assets/images/supplemental-not-official/` and are **not** official. Student application code was not copied.

## Required later file

- `docs/ai-tooling.md` — stub present; fill in during implementation (assignment requirement).

## Collaborator

Assignment requires GitHub collaborator **`quantic-grader`**. The **owner** must add that collaborator. Agents must not.

## Honesty

A status word is a claim. Probe **this session** or write Unknown. Uncommitted files are not shared memory. Do not claim this harness is antifragile.

Read `AGENTS.md` at session start. Skills (not 14 hats): `knowledge-guardian`, `coherence-guardian`, `product-owner`, `engineer`.

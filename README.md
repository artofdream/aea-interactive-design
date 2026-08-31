# aea-interactive-design

Quantic MSAIE **Café Fausse** project, and a transfer of the AEA outer harness onto GitHub (issues, PRs, Actions, knowledge site).

**MVP = official SRS** (`docs/srs.md`, FR-1..FR-18 and NFR-1..NFR-9; SoT = official PDF in `docs/official/`).  
**Future** = knowledge-site depth, GitHub E2E beyond the assignment, AEA prove / disprove / adjust. Extra restaurant features go in that future plan, not in this app cut.

Tracker and CI are **GitHub only**. No GitLab. **AWS is not in this PR.** Knowledge site = GitHub Pages. `cafe.artof.link` hosting remains future.

## Teams and two public surfaces

Documented names only. DNS and Pages enablement are **owner steps**. Do not invent other domains.

| Team | Intended hostname | What | Live URL |
|---|---|---|---|
| Café Fausse Knowledge | `knowledge.cafe.artof.link` | Thin map (formula, stack, SRS freeze, honesty, Future). GitHub Actions → GitHub Pages. | **Unknown** until a GET **this session** after Pages + DNS |
| Café Fausse App | `cafe.artof.link` | Restaurant (React + JSX, Flask, PostgreSQL). MVP = SRS. | **Unknown** — hosting future; no public GET this session |

This knowledge site is not the restaurant and not a CMS.

## Café Fausse restaurant (local)

React (JSX) front-end, Flask API, PostgreSQL. Scope is the official SRS only. Cite `FR-*` / `NFR-*` from `docs/srs.md`. Do not invent IDs.

Fail closed: missing database, a time slot with all **30** tables booked, or a timeout is an honest **no** — not a guessed yes.

### Prerequisites

- Python 3.12
- Node.js 22
- PostgreSQL 16 (local install, or Docker Compose below)

### Database

Create a database and apply FR-17 tables (`customers`, `reservations`):

```bash
# Option A — Docker (Postgres only; not AWS)
docker compose up -d db
export DATABASE_URL=postgresql://cafe:cafe@127.0.0.1:5432/cafe_fausse

# Option B — local PostgreSQL
createdb cafe_fausse
export DATABASE_URL=postgresql://USER:PASSWORD@127.0.0.1:5432/cafe_fausse
```

Then:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
cd backend && python -m cafe_fausse init-db
```

Copy `.env.example` to `.env` if you prefer a file over `export`.

### Run the API

From `backend/` with `DATABASE_URL` set:

```bash
flask --app wsgi run --port 5000
```

Or: `gunicorn --bind 127.0.0.1:5000 wsgi:app`

### Run the site

```bash
cd frontend
npm ci
npm run dev
```

Open `http://127.0.0.1:5173`. Vite proxies `/api` to Flask on port 5000.

Pages: Home, Menu, Reservations, About Us, Gallery, Contact. Newsletter signup is on Contact and in the footer.

### Tests

```bash
# API (needs DATABASE_URL for booking/newsletter storage tests; fail-closed tests do not)
cd backend && pip install -r requirements.txt -r requirements-dev.txt && pytest

# Front-end unit tests + production build
cd frontend && npm ci && npm test && npm run build

# Freeze facts (prices, address, no invented FR-19 / NFR-10)
python3 scripts/check_srs_facts.py
```

GitHub Actions workflow **App** runs the same checks. Existing **CI** (SRS PDF/zip SHA256) and **Knowledge site** workflows are unchanged.

### Course images

Quantic-official pack is **four** webps only (`assets/images/`, zip SHA256 in `docs/official/PROVENANCE.md`). Seventeen student-recovered files are in `assets/images/supplemental-not-official/` and are **not** official. The gallery shows official images first and labels supplemental photos **Not official**. Student application code was not copied.

### Hosting

Intended hostname: `cafe.artof.link`. Live URL: **Unknown**. This PR is local-run only. No AWS. Do not treat the hostname as a deploy.

## How to build the knowledge site

From the repo root (Python 3 stdlib; no pip packages):

```bash
python3 knowledge/build.py
```

Output: `knowledge/_site/`. Open `knowledge/_site/index.html`. GitHub Actions runs the same command and, on `main`, deploys GitHub Pages **after the owner sets Pages source to GitHub Actions**. Until that probe, the public URL stays Unknown.

CI **fails closed** if `docs/srs.md` is missing or if the official PDF/zip SHA256 does not match the freeze. Tracker and CI are GitHub only (no GitLab). **Author does not merge their own PR.**

## Assignment files

- `docs/ai-tooling.md` — tools and usage for this implementation.
- `docs/srs.md` — working ID freeze of the official PDF.

## Collaborator

Assignment requires GitHub collaborator **`quantic-grader`**. The **owner** must add that collaborator. Agents must not.

## Honesty

A status word is a claim. Probe **this session** or write Unknown. Uncommitted files are not shared memory. Do not claim this harness is antifragile. Do not claim `cafe.artof.link` is live.

Read `AGENTS.md` at session start. Hats (not 14): `knowledge-guardian`, `coherence-guardian`, `product-owner`, `engineer`. PR procedure (not a hat): `pr-coordinator`.

# aea-interactive-design

Quantic MSAIE **Café Fausse** project, and a transfer of the AEA outer harness onto GitHub (issues, PRs, Actions, knowledge site). Public repository.

**MVP = official SRS** (`docs/srs.md`, FR-1..FR-18 and NFR-1..NFR-9; SoT = official PDF in `docs/official/`).  
**Future** = AWS, `cafe.artof.link` hosting/DNS, knowledge-site depth, GitHub E2E beyond the assignment, AEA prove / disprove / adjust. Extra restaurant features go in that future plan, not in this app cut.

The restaurant app lives in this repo (`frontend/` React + JSX, `backend/` Flask, PostgreSQL). **AWS is not in this PR.** `cafe.artof.link` live URL: **Unknown** (no GET this session). Knowledge site = GitHub Pages (live URL **Unknown** until a GET this session after Pages + DNS).

## Teams and two public surfaces

Documented names only. DNS and Pages enablement are **owner steps**. Do not invent other domains.

| Team | Intended hostname | What | Live URL |
|---|---|---|---|
| Café Fausse Knowledge | `knowledge.cafe.artof.link` | Thin map (formula, stack, SRS freeze, honesty, Future). GitHub Actions → GitHub Pages. | **Unknown** until a GET **this session** after Pages + DNS |
| Café Fausse App | `cafe.artof.link` | Restaurant (React + JSX, Flask, PostgreSQL). MVP = SRS. | **Unknown** — hosting future; no GET this session |

This knowledge site is not the restaurant and not a CMS.

## Restaurant app — local deploy

Stack constraint from the SRS: React with JSX, CSS Flexbox/Grid, Flask REST API, PostgreSQL.

### 1. Environment

Copy `.env.example` to `.env` and set `DATABASE_URL`.

```bash
cp .env.example .env
```

Default:

```text
DATABASE_URL=postgresql://cafe:cafe@127.0.0.1:5432/cafe_fausse
DB_CONNECT_TIMEOUT=2
DB_STATEMENT_TIMEOUT_MS=2000
```

### 2. PostgreSQL

Create a database the URL can reach. Example with Docker:

```bash
docker run -d --name cafe-pg \
  -e POSTGRES_USER=cafe \
  -e POSTGRES_PASSWORD=cafe \
  -e POSTGRES_DB=cafe_fausse \
  -p 5432:5432 \
  postgres:16
```

Example with a local Postgres superuser:

```bash
createuser cafe
createdb -O cafe cafe_fausse
psql -c "ALTER USER cafe WITH PASSWORD 'cafe';"
```

If PostgreSQL is missing or unreachable, reservations and newsletter **fail closed**: the API returns an error and does **not** pretend the write succeeded.

### 3. Backend (Flask)

Python 3.12 recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
export PYTHONPATH=backend
set -a; source .env; set +a
python -m cafe_fausse.init_db
python -m cafe_fausse
```

API listens on `http://127.0.0.1:5000`. Apply `backend/schema.sql` via `python -m cafe_fausse.init_db` (Customers + Reservations, FR-17).

### 4. Frontend (React + JSX)

```bash
cd frontend
npm install
npm run dev
```

Vite serves `http://127.0.0.1:5173` and proxies `/api` and `/images` to Flask.

Production-style (Flask serves the built SPA):

```bash
cd frontend && npm install && npm run build && cd ..
export PYTHONPATH=backend
python -m cafe_fausse
```

Then open `http://127.0.0.1:5000`.

### 5. Tests

```bash
export PYTHONPATH=backend
export DATABASE_URL=postgresql://cafe:cafe@127.0.0.1:5432/cafe_fausse
pytest
```

Fail-closed coverage includes: missing `DATABASE_URL`, unreachable Postgres, and a time slot with 30 tables already booked (no 31st table; FR-9).

## How to build the knowledge site

From the repo root (Python 3 stdlib; no pip packages):

```bash
python3 knowledge/build.py
```

Output: `knowledge/_site/`. Open `knowledge/_site/index.html`. GitHub Actions runs the same command and, on `main`, deploys GitHub Pages **after the owner sets Pages source to GitHub Actions**. Until that probe, the public URL stays Unknown.

CI **fails closed** if `docs/srs.md` is missing or if the official PDF/zip SHA256 does not match the freeze. App CI runs Flask tests against PostgreSQL and builds the React frontend. Tracker and CI are GitHub only (no GitLab). **Author does not merge their own PR.**

## Scope (Café Fausse App)

- Home, Menu, Reservations, About Us, Gallery (FR-1..FR-14).
- Newsletter signup stored in PostgreSQL (FR-15, FR-16).
- Random table from 30; fully booked slot returns an error, not a table (FR-6..FR-9, FR-18).
- Freeze data (menu prices, address, hours, owners, awards, reviews) from `docs/srs.md` / `shared/freeze.json`. Do not invent FR-19 / NFR-10.

Course images: Quantic-official pack is **four** webps only (`assets/images/`, zip SHA256 in `docs/official/PROVENANCE.md`). Seventeen student-recovered files are in `assets/images/supplemental-not-official/` and are **not** official. The app serves only the official four. Student application code was not copied.

## Required assignment file

- `docs/ai-tooling.md` — tools used for this implementation.

## Collaborator

Assignment requires GitHub collaborator **`quantic-grader`**. The **owner** must add that collaborator. Agents must not.

## Honesty

A status word is a claim. Probe **this session** or write Unknown. Uncommitted files are not shared memory. Do not claim this harness is antifragile. Do not claim `cafe.artof.link` or Pages is live without a GET this session.

Read `AGENTS.md` at session start. Hats (not 14): `knowledge-guardian`, `coherence-guardian`, `product-owner`, `engineer`. PR procedure (not a hat): `pr-coordinator`.

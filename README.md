# aea-interactive-design

Quantic MSAIE **Café Fausse** project, and a transfer of the AEA outer harness onto GitHub (issues, PRs, Actions, knowledge site). Public repository.

**MVP = official SRS** (`docs/srs.md`, FR-1..FR-18 and NFR-1..NFR-9; SoT = official PDF in `docs/official/`).  
**Future** = permanent restaurant hosting ([#22](https://github.com/artofdream/aea-interactive-design/issues/22)), knowledge-site depth, GitHub E2E beyond the assignment, AEA prove / disprove / adjust, and beyond-SRS extras ([#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38)). Extra restaurant features go in that future plan, not in this app cut. Future is **not** “AWS does not exist”: weekend Lightsail staging ([#57](https://github.com/artofdream/aea-interactive-design/issues/57)) is already a probed share.

The restaurant app lives in this repo (`frontend/` React + JSX, `backend/` Flask, PostgreSQL). AWS is **not** in the restaurant MVP code cut (no AWS in the first app PR). Weekend staging is a separate infra issue ([#57](https://github.com/artofdream/aea-interactive-design/issues/57)), not forever production. Permanent hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22).

**Probe 2026-09-05 Europe/Berlin (this session):** `GET https://cafe.artof.link/` **200** (title Café Fausse; remote IP `54.165.102.60`); `/api/health` **200** `{"ok":true}`; `/operator` **200**; `/api/operator` **200**. TLS VERIFY_OK, CN `cafe.artof.link`, Let’s Encrypt `notAfter=2026-12-04`. DNS **A** `54.165.102.60` (Route53 TTL 60; Lightsail `cafe-fausse-staging` us-east-1; Caddy LE). HTTP → **308** HTTPS. Interim backup: `GET https://54-165-102-60.sslip.io/` **200**; `/api/health` **200** `{"ok":true}`. Knowledge: `GET https://knowledge.cafe.artof.link/` **200** (GitHub Pages; CNAME `artofdream.github.io`); HTTP → **301** HTTPS; TLS CN/SAN match, Let’s Encrypt `notAfter=2026-11-30`. Tunnel `https://shaky-deer-drive.loca.lt/` **timeout** (curl 28, 15s) — demoted; not live share. AEA RDS untouched. Newsletter = store only (**FR-15** / **FR-16**); no outbound mailer. Staging stays **up** until the owner explicitly requests tear-down. Monday **2026-09-08 16:00 Europe/Berlin** is an evaluate-only checkpoint (not automatic tear-down). Whether Quantic graders need the host up for video evaluation remains **Unknown** until the owner shares correspondence.

## Teams and two public surfaces

Documented names only. Do not invent other domains. A status word needs a GET **this session** or it stays **Unknown**.

| Team | Intended hostname | What | Live URL (probe 2026-09-05 Europe/Berlin) |
|---|---|---|---|
| Café Fausse Knowledge | `knowledge.cafe.artof.link` | Thin map (formula, stack, SRS freeze, honesty, Future). GitHub Actions → GitHub Pages. | HTTPS **GET 200** this session. HTTP **301** to HTTPS. TLS VERIFY_OK; CN/SAN `knowledge.cafe.artof.link`; Let’s Encrypt `notAfter=2026-11-30`. CNAME `artofdream.github.io`. |
| Café Fausse App | `cafe.artof.link` | Restaurant (React + JSX, Flask, PostgreSQL). MVP = SRS. | HTTPS **GET 200** this session (`/`, `/api/health` `{"ok":true}`, `/operator`). Lightsail `cafe-fausse-staging` us-east-1, IP `54.165.102.60`, Route53 **A** TTL 60, Caddy LE. Weekend staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57) — **not** forever production. Staging kept until owner decision. Monday **2026-09-08 16:00 Europe/Berlin** evaluate-only (not auto tear-down). Whether graders need the host for video evaluation remains **Unknown** until the owner shares correspondence. Interim backup `https://54-165-102-60.sslip.io/`. Permanent hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22). |

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

Output: `knowledge/_site/`. Open `knowledge/_site/index.html`. GitHub Actions runs the same command and, on `main`, deploys GitHub Pages. Public URL this session: `https://knowledge.cafe.artof.link/` HTTPS **GET 200** (2026-09-05). Re-probe next session or write **Unknown**.

CI **fails closed** if `docs/srs.md` is missing or if the official PDF/zip SHA256 does not match the freeze. App CI runs Flask tests against PostgreSQL and builds the React frontend. Tracker and CI are GitHub only (no GitLab). **Author does not merge their own PR.**

## Scope (Café Fausse App)

- Home, Menu, Reservations, About Us, Gallery (FR-1..FR-14).
- Newsletter signup stored in PostgreSQL (FR-15, FR-16).
- Random table from 30; fully booked slot returns an error, not a table (FR-6..FR-9, FR-18).
- Freeze data (menu prices, address, hours, owners, awards, reviews) from `docs/srs.md` / `shared/freeze.json`. Do not invent FR-19 / NFR-10.

Course images: Quantic-official pack is **four** webps only (`assets/images/`, zip SHA256 in `docs/official/PROVENANCE.md`). Seventeen student-recovered files are in `assets/images/supplemental-not-official/` and are **not** official. Flask `/images/` serves the official four plus an allowlisted subset mapped for Menu presentation (`shared/menu-presentation.json`). Unused supplemental files stay unserved. Student application code was not copied.

## Required assignment file

- `docs/ai-tooling.md` — tools used for this implementation.

## Collaborator

Assignment requires GitHub collaborator **`quantic-grader`**. The **owner** must add that collaborator. Agents must not.

## Honesty

A status word is a claim. Probe **this session** or write Unknown. Uncommitted files are not shared memory. Do not claim this harness is antifragile. Do not claim `cafe.artof.link` is forever production. Weekend staging (#57) and Pages were GET **200** this session (2026-09-05); a previous session is not a probe.

Read `AGENTS.md` at session start. Hats (not 14): `knowledge-guardian`, `coherence-guardian`, `product-owner`, `engineer`. PR procedure (not a hat): `pr-coordinator`.

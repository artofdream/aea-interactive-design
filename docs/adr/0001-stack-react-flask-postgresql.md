# ADR-0001: Stack: React + JSX frontend, Flask API, PostgreSQL

## Status

Accepted (retroactive, recorded 2026-10-07)

## Date

2026-08-31: the SRS freeze landed (PR #1) and the restaurant MVP landed on `main` (PR #9).

## Context

The official SRS (`docs/srs.md` §1.2, §2.4, §3.3.2) fixes the stack. The frontend must be React with JSX, styled with CSS Flexbox or Grid, and the backend must be Flask with a PostgreSQL database. The repo is graded against that SRS (`AGENTS.md`: "MVP = official SRS freeze"). So the stack was a constraint, not an open choice. The open choices were the toolchain, the module layout and the data-access style inside it.

## Decision

- **Frontend:** a React 18 single-page app in JSX under `frontend/`, built with Vite. Client-side routes (`react-router-dom`) cover the five SRS pages (Home, Menu, Reservations, About Us, Gallery) plus the read-only `/operator` recording helper, which is not a requirement. Styling lives in `frontend/src/styles/theme.css` and uses Flexbox/Grid (`repeat(auto-fit, minmax(…))`) plus a `@media (max-width: 800px)` breakpoint.
- **API:** the Flask app factory `create_app()` in `backend/cafe_fausse/__init__.py`. Routes are registered directly with `@app.get` / `@app.post` (no Blueprints). Logic is split into modules: `slots.py`, `reservations.py`, `newsletter.py`, `db.py`, `validate.py` and `content.py`. JSON lives under `/api/*`. In production-style runs the same Flask process also serves the built SPA from `frontend/dist`.
- **Database:** PostgreSQL through `psycopg2` with hand-written SQL (no ORM). `backend/schema.sql` defines the `customers` and `reservations` tables (FR-17), and `python -m cafe_fausse.init_db` applies them.
- **Official copy** (menu, hours, awards, reviews) is kept in `shared/freeze.json`, not in Postgres. See [ADR-0005](0005-srs-freeze-fail-closed-ci.md).

## Consequences

- The SRS stack constraint is met directly. No alternative stack is on record, because the SRS mandates this one.
- There are two toolchains, Node for the frontend build/test and Python for the API. CI therefore has separate `Restaurant frontend build` and `Restaurant API tests` jobs.
- Raw SQL keeps the capacity logic visible and reviewable ([ADR-0003](0003-slot-capacity-model.md)). It also means schema changes are manual: `CREATE TABLE IF NOT EXISTS`, with no migration tool.
- AWS is not part of the MVP code. Hosting is a separate decision ([ADR-0002](0002-staging-topology.md)).

## Related requirements

Related requirements: FR-4, FR-17, FR-18, NFR-8, NFR-9

## Evidence

- `ac1c485` feat: land SRS freeze, knowledge map, and GitHub harness (PR #1): `docs/srs.md` with the stack constraints.
- `5603d85` feat: implement Café Fausse restaurant MVP (#7) (PR #9): `frontend/`, `backend/cafe_fausse/`, `backend/schema.sql`.
- `8bacf1e` Knowledge: developer system map (stack, API, schema, FE/BE) (PR #161): pinned versions, and routes on the app factory rather than Blueprints.

## OPEN

- OPEN: Why Vite was chosen over another React toolchain is not recorded.
- OPEN: Why `psycopg2` with raw SQL was chosen over an ORM (for example SQLAlchemy), and why there is no migration tool, is not recorded.
- OPEN: Why routes sit on the app factory instead of Flask Blueprints is not recorded. `knowledge/developer-system-map.md` records the fact but not the reason.

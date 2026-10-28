# ADR-0005: SRS ID freeze, `freeze.json` official copy, and fail-closed CI gates

## Status

Accepted (retroactive, recorded 2026-10-07)

## Date

2026-08-31: the freeze, the PDF hashes and the first CI gate landed (PRs #1, #5, #9). 2026-09-05: the one-issue gate was added (PR #115).

## Context

The project is graded against the official SRS PDF. `AGENTS.md` sets four rules: cite FR/NFR IDs only from `docs/srs.md` and never invent FR-19 or NFR-10; do not "improve" freeze data such as prices, address, hours, owners, awards and reviews; fail closed when the freeze is missing; and work ratchet-only, so failures add guards and never remove them.

## Decision

- **ID freeze:** `docs/srs.md` is the working freeze of the official PDF (FR-1..FR-18, NFR-1..NFR-9). The PDF and the four-image zip are committed under `docs/official/`, with SHA256 hashes pinned in CI.
- **Official copy:** `shared/freeze.json` holds the SRS copy (name, address, phone, hours, history, founders, locally-sourced text, menu with prices, awards, reviews, official images) plus app constants (`timezone`, `slotIntervalMinutes`, `tableCount`). The React pages import it at build time, and Flask serves the same file through `/api/menu` and `/api/site`. The file is **hand-maintained**; the repo has no generator script. `backend/tests/test_freeze.py` fails if the menu prices, address, phone, hours, history, awards or reviews drift from `docs/srs.md`.
- **CI gates** (`.github/workflows/ci.yml`):
  - `SRS freeze present (fail-closed)` fails if `docs/srs.md` is missing, if any `**FR-n:**` / `**NFR-n:**` entry is missing, or if the PDF or zip is missing or its SHA256 differs.
  - `GitHub only (no GitLab CI files)` fails if `.gitlab-ci.yml` or `.gitlab/` exists.
  - `One issue per PR (fail-closed)` runs `scripts/ci/check_one_issue_closer.py`. It fails a PR body that closes more than one issue, and it reruns when the body is edited.
  - `Restaurant API tests` runs pytest against a `postgres:16` service. This includes fail-closed tests that run with no database, an unreachable database and a connect timeout, and that expect HTTP 503.
- This ADR set adds the gate `ADR related requirements exist in SRS (fail-closed)` (`scripts/ci/check_adr_requirements.py`), so ADRs cannot cite an ID that `docs/srs.md` does not define.

## Consequences

- An invented ID, a deleted freeze entry or a swapped PDF turns CI red, so the freeze can only change on purpose.
- Fields that `test_freeze.py` does not compare (for example the restaurant name, the founders and the locally-sourced text) can drift without a red build.
- The database-backed tests use the `require_db` fixture, which **skips** rather than fails when `DATABASE_URL` is unset. CI always sets it. But if that variable were lost, those tests would quietly become skips instead of a red build. The fail-closed behaviour of the *app* (503) is still tested without a database.
- Ratchet: gates are only ever added. Going green by deleting a check counts as a regression.

## Related requirements

Related requirements: FR-1, FR-2, FR-5, FR-10, FR-11, FR-14

`freeze.json` carries the SRS copy for these IDs. The CI gates protect the ID freeze itself, which has no FR or NFR ID of its own.

## Evidence

- `ac1c485` feat: land SRS freeze, knowledge map, and GitHub harness (PR #1): `docs/srs.md` and the `SRS freeze present` job.
- `e49f40c` docs: pin official PDF/zip SHA256 and isolate supplemental images (PR #1).
- `ecd61d2` fix: require **FR-n:** freeze entries in CI (#2) (PR #5).
- `5603d85` feat: implement Café Fausse restaurant MVP (#7) (PR #9): `shared/freeze.json`, `test_freeze.py`, the `GitHub only` and `Restaurant API tests` jobs, and the fail-closed tests.
- `cb03b3c` Ratchet: split multi-item issues; one closer per PR (#113) (PR #115).
- `17d7019` Ratchet: re-run one-issue-closer on PR body edits (#113) (PR #115).

## OPEN

- OPEN: Why `freeze.json` is maintained by hand instead of generated from `docs/srs.md` is not recorded.
- OPEN: Whether `require_db` should fail instead of skip when `DATABASE_URL` is missing in CI is undecided. Changing it is a test-harness change outside this ADR set.

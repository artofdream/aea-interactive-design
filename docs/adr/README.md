# Architecture Decision Records (ADRs)

These are lightweight, **retroactive** ADRs for the Café Fausse restaurant app (React + JSX, Flask, PostgreSQL). They were recorded on 2026-10-07 for issue #227. Each one records a decision that had already landed on `main`, and cites the commit(s) and PR where it landed. Wherever a rationale is not backed by a commit, a doc or the code, the ADR says so with an `OPEN:` line instead of guessing.

Requirement IDs come from the working freeze in [`docs/srs.md`](../srs.md) only (FR-1..FR-18, NFR-1..NFR-9). No other ID is used.

## Index

| ADR | Title | Related requirements |
|---|---|---|
| [ADR-0001](0001-stack-react-flask-postgresql.md) | Stack: React + JSX frontend, Flask API, PostgreSQL | FR-4, FR-17, FR-18, NFR-8, NFR-9 |
| [ADR-0002](0002-staging-topology.md) | Staging topology: one Lightsail instance (Caddy → Flask → on-host PostgreSQL) for cafe.artof.link | none |
| [ADR-0003](0003-slot-capacity-model.md) | Reservation slot and capacity model: 30 tables per seating, HTTP 409 when full, fail closed | FR-6, FR-7, FR-8, FR-9, FR-18, NFR-5, NFR-6 |
| [ADR-0004](0004-store-only-newsletter.md) | Store-only newsletter; optional SES mail only after the store, failing soft | FR-15, FR-16, NFR-6 |
| [ADR-0005](0005-srs-freeze-fail-closed-ci.md) | SRS ID freeze, `freeze.json` official copy, and fail-closed CI gates | FR-1, FR-2, FR-5, FR-10, FR-11, FR-14 |
| [ADR-0006](0006-restaurant-timezone.md) | Restaurant-local time zone (America/New_York) for slots and reservations | FR-2, FR-6, FR-7 |
| [ADR-0007](0007-official-images-only.md) | Only the official four-image pack counts as official; student-recovered images are isolated and allowlisted | FR-3, FR-12 |

Every status is `Accepted (retroactive, recorded 2026-10-07)`.

The per-ID view is the **Design** column in [`knowledge/coverage.md`](../../knowledge/coverage.md).

## Format

Each ADR is one Markdown file named `NNNN-short-title.md` with these sections:

1. **Title**: `# ADR-NNNN: …`
2. **Status**
3. **Date**: when the decision landed
4. **Context**
5. **Decision**
6. **Consequences**
7. **Related requirements**: must include a line that starts exactly with `Related requirements:`, followed by official IDs separated by commas (for example `FR-9, NFR-5`) or the single word `none`
8. **Evidence**: commit short SHA plus subject, and the PR number if there is one
9. **OPEN**: one `OPEN:` line per rationale that is not backed by evidence

## CI check

The `ADR related requirements exist in SRS (fail-closed)` job runs `python3 scripts/ci/check_adr_requirements.py`. It fails in each of these cases:

- `docs/srs.md` is missing, unreadable, or defines no `**FR-n:**` / `**NFR-n:**` entries.
- `docs/adr/` is missing or contains no ADR files.
- An ADR has no `Related requirements:` line, or has more than one.
- A `Related requirements:` line cites an ID that is not defined in `docs/srs.md` (for example FR-19 or NFR-10), or contains a token that is not an ID.

`none` is allowed. Run `--self-test` to exercise the parser without touching the repo files.

## Adding an ADR

Use the next free number and copy the format above. Cite only IDs defined in `docs/srs.md`. Update this index and the Design column in `knowledge/coverage.md`.

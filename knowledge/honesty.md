# Honesty

Status words are claims. They need a **probe**.

A probe is a command, an HTTP GET, a CI log, or a file that exists **now**. Remembering a previous session, publishing a hostname, or closing a PR is not a probe.

If evidence is missing, write **Unknown**.

## This repo, today

| Claim | Status |
|---|---|
| Knowledge site intended hostname `knowledge.cafe.artof.link` | Documented. **Live URL Unknown** (no GET; Pages/DNS owner step) |
| Restaurant intended hostname `cafe.artof.link` | Documented. **Live URL Unknown** (app not built; no GET) |
| Reconstructed SRS present at `docs/srs.md` | Must be true in git; CI fails closed if the file is missing |
| Restaurant reservations work | **Unknown** — not implemented in the foundation cut |
| System is antifragile | **Do not claim this.** Use ratchet: failures add guides/sensors |

## Fail closed (later restaurant MVP)

When Flask/PostgreSQL exist: missing database, a full book (30 tables, FR-9), or a timeout is an honest **no**, not a guessed **yes**.

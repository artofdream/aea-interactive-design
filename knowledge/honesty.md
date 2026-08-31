# Honesty

Status words are claims. They need a **probe**.

A probe is a command, an HTTP GET, a CI log, or a **committed** file that exists **now**, **this session**. Remembering a previous session, uncommitted files, publishing a hostname, or closing a PR is not a probe.

If evidence is missing, write **Unknown**.

## This repo, today

| Claim | Status |
|---|---|
| Knowledge site intended hostname `knowledge.cafe.artof.link` (Café Fausse Knowledge) | Documented. **Live URL Unknown** (no GET this session after Pages/DNS) |
| Restaurant intended hostname `cafe.artof.link` (Café Fausse App) | Documented. **Live URL Unknown** (app not built; hosting future; no GET this session) |
| Official SRS PDF at `docs/official/…SRS.pdf` | GET 200 this session; working freeze `docs/srs.md`; CI fails closed if missing |
| AWS / `cafe.artof.link` hosting | **Not in this PR.** Owner skipped AWS re-auth. Hosting remains future |
| Restaurant reservations work | **Unknown** — not implemented in the foundation cut |
| System is antifragile | **Do not claim this.** Use ratchet: failures add guides/sensors |

## Fail closed (later restaurant MVP)

When Flask/PostgreSQL exist: missing database, a full book (30 tables, FR-9), or a timeout is an honest **no**, not a guessed **yes**.

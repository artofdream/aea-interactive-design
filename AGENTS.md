# AGENTS.md — session-start SOP

This is a student / GitHub E2E repo for **Café Fausse** (Quantic MSAIE) and a transfer of the AEA **outer harness** onto a different stack. Read this file before writing code.

**MVP = reconstructed SRS** (`docs/srs.md`, FR-1..FR-18 and NFR-1..NFR-9). Everything else is future or refined — not the first restaurant cut, and not a second product on the knowledge site.

Do not claim this system is antifragile.

## Two public surfaces (pattern, not product)

| Surface | Intended hostname | What it is | Live URL |
|---|---|---|---|
| Knowledge | `knowledge.cafe.artof.link` | Formula, stack, SRS freeze, honesty. GitHub Pages. Not the restaurant, not a CMS. | **Unknown** until a GET probe after the owner enables Pages + DNS |
| Implementation | `cafe.artof.link` | Restaurant app (React + JSX, Flask, PostgreSQL). MVP = SRS. | **Unknown** — not built in this foundation; no GET probe |

Do not invent other domains. Do not configure DNS from an agent. Owner step: enable GitHub Pages (Actions), then DNS for the two hostnames.

Tracker and CI are **GitHub only**. No GitLab, no `glab`, no GitLab Pages, no GitLab CI.

## Session start (every turn)

1. Read this file, `docs/srs.md` (ID freeze), and `research/daily-briefs/YYYY-MM-DD.md` for **today** (Europe/Berlin). If today’s brief is missing, create it before doing other work.
2. Knowledge before code: for restaurant work, read the knowledge home + stack + SRS freeze pages first. Do not implement features that are not in the SRS freeze.
3. Honesty: status words are claims; they need a probe. If evidence is missing, write **Unknown**.
4. ID freeze: cite `FR-*` / `NFR-*` from `docs/srs.md`. Do not invent IDs. If an official Quantic PDF arrives, it wins over the reconstruction.
5. One finding → one GitHub issue → one branch → one PR. Do not batch unrelated findings.
6. Ratchet-only: a failure adds a tighter guide or sensor. Do not delete a guard to go green.
7. Fail closed: missing database, fully booked slot (30 tables), timeout, or missing freeze file = honest **no**, not a guessed **yes**.

## Honesty / probe

Allowed when probed: a concrete command, HTTP GET, CI log, or file that exists **now**.

Not a probe: hoping, remembering a previous session, “should be live”, a hostname on a slide.

Examples that stay **Unknown** until probed:

- GitHub Pages URL for `knowledge.cafe.artof.link`
- Restaurant at `cafe.artof.link`
- “Reservations work”
- “CI is green on main” without a run

If a probe fails or times out, report the failure. Do not retry-until-yes as a substitute for a sensor.

## Knowledge before code

The knowledge site is a **thin map** of the freeze (home, stack, SRS, honesty, plus a clearly labeled Future page). It is not the restaurant.

When implementing the restaurant later:

- Implement the SRS only as MVP.
- Extra features go in the Future plan (`knowledge/future.md` and notes under `knowledge/future/`), not in the first app cut.
- Do not copy other students’ application code.

## ID freeze

- Cite requirement IDs from `docs/srs.md` only.
- Current freeze: **FR-1..FR-18**, **NFR-1..NFR-9**.
- Do not invent `FR-19`, `NFR-10`, or renamed IDs.
- Menu prices, address, hours, owners, awards, and reviews in the SRS are freeze data — do not “improve” them in the MVP.

## DATE_RE and live handoff

The only **live handoff** file is:

```text
research/daily-briefs/YYYY-MM-DD.md
```

Date segment must match `DATE_RE`:

```text
^[0-9]{4}-[0-9]{2}-[0-9]{2}$
```

Use Europe/Berlin for “today”. Other notes (`research/random-thoughts/`, knowledge journal stub) are not the live handoff. Do not treat chat history as the handoff.

## Ratchet-only guards

When something fails (missing SRS, guessed status word, GitLab habit, invented ID), add a tighter guide (this file / `.cursor/rules`) or sensor (CI check). Keep the old guard. Going green by deleting a check is a regression.

This is **antifragility-as-ratchet**, not a claim that the system is antifragile.

## Fail closed

For later reservation/newsletter work (not this foundation PR):

- Missing PostgreSQL / no connection → do not accept a booking; return an honest error.
- Time slot at 30 tables → do not assign a table; **FR-9** error path.
- Timeout talking to the database or API → honest no, not a cached yes.

For this repo **now**:

- Missing `docs/srs.md` → CI fails. Do not skip the freeze.

## GitHub issues and PRs

- Tracker: GitHub issues in this repo.
- Change: one branch, one PR against `main`.
- Do not use GitLab issues, merge requests, or GitLab CI.
- The assignment requires collaborator `quantic-grader`. **The owner must add that collaborator.** An agent must not add it.

## Out of scope for the foundation / first app cut

- Restaurant React/Flask/PostgreSQL implementation (later; SRS only).
- Florist Path B, 14 hats, GitLab Pages, Kafka/BFF, 3DX Lab.
- Declaring Pages or `cafe.artof.link` live without a GET probe.
- A large skill library on top of this SOP.

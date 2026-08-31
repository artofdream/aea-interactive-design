# AGENTS.md — session-start SOP

This is a student / GitHub E2E repo for **Café Fausse** (Quantic MSAIE) and a transfer of the AEA **outer harness** onto a different stack. Read this file before writing code.

**MVP = official SRS freeze** (`docs/srs.md`, FR-1..FR-18 and NFR-1..NFR-9; SoT = official PDF in `docs/official/`). Everything else is future or refined — not the first restaurant cut, and not a second product on the knowledge site.

Do not claim this system is antifragile. AWS is **not** in this foundation PR. Knowledge site = GitHub Pages. `cafe.artof.link` hosting remains future.

## Teams and two public surfaces

| Team | Owns | Intended hostname | Live URL |
|---|---|---|---|
| Café Fausse Knowledge | Knowledge site (thin map, GitHub Pages) | `knowledge.cafe.artof.link` | **Unknown** until a GET probe **this session** after Pages + DNS |
| Café Fausse App | Restaurant MVP (React + JSX, Flask, PostgreSQL) | `cafe.artof.link` | **Unknown** — not built; hosting future; no GET this session |

This PR stays foundation + thin knowledge site. Do not invent other domains. Do not configure DNS from an agent. Owner step: enable GitHub Pages (Actions), then DNS.

Tracker and CI are **GitHub only**. No GitLab, no `glab`, no GitLab Pages, no GitLab CI.

## Session start (every turn)

1. Read this file, `docs/srs.md` (ID freeze), and `research/daily-briefs/YYYY-MM-DD.md` for **today** (Europe/Berlin). If today’s brief is missing, create it before doing other work.
2. Knowledge before code: Café Fausse Knowledge map first. Do not implement features that are not in the SRS freeze.
3. Honesty: a status word is a claim. Probe **this session** or write **Unknown**. A previous session is not a probe.
4. ID freeze: cite `FR-*` / `NFR-*` from `docs/srs.md` (official PDF SoT). Do not invent IDs.
5. One finding → one GitHub issue → one branch → one PR. Do not batch unrelated findings. **The author does not merge their own PR.**
6. Ratchet-only: a failure adds a tighter guide or sensor. Do not delete a guard to go green.
7. Fail closed: missing database, fully booked slot (30 tables), timeout, or missing freeze file = honest **no**, not a guessed **yes**.
8. Uncommitted files are **not** shared memory. Only committed git + today’s daily brief count as handoff.

## Honesty / probe

Allowed when probed **this session**: a concrete command, HTTP GET, CI log, or **committed** file that exists now.

Not a probe: hoping, a previous session, uncommitted working tree, “should be live”, a hostname on a slide.

Examples that stay **Unknown** until probed this session:

- GitHub Pages URL for `knowledge.cafe.artof.link`
- Restaurant at `cafe.artof.link`
- “Reservations work”
- “CI is green on main” without a run this session

If a probe fails or times out, report the failure. Do not retry-until-yes as a substitute for a sensor.

## Knowledge before code

The knowledge site is a **thin map** (home, stack, SRS, honesty, plus a clearly labeled Future page). It is not the restaurant. Café Fausse Knowledge owns it.

When Café Fausse App implements the restaurant later:

- Implement the SRS only as MVP.
- Extra features go in the Future plan (`knowledge/future.md`), not in the first app cut.
- Do not copy other students’ application code.
- Do not add AWS in the foundation cut; hosting of `cafe.artof.link` is future.

## ID freeze

- Cite requirement IDs from `docs/srs.md` only (working freeze of the official PDF).
- Current freeze: **FR-1..FR-18**, **NFR-1..NFR-9** (verified from the official PDF this session).
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

Use Europe/Berlin for “today”. Other notes (`research/random-thoughts/`, knowledge journal stub) are not the live handoff. Chat history is not the handoff. **Uncommitted files are not shared memory.**

## Skills (2–4, not 14 hats)

Portable seeds only, in `.cursor/skills/`:

- `knowledge-guardian` — knowledge site stays a thin map; not the restaurant
- `coherence-guardian` — IDs, probes, DATE_RE, PR loop, memory
- `product-owner` — MVP vs Future, team ownership
- `engineer` — later React/Flask/Postgres and GitHub Actions; not this cut’s app

Do not grow this into a 14-hat library.

## Ratchet-only guards

When something fails (missing SRS, guessed status word, GitLab habit, invented ID), add a tighter guide (this file / `.cursor/rules` / a skill) or sensor (CI check). Keep the old guard. Going green by deleting a check is a regression.

This is **antifragility-as-ratchet**, not a claim that the system is antifragile.

## Fail closed

For later reservation/newsletter work (not this foundation PR):

- Missing PostgreSQL / no connection → do not accept a booking; return an honest error.
- Time slot at 30 tables → do not assign a table; **FR-9** error path.
- Timeout talking to the database or API → honest no, not a cached yes.

For this repo **now**:

- Missing `docs/srs.md` or the official PDF → CI fails. Do not skip the freeze.

## GitHub issues and PRs

- Tracker: GitHub issues in this repo.
- Change: one branch, one PR against `main`.
- **Author does not merge their own PR.**
- Do not use GitLab issues, merge requests, or GitLab CI.
- The assignment requires collaborator `quantic-grader`. **The owner must add that collaborator.** An agent must not add it.

## Out of scope for the foundation / first app cut

- Restaurant React/Flask/PostgreSQL implementation (later; SRS only; Café Fausse App).
- AWS / re-auth / `cafe.artof.link` hosting (future).
- Florist Path B, 14 hats, GitLab Pages, Kafka/BFF, 3DX Lab, Grafana.
- Declaring Pages or `cafe.artof.link` live without a GET **this session**.
- A skill library larger than the four seeds above.

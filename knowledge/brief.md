# Teammate brief — Wed 2026-09-02 19:00 CET

Thin handoff for the teammate meeting. Not the restaurant. Not a second product.

**Probe date for live claims on this page:** 2026-09-01 Europe/Berlin (this session).

## Where we are

- Public GitHub repo `artofdream/aea-interactive-design`. Tracker and CI are **GitHub only**. No GitLab.
- **MVP = official SRS only.** PDF is SoT (`docs/official/…SRS.pdf`). Working freeze `docs/srs.md` (**FR-1..FR-18**, **NFR-1..NFR-9**). Do not invent FR-19 / NFR-10. Freeze data (menu prices, address, hours, owners, awards, reviews) is not to be “improved.”
- Restaurant MVP code is **on `main`** (PRs #9 + timezone #12): React + JSX, Flask, PostgreSQL. Extra ideas stay in [Future](future.md).
- Knowledge site (this map) publishes via GitHub Actions → GitHub Pages.

## Two surfaces

| Surface | Hostname | This session |
|---|---|---|
| Café Fausse Knowledge | `knowledge.cafe.artof.link` | GET **200**; TLS VERIFY_OK; CN/SAN match; Let’s Encrypt, expires 2026-11-30. Pages API: `cname=knowledge.cafe.artof.link`, **`https_enforced=false`** — owner still needs to tick Enforce HTTPS. |
| Café Fausse App | `cafe.artof.link` | DNS CNAME → `aaafeaf0606ec43f5ad23cfe94d6273e-1de430975830beed.elb.eu-north-1.amazonaws.com.` **Not our restaurant.** Do not claim this hostname is live Café Fausse. Hosting is future. |

Local validate on cts-ai (not this agent VM): Vite `http://127.0.0.1:5173`, Flask `:5000`, `cafe-pg` Postgres. A Journey 1–9 UX checklist is described for that machine. **Pass/fail = Unknown** unless someone probes those journeys this session. This agent did not.

## Freeze vs Future

- **In MVP:** the official SRS pages and APIs (Home, Menu, Reservations, About, Gallery, newsletter, 30 tables, fail-closed DB). See [Coverage](coverage.md).
- **Not in MVP:** AWS / `cafe.artof.link` hosting, florist Path B, 14 hats, Kafka/BFF, 3DX Lab, GitLab, invented requirement IDs, claiming the system is antifragile.

## GitHub loop (do not skip)

One finding → one issue → one branch → one PR against `main`. **The author does not merge their own PR.** Lesson: PR #14 / issue #13.

MRC: a COMMENT is role-approve until a distinct GitHub App identity. Merge gate is GitHub review **`APPROVE` from a login that is not the PR author**. Bugbot comments are a signal, not the gate. `cursor[bot]` may `APPROVE` `artofdream`-authored PRs after a this-run CI probe; `artofdream` may `APPROVE` `cursor[bot]`-authored PRs. Same login cannot self-APPROVE.

Assignment collaborator `quantic-grader` must be added by the **owner**. Agents must not.

## What to decide tomorrow

1. **Enforce HTTPS** on GitHub Pages (owner tick). Probe shows `https_enforced=false`.
2. **Presentation honesty:** use [Coverage](coverage.md). NFR load/submit timings without a measured probe stay **Unknown**. Journey 1–9 results stay **Unknown** until probed. Do not say `cafe.artof.link` is the restaurant.
3. **Owner-only:** add `quantic-grader`. Do not ask an agent to add collaborators.
4. **Scope ratchet:** any extra feature idea goes to Future, not a new FR. Do not batch unrelated findings into one PR.
5. **Local demo path** if needed: Vite `:5173` + Flask `:5000` + `cafe-pg` — not the AWS ELB behind `cafe.artof.link`.

## Read next

- [Stack](stack.md) — as-is vs intended HLD
- [Coverage](coverage.md) — every FR/NFR
- [Honesty](honesty.md) — what we will not claim

# Teammate brief — Wed 2026-09-02 19:00 CET

Thin handoff for the teammate meeting. Not the restaurant. Not a second product.

**Probe date for live claims on this page:** 2026-09-02 Europe/Berlin (this session).

**Tonight (owner locked 1, 3, 4 — not 2):** demo this brief + clips and/or local Vite/Flask; FS v0.1 extras = Future; presentation = [Coverage](coverage.md). See compare below. Not 2: `quantic-grader` is an owner step, not tonight.

## Demo clips

Silent ~30s demos of the restaurant MVP (Café Fausse App). The tunnel or local stack may be offline; these files are the shareable look. They are not a probe that reservations work on a public host, and they are not Café Fausse at `cafe.artof.link`.

**Home → Menu (~32s)**

<video controls src="clips/01-home-menu.mp4"></video>

**Happy reservation (~33s)**

<video controls src="clips/02-happy-book.mp4"></video>

## Course grade 5 — covered vs decide

1. **What a grade of 5 needs.** Official SRS only (**FR-1..FR-18**, **NFR-1..NFR-9**). PDF in `docs/official/` is SoT; working freeze `docs/srs.md`. Do not invent FR-19 / NFR-10. Freeze data is not to be “improved.” Extra ideas are Future, not extra credit.

2. **Already covered.** Restaurant MVP **on `main`** (PRs #9 + #12). Knowledge live HTTPS: `GET https://knowledge.cafe.artof.link/` **200** this session (TLS VERIFY_OK; CN/SAN match). HTTP `http://knowledge.cafe.artof.link/` → **301** to HTTPS. Pages **`https_enforced=true`**; cert **approved**. [Coverage](coverage.md) maps every freeze ID. Demo clips on this brief (shareable look, not a live restaurant host). [Stack](stack.md) HLD as-is vs intended-to-be.

3. **Tonight’s focus (1, 3, 4).** Demo this brief + clips and/or local Vite/Flask — not `cafe.artof.link`. FS v0.1 extras = Future/hardening (no new FR/NFR IDs). Presentation = [Coverage](coverage.md); **Unknown** where not probed. Journey 1–9, **NFR-1** / **NFR-2** stay **Unknown** without a measured probe this session. `cafe.artof.link` hosting is [Future #22](https://github.com/artofdream/aea-interactive-design/issues/22).

## Where we are

- Public GitHub repo `artofdream/aea-interactive-design`. Tracker and CI are **GitHub only**. No GitLab.
- **MVP = official SRS only.** PDF is SoT (`docs/official/…SRS.pdf`). Working freeze `docs/srs.md` (**FR-1..FR-18**, **NFR-1..NFR-9**). Do not invent FR-19 / NFR-10. Freeze data (menu prices, address, hours, owners, awards, reviews) is not to be “improved.”
- Restaurant MVP code is **on `main`** (PRs #9 + timezone #12): React + JSX, Flask, PostgreSQL. Extra ideas stay in [Future](future.md).
- Knowledge site (this map) publishes via GitHub Actions → GitHub Pages.

## Two surfaces

| Surface | Hostname | This session |
|---|---|---|
| Café Fausse Knowledge | `knowledge.cafe.artof.link` | HTTPS GET **200**; HTTP **301** to HTTPS; TLS VERIFY_OK; CN/SAN match; Let’s Encrypt, expires 2026-11-30. Pages API: `cname=knowledge.cafe.artof.link`, cert **approved**, **`https_enforced=true`**. |
| Café Fausse App | `cafe.artof.link` | DNS CNAME → `aaafeaf0606ec43f5ad23cfe94d6273e-1de430975830beed.elb.eu-north-1.amazonaws.com.` **Not our restaurant.** Do not claim this hostname is live Café Fausse. Hosting is future. |

Local validate on cts-ai (not this agent VM): Vite `http://127.0.0.1:5173`, Flask `:5000`, `cafe-pg` Postgres. A Journey 1–9 UX checklist is described for that machine. **Pass/fail = Unknown** unless someone probes those journeys this session. This agent did not.

## Compare: team Functional Spec v0.1 vs SRS MVP on main

Team FS v0.1 (2026-09-02) — Customer, Newsletter, Reservation, Menu flows (FS-01..FS-05). **Not a new freeze.** FS labels are the team’s; official IDs stay **FR-1..FR-18** / **NFR-1..NFR-9**. Do not mint FR-19+.

### Already on `main` / aligns with official SRS

Evidence is committed files this session (PRs #9 + #12 on `main`). Not a live-host probe.

- **Newsletter** → `customers.newsletter_signup` (**FR-15**, **FR-16**): `backend/cafe_fausse/newsletter.py`, `backend/schema.sql`.
- **Reservations** **FR-6..FR-9**, **FR-17..FR-18**: form fields, slot check, random table 1–30, full-book error, Customers + Reservations, Flask assign. `guest_count` is already in `schema.sql` (supports **FR-6**; not a new ID).
- **NFR-5:** unique index `reservations_slot_table` on `(time_slot, table_number)`.
- **Menu FR-5:** `shared/freeze.json` + `GET /api/menu` — **read-only display**, not a staff CMS.
- **No payment** (out of scope in both the official SRS and FS v0.1).

### In FS v0.1 but not in MVP (Future / beyond assignment floor)

Park these as Future issues (already filed). Do not treat them as missing grade items. Do not invent FR-19+.

- **PENDING → ASSIGNED → RELEASED** lifecycle; `release_reason`; `released_at` ([#34](https://github.com/artofdream/aea-interactive-design/issues/34), FS-03/04). On main, a reservation is an inserted row; no status column.
- Customer cancel / restaurant checkout / admin release APIs ([#35](https://github.com/artofdream/aea-interactive-design/issues/35), FS-04).
- **Menu** categories/items as persistent tables + staff CRUD + `is_available` ([#36](https://github.com/artofdream/aea-interactive-design/issues/36), FS-05). On main, menu is freeze JSON, not persistent items.
- **Concurrency retry** beyond the unique index ([#38](https://github.com/artofdream/aea-interactive-design/issues/38), FS-03). On main: slot `FOR UPDATE` + unique `(time_slot, table_number)`; `UniqueViolation` asks the client to resubmit. No automatic retry loop.
- **Verbatim case-sensitive email** as an explicit FS product rule ([#37](https://github.com/artofdream/aea-interactive-design/issues/37), FS-01). On main: `email_address TEXT NOT NULL UNIQUE`; `validate_email` **lowercases** before store (`backend/cafe_fausse/validate.py`, committed this session). That is not verbatim case. Raw SQL that bypasses the app vs TEXT `UNIQUE` case: **Unknown** (no live Postgres probe this session).
- **QCFA `run-sql.sh` / migration packaging** vs our path: `backend/schema.sql` + `backend/cafe_fausse/init_db.py`. No GitHub issue filed for this packaging difference.
- Hosting `cafe.artof.link` remains [Future #22](https://github.com/artofdream/aea-interactive-design/issues/22) (not an FS flow extra; not tonight’s demo target).

### Discussion frame

- FS v0.1 = proposed **Future / hardening** baseline, not a replacement for the official PDF.
- **Grade floor** = official **FR-1..FR-18** / **NFR-1..NFR-9** only.
- Park FS extras as [Future](future.md). Do not invent FR-19 / NFR-10.

## Freeze vs Future

- **In MVP:** the official SRS pages and APIs (Home, Menu, Reservations, About, Gallery, newsletter, 30 tables, fail-closed DB). See [Coverage](coverage.md).
- **Not in MVP:** FS v0.1 extras above; AWS / `cafe.artof.link` hosting; florist Path B; 14 hats; Kafka/BFF; 3DX Lab; GitLab; invented requirement IDs; claiming the system is antifragile.

## GitHub loop (do not skip)

One finding → one issue → one branch → one PR against `main`. **The author does not merge their own PR.** Lesson: PR #14 / issue #13.

MRC: a COMMENT is role-approve until a distinct GitHub App identity. Merge gate is GitHub review **`APPROVE` from a login that is not the PR author**. Bugbot comments are a signal, not the gate. `cursor[bot]` may `APPROVE` `artofdream`-authored PRs after a this-run CI probe; `artofdream` may `APPROVE` `cursor[bot]`-authored PRs. Same login cannot self-APPROVE.

Assignment collaborator `quantic-grader` must be added by the **owner**. Agents must not. **Not tonight** (decision 2 parked).

## Tonight — owner locked (1, 3, 4)

Not **2:** `quantic-grader` stays an owner step. Not on tonight’s agenda.

1. **Demo:** this Knowledge brief + clips, and/or local Vite/Flask/`cafe-pg`. **Not** `cafe.artof.link` (AWS ELB, not our restaurant; hosting is [Future #22](https://github.com/artofdream/aea-interactive-design/issues/22)).
3. **Scope:** FS v0.1 extras = Future/hardening, not new FR/NFR IDs (compare above; [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38)). Grade floor = official **FR-1..FR-18** / **NFR-1..NFR-9**.
4. **Presentation:** [Coverage](coverage.md) freeze map. Journey 1–9, **NFR-1** / **NFR-2**, **NFR-7** stay **Unknown** where not probed this session.

## Read next

- [Stack](stack.md) — as-is vs intended HLD
- [Coverage](coverage.md) — every FR/NFR
- [Honesty](honesty.md) — what we will not claim
- [Future](future.md) — parked FS extras; not a second freeze

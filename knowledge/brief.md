# Teammate brief — Fri 2026-09-04 19:00 Europe/Berlin

Thin handoff for the teammate meeting. Not the restaurant. Not a second product.

**Probe date for live claims on this page:** 2026-09-04 Europe/Berlin (this session).

**App tunnel this session:** `https://shaky-deer-drive.loca.lt/` — GET **200** (SPA HTML). `https://shaky-deer-drive.loca.lt/api/health` — GET **200** `{"ok":true}`. Knowledge GET: root **200** (~24s); `/operator` **200** (~14s); `/api/operator` **200** (~11s); `/api/health` **200** `{"ok":true}` (~12s). **Slow (~10–20s+)**; **interstitial-possible** in browsers. Short timeouts can look like failure. Not snappy. Not always-on. Temporary localtunnel to Flask on cts-ai. **Not** `cafe.artof.link`. Clips stay the fallback. Old `https://happy-glasses-film.loca.lt/` and `https://real-goats-shop.loca.lt/` are **stale** — do not keep as the live share URL. Read-only `/operator` is on the tunnel ([PR #58](https://github.com/artofdream/aea-interactive-design/pull/58) / [#54](https://github.com/artofdream/aea-interactive-design/issues/54)) — **not FR-19**. Never claim `cafe.artof.link` is Café Fausse. FS v0.1 extras = Future; presentation = [Coverage](coverage.md). `quantic-grader` remains an owner step.

## Friday 2026-09-04 19:00 Europe/Berlin (score 5)

**App tunnel this session:** `https://shaky-deer-drive.loca.lt/` GET **200** (SPA HTML). `/api/health` GET **200** `{"ok":true}`. Knowledge GET: root **200** (~24s); `/operator` **200** (~14s); `/api/operator` **200** (~11s); `/api/health` **200** `{"ok":true}` (~12s). **Slow (~10–20s+)**; **interstitial-possible** in browsers. Short timeouts can look like failure. Not snappy. Not always-on. Temporary localtunnel to Flask on cts-ai. Clips stay fallback. **Not** `cafe.artof.link`. Old `https://happy-glasses-film.loca.lt/` and `https://real-goats-shop.loca.lt/` are **stale** — do not keep as the live share URL. 

- **Primary live surface:** `https://knowledge.cafe.artof.link/` (HTTPS GET **200** this session).
- **App tunnel (share this tab):** `https://shaky-deer-drive.loca.lt/` — GET **200** this session (SPA HTML, title Café Fausse). Health `https://shaky-deer-drive.loca.lt/api/health` — GET **200** `{"ok":true}`. Knowledge GET: root **200** (~24s); `/operator` **200** (~14s); `/api/operator` **200** (~11s); `/api/health` **200** `{"ok":true}` (~12s). **Slow (~10–20s+)**; **interstitial-possible** in browsers. Short timeouts can look like failure. Temporary; not snappy, not always-on. Old `https://happy-glasses-film.loca.lt/` and `https://real-goats-shop.loca.lt/` are **stale** — do not keep as the live share URL.
- **Fallback:** committed clips below (if the tunnel is **slow (~10–20s+)**, shows an interstitial, or drops).
- **Operator view (recording helper):** `https://shaky-deer-drive.loca.lt/operator` — Knowledge GET **200** (~14s). Read-only customers + reservations so you can see the DB after a booking. **Not** an admin console (no CRUD / cancel). **Not FR-19.** Landed on `main` via [PR #58](https://github.com/artofdream/aea-interactive-design/pull/58) / [issue 54](https://github.com/artofdream/aea-interactive-design/issues/54). **Slow (~10–20s+)**; **interstitial-possible**. Temporary tunnel; **not** `cafe.artof.link`.
- **Never** `cafe.artof.link` (AWS ELB, not our restaurant).

## Operator view (recording helper — not FR-19)

**What:** read-only `/operator`. Shows customers + reservations so a recording can see the PostgreSQL effect after a booking. **Not** an admin console (no CRUD / cancel / checkout). **Not FR-19.**

**Where (live share this session):** `https://shaky-deer-drive.loca.lt/operator` — Knowledge GET **200** this session (~14s). **Slow (~10–20s+)**; **interstitial-possible** in browsers. Temporary localtunnel to Flask on cts-ai; **not** `cafe.artof.link`.

**Ship:** landed on `main` via [PR #58](https://github.com/artofdream/aea-interactive-design/pull/58) / [issue 54](https://github.com/artofdream/aea-interactive-design/issues/54). Footer `Operator` link only — not in the primary SRS nav.

## Friday room

Room job: **tech access** + **lock video and scenarios**. Working references (not official Quantic dashboard text):

- [Friday plan](friday-plan.md) — P0 / P1 / P2; live Knowledge HTTPS vs App after a this-session GET vs Future `cafe.artof.link`
- [Video script](video-script.md) — ~10 minute beats + scenario menu A–F; clips `clips/01-home-menu.mp4` and `clips/02-happy-book.mp4`
- [Talk cuts](presentation.md) — Saturday recording: three ~10 min variants + shared close
- [Slide outline](presentation-sample.md) — 12-slide outline and the **8-slide cut**

**Ready (do not over-claim):** restaurant MVP on `main`; Coverage maps every freeze ID; Knowledge HTTPS GET **200** this session; App tunnel `https://shaky-deer-drive.loca.lt/` GET **200** (SPA + `/operator` + `/api/health`; **slow (~10–20s+)**; **interstitial-possible** in browsers — not snappy, not always-on); two silent clips as fallback (a look, not a public restaurant host). Temporary tunnel — not `cafe.artof.link`.

**[#40](https://github.com/artofdream/aea-interactive-design/issues/40) / [#44](https://github.com/artofdream/aea-interactive-design/issues/44) recorded on [Coverage](coverage.md):** Journey **J1–J8 PASS** (cts-ai local UX, DB up, 2026-09-02). **J9 / NFR-3 / NFR-8 PASS** (Vite-only; Edge `probe-nfr/` 375×812 home, 768×1024 menu, 1280×800 reservations + theme.css; not Flask+Postgres). **NFR-1** / **NFR-2** local Vite timings noted (56 ms / 32 ms) — **not** claimed met. **NFR-7** **partial** (Edge all routes with screenshots + Firefox home; Chrome not installed on cts-ai; Safari Unknown).

**Not grade work:** Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22) (hosting) and [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38). Missing them is not a missing FR/NFR. AWS schema map ([#46](https://github.com/artofdream/aea-interactive-design/issues/46) / [PR #47](https://github.com/artofdream/aea-interactive-design/pull/47), **merged**) is Future reuse notes, not a new FR freeze. Live GET `https://knowledge.cafe.artof.link/future/aws-schema-map.html` **200** this session.

## Demo clips

Silent ~30s demos of the restaurant MVP (Café Fausse App). **Fallback** if `https://shaky-deer-drive.loca.lt/` is **slow (~10–20s+)**, shows a localtunnel interstitial in browsers, or drops. They are not a probe that reservations work on a public host, and they are not Café Fausse at `cafe.artof.link`. The live share tunnel this session is `https://shaky-deer-drive.loca.lt/` (GET **200** SPA + `/operator` + `/api/health`; **slow (~10–20s+)**; **interstitial-possible** in browsers — not snappy, not always-on) — temporary localtunnel to Flask on cts-ai. Do not keep `https://happy-glasses-film.loca.lt/` or `https://real-goats-shop.loca.lt/` as the live share URL.

**Home → Menu (~32s)**

<video controls src="clips/01-home-menu.mp4"></video>

**Happy reservation (~33s)**

<video controls src="clips/02-happy-book.mp4"></video>

## Course grade 5 — covered vs decide

1. **What a grade of 5 needs.** Official SRS only (**FR-1..FR-18**, **NFR-1..NFR-9**). PDF in `docs/official/` is SoT; working freeze `docs/srs.md`. Do not invent FR-19 / NFR-10. Freeze data is not to be “improved.” Extra ideas are Future, not extra credit.

2. **Already covered.** Restaurant MVP **on `main`** (PRs #9 + #12). Knowledge live HTTPS: `GET https://knowledge.cafe.artof.link/` **200** this session (TLS VERIFY_OK; CN/SAN match). HTTP `http://knowledge.cafe.artof.link/` → **301** to HTTPS. [Coverage](coverage.md) maps every freeze ID. Demo clips on this brief (shareable look, not a live restaurant host). [Stack](stack.md) HLD as-is vs intended-to-be.

3. **Wed 2026-09-02 focus (1, 3, 4).** That night: this brief + clips and/or local Vite/Flask — not `cafe.artof.link`. **Friday 2026-09-04:** Knowledge + clips; App tunnel `https://shaky-deer-drive.loca.lt/` GET **200** (SPA + `/operator` + `/api/health`; **slow (~10–20s+)**; **interstitial-possible** in browsers — not snappy, not always-on). Temporary localtunnel to Flask on cts-ai — **not** `cafe.artof.link`. FS v0.1 extras = Future/hardening (no new FR/NFR IDs). Presentation = [Coverage](coverage.md). J1–J8 PASS is local cts-ai UX while DB was up; J9 **PASS** is Vite-only; **NFR-7** is **partial**; **NFR-1** / **NFR-2** stay not-claimed-met. `cafe.artof.link` hosting is [Future #22](https://github.com/artofdream/aea-interactive-design/issues/22).

## Where we are

- Public GitHub repo `artofdream/aea-interactive-design`. Tracker and CI are **GitHub only**. No GitLab.
- **MVP = official SRS only.** PDF is SoT (`docs/official/…SRS.pdf`). Working freeze `docs/srs.md` (**FR-1..FR-18**, **NFR-1..NFR-9**). Do not invent FR-19 / NFR-10. Freeze data (menu prices, address, hours, owners, awards, reviews) is not to be “improved.”
- Restaurant MVP code is **on `main`** (PRs #9 + timezone #12): React + JSX, Flask, PostgreSQL. Extra ideas stay in [Future](future.md).
- Knowledge site (this map) publishes via GitHub Actions → GitHub Pages.

## Two surfaces

| Surface | Hostname | This session |
|---|---|---|
| Café Fausse Knowledge | `knowledge.cafe.artof.link` | HTTPS GET **200** this session (2026-09-04); HTTP **301** to HTTPS; TLS VERIFY_OK; CN/SAN match; Let’s Encrypt, expires 2026-11-30. |
| Café Fausse App | `cafe.artof.link` | DNS CNAME → `aaafeaf0606ec43f5ad23cfe94d6273e-1de430975830beed.elb.eu-north-1.amazonaws.com.` **Not our restaurant.** Do not claim this hostname is live Café Fausse. Hosting is future. |

App on cts-ai (not this agent VM): Vite `http://127.0.0.1:5173`, Flask `:5000`, `cafe-pg` Postgres. **Tunnel this session:** `https://shaky-deer-drive.loca.lt/` GET **200** (SPA HTML); `/api/health` GET **200** `{"ok":true}`. Knowledge GET: root **200** (~24s); `/operator` **200** (~14s); `/api/operator` **200** (~11s); `/api/health` **200** `{"ok":true}` (~12s). **Slow (~10–20s+)**; **interstitial-possible** in browsers. Short timeouts can look like failure. Temporary localtunnel to Flask on cts-ai. Not snappy. Not always-on. **Not** `cafe.artof.link`. This Knowledge VM did not reach Vite on `:5173`. Journey **J1–J8 PASS** recorded 2026-09-02 while the DB was up; **J9 / NFR-3 / NFR-8 PASS** later on Vite-only `:5173` (Edge `probe-nfr/` screenshots + theme.css; not Flask+Postgres). **NFR-7** **partial** (Edge all routes with screenshots; Firefox home; Chrome not installed; Safari Unknown). After the J1–J8 handoff, App reported `cafe-pg` unreachable — do not claim reservations on the tunnel without a write probe. Old `https://happy-glasses-film.loca.lt/` and `https://real-goats-shop.loca.lt/` are **stale** — do not keep as the live share URL. Do **not** claim `cafe.artof.link` is the restaurant.

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

MRC **COMMENT** is the role-approve signal. For `artofdream`-authored PRs, `cursor[bot]` may merge after this-run green checks and Bugbot resolve-or-decline. Bugbot comments are a signal, not the merge. Same login cannot review-approve its own PR. Owner `artofdream` may review-approve only `cursor[bot]`-authored PRs.

Assignment collaborator `quantic-grader` must be added by the **owner**. Agents must not. **Not tonight** (decision 2 parked).

## Friday room — remote default, then optional tunnel

Not **2:** `quantic-grader` stays an owner step.

**App tunnel this session:** `https://shaky-deer-drive.loca.lt/` GET **200** (SPA + `/operator` + `/api/health`). Knowledge GET: root **200** (~24s); `/operator` **200** (~14s); `/api/operator` **200** (~11s); `/api/health` **200** `{"ok":true}` (~12s). **Slow (~10–20s+)**; **interstitial-possible** in browsers. Short timeouts can look like failure. Not snappy. Not always-on. Temporary localtunnel to Flask on cts-ai. Clips stay fallback. **Not** `cafe.artof.link`. Do not keep old `https://happy-glasses-film.loca.lt/` or `https://real-goats-shop.loca.lt/` as the live share URL.

Wed 2026-09-02 locked **1, 3, 4** (not 2). Those decisions still hold:

1. **Demo:** Knowledge brief + clips; App tunnel `https://shaky-deer-drive.loca.lt/` GET **200** (SPA + `/operator` + `/api/health`; **slow (~10–20s+)**; **interstitial-possible** in browsers — not snappy, not always-on). **Not** `cafe.artof.link` (AWS ELB, not our restaurant; hosting is [Future #22](https://github.com/artofdream/aea-interactive-design/issues/22)).
3. **Scope:** FS v0.1 extras = Future/hardening, not new FR/NFR IDs (compare above; [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38)). Grade floor = official **FR-1..FR-18** / **NFR-1..NFR-9**.
4. **Presentation:** [Coverage](coverage.md) freeze map + Journey table. J1–J8 PASS (cts-ai, DB up). J9 / NFR-3 / NFR-8 **PASS** (Vite-only Edge screenshots + theme.css). **NFR-7** **partial** (Edge + Firefox home; Chrome not installed; Safari Unknown). **NFR-1** / **NFR-2** stay not-claimed-met. Tunnel URL written after GET **200** this session.

## Read next

- [Friday plan](friday-plan.md) — score-5 P0/P1/P2; live vs local vs Future
- [Video script](video-script.md) — ~10 min beats; scenarios A–F
- [Talk cuts](presentation.md) — Saturday three-cut recording
- [Slide outline](presentation-sample.md) — 8-slide cut
- [Stack](stack.md) — as-is vs intended HLD
- [Coverage](coverage.md) — every FR/NFR
- [Honesty](honesty.md) — what we will not claim
- [Future](future.md) — parked FS extras; not a second freeze

# FR / NFR coverage map

Presentation map for the Quantic course. Every freeze ID from `docs/srs.md` (official PDF SoT). **FR-1..FR-18** and **NFR-1..NFR-9** only. Do not invent FR-19 / NFR-10.

This page is not the restaurant. Paths are the in-repo Café Fausse App on `main` (PRs #9 + timezone #12) plus knowledge/CI where that is the evidence.

**Evidence classes:** `code` = committed file this session; `CI` = GitHub Actions job in `.github/workflows/`; `local GET / UX (cts-ai, 2026-09-02)` = Café Fausse App probe (J1–J8: Vite + Flask + `cafe-pg` while the DB was up; J9 / NFR-7 Vite slice: **Vite-only** `:5173`); `owner/sponsor mobile UX this session (2026-09-05)` = owner report of Safari on iPhone 16 plus A36 mobile fit on the public hosts; `Unknown` = no probe this session, or a measured number that is **not** an SRS-budget claim.

[Issue #40](https://github.com/artofdream/aea-interactive-design/issues/40) recorded J1–J8 (PR #43). [Issue #44](https://github.com/artofdream/aea-interactive-design/issues/44) records J9 + the Vite-only NFR-7 slice. [Issue #117](https://github.com/artofdream/aea-interactive-design/issues/117) records the owner/sponsor mobile UX probe this session (2026-09-05). This Knowledge VM did not reach cts-ai Vite `:5173` / Flask `:5000` and did not run the phones. The Journey table below is App’s 2026-09-02 handoff plus the owner report cited on NFR-7 / NFR-8.

In plain language: the FR/NFR tables are “where the freeze shows up in the repo.” **Code** and **CI** are not the same as “we timed broadband” or “we checked four browsers.” Friday score-5 talk track: [Friday plan](friday-plan.md).

## Journey 1–9 (App naming this run)

Recorded from Café Fausse App (cts-ai) **2026-09-02 Europe/Berlin**.

**J1–J8** ([#40](https://github.com/artofdream/aea-interactive-design/issues/40) / PR #43): local UX / GET on Vite + Flask + `cafe-pg` **while the database was up** (seeded `friday.demo@example.com` and `newsletter.friday@example.com`). After that handoff, App reported `cafe-pg` unreachable and cts-ai dropped. Those later drops do **not** erase the J1–J8 PASS numbers from while the DB was up.

**J9 + NFR-3 / NFR-8 + NFR-7 Vite slice** ([#44](https://github.com/artofdream/aea-interactive-design/issues/44)): later **Vite-only** local UX on `:5173` (2026-09-02). Edge headless screenshots + theme.css (viewports); partial browser matrix. **Do not** claim Flask + PostgreSQL for that Vite-only probe. That slice is **not** a public-host GET.

**Owner/sponsor mobile UX this session (2026-09-05)** ([#117](https://github.com/artofdream/aea-interactive-design/issues/117)): Safari on iPhone 16 — UX validated (restaurant App + Knowledge mobile fit). Sponsor also checks UX on iPhone + A36 (mobile) — source of earlier fit issues. Owner report; this agent did not run those devices. Chrome and Firefox are now **installed on cts-ai** — **probeable**; status **Unknown until App probes**. Do **not** mark PASS from install alone. Not a four-browser **NFR-7** pass. Not an **NFR-1** / **NFR-2** stopwatch.

Tunnel / Flask (2026-09-02 Vite note): App reported Docker Engine still coming up. Mentioned tunnel `https://nine-teams-try.loca.lt/` is ephemeral. Knowledge VM `GET` of that URL **timed out** (curl 28, 12s). **Do not** claim that tunnel is the live share. Public restaurant share this session is `https://cafe.artof.link/` (this agent HTTPS **GET 200**; Lightsail staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57)) — not tunnel-only.

| Journey | App name | Result | Notes (this session) | Freeze IDs (cite only) |
|---|---|---|---|---|
| J1 | Orient | **PASS** | Home name, contact, hours, nav | FR-1..FR-4 |
| J2 | Menu | **PASS** | Four freeze categories | FR-5 |
| J3 | Owners | **PASS** | About founders | FR-10, FR-11 |
| J4 | Gallery | **PASS** | Official images HTTP 200 | FR-12..FR-14 |
| J5 | Happy book | **PASS** | Table 27; sample `friday.demo@example.com` | FR-6..FR-9, FR-17, FR-18 |
| J6 | Full book | **PASS** | 30 tables then HTTP 409 | FR-9, NFR-5 |
| J7 | Newsletter | **PASS** | Sample `newsletter.friday@example.com` | FR-15, FR-16 |
| J8 | DB down | **PASS** | HTTP 503 fail-closed | NFR-6 |
| J9 | Responsive | **PASS** | Vite-only `:5173` (cts-ai, 2026-09-02). Edge headless screenshots under `probe-nfr/` (375×812 home, 768×1024 menu, 1280×800 reservations; App reported valid PNG signatures). Viewport meta + `@media (max-width: 800px)` + Flex/Grid `auto-fit` in `theme.css`. **Not** Flask+Postgres. That Vite slice is **not** a public-host GET. Public-host mobile UX this session is on the **NFR-8** row (owner/sponsor report). | NFR-8 |

Vite routes `/`, `/menu`, `/about`, `/gallery`, `/reservations` all returned **200** on that local stack (App this session). That is local UX evidence, not a public-host probe.

## Functional requirements

| ID | Summary | In-repo | Evidence | Why it matters for the course |
|---|---|---|---|---|
| FR-1 | Display Café Fausse’s name prominently | `frontend/src/pages/Home.jsx` (`<h1>` from freeze); `frontend/src/components/Layout.jsx` wordmark | code; local UX J1 PASS (cts-ai) | Home is the first SRS product function. Graders look for the restaurant name on the digital front door. |
| FR-2 | Contact + hours (freeze address, phone, Mon–Sat / Sunday hours) | `Home.jsx` visit/hours cards; `Layout.jsx` footer; `shared/freeze.json`; Flask `GET /api/site` | code; CI (`test_freeze.py`); local UX J1 PASS (cts-ai) | Freeze data. Changing the address or hours is a spec miss, not a polish. |
| FR-3 | High-quality images and a consistent theme | `Home.jsx` hero from official images; `frontend/src/styles/theme.css` | code | Course image pack is **four webps only**. Theme must hold across pages (NFR-4 adjacency). |
| FR-4 | Nav to Menu, Reservations, About Us, Gallery | `Layout.jsx` `LINKS`; `frontend/src/App.jsx` routes | code; local UX J1 PASS (cts-ai) | SRS names those four destinations. Missing a route is a missing FR. |
| FR-5 | Menu by category with freeze items and prices | `frontend/src/pages/Menu.jsx`; `shared/freeze.json`; `backend/cafe_fausse/content.py`; `GET /api/menu` | code; CI (`test_freeze.py`); local UX J2 PASS (cts-ai, 4 cats) | Prices and copy are SoT. Do not “improve” the menu in MVP. |
| FR-6 | Reservation form: time slot, guests, name, email, optional phone | `frontend/src/pages/Reservations.jsx`; `backend/cafe_fausse/validate.py` | code; local UX J5 PASS (cts-ai) | This is the reservations page the SRS lists as a product function. |
| FR-7 | Validate the selected slot is available and valid | `backend/cafe_fausse/slots.py`; `reservations.py`; `GET /api/slots`; tests in `test_reservations.py` | code; CI; local UX J5/J6 PASS (cts-ai) | Invalid or closed hours must not book. Sunday last seating is freeze hours, not a guess. |
| FR-8 | Assign a random table from 30 when the slot has room | `reservations.py` (`ORDER BY random()`); `schema.sql` `table_number BETWEEN 1 AND 30` | code; CI (`test_reservations.py`, `test_fail_closed.py`); local UX J5 PASS (table 27) | Table pool is 30. A 31st table would violate the SRS. |
| FR-9 | Success message, or error if the slot is fully booked | `Reservations.jsx` banners; `reservations.py` `fully_booked`; `test_fail_closed.py` | code; CI; local UX J5 PASS + J6 PASS (30 then 409) | Fail closed: a full book is an honest **no**, not a guessed table. |
| FR-10 | History: founded 2010 by Chef Antonio Rossi and Maria Lopez | `frontend/src/pages/About.jsx` (`freeze.history`) | code; CI (`test_freeze.py`); local UX J3 PASS (cts-ai) | About Us copy is freeze text. |
| FR-11 | Founder biographies; locally sourced ingredients | `About.jsx` founders + `freeze.locallySourced` | code; local UX J3 PASS (cts-ai) | SRS About Us is history **and** founder bios / sourcing, not a slogan page. |
| FR-12 | Gallery: interior, dishes, events / behind-the-scenes | `frontend/src/pages/Gallery.jsx`; official four webps in `assets/images/` | code; local UX J4 PASS (official images 200) | App must not substitute the 17 student-recovered files in `supplemental-not-official/`. |
| FR-13 | Lightbox for enlarged images | `frontend/src/components/Lightbox.jsx` used by `Gallery.jsx` | code; local UX J4 PASS (cts-ai) | SRS asks for enlarged viewing, not thumbnails only. |
| FR-14 | Awards 2022/2023 and quoted reviews | `Gallery.jsx` awards + reviews from freeze | code; CI (`test_freeze.py`); local UX J4 PASS (cts-ai) | Award names and review quotes are freeze data. |
| FR-15 | Newsletter signup with email-format validation | `frontend/src/components/NewsletterForm.jsx`; `validate.py`; `test_fail_closed.py` invalid email | code; CI; local UX J7 PASS (cts-ai) | Bad emails must not be stored. HTML `type=email` plus server check. |
| FR-16 | Store submitted emails in the backend database | `backend/cafe_fausse/newsletter.py`; `customers.newsletter_signup` in `schema.sql` | code; CI (`test_newsletter.py`); local UX J7 PASS (`newsletter.friday@example.com`) | Signup is a write. Missing DB → honest no (NFR-6), not a fake success. |
| FR-17 | PostgreSQL Customers + Reservations tables | `backend/schema.sql`; `backend/cafe_fausse/init_db.py`; `db.py` | code; CI (restaurant-api job); local UX J5/J8 (write while up; 503 when down) | SRS names the tables and columns. No database → no booking. |
| FR-18 | Flask: insert customer, check availability, random table, confirm or error | `backend/cafe_fausse/__init__.py` (`POST /api/reservations`); `reservations.py` | code; CI; local UX J5/J6 PASS (cts-ai) | Back-end reservation system is an SRS product function, not a static form. |

**Recording helper (not a freeze ID):** read-only `/operator` shows customers + reservations so a recording can see the DB after a booking. **Not** an admin console (no CRUD / cancel). **Not FR-19.** Landed on `main` via [PR #58](https://github.com/artofdream/aea-interactive-design/pull/58) / [issue 54](https://github.com/artofdream/aea-interactive-design/issues/54). Prefer `https://cafe.artof.link/operator` — Knowledge GET **200** (~0.6s). Lightsail staging (#57) — not production forever. Interim backup: `https://54-165-102-60.sslip.io/operator`. See the [Brief](brief.md).

## Non-functional requirements

| ID | Summary | In-repo | Evidence | Why it matters for the course |
|---|---|---|---|---|
| NFR-1 | Page load within 3 seconds on standard broadband | Intended SPA + static assets under `frontend/` and `theme.css`. | **Unknown** — local Vite home **56 ms** recorded on cts-ai this session. That is **not** an SRS broadband stopwatch. Do not say NFR-1 is **met**. | The SRS states a 3s budget on standard broadband. A single local Vite sample is an evidence note only. |
| NFR-2 | Form submissions processed within 2 seconds | `DB_STATEMENT_TIMEOUT_MS=2000` / `DB_CONNECT_TIMEOUT` in `db.py` (fail-closed timeout, **not** a UX stopwatch). | **Unknown** — local Vite `GET /api/site` **32 ms** recorded on cts-ai this session. That is not a reservation/newsletter submit stopwatch. Do not say NFR-2 is **met**. | A 2s **timeout** plus a local GET sample are not evidence that happy-path submits finish in 2s on broadband. |
| NFR-3 | Interface intuitive and easy to navigate | `Layout.jsx` primary nav; `App.jsx` routes matching SRS pages | code; local UX J1–J8 **PASS** (cts-ai, DB up) supports navigation. J9 / NFR-3 **PASS** this session: Edge headless screenshots (home 375×812, menu 768×1024, reservations 1280×800) under `probe-nfr/` (App: valid PNG signatures). Vite-only. | Course UX is the five SRS pages plus newsletter. J1–J8 is local Journey UX with Flask+DB. Screenshot PASS is Vite-only, not a public device lab. |
| NFR-4 | Consistent, visually appealing brand | `theme.css` (burgundy/cream, Flexbox/Grid); Layout chrome on every page | code | SRS asks for brand consistency. Aesthetic judgment beyond the committed theme is Unknown. |
| NFR-5 | No double or over-bookings | Unique index `reservations_slot_table`; 30-table cap; `test_fail_closed.py` 31st table | code; CI; local UX J6 PASS (30 then 409) | Integrity is the reservation NFR. A race that assigns table 31 fails the assignment. |
| NFR-6 | User-friendly failure handling | `test_fail_closed.py` (missing DB, unreachable DB, timeout, full slot); frontend error banners | code; CI; local UX J8 PASS (503 fail-closed) | Fail closed: honest **no**, not a cached yes. Maps to FR-9 when the slot is full. |
| NFR-7 | Chrome, Firefox, Safari, Edge | Standard React SPA + CSS. Partial matrix: Vite-only `:5173` (cts-ai, 2026-09-02) plus owner/sponsor mobile UX this session (2026-09-05). | **Partial** — Safari **PASS** (owner/sponsor report this session, 2026-09-05): Safari on iPhone 16, restaurant App + Knowledge mobile fit. This is **mobile Safari**, not a desktop Safari probe. Edge **PASS** all routes with screenshots (Home, Menu, About, Gallery, Reservations; Vite-only 2026-09-02). Firefox **PASS** home (same Vite-only session — prior evidence). Chrome **Unknown**. Chrome and Firefox are now **installed on cts-ai** (owner report this session) — **probeable**; status **Unknown until App probes**. Do **not** mark PASS from install alone. A36 mobile UX probe this session (owner/sponsor); browser engine **Unknown** until named. Not a four-browser claim. [#44](https://github.com/artofdream/aea-interactive-design/issues/44) / [#117](https://github.com/artofdream/aea-interactive-design/issues/117). | Compatibility is an SRS NFR. Mobile Safari PASS plus Edge/Firefox Vite notes is still not Chrome + Firefox + Safari + Edge. An install on cts-ai is not a probe. |
| NFR-8 | Responsive desktop, tablet, smartphone | `frontend/index.html` viewport meta; `theme.css` Flex/Grid `repeat(auto-fit, minmax(…))` + `@media (max-width: 800px)` | code; J9 / NFR-8 **PASS** (Vite-only Edge screenshots, 2026-09-02). Public-host mobile note this session (2026-09-05, owner/sponsor report): iPhone 16 Safari + A36 UX fit on `cafe.artof.link` and Knowledge. Vite-only J9 is **not** the only evidence. Not an **NFR-1** / **NFR-2** stopwatch. | SRS requires Flexbox or Grid and responsive layout. Vite screenshots are local UX. Public-host mobile is owner/sponsor UX fit — not Flask+Postgres write proof. |
| NFR-9 | Modular, documented code | `backend/cafe_fausse/` packages; page components; `README.md`; this knowledge map | code | Maintainability is in the freeze. A single script dump would miss the NFR. |

### NFR-1 / NFR-2 timing notes (not a “met” claim)

App local Vite samples this session (cts-ai, while the stack was up):

- Vite home: **56 ms**
- `GET /api/site`: **32 ms**

These numbers stay in the evidence note. The SRS broadband claims (**NFR-1** 3s, **NFR-2** 2s form submit) stay **Unknown**. Timing probe recorded; not claiming the SRS budget is met.

### J9 / NFR-3 / NFR-8 viewport notes (Vite-only)

App Edge headless screenshots this session (cts-ai, Vite `:5173`). Files under `probe-nfr/` **on that machine**. App reported valid PNG signatures. **Not** committed in this repo. This Knowledge VM did not open those files.

- 375×812 home
- 768×1024 menu
- 1280×800 reservations

Committed theme (code this session): `frontend/index.html` `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`; `frontend/src/styles/theme.css` `@media (max-width: 800px)` and `grid-template-columns: repeat(auto-fit, minmax(…))`.

### Public-host mobile UX (owner/sponsor, 2026-09-05)

Owner report this session ([#117](https://github.com/artofdream/aea-interactive-design/issues/117)): Safari on iPhone 16 — UX validated for the restaurant App and Knowledge mobile fit. Sponsor also checks UX on iPhone + A36 (mobile). Hosts: `https://cafe.artof.link/` and Knowledge. This agent HTTPS **GET 200** on those hosts this session (liveness only — not the device UX). A36 browser engine **Unknown** until named. Not a four-browser **NFR-7** pass. **NFR-1** / **NFR-2** stay **Unknown**.

Prefer live share this session: `https://cafe.artof.link/` GET **200**. Interim backup `https://54-165-102-60.sslip.io/`. Old `https://shaky-deer-drive.loca.lt/` is **stale**. Do **not** claim production-forever hosting.

## Knowledge-site rows (not extra FRs)

These are harness surfaces, not new requirement IDs.

| Surface | In-repo | Evidence | Why it matters |
|---|---|---|---|
| SRS freeze on this map | `knowledge/srs.md`, built `srs-full.html` from `docs/srs.md` | code; CI (knowledge-site + srs-present) | Graders can see the ID freeze without opening the PDF first. |
| Honesty vocabulary | `knowledge/honesty.md` | code; local GET 200 on `https://knowledge.cafe.artof.link/honesty.html` this session | Prefer `cafe.artof.link` as weekend Lightsail staging (#57). Stops claiming production-forever hosting or that the `*.artof.link` ELB wildcard is Café Fausse. |
| Teammate brief | `knowledge/brief.md` | code | Meeting 2026-09-02 19:00 CET; Friday score-5 section. |
| Friday plan + video/slides | `knowledge/friday-plan.md`, `video-script.md`, `presentation.md`, `presentation-sample.md` | code | Working references for Friday 2026-09-04 and Saturday recording cuts. Not a substitute for the Journey table above. |
| Journey / NFR recording | this page; [#40](https://github.com/artofdream/aea-interactive-design/issues/40) / [#44](https://github.com/artofdream/aea-interactive-design/issues/44) / [#117](https://github.com/artofdream/aea-interactive-design/issues/117) | App local UX / GET 2026-09-02 (cts-ai); J9 / NFR-3 / NFR-8 Vite slice **Vite-only**; `probe-nfr/` PNGs on cts-ai (not in this repo); owner/sponsor mobile UX this session (2026-09-05) on public hosts; Chrome + Firefox now installed on cts-ai (probeable; Unknown until App probes); Knowledge GET of the 2026-09-02 tunnel timed out | J1–J8 PASS while DB was up; J9 / NFR-3 / NFR-8 PASS (Vite-only Edge screenshots + theme.css) plus public-host mobile note (iPhone 16 Safari + A36 UX fit). NFR-7 **partial** (Safari **PASS** on iPhone 16; Edge all routes + Firefox home on Vite; Chrome Unknown; Chrome/Firefox installed on cts-ai — probeable, not PASS from install; A36 browser engine Unknown). NFR-1 / NFR-2 not claimed met. Tunnel is not the live share; `cafe.artof.link` is. |
| Operator view `/operator` | App on `main` ([PR #58](https://github.com/artofdream/aea-interactive-design/pull/58) / [#54](https://github.com/artofdream/aea-interactive-design/issues/54)); brief note above | Knowledge GET `https://cafe.artof.link/operator` **200** this session (~0.6s). Interim backup `https://54-165-102-60.sslip.io/operator`. | Read-only recording helper (customers + reservations). **Not** an admin console. **Not FR-19.** Lightsail staging (#57); **not** production forever. |
| Knowledge nav / readability | `knowledge/style.css`; `knowledge/build.py` nav + section icons; table wraps | code ([#69](https://github.com/artofdream/aea-interactive-design/issues/69)) | Map affordance for phone + desktop. **Not** an **NFR-1** / **NFR-2** claim. Restaurant **NFR-8** is the App Vite record plus the public-host mobile note above. |

## Out of this table

Florist Path B, 14 hats, Kafka, BFF, 3DX Lab, GitLab, inventing FR-19, outbound newsletter mailer, claiming production-forever hosting. Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22) / [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38) stay parked. Weekend Lightsail [#57](https://github.com/artofdream/aea-interactive-design/issues/57) does not close #22. Public repo. Do not claim antifragile.

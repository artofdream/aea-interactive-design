# FR / NFR coverage map

Presentation map for the Quantic course. Every freeze ID from `docs/srs.md` (official PDF SoT). **FR-1..FR-18** and **NFR-1..NFR-9** only. Do not invent FR-19 / NFR-10.

This page is not the restaurant. Paths are the in-repo Café Fausse App on `main` (PRs #9 + timezone #12) plus knowledge/CI where that is the evidence.

**Evidence classes:** `code` = committed file this session; `CI` = GitHub Actions job in `.github/workflows/`; `local GET / UX this session (cts-ai)` = Café Fausse App probe (J1–J8: Vite + Flask + `cafe-pg` while the DB was up; J9 / NFR-7: **Vite-only** `:5173`); `Unknown` = no probe this session, or a measured number that is **not** an SRS-budget claim.

[Issue #40](https://github.com/artofdream/aea-interactive-design/issues/40) recorded J1–J8 (PR #43). [Issue #44](https://github.com/artofdream/aea-interactive-design/issues/44) records J9 + partial NFR-7. This Knowledge VM did not reach cts-ai Vite `:5173` / Flask `:5000`. The Journey table below is App’s this-session handoff, not a probe from this VM.

In plain language: the FR/NFR tables are “where the freeze shows up in the repo.” **Code** and **CI** are not the same as “we timed broadband” or “we checked four browsers.” Friday score-5 talk track: [Friday plan](friday-plan.md).

## Journey 1–9 (App naming this run)

Recorded from Café Fausse App (cts-ai) **2026-09-02 Europe/Berlin**.

**J1–J8** ([#40](https://github.com/artofdream/aea-interactive-design/issues/40) / PR #43): local UX / GET on Vite + Flask + `cafe-pg` **while the database was up** (seeded `friday.demo@example.com` and `newsletter.friday@example.com`). After that handoff, App reported `cafe-pg` unreachable and cts-ai dropped. Those later drops do **not** erase the J1–J8 PASS numbers from while the DB was up.

**J9 + NFR-3 / NFR-8 + NFR-7** ([#44](https://github.com/artofdream/aea-interactive-design/issues/44)): later **Vite-only** local UX on `:5173` this session. Edge headless screenshots + theme.css (viewports); partial browser matrix. **Do not** claim Flask + PostgreSQL for this probe. **Do not** claim `cafe.artof.link`.

Tunnel / Flask: App reports Docker Engine still coming up. Mentioned tunnel `https://nine-teams-try.loca.lt/` is ephemeral. This Knowledge VM `GET` of that URL **this session timed out** (curl 28, 12s). **Do not** claim the tunnel or Flask is live. No `cafe.artof.link` DNS for the restaurant.

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
| J9 | Responsive | **PASS** | Vite-only `:5173` this session (cts-ai). Edge headless screenshots under `probe-nfr/` (375×812 home, 768×1024 menu, 1280×800 reservations; App reported valid PNG signatures). Viewport meta + `@media (max-width: 800px)` + Flex/Grid `auto-fit` in `theme.css`. **Not** Flask+Postgres. **Not** `cafe.artof.link`. | NFR-8 |

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

## Non-functional requirements

| ID | Summary | In-repo | Evidence | Why it matters for the course |
|---|---|---|---|---|
| NFR-1 | Page load within 3 seconds on standard broadband | Intended SPA + static assets under `frontend/` and `theme.css`. | **Unknown** — local Vite home **56 ms** recorded on cts-ai this session. That is **not** an SRS broadband stopwatch. Do not say NFR-1 is **met**. | The SRS states a 3s budget on standard broadband. A single local Vite sample is an evidence note only. |
| NFR-2 | Form submissions processed within 2 seconds | `DB_STATEMENT_TIMEOUT_MS=2000` / `DB_CONNECT_TIMEOUT` in `db.py` (fail-closed timeout, **not** a UX stopwatch). | **Unknown** — local Vite `GET /api/site` **32 ms** recorded on cts-ai this session. That is not a reservation/newsletter submit stopwatch. Do not say NFR-2 is **met**. | A 2s **timeout** plus a local GET sample are not evidence that happy-path submits finish in 2s on broadband. |
| NFR-3 | Interface intuitive and easy to navigate | `Layout.jsx` primary nav; `App.jsx` routes matching SRS pages | code; local UX J1–J8 **PASS** (cts-ai, DB up) supports navigation. J9 / NFR-3 **PASS** this session: Edge headless screenshots (home 375×812, menu 768×1024, reservations 1280×800) under `probe-nfr/` (App: valid PNG signatures). Vite-only. | Course UX is the five SRS pages plus newsletter. J1–J8 is local Journey UX with Flask+DB. Screenshot PASS is Vite-only, not a public device lab. |
| NFR-4 | Consistent, visually appealing brand | `theme.css` (burgundy/cream, Flexbox/Grid); Layout chrome on every page | code | SRS asks for brand consistency. Aesthetic judgment beyond the committed theme is Unknown. |
| NFR-5 | No double or over-bookings | Unique index `reservations_slot_table`; 30-table cap; `test_fail_closed.py` 31st table | code; CI; local UX J6 PASS (30 then 409) | Integrity is the reservation NFR. A race that assigns table 31 fails the assignment. |
| NFR-6 | User-friendly failure handling | `test_fail_closed.py` (missing DB, unreachable DB, timeout, full slot); frontend error banners | code; CI; local UX J8 PASS (503 fail-closed) | Fail closed: honest **no**, not a cached yes. Maps to FR-9 when the slot is full. |
| NFR-7 | Chrome, Firefox, Safari, Edge | Standard React SPA + CSS. Partial browser matrix, **Vite-only** `:5173` this session (cts-ai). | **Partial** — Edge **PASS** all routes with screenshots (Home, Menu, About, Gallery, Reservations); Firefox **PASS** home; Chrome **Unknown** (not installed on cts-ai); Safari **Unknown** (not reported). Not a four-browser claim. | Compatibility is an SRS NFR. Two browsers probed is not Chrome + Firefox + Safari + Edge. |
| NFR-8 | Responsive desktop, tablet, smartphone | `frontend/index.html` viewport meta; `theme.css` Flex/Grid `repeat(auto-fit, minmax(…))` + `@media (max-width: 800px)` | code; J9 / NFR-8 **PASS** (Vite-only). Edge headless: 375×812 home, 768×1024 menu, 1280×800 reservations under `probe-nfr/` (App: valid PNG signatures). Public host **Unknown**. | SRS requires Flexbox or Grid and responsive layout. Screenshot PASS is local Vite UX, not Flask+Postgres or a public-host claim. |
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

Tunnel / Flask still wait on Docker Engine. Do **not** claim a tunnel is live.

## Knowledge-site rows (not extra FRs)

These are harness surfaces, not new requirement IDs.

| Surface | In-repo | Evidence | Why it matters |
|---|---|---|---|
| SRS freeze on this map | `knowledge/srs.md`, built `srs-full.html` from `docs/srs.md` | code; CI (knowledge-site + srs-present) | Graders can see the ID freeze without opening the PDF first. |
| Honesty vocabulary | `knowledge/honesty.md` | code; local GET 200 on `https://knowledge.cafe.artof.link/honesty.html` this session | Stops claiming `cafe.artof.link` is live Café Fausse. |
| Teammate brief | `knowledge/brief.md` | code | Meeting 2026-09-02 19:00 CET; Friday score-5 section. |
| Friday plan + video/slides | `knowledge/friday-plan.md`, `video-script.md`, `presentation-sample.md` | code | Working references for 2026-09-04 19:00 Europe/Berlin. Not a substitute for the Journey table above. |
| Journey / NFR recording | this page; [#40](https://github.com/artofdream/aea-interactive-design/issues/40) / [#44](https://github.com/artofdream/aea-interactive-design/issues/44) | App local UX / GET this session (cts-ai); J9 / NFR-3 / NFR-8 / NFR-7 **Vite-only**; `probe-nfr/` PNGs on cts-ai (not in this repo); Knowledge GET of mentioned tunnel timed out | J1–J8 PASS while DB was up; J9 / NFR-3 / NFR-8 PASS (Edge screenshots + theme.css); NFR-7 partial (Edge + Firefox home; Chrome not installed; Safari Unknown); NFR-1 / NFR-2 not claimed met. Tunnel / Flask not live (Docker Engine still coming). |

## Out of this table

Florist Path B, 14 hats, Kafka, BFF, 3DX Lab, GitLab, AWS restaurant hosting, invented IDs. Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22) / [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38) stay parked. Public repo. Do not claim antifragile.

# FR / NFR presentation coverage

Quantic presentation map: each official ID, where it lives in this repo, what was probed, and why it matters for the course. **IDs are only FR-1..FR-18 and NFR-1..NFR-9** from [`docs/srs.md`](srs.md) (PDF SoT). Do not invent IDs.

**Evidence class** is one or more of: `code` (committed path exists now), `CI` (GitHub Actions on `main` this session: workflow `CI` **success** on `dc42ece`), `HTTPS GET this session`, `local GET this session`, `Unknown`.

This cloud session did **not** have Vite `:5173`, Flask `:5000`, or `cafe-pg` listening (connection refused / Docker unavailable). UX journeys 1–9: **Unknown** (no journey files in this repo; no local GET). `cafe.artof.link` is **not** evidence of the app.

## Functional requirements

| ID | Summary | In-repo (page / path / API / CI) | Evidence class | Why for the course |
|---|---|---|---|---|
| FR-1 | Display Café Fausse’s name prominently | Home `<h1>` in `frontend/src/pages/Home.jsx`; header wordmark in `frontend/src/components/Layout.jsx`; `shared/freeze.json` `name` | code; CI `restaurant-frontend` | Home page of the SRS is visible in the SPA, not only in a slide |
| FR-2 | Contact + hours (freeze address, phone, hours) | Home visit/hours cards (`Home.jsx`); footer in `Layout.jsx`; `shared/freeze.json`; slot labels use `America/New_York` in `frontend/src/restaurantTime.js` (merged PR #12) | code; CI frontend unit tests | Freeze contact data was not rewritten; DC hours, not the browser calendar |
| FR-3 | High-quality images and a consistent theme | Official four webps in `assets/images/`; Home hero; `frontend/src/styles/theme.css` | code; CI `test_official_image_served_and_supplemental_is_not` | Course image pack only; student extras are not presented as official |
| FR-4 | Nav to Menu, Reservations, About Us, Gallery | `Layout.jsx` primary nav; `frontend/src/App.jsx` routes `/menu`, `/reservations`, `/about`, `/gallery` | code | Required five-page information architecture |
| FR-5 | Menu with frozen items and prices | `frontend/src/pages/Menu.jsx`; `shared/freeze.json` `menu`; Flask `GET /api/menu` in `backend/cafe_fausse/__init__.py`; `backend/tests/test_freeze.py` | code; CI `restaurant-api` | Menu prices match the SRS; no invented dishes |
| FR-6 | Reservation form: time slot, guests, name, email, optional phone | `frontend/src/pages/Reservations.jsx`; `POST /api/reservations`; `backend/cafe_fausse/validate.py` | code | Form fields match the SRS list |
| FR-7 | Validate time slot available and valid | `backend/cafe_fausse/slots.py`; `GET /api/slots`, `GET /api/availability`; `backend/tests/test_reservations.py` (`test_invalid_slot_rejected`) | code; CI | Hours and seating times come from the freeze, not a guessed calendar |
| FR-8 | Assign a random table from 30 when available | `backend/cafe_fausse/reservations.py` (`ORDER BY random()`, tables 1–30); `backend/schema.sql` `table_number`; freeze `tableCount` 30 | code; CI `test_reservation_assigns_a_table_from_thirty` | Core reservation demo: a real table number from 30 |
| FR-9 | Success message, or error if the slot is fully booked | Reservations status banner; `reservations.py` 409 `fully_booked`; `backend/tests/test_fail_closed.py` (no 31st table) | code; CI | Fail closed: a full book is an honest no, not a 31st table |
| FR-10 | History: founded 2010 by Chef Antonio Rossi and Maria Lopez | `frontend/src/pages/About.jsx`; Home lede; `shared/freeze.json` `history`; freeze-vs-SRS test | code; CI | About Us history is the SRS paragraph, not rewritten lore |
| FR-11 | Founder biographies; locally sourced ingredients | `About.jsx` founders + `locallySourced`; `shared/freeze.json` `founders` | code | Founders and sourcing commitment are on About Us as specified |
| FR-12 | Gallery: interior, dishes, events / behind-the-scenes | `frontend/src/pages/Gallery.jsx`; official `gallery-cafe-interior.webp`, `gallery-ribeye-steak.webp`, `gallery-special-event.webp`. Official zip has **four** files only — no separate behind-the-scenes file | code | Gallery uses the official pack; “behind-the-scenes” is not a fifth official image |
| FR-13 | Lightbox for enlarged images | `frontend/src/components/Lightbox.jsx` (used from `Gallery.jsx`) | code | Enlarged viewing is implemented, not a placeholder caption |
| FR-14 | Awards 2022/2023 and quoted reviews | `Gallery.jsx` awards + reviews; `shared/freeze.json`; `test_contact_hours_and_awards_match_srs` | code; CI | Awards and quotes are freeze data |
| FR-15 | Newsletter signup with email validation | `frontend/src/components/NewsletterForm.jsx` (`type=email`); `backend/cafe_fausse/validate.py`; `POST /api/newsletter` | code; CI `test_newsletter.py` | Email format is checked before a write |
| FR-16 | Store submitted emails in the backend database | `backend/cafe_fausse/newsletter.py` sets `customers.newsletter_signup`; `backend/schema.sql` | code; CI | Signup is a PostgreSQL write, not a client-only thank-you |
| FR-17 | PostgreSQL Customers and Reservations tables | `backend/schema.sql`; `backend/cafe_fausse/init_db.py`; CI job `restaurant-api` (Postgres 16 service) | code; CI | Schema matches the SRS tables (plus guest_count / timestamps; no new IDs) |
| FR-18 | Flask: insert customer, check availability, random table, confirm or error | `backend/cafe_fausse/__init__.py` (`POST /api/reservations`, availability/slots); `reservations.py` | code; CI | Backend reservation logic is Flask, as the SRS stack requires |

## Non-functional requirements

| ID | Summary | In-repo (page / path / API / CI) | Evidence class | Why for the course |
|---|---|---|---|---|
| NFR-1 | Load within 3 seconds on standard broadband | No 3-second load test, Lighthouse job, or this-session timing probe found in-repo | **Unknown** | Do not claim 3s in the presentation without a probe |
| NFR-2 | Form submissions processed within 2 seconds | Backend cap: `DB_CONNECT_TIMEOUT=2` and `DB_STATEMENT_TIMEOUT_MS=2000` in `backend/cafe_fausse/db.py` and `.github/workflows/ci.yml`. Frontend abort in `frontend/src/api.js` is **8000 ms**, not 2s. No wall-clock 2s measurement this session | code (timeout cap); measured 2s **Unknown** | Fail-closed DB timeouts exist; “processed in 2s” is unmeasured here |
| NFR-3 | Intuitive and easy to navigate | Primary nav + five routes (`Layout.jsx`, `App.jsx`) | code; usability study **Unknown** | Required IA is in the SPA; “intuitive” is not a GET |
| NFR-4 | Consistent brand; visually appealing | `frontend/src/styles/theme.css` (burgundy/cream/gold); official images | code; visual-appeal probe **Unknown** | Theme tokens exist; “appealing” is a judgment, not a sensor |
| NFR-5 | No double or over-bookings | `schema.sql` unique index `reservations_slot_table`; row lock + 30-table cap in `reservations.py`; `test_fail_closed.py` | code; CI | Data integrity for the reservation demo |
| NFR-6 | User-friendly failure handling | Flask 503 `DatabaseUnavailable`; form banners on Reservations and Newsletter; fail-closed tests | code; CI | Missing DB / timeout is an honest error, not a cached yes |
| NFR-7 | Chrome, Firefox, Safari, Edge | No browser-matrix CI, Playwright project, or this-session browser probe found | **Unknown** | Compatibility is specified; it is unprobed in this session |
| NFR-8 | Responsive: desktop, tablet, smartphone | Flexbox/Grid in `theme.css`; `@media (max-width: 800px)` | code; viewport probe this session **Unknown** | Responsive CSS is present; no device-lab GET this session |
| NFR-9 | Modular, well-documented code | Flask package `backend/cafe_fausse/` (factory + modules); React pages/components; README local-run; module docstrings | code | Maintainable layout for graders and teammates |

## CI and freeze sensors (not extra IDs)

| Sensor | Path | This session |
|---|---|---|
| SRS freeze present (FR-1..FR-18 / NFR-1..NFR-9 entries + PDF/zip SHA256) | `.github/workflows/ci.yml` job `srs-present` | CI on `main` **success** (`dc42ece`) |
| GitHub only (no GitLab CI files) | `.github/workflows/ci.yml` job `github-only` | same run **success** |
| Restaurant API tests | `.github/workflows/ci.yml` job `restaurant-api` | same run **success** |
| Restaurant frontend test + build | `.github/workflows/ci.yml` job `restaurant-frontend` | same run **success** |
| Knowledge Markdown → Pages | `.github/workflows/knowledge-site.yml` | Knowledge site on `main` **success** (`dc42ece`) |

## Not claimed

- Live restaurant at `cafe.artof.link` — CNAME to an AWS ELB hostname that did not resolve this session.
- Local Vite/Flask/Postgres in **this** cloud session — ports closed.
- UX journeys 1–9 — **Unknown**.
- System is antifragile — do not say this.

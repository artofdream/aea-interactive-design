# FR / NFR coverage map

Presentation map for the Quantic course. Every freeze ID from `docs/srs.md` (official PDF SoT). **FR-1..FR-18** and **NFR-1..NFR-9** only. Do not invent FR-19 / NFR-10.

This page is not the restaurant. Paths are the in-repo Café Fausse App on `main` (PRs #9 + timezone #12) plus knowledge/CI where that is the evidence.

**Evidence classes:** `code` = committed file this session; `CI` = GitHub Actions job in `.github/workflows/`; `local GET this session` = HTTP GET from this agent VM; `Unknown` = no probe this session.

**This agent VM** did not reach cts-ai Vite `:5173` / Flask `:5000`. Journey 1–9 pass/fail stays **Unknown**. NFR load and submit timings stay **Unknown** (no stopwatch this session).

## Functional requirements

| ID | Summary | In-repo | Evidence | Why it matters for the course |
|---|---|---|---|---|
| FR-1 | Display Café Fausse’s name prominently | `frontend/src/pages/Home.jsx` (`<h1>` from freeze); `frontend/src/components/Layout.jsx` wordmark | code | Home is the first SRS product function. Graders look for the restaurant name on the digital front door. |
| FR-2 | Contact + hours (freeze address, phone, Mon–Sat / Sunday hours) | `Home.jsx` visit/hours cards; `Layout.jsx` footer; `shared/freeze.json`; Flask `GET /api/site` | code; CI (`test_freeze.py`) | Freeze data. Changing the address or hours is a spec miss, not a polish. |
| FR-3 | High-quality images and a consistent theme | `Home.jsx` hero from official images; `frontend/src/styles/theme.css` | code | Course image pack is **four webps only**. Theme must hold across pages (NFR-4 adjacency). |
| FR-4 | Nav to Menu, Reservations, About Us, Gallery | `Layout.jsx` `LINKS`; `frontend/src/App.jsx` routes | code | SRS names those four destinations. Missing a route is a missing FR. |
| FR-5 | Menu by category with freeze items and prices | `frontend/src/pages/Menu.jsx`; `shared/freeze.json`; `backend/cafe_fausse/content.py`; `GET /api/menu` | code; CI (`test_freeze.py`) | Prices and copy are SoT. Do not “improve” the menu in MVP. |
| FR-6 | Reservation form: time slot, guests, name, email, optional phone | `frontend/src/pages/Reservations.jsx`; `backend/cafe_fausse/validate.py` | code | This is the reservations page the SRS lists as a product function. |
| FR-7 | Validate the selected slot is available and valid | `backend/cafe_fausse/slots.py`; `reservations.py`; `GET /api/slots`; tests in `test_reservations.py` | code; CI | Invalid or closed hours must not book. Sunday last seating is freeze hours, not a guess. |
| FR-8 | Assign a random table from 30 when the slot has room | `reservations.py` (`ORDER BY random()`); `schema.sql` `table_number BETWEEN 1 AND 30` | code; CI (`test_reservations.py`, `test_fail_closed.py`) | Table pool is 30. A 31st table would violate the SRS. |
| FR-9 | Success message, or error if the slot is fully booked | `Reservations.jsx` banners; `reservations.py` `fully_booked`; `test_fail_closed.py` | code; CI | Fail closed: a full book is an honest **no**, not a guessed table. |
| FR-10 | History: founded 2010 by Chef Antonio Rossi and Maria Lopez | `frontend/src/pages/About.jsx` (`freeze.history`) | code; CI (`test_freeze.py`) | About Us copy is freeze text. |
| FR-11 | Founder biographies; locally sourced ingredients | `About.jsx` founders + `freeze.locallySourced` | code | SRS About Us is history **and** founder bios / sourcing, not a slogan page. |
| FR-12 | Gallery: interior, dishes, events / behind-the-scenes | `frontend/src/pages/Gallery.jsx`; official four webps in `assets/images/` | code | App must not substitute the 17 student-recovered files in `supplemental-not-official/`. |
| FR-13 | Lightbox for enlarged images | `frontend/src/components/Lightbox.jsx` used by `Gallery.jsx` | code | SRS asks for enlarged viewing, not thumbnails only. |
| FR-14 | Awards 2022/2023 and quoted reviews | `Gallery.jsx` awards + reviews from freeze | code; CI (`test_freeze.py`) | Award names and review quotes are freeze data. |
| FR-15 | Newsletter signup with email-format validation | `frontend/src/components/NewsletterForm.jsx`; `validate.py`; `test_fail_closed.py` invalid email | code; CI | Bad emails must not be stored. HTML `type=email` plus server check. |
| FR-16 | Store submitted emails in the backend database | `backend/cafe_fausse/newsletter.py`; `customers.newsletter_signup` in `schema.sql` | code; CI (`test_newsletter.py`) | Signup is a write. Missing DB → honest no (NFR-6), not a fake success. |
| FR-17 | PostgreSQL Customers + Reservations tables | `backend/schema.sql`; `backend/cafe_fausse/init_db.py`; `db.py` | code; CI (restaurant-api job) | SRS names the tables and columns. No database → no booking. |
| FR-18 | Flask: insert customer, check availability, random table, confirm or error | `backend/cafe_fausse/__init__.py` (`POST /api/reservations`); `reservations.py` | code; CI | Back-end reservation system is an SRS product function, not a static form. |

## Non-functional requirements

| ID | Summary | In-repo | Evidence | Why it matters for the course |
|---|---|---|---|---|
| NFR-1 | Page load within 3 seconds on standard broadband | Intended SPA + static assets under `frontend/` and `theme.css`. **No timing run this session.** | Unknown | The SRS states a 3s budget. Without a measured probe, do not say it is met. |
| NFR-2 | Form submissions processed within 2 seconds | `DB_STATEMENT_TIMEOUT_MS=2000` / `DB_CONNECT_TIMEOUT` in `db.py` (fail-closed timeout, **not** a UX stopwatch). | Unknown | A 2s **timeout** is not evidence that happy-path submits finish in 2s. Timing stays Unknown. |
| NFR-3 | Interface intuitive and easy to navigate | `Layout.jsx` primary nav; `App.jsx` routes matching SRS pages | code | Course UX is the five SRS pages plus newsletter. Journey 1–9 pass/fail: **Unknown**. |
| NFR-4 | Consistent, visually appealing brand | `theme.css` (burgundy/cream, Flexbox/Grid); Layout chrome on every page | code | SRS asks for brand consistency. Aesthetic judgment beyond the committed theme is Unknown. |
| NFR-5 | No double or over-bookings | Unique index `reservations_slot_table`; 30-table cap; `test_fail_closed.py` 31st table | code; CI | Integrity is the reservation NFR. A race that assigns table 31 fails the assignment. |
| NFR-6 | User-friendly failure handling | `test_fail_closed.py` (missing DB, unreachable DB, timeout, full slot); frontend error banners | code; CI | Fail closed: honest **no**, not a cached yes. Maps to FR-9 when the slot is full. |
| NFR-7 | Chrome, Firefox, Safari, Edge | Standard React SPA + CSS. **No browser matrix probe this session.** | Unknown | Compatibility is an SRS NFR. Claiming four browsers without a probe is a status-word miss. |
| NFR-8 | Responsive desktop, tablet, smartphone | `theme.css` Grid/Flexbox + `@media (max-width: 800px)` | code | SRS requires Flexbox or Grid and responsive layout. Device lab results: **Unknown**. |
| NFR-9 | Modular, documented code | `backend/cafe_fausse/` packages; page components; `README.md`; this knowledge map | code | Maintainability is in the freeze. A single script dump would miss the NFR. |

## Knowledge-site rows (not extra FRs)

These are harness surfaces, not new requirement IDs.

| Surface | In-repo | Evidence | Why it matters |
|---|---|---|---|
| SRS freeze on this map | `knowledge/srs.md`, built `srs-full.html` from `docs/srs.md` | code; CI (knowledge-site + srs-present) | Graders can see the ID freeze without opening the PDF first. |
| Honesty vocabulary | `knowledge/honesty.md` | code; local GET 200 on `https://knowledge.cafe.artof.link/honesty.html` this session | Stops claiming `cafe.artof.link` is live Café Fausse. |
| Teammate brief | `knowledge/brief.md` | code | Meeting 2026-09-02 19:00 CET. |

## Out of this table

Florist Path B, 14 hats, Kafka, BFF, 3DX Lab, GitLab, AWS restaurant hosting, invented IDs. Public repo. Do not claim antifragile.

# SRS freeze

The restaurant **MVP is this freeze**. Do not invent IDs. Do not grow the first app cut past these requirements.

**Source of truth:** official PDF (SHA256 `6075e5964601aa3e3c7a3085c626eab820e3d733a396b00e20339cfdc77a9d82`), local `docs/official/MSEE_Web_Application_and_Interface_Design_Cafe_Fausse_SRS.pdf`. Working freeze: [docs/srs.md](srs-full.html).

Two public student transcripts **corroborate** FR-1..FR-18 and NFR-1..NFR-9; they are not SoT. If a later official PDF differs, the PDF wins.

The restaurant MVP is implemented **in-repo** (`frontend/`, `backend/`, `shared/freeze.json`) on `main` (merged PRs #9, #12). This knowledge site is **not** the restaurant. Public `cafe.artof.link` is **not** our live app (see [Honesty](honesty.md)). Presentation map: [FR/NFR coverage](coverage.md).

## Functional requirements

| ID | Summary |
|---|---|
| FR-1 | Display Café Fausse’s name prominently |
| FR-2 | Contact: 1234 Culinary Ave, Suite 100, Washington, DC 20002; (202) 555-4567; Mon–Sat 5:00PM–11:00 PM, Sun 5:00 PM–9:00 PM |
| FR-3 | High-quality images and a consistent theme |
| FR-4 | Nav to Menu, Reservations, About Us, Gallery |
| FR-5 | Menu with frozen items and prices (see full SRS) |
| FR-6 | Reservation form: time slot, guests, name, email, optional phone |
| FR-7 | Validate time slot available and valid |
| FR-8 | Assign a random table from 30 when available |
| FR-9 | Success message, or error if the slot is fully booked |
| FR-10 | History: founded 2010 by Chef Antonio Rossi and Maria Lopez |
| FR-11 | Founder biographies; locally sourced ingredients |
| FR-12 | Gallery: interior, dishes, events / behind-the-scenes |
| FR-13 | Lightbox for enlarged images |
| FR-14 | Awards 2022/2023 and quoted reviews |
| FR-15 | Newsletter signup with email validation |
| FR-16 | Store submitted emails in the backend database |
| FR-17 | PostgreSQL: Customers and Reservations tables |
| FR-18 | Flask: insert customer, check availability, random table, confirm or error |

## Non-functional requirements

| ID | Summary |
|---|---|
| NFR-1 | Load within 3 seconds on standard broadband |
| NFR-2 | Form submissions processed within 2 seconds |
| NFR-3 | Intuitive navigation |
| NFR-4 | Consistent, visually appealing brand |
| NFR-5 | No double or over-bookings |
| NFR-6 | User-friendly failure handling |
| NFR-7 | Chrome, Firefox, Safari, Edge |
| NFR-8 | Responsive: desktop, tablet, smartphone |
| NFR-9 | Modular, documented code |

## Not in the MVP

Anything not listed above is [Future / not-MVP](future.md).

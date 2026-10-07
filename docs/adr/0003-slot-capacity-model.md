# ADR-0003: Reservation slot and capacity model: 30 tables per seating, HTTP 409 when full, fail closed

## Status

Accepted (retroactive, recorded 2026-10-07)

## Date

2026-08-31: landed with the restaurant MVP (PR #9).

## Context

The SRS asks for a reservation form with a time slot (FR-6), and requires that the selected slot be checked as available and valid (FR-7). The system must assign a random table out of 30 (FR-8, FR-18) and show an error when the slot is fully booked (FR-9). It must prevent double or over-bookings (NFR-5) and handle failures in a user-friendly way (NFR-6). `AGENTS.md` adds a fail-closed rule: a missing database, a fully booked slot (30 tables) or a timeout gets an honest **no**, never a guessed yes.

## Decision

- **Seatings:** discrete slots every `slotIntervalMinutes` (60), taken from `shared/freeze.json` `hoursByWeekday`. The first seating is 17:00. The last seating is 22:00 Monday–Saturday and 20:00 on Sunday, in restaurant-local time ([ADR-0006](0006-restaurant-timezone.md)). `GET /api/slots?date=` lists future seatings only. `parse_time_slot` rejects a slot that is missing, not ISO-8601, off the interval, outside hours or in the past, with HTTP 400 `invalid_slot`.
- **Capacity:** each seating has `tableCount` = 30 tables (freeze). One booking takes one table whatever the party size. The guest count (1–20) is validated but does not change capacity.
- **Assignment (FR-8):** everything happens in one transaction. First, upsert the customer by email. Then `SELECT … FOR UPDATE` the seating's existing reservation rows. Finally, insert with a random free table (`generate_series(1, 30)` minus the taken tables, `ORDER BY random() LIMIT 1`).
- **Integrity backstop (NFR-5):** `UNIQUE (time_slot, table_number)` and `CHECK (table_number BETWEEN 1 AND 30)` in `backend/schema.sql`.
- **Full seating (FR-9):** HTTP **409**, `code: "fully_booked"`, with the message "This time slot is fully booked. No table was assigned." A concurrent insert that hits the unique index gets 409 `fully_booked` if the seating is now full, otherwise 409 `table_conflict` ("submit the reservation again"). The API never guesses a table.
- **Fail closed (NFR-6):** a missing `DATABASE_URL`, unreachable PostgreSQL, a connect timeout (`DB_CONNECT_TIMEOUT`, default 2 s) or a statement timeout (`DB_STATEMENT_TIMEOUT_MS`, default 2000) returns HTTP **503** with `ok: false` and "The request was not saved." Any error rolls the transaction back.
- `GET /api/availability?time_slot=` reports the remaining tables and `fully_booked`. The Reservations page shows the server message in a success or error banner.

## Consequences

- The system cannot book more than 30 tables per seating, even under concurrency. The database enforces the limit and the API reports it honestly.
- `FOR UPDATE` only locks rows that already exist, so two first bookings for an empty seating can race. The unique index catches that case and the guest is asked to resubmit (409 `table_conflict`). There is no automatic retry.
- Party size does not affect capacity: a 20-guest booking uses one table, the same as a 2-guest booking.
- The customer upsert by email overwrites the stored name, and the phone number when one is given, on every booking.
- Covered by `test_reservation_assigns_a_table_from_thirty`, `test_full_slot_does_not_assign_a_31st_table`, `test_availability_zero_when_full` and `test_sunday_last_seating_is_8pm_not_10pm`, plus the no-database, unreachable-database and timeout tests in `backend/tests/test_fail_closed.py`.

## Related requirements

Related requirements: FR-6, FR-7, FR-8, FR-9, FR-18, NFR-5, NFR-6

## Evidence

- `5603d85` feat: implement Café Fausse restaurant MVP (#7) (PR #9): `slots.py`, `reservations.py`, `db.py`, `schema.sql`, 409 `fully_booked`, 503 fail-closed. The PR #9 body states "Time slot with 30 tables booked → HTTP 409 `fully_booked`, no 31st table".
- Probe record: `knowledge/coverage.md` Journey J6, "30 tables then HTTP 409" (issue #40).

## OPEN

- OPEN: Why seatings are 60 minutes apart and the last seating is one hour before closing is not recorded. The SRS gives opening hours only, with no seating interval or last seating.
- OPEN: Why capacity is one table per booking regardless of party size, and why the guest cap is 20, is not recorded.
- OPEN: Why a full slot returns HTTP 409 rather than another 4xx status is not recorded. PR #9 states the choice but not the reason.

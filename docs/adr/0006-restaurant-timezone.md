# ADR-0006: Restaurant-local time zone (America/New_York) for slots and reservations

## Status

Accepted (retroactive, recorded 2026-10-07)

## Date

2026-08-31: the backend landed with the MVP (PR #9). The frontend fix landed the same day (PR #12).

## Context

The SRS gives a Washington, DC address and local opening hours (FR-2), and the reservation form needs a date and time (FR-6) that can be validated (FR-7). Visitors, CI runners and the staging host can each sit in a different time zone. Bugbot on PR #9 found that the Reservations page used the browser's calendar and clock, while `/api/slots` used America/New_York. Outside US Eastern time, the date picker could hide the restaurant's current day, and the slot labels disagreed with the published DC hours (issue #11). Issue #11 cites FR-3 for the hours, but in `docs/srs.md` the hours are FR-2, which is what PR #12 cites.

## Decision

- **One zone for all restaurant time:** `shared/freeze.json` `timezone: "America/New_York"`, loaded as `TIMEZONE_NAME` in `backend/cafe_fausse/content.py`.
- **Backend** (`backend/cafe_fausse/slots.py`, `zoneinfo`):
  - `GET /api/slots?date=YYYY-MM-DD` treats the date as a New York calendar date and returns seatings with their real UTC offset, for example `2028-06-15T17:00:00-04:00`.
  - A time slot without a zone is read as New York time. A slot with a zone is converted to New York time before the hour and interval checks.
  - "In the future" is judged against the current time in New York.
- **Storage:** `reservations.time_slot` is `TIMESTAMPTZ`, an absolute instant. The confirmation message prints New York local time with the zone abbreviation.
- **Frontend** (`frontend/src/restaurantTime.js`): `todayISODate` and `formatSlot` use `Intl` with `freeze.timezone`. They throw if no zone is given instead of falling back to the browser's zone. A source test stops `Reservations.jsx` from going back to `getFullYear`, `getMonth` or the browser-default `toLocaleTimeString`.

## Consequences

- A visitor in Europe or California sees the restaurant's dates and DC times, so no seating is hidden by a different local "today".
- Daylight-saving shifts come from the IANA tz database. Seatings run 17:00–22:00, so none falls in the 02:00 DST gap or overlap.
- The backend needs IANA tz data at runtime. The Linux CI runners and the staging host have it. On a Windows Python 3.12 install without the `tzdata` package, `ZoneInfo("America/New_York")` raises `ZoneInfoNotFoundError` (observed on 2026-10-07 while recording this ADR). `backend/requirements.txt` does not list `tzdata`.
- Covered by `backend/tests/test_restaurant_timezone.py` (New York calendar rather than UTC, Sunday last seating at 20:00, a UTC instant that is already the next morning) and `frontend/src/restaurantTime.test.js`.

## Related requirements

Related requirements: FR-2, FR-6, FR-7

## Evidence

- `5603d85` feat: implement Café Fausse restaurant MVP (#7) (PR #9): `freeze.timezone`, `slots.py` with `ZoneInfo`, `TIMESTAMPTZ` slots.
- `d508ec3` fix: use America/New_York for reservation dates and slot labels (#11) (PR #12): `restaurantTime.js`, frontend tests, `test_restaurant_timezone.py`.

## OPEN

- OPEN: Whether the restaurant zone should ever be configurable (environment versus `freeze.json`) is not recorded. Today it is a freeze constant.
- OPEN: Whether to add `tzdata` to `backend/requirements.txt` for Windows development hosts is undecided. Adding it would be a dependency change outside this ADR set.

"""Valid reservation time slots (FR-7). Hours from the official SRS freeze (FR-2).

Monday–Saturday: 5:00 PM – 11:00 PM
Sunday: 5:00 PM – 9:00 PM

Slots are 30-minute starts in America/New_York. Last seating is 30 minutes
before posted close so a party is not seated at closing.
"""

from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

from cafe_fausse.config import RESTAURANT_TZ

TZ = ZoneInfo(RESTAURANT_TZ)
OPEN = time(17, 0)
LAST_SEAT_WEEKDAY = time(22, 30)  # Mon–Sat close 23:00
LAST_SEAT_SUNDAY = time(20, 30)  # Sunday close 21:00


def last_seating_for(weekday):
    """weekday: Monday=0 … Sunday=6."""
    if weekday == 6:
        return LAST_SEAT_SUNDAY
    return LAST_SEAT_WEEKDAY


def parse_timeslot(value):
    """Parse an ISO-8601 string to an aware datetime, or None."""
    if not isinstance(value, str) or not value.strip():
        return None
    raw = value.strip()
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=TZ)
    return dt


def as_local(dt):
    return dt.astimezone(TZ)


def is_on_half_hour(dt):
    local = as_local(dt)
    return local.second == 0 and local.microsecond == 0 and local.minute in (0, 30)


def is_within_hours(dt):
    """True when the slot is a valid seating time on that local calendar day."""
    if not is_on_half_hour(dt):
        return False
    local = as_local(dt)
    last = last_seating_for(local.weekday())
    stamp = local.timetz().replace(tzinfo=None)
    return OPEN <= stamp <= last


def is_in_the_future(dt, now=None):
    now = now or datetime.now(TZ)
    return as_local(dt) > now


def is_valid_slot(dt, now=None):
    """FR-7: slot must be valid (hours + half-hour) and not in the past."""
    return is_within_hours(dt) and is_in_the_future(dt, now=now)


def slots_for_date(day, now=None):
    """Return aware datetimes for every valid slot on `day` (local date)."""
    if not isinstance(day, date):
        return []
    last = last_seating_for(day.weekday())
    cursor = datetime.combine(day, OPEN, tzinfo=TZ)
    end = datetime.combine(day, last, tzinfo=TZ)
    now = now or datetime.now(TZ)
    out = []
    while cursor <= end:
        if cursor > now:
            out.append(cursor)
        cursor += timedelta(minutes=30)
    return out


def isoformat_local(dt):
    return as_local(dt).isoformat()

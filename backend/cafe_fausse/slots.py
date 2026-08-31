"""Valid reservation time slots from freeze hours (FR-7)."""

from __future__ import annotations

from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

from cafe_fausse.content import TIMEZONE_NAME, freeze

TZ = ZoneInfo(TIMEZONE_NAME)
SLOT_MINUTES = int(freeze["slotIntervalMinutes"])


class SlotError(ValueError):
    pass


def _parse_hhmm(value: str) -> time:
    hour, minute = value.split(":")
    return time(int(hour), int(minute))


def _hours_for(dt: datetime) -> tuple[time, time]:
    key = dt.strftime("%A").lower()
    spec = freeze["hoursByWeekday"][key]
    return _parse_hhmm(spec["open"]), _parse_hhmm(spec["lastSeating"])


def _on_the_interval(dt: datetime) -> bool:
    local = dt.astimezone(TZ)
    return local.minute % SLOT_MINUTES == 0 and local.second == 0 and local.microsecond == 0


def iter_slots_on_date(day: datetime, *, now: datetime | None = None) -> list[datetime]:
    """Return bookable slots for a local calendar date (timezone-aware)."""
    local_day = day.astimezone(TZ).replace(hour=0, minute=0, second=0, microsecond=0)
    open_at, last_seating = _hours_for(local_day)
    cursor = local_day.replace(hour=open_at.hour, minute=open_at.minute)
    last = local_day.replace(hour=last_seating.hour, minute=last_seating.minute)
    now_local = (now or datetime.now(TZ)).astimezone(TZ)
    slots: list[datetime] = []
    step = timedelta(minutes=SLOT_MINUTES)
    while cursor <= last:
        if cursor > now_local:
            slots.append(cursor)
        cursor += step
    return slots


def list_slots_for_date(date_str: str, *, now: datetime | None = None) -> list[str]:
    try:
        year, month, day = (int(p) for p in date_str.split("-"))
        local_midnight = datetime(year, month, day, tzinfo=TZ)
    except (TypeError, ValueError) as exc:
        raise SlotError("Date must be YYYY-MM-DD.") from exc
    return [dt.isoformat() for dt in iter_slots_on_date(local_midnight, now=now)]


def parse_time_slot(raw: str, *, now: datetime | None = None) -> datetime:
    if not raw or not str(raw).strip():
        raise SlotError("Time slot is required.")
    try:
        parsed = datetime.fromisoformat(str(raw).strip())
    except ValueError as exc:
        raise SlotError("Time slot must be an ISO-8601 date and time.") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=TZ)
    else:
        parsed = parsed.astimezone(TZ)
    parsed = parsed.replace(microsecond=0)
    if not _on_the_interval(parsed):
        raise SlotError("Time slot must fall on a restaurant seating time.")
    open_at, last_seating = _hours_for(parsed)
    seating = parsed.timetz().replace(tzinfo=None)
    if seating < open_at or seating > last_seating:
        raise SlotError("Time slot is outside Café Fausse hours.")
    now_local = (now or datetime.now(TZ)).astimezone(TZ)
    if parsed <= now_local:
        raise SlotError("Time slot must be in the future.")
    return parsed

"""FR-7: time slots must match posted hours and half-hour seating."""

from datetime import datetime

from cafe_fausse.slots import TZ, is_valid_slot, slots_for_date
from cafe_fausse.validate import require_timeslot
from cafe_fausse.errors import ApiError
import pytest


FROZEN_NOW = datetime(2026, 8, 31, 12, 0, tzinfo=TZ)


def test_saturday_dinner_is_valid():
    dt = datetime(2026, 9, 5, 19, 0, tzinfo=TZ)
    assert is_valid_slot(dt, now=FROZEN_NOW)


def test_sunday_last_seating_2030_is_valid():
    dt = datetime(2026, 9, 6, 20, 30, tzinfo=TZ)
    assert is_valid_slot(dt, now=FROZEN_NOW)


def test_sunday_at_close_is_invalid():
    dt = datetime(2026, 9, 6, 21, 0, tzinfo=TZ)
    assert not is_valid_slot(dt, now=FROZEN_NOW)


def test_before_open_is_invalid():
    dt = datetime(2026, 9, 5, 16, 30, tzinfo=TZ)
    assert not is_valid_slot(dt, now=FROZEN_NOW)


def test_weekday_last_seating_2230_is_valid():
    dt = datetime(2026, 9, 5, 22, 30, tzinfo=TZ)
    assert is_valid_slot(dt, now=FROZEN_NOW)


def test_weekday_at_close_is_invalid():
    dt = datetime(2026, 9, 5, 23, 0, tzinfo=TZ)
    assert not is_valid_slot(dt, now=FROZEN_NOW)


def test_quarter_hour_is_invalid():
    dt = datetime(2026, 9, 5, 19, 15, tzinfo=TZ)
    assert not is_valid_slot(dt, now=FROZEN_NOW)


def test_past_slot_is_invalid():
    dt = datetime(2026, 8, 30, 19, 0, tzinfo=TZ)
    assert not is_valid_slot(dt, now=FROZEN_NOW)


def test_require_timeslot_rejects_garbage():
    with pytest.raises(ApiError) as exc:
        require_timeslot("not-a-time")
    assert exc.value.code == "invalid_slot"


def test_slots_for_saturday_span_dinner():
    day = datetime(2026, 9, 5).date()
    slots = slots_for_date(day, now=FROZEN_NOW)
    assert slots[0].hour == 17 and slots[0].minute == 0
    assert slots[-1].hour == 22 and slots[-1].minute == 30

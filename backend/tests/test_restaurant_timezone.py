"""Reservation dates and slot labels follow America/New_York (issue #11)."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from cafe_fausse.content import TIMEZONE_NAME, freeze
from cafe_fausse.slots import list_slots_for_date

REPO = Path(__file__).resolve().parents[2]
RESERVATIONS_PAGE = REPO / "frontend" / "src" / "pages" / "Reservations.jsx"
RESTAURANT_TIME = REPO / "frontend" / "src" / "restaurantTime.js"


def test_freeze_timezone_is_america_new_york():
    assert freeze["timezone"] == "America/New_York"
    assert TIMEZONE_NAME == "America/New_York"


def test_slots_date_query_is_new_york_calendar_not_utc():
    now = datetime(2028, 6, 15, 16, 0, tzinfo=ZoneInfo("America/New_York"))
    slots = list_slots_for_date("2028-06-15", now=now)
    assert slots[0] == "2028-06-15T17:00:00-04:00"
    assert slots[-1] == "2028-06-15T22:00:00-04:00"


def test_slots_sunday_last_seating_is_8pm_eastern():
    now = datetime(2028, 6, 18, 16, 0, tzinfo=ZoneInfo("America/New_York"))
    slots = list_slots_for_date("2028-06-18", now=now)
    assert slots[-1] == "2028-06-18T20:00:00-04:00"
    assert "2028-06-18T22:00:00-04:00" not in slots


def test_utc_next_morning_does_not_change_new_york_date():
    """11:30pm EDT is already 03:30 UTC next day; the date string is still NY's."""
    now = datetime(2028, 6, 16, 3, 30, tzinfo=ZoneInfo("UTC"))
    slots = list_slots_for_date("2028-06-15", now=now)
    assert slots == []


def test_reservations_page_uses_restaurant_timezone_helpers():
    page = RESERVATIONS_PAGE.read_text(encoding="utf-8")
    helper = RESTAURANT_TIME.read_text(encoding="utf-8")
    assert "restaurantTime.js" in page
    assert "todayISODate" in page
    assert "formatSlot" in page
    assert "freeze.timezone" in page
    assert "getFullYear" not in page
    assert "getMonth" not in page
    assert "toLocaleTimeString(undefined" not in page
    assert "timeZone" in helper
    assert "browser calendar" in helper or "America/New_York" in helper or "freeze.timezone" in page

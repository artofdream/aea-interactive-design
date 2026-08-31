"""Input validation for reservation and newsletter forms (FR-6, FR-7, FR-15)."""

import re

from cafe_fausse.config import MAX_GUESTS_PER_TABLE
from cafe_fausse.errors import ApiError
from cafe_fausse.slots import is_valid_slot, parse_timeslot

# Practical email check (FR-15). Not a full RFC parser; rejects empty and obvious junk.
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
PHONE_RE = re.compile(r"^[0-9+().\s-]{7,20}$")


def normalize_email(value):
    if not isinstance(value, str):
        return ""
    return value.strip().lower()


def is_valid_email(value):
    email = normalize_email(value)
    return bool(email) and EMAIL_RE.match(email) is not None


def require_email(value):
    if not is_valid_email(value):
        raise ApiError(400, "invalid_email", "Please enter a valid email address.")
    return normalize_email(value)


def require_name(value):
    if not isinstance(value, str):
        raise ApiError(400, "invalid_name", "Please enter the name for this reservation.")
    name = " ".join(value.split())
    if not name or len(name) > 120:
        raise ApiError(400, "invalid_name", "Please enter the name for this reservation.")
    return name


def optional_phone(value):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ApiError(400, "invalid_phone", "Please enter a valid phone number, or leave it blank.")
    phone = value.strip()
    if not phone:
        return None
    if not PHONE_RE.match(phone):
        raise ApiError(400, "invalid_phone", "Please enter a valid phone number, or leave it blank.")
    return phone


def require_guests(value):
    try:
        guests = int(value)
    except (TypeError, ValueError):
        raise ApiError(
            400,
            "invalid_guests",
            f"Number of guests must be a whole number from 1 to {MAX_GUESTS_PER_TABLE}.",
        )
    if guests < 1 or guests > MAX_GUESTS_PER_TABLE:
        raise ApiError(
            400,
            "invalid_guests",
            f"Each table seats 1 to {MAX_GUESTS_PER_TABLE} guests. For larger parties, please call (202) 555-4567.",
        )
    return guests


def require_timeslot(value):
    dt = parse_timeslot(value)
    if dt is None:
        raise ApiError(400, "invalid_slot", "Please choose a valid date and time.")
    if not is_valid_slot(dt):
        raise ApiError(
            400,
            "invalid_slot",
            "That time is not available. Choose a half-hour slot during restaurant hours: "
            "Monday–Saturday 5:00 PM–11:00 PM, Sunday 5:00 PM–9:00 PM (last seating 30 minutes before close).",
        )
    return dt

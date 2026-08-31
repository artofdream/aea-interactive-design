"""Reservation writes. Fail closed on missing DB, timeout, or a full slot (FR-6..FR-9, FR-18)."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from psycopg2.errors import UniqueViolation

from cafe_fausse.content import TABLE_COUNT
from cafe_fausse.db import DatabaseUnavailable, transaction
from cafe_fausse.slots import SlotError, parse_time_slot
from cafe_fausse.validate import InputError, validate_email


class ReservationError(Exception):
    def __init__(self, message: str, *, status: int = 400, code: str = "invalid"):
        super().__init__(message)
        self.status = status
        self.code = code


def _guest_count(raw: Any) -> int:
    try:
        guests = int(raw)
    except (TypeError, ValueError) as exc:
        raise ReservationError("Number of guests must be a whole number.") from exc
    if guests < 1 or guests > 20:
        raise ReservationError("Number of guests must be between 1 and 20.")
    return guests


def _phone(raw: Any) -> str | None:
    if raw is None:
        return None
    phone = str(raw).strip()
    if not phone:
        return None
    if len(phone) > 40:
        raise ReservationError("Phone number is too long.")
    return phone


def _name(raw: Any) -> str:
    name = ("" if raw is None else str(raw)).strip()
    if not name:
        raise ReservationError("Customer name is required.")
    if len(name) > 200:
        raise ReservationError("Customer name is too long.")
    return name


def remaining_tables(slot: datetime) -> int:
    try:
        with transaction() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COUNT(*) AS n FROM reservations WHERE time_slot = %s",
                    (slot,),
                )
                taken = int(cur.fetchone()["n"])
    except DatabaseUnavailable:
        raise
    except Exception as exc:
        raise DatabaseUnavailable(
            "Cannot read table availability. The request was not saved."
        ) from exc
    remaining = TABLE_COUNT - taken
    return remaining if remaining > 0 else 0


def _upsert_customer(cur, *, name: str, email: str, phone: str | None) -> int:
    cur.execute(
        """
        INSERT INTO customers (customer_name, email_address, phone_number, newsletter_signup)
        VALUES (%s, %s, %s, FALSE)
        ON CONFLICT (email_address) DO UPDATE
            SET customer_name = EXCLUDED.customer_name,
                phone_number = COALESCE(EXCLUDED.phone_number, customers.phone_number),
                updated_at = NOW()
        RETURNING customer_id
        """,
        (name, email, phone),
    )
    row = cur.fetchone()
    if not row:
        raise DatabaseUnavailable("Could not save customer. The request was not saved.")
    return int(row["customer_id"])


def create_reservation(payload: dict[str, Any]) -> dict[str, Any]:
    """Insert customer + reservation, or return an honest error. Never fake success."""
    try:
        slot = parse_time_slot(str(payload.get("time_slot") or ""))
    except SlotError as exc:
        raise ReservationError(str(exc), code="invalid_slot") from exc
    name = _name(payload.get("customer_name") or payload.get("name"))
    try:
        email = validate_email(str(payload.get("email") or payload.get("email_address") or ""))
    except InputError as exc:
        raise ReservationError(str(exc)) from exc
    guests = _guest_count(payload.get("guest_count") or payload.get("guests"))
    phone = _phone(payload.get("phone") or payload.get("phone_number"))

    try:
        with transaction() as conn:
            with conn.cursor() as cur:
                customer_id = _upsert_customer(cur, name=name, email=email, phone=phone)
                # Lock existing rows for this slot, then pick a free table at random (FR-8).
                cur.execute(
                    """
                    SELECT table_number
                    FROM reservations
                    WHERE time_slot = %s
                    FOR UPDATE
                    """,
                    (slot,),
                )
                taken = {int(row["table_number"]) for row in cur.fetchall()}
                if len(taken) >= TABLE_COUNT:
                    raise ReservationError(
                        "This time slot is fully booked. No table was assigned.",
                        status=409,
                        code="fully_booked",
                    )
                cur.execute(
                    """
                    INSERT INTO reservations (customer_id, time_slot, table_number, guest_count)
                    SELECT %s, %s, num, %s
                    FROM generate_series(1, %s) AS num
                    WHERE num NOT IN (
                        SELECT table_number FROM reservations WHERE time_slot = %s
                    )
                    ORDER BY random()
                    LIMIT 1
                    RETURNING reservation_id, table_number
                    """,
                    (customer_id, slot, guests, TABLE_COUNT, slot),
                )
                booked = cur.fetchone()
                if not booked:
                    raise ReservationError(
                        "This time slot is fully booked. No table was assigned.",
                        status=409,
                        code="fully_booked",
                    )
                return {
                    "reservation_id": int(booked["reservation_id"]),
                    "customer_id": customer_id,
                    "time_slot": slot.isoformat(),
                    "table_number": int(booked["table_number"]),
                    "guest_count": guests,
                    "message": (
                        f"Reservation confirmed. Table {int(booked['table_number'])} "
                        f"for {guests} on {slot.strftime('%A, %B %d, %Y at %I:%M %p %Z')}."
                    ),
                }
    except ReservationError:
        raise
    except UniqueViolation as exc:
        remaining = remaining_tables(slot)
        if remaining <= 0:
            raise ReservationError(
                "This time slot is fully booked. No table was assigned.",
                status=409,
                code="fully_booked",
            ) from exc
        raise ReservationError(
            "That table was just taken. Please submit the reservation again.",
            status=409,
            code="table_conflict",
        ) from exc
    except DatabaseUnavailable:
        raise
    except Exception as exc:
        raise DatabaseUnavailable(
            "PostgreSQL could not complete the reservation. The request was not saved."
        ) from exc

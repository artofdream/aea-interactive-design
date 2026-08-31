"""Newsletter signup stored on Customers (FR-15, FR-16). Fail closed if DB is down."""

from __future__ import annotations

from typing import Any

from cafe_fausse.db import DatabaseUnavailable, transaction
from cafe_fausse.reservations import ReservationError
from cafe_fausse.validate import InputError, validate_email


def subscribe(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        email = validate_email(str(payload.get("email") or payload.get("email_address") or ""))
    except InputError as exc:
        raise ReservationError(str(exc)) from exc
    name = (payload.get("customer_name") or payload.get("name") or "").strip()
    if not name:
        name = "Newsletter subscriber"

    try:
        with transaction() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO customers (customer_name, email_address, phone_number, newsletter_signup)
                    VALUES (%s, %s, NULL, TRUE)
                    ON CONFLICT (email_address) DO UPDATE
                        SET newsletter_signup = TRUE,
                            updated_at = NOW()
                    RETURNING customer_id, email_address, newsletter_signup
                    """,
                    (name, email),
                )
                row = cur.fetchone()
                if not row or not row["newsletter_signup"]:
                    raise DatabaseUnavailable(
                        "Newsletter signup could not be stored. The request was not saved."
                    )
                return {
                    "customer_id": int(row["customer_id"]),
                    "email": row["email_address"],
                    "message": "You are subscribed to the Café Fausse newsletter.",
                }
    except ReservationError:
        raise
    except DatabaseUnavailable:
        raise
    except Exception as exc:
        raise DatabaseUnavailable(
            "PostgreSQL could not store the newsletter signup. The request was not saved."
        ) from exc

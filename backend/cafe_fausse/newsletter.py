"""Newsletter signup stored on Customers (FR-15, FR-16). Fail closed if DB is down.

Optional SES confirmation after a successful store is Future #135 (not a new FR).
SES must not fail the signup.
"""

from __future__ import annotations

from typing import Any

from cafe_fausse.db import DatabaseUnavailable, transaction
from cafe_fausse.reservations import ReservationError
from cafe_fausse.ses_mail import send_newsletter_confirmation
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
                stored = {
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

    # Future #135: send only after FR-16 store commits. Fail soft.
    stored["email_delivery"] = send_newsletter_confirmation(stored["email"])
    return stored


def unsubscribe(raw_email: str) -> dict[str, Any]:
    """Minimal Future #135 compliance: flip newsletter_signup off. Fail closed if DB is down."""
    try:
        email = validate_email(raw_email)
    except InputError as exc:
        raise ReservationError(str(exc)) from exc

    try:
        with transaction() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE customers
                    SET newsletter_signup = FALSE,
                        updated_at = NOW()
                    WHERE email_address = %s
                    RETURNING customer_id, email_address, newsletter_signup
                    """,
                    (email,),
                )
                row = cur.fetchone()
    except DatabaseUnavailable:
        raise
    except Exception as exc:
        raise DatabaseUnavailable(
            "PostgreSQL could not update the newsletter preference. The request was not saved."
        ) from exc

    if not row:
        return {
            "email": email,
            "newsletter_signup": False,
            "message": "This address is not on the newsletter list.",
        }
    return {
        "email": row["email_address"],
        "newsletter_signup": bool(row["newsletter_signup"]),
        "message": "You are unsubscribed from Café Fausse demo mail.",
    }

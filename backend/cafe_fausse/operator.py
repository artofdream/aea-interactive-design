"""Read-only operator snapshot for the Quantic recording demo.

Not a new SRS requirement (not FR-19). GET only. Fail closed if PostgreSQL
is missing or unreachable — never invent an empty success.
"""

from __future__ import annotations

from typing import Any

from cafe_fausse.db import DatabaseUnavailable, transaction

RESERVATION_LIMIT = 50
NEWSLETTER_ONLY_LIMIT = 50


def _iso(value: Any) -> Any:
    if value is None:
        return None
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return value


def list_operator_snapshot() -> dict[str, Any]:
    """Recent reservations plus newsletter-only customers. Does not write."""
    try:
        with transaction() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        r.reservation_id,
                        r.time_slot,
                        r.table_number,
                        r.guest_count,
                        c.customer_name,
                        c.email_address,
                        c.newsletter_signup
                    FROM reservations r
                    JOIN customers c ON c.customer_id = r.customer_id
                    ORDER BY r.created_at DESC, r.reservation_id DESC
                    LIMIT %s
                    """,
                    (RESERVATION_LIMIT,),
                )
                reservations = [
                    {
                        "reservation_id": int(row["reservation_id"]),
                        "customer_name": row["customer_name"],
                        "email": row["email_address"],
                        "newsletter": bool(row["newsletter_signup"]),
                        "time_slot": _iso(row["time_slot"]),
                        "table_number": int(row["table_number"]),
                        "guest_count": int(row["guest_count"]),
                    }
                    for row in cur.fetchall()
                ]
                cur.execute(
                    """
                    SELECT
                        c.customer_id,
                        c.customer_name,
                        c.email_address,
                        c.newsletter_signup
                    FROM customers c
                    WHERE c.newsletter_signup = TRUE
                      AND NOT EXISTS (
                          SELECT 1 FROM reservations r
                          WHERE r.customer_id = c.customer_id
                      )
                    ORDER BY c.created_at DESC, c.customer_id DESC
                    LIMIT %s
                    """,
                    (NEWSLETTER_ONLY_LIMIT,),
                )
                newsletter_only = [
                    {
                        "customer_id": int(row["customer_id"]),
                        "customer_name": row["customer_name"],
                        "email": row["email_address"],
                        "newsletter": bool(row["newsletter_signup"]),
                    }
                    for row in cur.fetchall()
                ]
                return {
                    "reservations": reservations,
                    "newsletter_only": newsletter_only,
                }
    except DatabaseUnavailable:
        raise
    except Exception as exc:
        raise DatabaseUnavailable(
            "Cannot read the operator snapshot. PostgreSQL did not respond honestly."
        ) from exc

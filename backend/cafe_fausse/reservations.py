"""Reservation booking (FR-8, FR-9, FR-18). Fail closed on missing DB or a full book."""

import random

from psycopg.errors import UniqueViolation

from cafe_fausse.config import TABLE_COUNT
from cafe_fausse.db import connect, require_schema
from cafe_fausse.errors import ApiError, DatabaseUnavailable
from cafe_fausse.validate import optional_phone, require_email, require_guests, require_name, require_timeslot


def _booked_tables(cur, timeslot):
    cur.execute(
        "SELECT table_number FROM reservations WHERE timeslot = %s FOR UPDATE",
        (timeslot,),
    )
    return {row["table_number"] for row in cur.fetchall()}


def _insert_customer(cur, name, email, phone):
    cur.execute(
        """
        INSERT INTO customers (name, email, phone, newsletter_signup)
        VALUES (%s, %s, %s, FALSE)
        RETURNING id
        """,
        (name, email, phone),
    )
    return cur.fetchone()["id"]


def create_reservation(payload):
    """Assign a random free table from 30, or return a fully-booked error (FR-8, FR-9)."""
    if not isinstance(payload, dict):
        raise ApiError(400, "invalid_request", "Please send a reservation form.")

    timeslot = require_timeslot(payload.get("timeslot"))
    guests = require_guests(payload.get("guests"))
    name = require_name(payload.get("name"))
    email = require_email(payload.get("email"))
    phone = optional_phone(payload.get("phone"))
    # guests is required by FR-6 and validated; FR-17 does not store a guest column.
    _ = guests

    conn = connect()
    try:
        require_schema(conn)
        reservation_id = None
        table_number = None
        last_conflict = False
        for _attempt in range(3):
            last_conflict = False
            try:
                with conn.cursor() as cur:
                    taken = _booked_tables(cur, timeslot)
                    free = [n for n in range(1, TABLE_COUNT + 1) if n not in taken]
                    if not free:
                        conn.rollback()
                        raise ApiError(
                            409,
                            "fully_booked",
                            "This time slot is fully booked (all 30 tables are taken). Please choose another time.",
                        )
                    table_number = random.choice(free)
                    customer_id = _insert_customer(cur, name, email, phone)
                    cur.execute(
                        """
                        INSERT INTO reservations (customer_id, timeslot, table_number)
                        VALUES (%s, %s, %s)
                        RETURNING id
                        """,
                        (customer_id, timeslot, table_number),
                    )
                    reservation_id = cur.fetchone()["id"]
                conn.commit()
                break
            except UniqueViolation:
                last_conflict = True
                conn.rollback()
        if reservation_id is None:
            raise ApiError(
                409,
                "fully_booked",
                "This time slot is fully booked (all 30 tables are taken). Please choose another time.",
            ) if last_conflict else DatabaseUnavailable()
        return {
            "ok": True,
            "reservation_id": reservation_id,
            "table_number": table_number,
            "timeslot": timeslot.isoformat(),
            "message": f"Your table is reserved. You have table {table_number}.",
        }
    except ApiError:
        raise
    except DatabaseUnavailable:
        raise
    except Exception:
        try:
            conn.rollback()
        except Exception:
            pass
        raise DatabaseUnavailable() from None
    finally:
        conn.close()


def remaining_tables(timeslot):
    """How many of the 30 tables are still free. Fail closed if the DB is down."""
    conn = connect()
    try:
        require_schema(conn)
        with conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) AS taken FROM reservations WHERE timeslot = %s",
                (timeslot,),
            )
            taken = int(cur.fetchone()["taken"])
        return max(0, TABLE_COUNT - taken)
    except ApiError:
        raise
    except Exception:
        raise DatabaseUnavailable() from None
    finally:
        conn.close()

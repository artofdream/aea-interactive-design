"""Newsletter signup (FR-15, FR-16). Emails are stored on the customers table."""

from cafe_fausse.db import connect, require_schema
from cafe_fausse.errors import ApiError, DatabaseUnavailable
from cafe_fausse.validate import require_email


def subscribe(payload):
    if not isinstance(payload, dict):
        raise ApiError(400, "invalid_request", "Please send an email address.")
    email = require_email(payload.get("email"))

    conn = connect()
    try:
        require_schema(conn)
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM customers WHERE email = %s AND newsletter_signup = TRUE LIMIT 1",
                (email,),
            )
            existing = cur.fetchone()
            if existing:
                conn.commit()
                return {
                    "ok": True,
                    "already_subscribed": True,
                    "message": "This email is already on the newsletter list.",
                }
            cur.execute(
                """
                INSERT INTO customers (name, email, phone, newsletter_signup)
                VALUES (%s, %s, NULL, TRUE)
                """,
                ("", email),
            )
        conn.commit()
        return {
            "ok": True,
            "already_subscribed": False,
            "message": "Thank you. You are subscribed to the Café Fausse newsletter.",
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
        raise DatabaseUnavailable(
            "Newsletter signup cannot be saved because the database is unavailable."
        ) from None
    finally:
        conn.close()

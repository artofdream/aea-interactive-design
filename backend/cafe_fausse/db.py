"""PostgreSQL access. Fail closed when the database is missing or unreachable."""

from pathlib import Path

import psycopg
from psycopg.rows import dict_row

from cafe_fausse.config import database_url
from cafe_fausse.errors import DatabaseUnavailable

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema.sql"


def connect():
    """Open a connection or raise DatabaseUnavailable (honest no)."""
    url = database_url()
    if not url:
        raise DatabaseUnavailable()
    try:
        conn = psycopg.connect(url, row_factory=dict_row, connect_timeout=3)
        conn.autocommit = False
        return conn
    except Exception:
        raise DatabaseUnavailable() from None


def ping():
    """Return True if PostgreSQL answers; False otherwise. Never invents success."""
    try:
        conn = connect()
    except DatabaseUnavailable:
        return False
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            cur.fetchone()
        return True
    except Exception:
        return False
    finally:
        conn.close()


def apply_schema(conn):
    """Create FR-17 tables if they do not exist."""
    sql = SCHEMA_PATH.read_text(encoding="utf-8")
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()


def require_schema(conn):
    """Fail closed if the reservation tables are missing."""
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_name IN ('customers', 'reservations')
            """
        )
        names = {row["table_name"] for row in cur.fetchall()}
    if names != {"customers", "reservations"}:
        raise DatabaseUnavailable(
            "Reservations cannot be accepted because the database schema is not ready."
        )

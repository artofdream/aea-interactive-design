"""Apply schema.sql. Fail closed if PostgreSQL is missing."""

from __future__ import annotations

from pathlib import Path

from cafe_fausse.db import DatabaseUnavailable, connect

SCHEMA = Path(__file__).resolve().parent.parent / "schema.sql"


def init_db() -> None:
    sql = SCHEMA.read_text(encoding="utf-8")
    conn = connect()
    try:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(sql)
    except DatabaseUnavailable:
        raise
    except Exception as exc:
        raise DatabaseUnavailable(
            "Could not apply the Café Fausse schema. Database was not initialized."
        ) from exc
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print("schema applied")

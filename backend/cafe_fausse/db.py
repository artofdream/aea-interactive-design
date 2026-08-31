"""PostgreSQL access with fail-closed timeouts (FR-17, NFR-5, NFR-6)."""

from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Iterator

import psycopg2
from psycopg2.extensions import connection as PgConnection
from psycopg2.extras import RealDictCursor


class DatabaseUnavailable(Exception):
    """Honest no: nothing was written."""


def _timeouts() -> tuple[int, int]:
    connect = int(os.environ.get("DB_CONNECT_TIMEOUT", "2"))
    statement_ms = int(os.environ.get("DB_STATEMENT_TIMEOUT_MS", "2000"))
    return connect, statement_ms


def connect() -> PgConnection:
    url = (os.environ.get("DATABASE_URL") or "").strip()
    if not url:
        raise DatabaseUnavailable(
            "PostgreSQL is not configured (DATABASE_URL is missing). "
            "The request was not saved."
        )
    connect_timeout, statement_ms = _timeouts()
    try:
        conn = psycopg2.connect(
            url,
            connect_timeout=connect_timeout,
            cursor_factory=RealDictCursor,
            options=f"-c statement_timeout={statement_ms}",
        )
    except psycopg2.OperationalError as exc:
        raise DatabaseUnavailable(
            "Cannot reach PostgreSQL. The request was not saved."
        ) from exc
    conn.autocommit = False
    return conn


@contextmanager
def transaction() -> Iterator[PgConnection]:
    conn = connect()
    try:
        yield conn
        conn.commit()
    except Exception:
        try:
            conn.rollback()
        except Exception:
            pass
        raise
    finally:
        conn.close()


def ping() -> None:
    """Fail closed if the database is missing or times out. Does not write."""
    with transaction() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 AS ok")
            row = cur.fetchone()
            if not row or row["ok"] != 1:
                raise DatabaseUnavailable("PostgreSQL did not respond honestly.")

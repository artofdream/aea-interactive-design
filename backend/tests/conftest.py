"""Shared fixtures. Tests that need PostgreSQL use DATABASE_URL."""

import os
import sys
from pathlib import Path

import pytest

BACKEND_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_ROOT))

from cafe_fausse import create_app  # noqa: E402
from cafe_fausse.db import apply_schema, connect  # noqa: E402


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db_ready():
    if not os.environ.get("DATABASE_URL", "").strip():
        pytest.skip("DATABASE_URL is not set")
    conn = connect()
    try:
        apply_schema(conn)
        with conn.cursor() as cur:
            cur.execute("DELETE FROM reservations")
            cur.execute("DELETE FROM customers")
        conn.commit()
    finally:
        conn.close()
    return True

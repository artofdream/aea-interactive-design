from __future__ import annotations

import os

import pytest

from cafe_fausse import create_app
from cafe_fausse.db import connect
from cafe_fausse.init_db import init_db

FUTURE_SLOT = "2028-06-15T19:00:00-04:00"


@pytest.fixture
def require_db():
    if not (os.environ.get("DATABASE_URL") or "").strip():
        pytest.skip("DATABASE_URL is required for database tests")
    conn = connect()
    conn.autocommit = True
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS reservations CASCADE")
            cur.execute("DROP TABLE IF EXISTS customers CASCADE")
    finally:
        conn.close()
    init_db()


@pytest.fixture
def client(require_db):
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


@pytest.fixture
def no_db_client(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

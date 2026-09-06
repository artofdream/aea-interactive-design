"""Fail closed: missing DB, unreachable DB, full slot. No fake success."""

from __future__ import annotations

from cafe_fausse import create_app
from cafe_fausse.db import connect

FUTURE_SLOT = "2028-06-15T19:00:00-04:00"


def _count(sql: str) -> int:
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            return int(cur.fetchone()["n"])
    finally:
        conn.close()


def test_reservation_without_database_is_honest_no(no_db_client):
    response = no_db_client.post(
        "/api/reservations",
        json={
            "time_slot": FUTURE_SLOT,
            "guest_count": 2,
            "customer_name": "Ada Guest",
            "email": "ada@example.com",
        },
    )
    body = response.get_json()
    assert response.status_code == 503
    assert body["ok"] is False
    assert "not saved" in body["error"].lower() or "not configured" in body["error"].lower()


def test_newsletter_without_database_is_honest_no(no_db_client):
    response = no_db_client.post("/api/newsletter", json={"email": "news@example.com"})
    body = response.get_json()
    assert response.status_code == 503
    assert body["ok"] is False
    assert "not saved" in body["error"].lower() or "not configured" in body["error"].lower()


def test_unsubscribe_without_database_is_honest_no(no_db_client):
    response = no_db_client.get(
        "/api/newsletter/unsubscribe",
        query_string={"email": "news@example.com"},
    )
    body = response.get_json()
    assert response.status_code == 503
    assert body["ok"] is False


def test_unreachable_postgres_is_honest_no(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://cafe:cafe@127.0.0.1:1/cafe_fausse")
    monkeypatch.setenv("DB_CONNECT_TIMEOUT", "1")
    app = create_app()
    client = app.test_client()
    response = client.post(
        "/api/reservations",
        json={
            "time_slot": FUTURE_SLOT,
            "guest_count": 2,
            "customer_name": "Ada Guest",
            "email": "ada@example.com",
        },
    )
    body = response.get_json()
    assert response.status_code == 503
    assert body["ok"] is False
    assert body.get("ok") is not True


def test_connect_timeout_is_honest_no(monkeypatch):
    # TEST-NET-1 is not routed; connect_timeout must fail closed, not succeed.
    monkeypatch.setenv("DATABASE_URL", "postgresql://cafe:cafe@192.0.2.1:5432/cafe_fausse")
    monkeypatch.setenv("DB_CONNECT_TIMEOUT", "1")
    app = create_app()
    client = app.test_client()
    response = client.post("/api/newsletter", json={"email": "slow@example.com"})
    body = response.get_json()
    assert response.status_code == 503
    assert body["ok"] is False


def test_full_slot_does_not_assign_a_31st_table(client, require_db):
    tables = set()
    for i in range(30):
        response = client.post(
            "/api/reservations",
            json={
                "time_slot": FUTURE_SLOT,
                "guest_count": 2,
                "customer_name": f"Guest {i}",
                "email": f"guest{i}@example.com",
            },
        )
        body = response.get_json()
        assert response.status_code == 201, body
        assert body["ok"] is True
        tables.add(body["table_number"])
    assert tables == set(range(1, 31))
    assert _count("SELECT COUNT(*) AS n FROM reservations") == 30

    response = client.post(
        "/api/reservations",
        json={
            "time_slot": FUTURE_SLOT,
            "guest_count": 2,
            "customer_name": "Late Guest",
            "email": "late@example.com",
        },
    )
    body = response.get_json()
    assert response.status_code == 409
    assert body["ok"] is False
    assert body["code"] == "fully_booked"
    assert "fully booked" in body["error"].lower()
    assert _count("SELECT COUNT(*) AS n FROM reservations") == 30
    assert _count("SELECT COUNT(*) AS n FROM customers WHERE email_address = 'late@example.com'") == 0


def test_invalid_email_is_not_stored(client, require_db):
    response = client.post("/api/newsletter", json={"email": "not-an-email"})
    body = response.get_json()
    assert response.status_code == 400
    assert body["ok"] is False
    assert _count("SELECT COUNT(*) AS n FROM customers") == 0


def test_health_without_database(no_db_client):
    response = no_db_client.get("/api/health")
    assert response.status_code == 503
    assert response.get_json()["ok"] is False

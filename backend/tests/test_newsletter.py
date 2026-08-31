from __future__ import annotations

from cafe_fausse.db import connect


def test_newsletter_stores_email(client, require_db):
    response = client.post("/api/newsletter", json={"email": "diner@example.com"})
    body = response.get_json()
    assert response.status_code == 201, body
    assert body["ok"] is True
    assert body["email"] == "diner@example.com"

    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT newsletter_signup FROM customers WHERE email_address = %s",
                ("diner@example.com",),
            )
            row = cur.fetchone()
            assert row["newsletter_signup"] is True
    finally:
        conn.close()


def test_newsletter_is_idempotent(client, require_db):
    first = client.post("/api/newsletter", json={"email": "repeat@example.com"})
    second = client.post("/api/newsletter", json={"email": "repeat@example.com"})
    assert first.status_code == 201
    assert second.status_code == 201
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) AS n FROM customers")
            assert int(cur.fetchone()["n"]) == 1
    finally:
        conn.close()

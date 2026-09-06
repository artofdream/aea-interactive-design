from __future__ import annotations

from cafe_fausse.db import connect


def test_newsletter_stores_email(client, require_db):
    response = client.post("/api/newsletter", json={"email": "diner@example.com"})
    body = response.get_json()
    assert response.status_code == 201, body
    assert body["ok"] is True
    assert body["email"] == "diner@example.com"
    assert body["email_delivery"]["status"] == "skipped"
    assert body["email_delivery"]["reason"] == "email not configured"

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


def test_newsletter_without_ses_stays_store_only(client, require_db, monkeypatch):
    monkeypatch.delenv("SES_FROM_EMAIL", raising=False)
    monkeypatch.delenv("SES_REGION", raising=False)
    monkeypatch.delenv("AWS_DEFAULT_REGION", raising=False)
    response = client.post("/api/newsletter", json={"email": "store-only@example.com"})
    body = response.get_json()
    assert response.status_code == 201, body
    assert body["ok"] is True
    assert body["email_delivery"] == {
        "attempted": False,
        "status": "skipped",
        "reason": "email not configured",
    }


def test_newsletter_with_mocked_ses_still_stores(client, require_db, monkeypatch):
    monkeypatch.setenv("SES_REGION", "us-east-1")
    monkeypatch.setenv("SES_FROM_EMAIL", "newsletter@cafe.artof.link")

    def fake_send(to_email: str):
        assert to_email == "ses-ok@example.com"
        return {"attempted": True, "status": "sent", "provider": "ses-v2"}

    monkeypatch.setattr("cafe_fausse.newsletter.send_newsletter_confirmation", fake_send)
    response = client.post("/api/newsletter", json={"email": "ses-ok@example.com"})
    body = response.get_json()
    assert response.status_code == 201, body
    assert body["ok"] is True
    assert body["email_delivery"]["status"] == "sent"
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT newsletter_signup FROM customers WHERE email_address = %s",
                ("ses-ok@example.com",),
            )
            assert cur.fetchone()["newsletter_signup"] is True
    finally:
        conn.close()


def test_newsletter_ses_failure_does_not_fail_signup(client, require_db, monkeypatch):
    monkeypatch.setenv("SES_REGION", "us-east-1")
    monkeypatch.setenv("SES_FROM_EMAIL", "newsletter@cafe.artof.link")

    def boom(_to_email: str):
        return {
            "attempted": True,
            "status": "failed",
            "reason": "SES send failed; signup was stored.",
        }

    monkeypatch.setattr("cafe_fausse.newsletter.send_newsletter_confirmation", boom)
    response = client.post("/api/newsletter", json={"email": "ses-fail@example.com"})
    body = response.get_json()
    assert response.status_code == 201, body
    assert body["ok"] is True
    assert body["email_delivery"]["status"] == "failed"
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT newsletter_signup FROM customers WHERE email_address = %s",
                ("ses-fail@example.com",),
            )
            assert cur.fetchone()["newsletter_signup"] is True
    finally:
        conn.close()


def test_unsubscribe_clears_newsletter_flag(client, require_db):
    signup = client.post("/api/newsletter", json={"email": "leave@example.com"})
    assert signup.status_code == 201
    response = client.get("/api/newsletter/unsubscribe", query_string={"email": "leave@example.com"})
    body = response.get_json()
    assert response.status_code == 200, body
    assert body["ok"] is True
    assert body["newsletter_signup"] is False
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT newsletter_signup FROM customers WHERE email_address = %s",
                ("leave@example.com",),
            )
            assert cur.fetchone()["newsletter_signup"] is False
    finally:
        conn.close()


def test_unsubscribe_page_is_html(client, require_db):
    client.post("/api/newsletter", json={"email": "html-unsub@example.com"})
    response = client.get("/unsubscribe", query_string={"email": "html-unsub@example.com"})
    assert response.status_code == 200
    assert response.mimetype == "text/html"
    assert b"unsubscribed" in response.data.lower()
    assert b"Future #135" in response.data

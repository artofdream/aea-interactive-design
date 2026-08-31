"""FR-15 / FR-16: validate email and store newsletter signups."""


def test_newsletter_rejects_invalid_email(client):
    res = client.post("/api/newsletter", json={"email": "not-an-email"})
    assert res.status_code == 400
    assert res.get_json()["error"] == "invalid_email"


def test_newsletter_rejects_empty_payload(client):
    res = client.post("/api/newsletter", json={})
    assert res.status_code == 400
    assert res.get_json()["error"] == "invalid_email"


def test_newsletter_stores_email(client, db_ready):
    res = client.post("/api/newsletter", json={"email": "diner@example.com"})
    assert res.status_code == 201
    body = res.get_json()
    assert body["ok"] is True
    assert body["already_subscribed"] is False

    again = client.post("/api/newsletter", json={"email": "DINER@example.com"})
    assert again.status_code == 200
    assert again.get_json()["already_subscribed"] is True

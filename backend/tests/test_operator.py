"""Read-only operator snapshot. Fail closed; no writes; not FR-19."""

from __future__ import annotations

FUTURE_SLOT = "2028-06-15T19:00:00-04:00"


def test_operator_without_database_is_honest_no(no_db_client):
    response = no_db_client.get("/api/operator")
    body = response.get_json()
    assert response.status_code == 503
    assert body["ok"] is False
    assert body.get("reservations") is None


def test_operator_includes_created_reservation(client, require_db):
    created = client.post(
        "/api/reservations",
        json={
            "time_slot": FUTURE_SLOT,
            "guest_count": 3,
            "customer_name": "Operator Guest",
            "email": "operator-guest@example.com",
        },
    )
    booked = created.get_json()
    assert created.status_code == 201, booked

    response = client.get("/api/operator")
    body = response.get_json()
    assert response.status_code == 200
    assert body["ok"] is True
    match = next(
        row
        for row in body["reservations"]
        if row["email"] == "operator-guest@example.com"
    )
    assert match["customer_name"] == "Operator Guest"
    assert match["table_number"] == booked["table_number"]
    assert 1 <= match["table_number"] <= 30
    assert match["guest_count"] == 3
    assert match["reservation_id"] == booked["reservation_id"]
    assert "2028-06-15" in match["time_slot"]
    assert match["newsletter"] is False


def test_operator_includes_newsletter_only_customers(client, require_db):
    signup = client.post("/api/newsletter", json={"email": "news-only@example.com"})
    assert signup.status_code == 201, signup.get_json()

    response = client.get("/api/operator")
    body = response.get_json()
    assert response.status_code == 200
    assert body["ok"] is True
    match = next(
        row
        for row in body["newsletter_only"]
        if row["email"] == "news-only@example.com"
    )
    assert match["newsletter"] is True
    assert match["customer_name"]


def test_operator_rejects_writes(client, require_db):
    post = client.post("/api/operator", json={"customer_name": "No Write"})
    assert post.status_code in (405, 404)
    patch = client.patch("/api/operator", json={"cancel": True})
    assert patch.status_code in (405, 404)
    delete = client.delete("/api/operator")
    assert delete.status_code in (405, 404)

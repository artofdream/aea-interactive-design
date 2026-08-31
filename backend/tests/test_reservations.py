from __future__ import annotations

from cafe_fausse.db import connect
from cafe_fausse.slots import parse_time_slot

FUTURE_SLOT = "2028-06-15T19:00:00-04:00"


def test_reservation_assigns_a_table_from_thirty(client, require_db):
    response = client.post(
        "/api/reservations",
        json={
            "time_slot": FUTURE_SLOT,
            "guests": 4,
            "name": "Jordan Patron",
            "email": "jordan@example.com",
            "phone": "(202) 555-0100",
        },
    )
    body = response.get_json()
    assert response.status_code == 201, body
    assert body["ok"] is True
    assert 1 <= body["table_number"] <= 30
    assert "confirmed" in body["message"].lower()

    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) AS n FROM reservations")
            assert int(cur.fetchone()["n"]) == 1
            cur.execute("SELECT customer_name, email_address, phone_number FROM customers")
            row = cur.fetchone()
            assert row["customer_name"] == "Jordan Patron"
            assert row["email_address"] == "jordan@example.com"
            assert row["phone_number"] == "(202) 555-0100"
    finally:
        conn.close()


def test_invalid_slot_rejected(client, require_db):
    response = client.post(
        "/api/reservations",
        json={
            "time_slot": "2028-06-15T13:00:00-04:00",
            "guest_count": 2,
            "customer_name": "Noon Guest",
            "email": "noon@example.com",
        },
    )
    body = response.get_json()
    assert response.status_code == 400
    assert body["ok"] is False
    assert body["code"] == "invalid_slot"


def test_sunday_last_seating_is_8pm_not_10pm():
    parse_time_slot("2028-06-18T20:00:00-04:00")
    try:
        parse_time_slot("2028-06-18T22:00:00-04:00")
        raise AssertionError("Sunday 10pm must be invalid")
    except ValueError:
        pass


def test_availability_zero_when_full(client, require_db):
    slot = parse_time_slot(FUTURE_SLOT)
    for i in range(30):
        client.post(
            "/api/reservations",
            json={
                "time_slot": FUTURE_SLOT,
                "guest_count": 1,
                "customer_name": f"G{i}",
                "email": f"g{i}@example.com",
            },
        )
    response = client.get("/api/availability", query_string={"time_slot": slot.isoformat()})
    body = response.get_json()
    assert body["ok"] is True
    assert body["remaining"] == 0
    assert body["fully_booked"] is True


def test_slots_require_date(client, require_db):
    response = client.get("/api/slots")
    assert response.status_code == 400
    assert response.get_json()["ok"] is False

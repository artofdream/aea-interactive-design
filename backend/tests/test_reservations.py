"""FR-6..FR-9 and FR-18: book a random free table, or fail closed when full."""

from datetime import datetime, timedelta

from cafe_fausse.config import TABLE_COUNT
from cafe_fausse.db import connect
from cafe_fausse.slots import TZ


def _future_slot():
    day = datetime.now(TZ) + timedelta(days=14)
    while day.weekday() != 5:
        day += timedelta(days=1)
    return day.replace(hour=19, minute=0, second=0, microsecond=0)


def _payload(**overrides):
    body = {
        "timeslot": _future_slot().isoformat(),
        "guests": 2,
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "phone": "(202) 555-0100",
    }
    body.update(overrides)
    return body


def test_missing_name(client):
    res = client.post("/api/reservations", json=_payload(name=""))
    assert res.status_code == 400
    assert res.get_json()["error"] == "invalid_name"


def test_invalid_guests(client):
    res = client.post("/api/reservations", json=_payload(guests=0))
    assert res.status_code == 400
    assert res.get_json()["error"] == "invalid_guests"


def test_phone_is_optional(client, db_ready):
    res = client.post("/api/reservations", json=_payload(phone=""))
    assert res.status_code == 201
    body = res.get_json()
    assert body["ok"] is True
    assert 1 <= body["table_number"] <= TABLE_COUNT


def test_books_random_free_table(client, db_ready):
    first = client.post("/api/reservations", json=_payload(email="one@example.com"))
    second = client.post("/api/reservations", json=_payload(email="two@example.com"))
    assert first.status_code == 201
    assert second.status_code == 201
    t1 = first.get_json()["table_number"]
    t2 = second.get_json()["table_number"]
    assert t1 != t2
    assert 1 <= t1 <= TABLE_COUNT
    assert 1 <= t2 <= TABLE_COUNT


def test_fully_booked_returns_error(client, db_ready):
    slot = _future_slot()
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO customers (name, email, phone, newsletter_signup) VALUES (%s, %s, NULL, FALSE) RETURNING id",
                ("Fill", "fill@example.com"),
            )
            customer_id = cur.fetchone()["id"]
            for table in range(1, TABLE_COUNT + 1):
                cur.execute(
                    "INSERT INTO reservations (customer_id, timeslot, table_number) VALUES (%s, %s, %s)",
                    (customer_id, slot, table),
                )
        conn.commit()
    finally:
        conn.close()

    res = client.post("/api/reservations", json=_payload(timeslot=slot.isoformat()))
    assert res.status_code == 409
    body = res.get_json()
    assert body["ok"] is False
    assert body["error"] == "fully_booked"


def test_slots_report_remaining(client, db_ready):
    slot = _future_slot()
    booked = client.post("/api/reservations", json=_payload(timeslot=slot.isoformat()))
    assert booked.status_code == 201
    res = client.get(f"/api/slots?date={slot.date().isoformat()}")
    assert res.status_code == 200
    match = [s for s in res.get_json()["slots"] if s["timeslot"].startswith(slot.isoformat()[:16])]
    assert match
    assert match[0]["tables_remaining"] == TABLE_COUNT - 1

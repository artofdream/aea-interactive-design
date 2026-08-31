"""Fail closed: missing or unreachable DB must not accept a booking (FR-9 / NFR-5)."""

from datetime import datetime, timedelta

from cafe_fausse.slots import TZ


def _future_slot():
    day = datetime.now(TZ) + timedelta(days=14)
    # Walk forward to a Saturday 19:00.
    while day.weekday() != 5:
        day += timedelta(days=1)
    return day.replace(hour=19, minute=0, second=0, microsecond=0).isoformat()


def test_reservation_without_database_url(monkeypatch, app):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    res = app.test_client().post(
        "/api/reservations",
        json={
            "timeslot": _future_slot(),
            "guests": 2,
            "name": "Test Guest",
            "email": "guest@example.com",
        },
    )
    assert res.status_code == 503
    body = res.get_json()
    assert body["ok"] is False
    assert body["error"] == "database_unavailable"


def test_newsletter_without_database_url(monkeypatch, app):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    res = app.test_client().post("/api/newsletter", json={"email": "guest@example.com"})
    assert res.status_code == 503
    body = res.get_json()
    assert body["ok"] is False
    assert body["error"] == "database_unavailable"


def test_health_without_database_url(monkeypatch, app):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    res = app.test_client().get("/api/health")
    assert res.status_code == 503
    assert res.get_json()["database"] == "down"


def test_reservation_unreachable_database(monkeypatch, app):
    monkeypatch.setenv("DATABASE_URL", "postgresql://cafe:cafe@127.0.0.1:1/does_not_exist")
    res = app.test_client().post(
        "/api/reservations",
        json={
            "timeslot": _future_slot(),
            "guests": 2,
            "name": "Test Guest",
            "email": "guest@example.com",
        },
    )
    assert res.status_code == 503
    assert res.get_json()["ok"] is False

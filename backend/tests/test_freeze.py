from __future__ import annotations

from pathlib import Path

from cafe_fausse import create_app
from cafe_fausse.content import freeze

REPO = Path(__file__).resolve().parents[2]
SRS = (REPO / "docs" / "srs.md").read_text(encoding="utf-8")
FRONTEND = REPO / "frontend"


def test_freeze_prices_match_srs():
    expected = [
        ("Bruschetta", "8.50"),
        ("Caesar Salad", "9.00"),
        ("Grilled Salmon", "22.00"),
        ("Ribeye Steak", "28.00"),
        ("Vegetable Risotto", "18.00"),
        ("Tiramisu", "7.50"),
        ("Cheesecake", "7.00"),
        ("Red Wine (Glass)", "10.00"),
        ("White Wine (Glass)", "9.00"),
        ("Craft Beer", "6.00"),
        ("Espresso", "3.00"),
    ]
    found = {
        item["name"]: item["price"]
        for category in freeze["menu"]
        for item in category["items"]
    }
    assert found == dict(expected)
    for name, price in expected:
        assert name in SRS
        assert f"${price}" in SRS


def test_contact_hours_and_awards_match_srs():
    assert freeze["address"] in SRS
    assert freeze["phone"] in SRS
    assert freeze["hoursDisplay"] in SRS
    assert freeze["history"] in SRS
    for award in freeze["awards"]:
        assert award in SRS
    for review in freeze["reviews"]:
        assert review["quote"] in SRS
        assert review["attribution"] in SRS


def test_menu_endpoint(client, require_db):
    response = client.get("/api/menu")
    body = response.get_json()
    assert body["ok"] is True
    assert [c["category"] for c in body["menu"]] == [
        "Starters",
        "Main Courses",
        "Desserts",
        "Beverages",
    ]


def test_official_image_served_and_supplemental_is_not():
    client = create_app().test_client()
    ok = client.get("/images/home-cafe-fausse.webp")
    assert ok.status_code == 200
    assert ok.data[:4] == b"RIFF" or ok.mimetype in {"image/webp", "application/octet-stream"}
    blocked = client.get("/images/bar-interior.jpg")
    assert blocked.status_code == 404


def test_frontend_does_not_reference_supplemental_files():
    needles = [
        "supplemental-not-official",
        "bar-interior.jpg",
        "caesar-salad.png",
        "caprese-salad.jpg",
        "cheesecake.png",
        "chef-hands.jpg",
        "cocktail-bar.jpg",
        "craft-beer.png",
        "dessert-closeup.jpg",
        "elegant-desserts.jpg",
        "elegant-table.jpg",
        "espresso-coffee.jpg",
        "red-wine.png",
        "salmon-dish.jpg",
        "tiramisu.jpg",
        "vegetable-risotto.png",
        "white-wine.png",
        "wine-cellar.jpg",
    ]
    blob = []
    for path in FRONTEND.rglob("*"):
        if path.suffix.lower() in {".js", ".jsx", ".css", ".html", ".json", ".md"}:
            blob.append(path.read_text(encoding="utf-8"))
    text = "\n".join(blob)
    for needle in needles:
        assert needle not in text, needle

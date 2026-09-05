from __future__ import annotations

from pathlib import Path

from cafe_fausse import create_app
from cafe_fausse.content import (
    OFFICIAL_IMAGE_FILES,
    SUPPLEMENTAL_MENU_IMAGE_FILES,
    freeze,
    menu_presentation,
)

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


def test_menu_presentation_maps_freeze_names_without_prices():
    freeze_names = {
        item["name"] for category in freeze["menu"] for item in category["items"]
    }
    assert set(menu_presentation["items"]) == freeze_names
    for visual in menu_presentation["items"].values():
        assert "price" not in visual
        assert visual["kind"] in {"official", "student-recovered", "placeholder"}
    assert menu_presentation["items"]["Ribeye Steak"]["kind"] == "official"
    assert menu_presentation["items"]["Ribeye Steak"]["file"] == "gallery-ribeye-steak.webp"
    assert menu_presentation["items"]["Bruschetta"]["kind"] == "placeholder"
    assert menu_presentation["items"]["Bruschetta"]["file"] is None


def test_official_and_allowlisted_menu_images_served_unused_supplemental_blocked():
    client = create_app().test_client()
    ok = client.get("/images/home-cafe-fausse.webp")
    assert ok.status_code == 200
    assert ok.data[:4] == b"RIFF" or ok.mimetype in {"image/webp", "application/octet-stream"}
    salmon = client.get("/images/salmon-dish.jpg")
    assert salmon.status_code == 200
    assert salmon.data[:3] == b"\xff\xd8\xff" or salmon.mimetype.startswith("image/")
    blocked = client.get("/images/bar-interior.jpg")
    assert blocked.status_code == 404
    nested = client.get("/images/supplemental-not-official/salmon-dish.jpg")
    assert nested.status_code == 404
    assert "bar-interior.jpg" not in SUPPLEMENTAL_MENU_IMAGE_FILES
    assert SUPPLEMENTAL_MENU_IMAGE_FILES.isdisjoint(OFFICIAL_IMAGE_FILES)


def test_frontend_does_not_reference_unmapped_supplemental_files():
    unused = [
        "bar-interior.jpg",
        "caprese-salad.jpg",
        "chef-hands.jpg",
        "cocktail-bar.jpg",
        "dessert-closeup.jpg",
        "elegant-desserts.jpg",
        "elegant-table.jpg",
        "wine-cellar.jpg",
    ]
    blob = []
    skip_parts = {"dist", "node_modules"}
    for path in FRONTEND.rglob("*"):
        if any(part in skip_parts for part in path.parts):
            continue
        if path.suffix.lower() in {".js", ".jsx", ".css", ".html", ".json", ".md"}:
            blob.append(path.read_text(encoding="utf-8"))
    text = "\n".join(blob)
    assert "supplemental-not-official" not in text
    for needle in unused:
        assert needle not in text, needle

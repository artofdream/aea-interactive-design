#!/usr/bin/env python3
"""Fail closed if MVP freeze facts drift. Cite FR-1..FR-18 only; do not invent IDs."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

MUST_APPEAR = {
    "frontend/src/data/restaurant.js": [
        "Café Fausse",
        "1234 Culinary Ave",
        "Suite 100",
        "Washington, DC",
        "20002",
        "(202) 555-4567",
        "Chef Antonio Rossi",
        "Maria Lopez",
        "2010",
        "Culinary Excellence Award",
        "Restaurant of the Year",
        "Best Fine Dining Experience",
        "Gourmet Review",
        "The Daily Bite",
    ],
    "frontend/src/data/menu.js": [
        "Bruschetta",
        "8.5",
        "Caesar Salad",
        "9.0",
        "Grilled Salmon",
        "22.0",
        "Ribeye Steak",
        "28.0",
        "Vegetable Risotto",
        "18.0",
        "Tiramisu",
        "7.5",
        "Cheesecake",
        "7.0",
        "Red Wine (Glass)",
        "10.0",
        "White Wine (Glass)",
        "9.0",
        "Craft Beer",
        "6.0",
        "Espresso",
        "3.0",
    ],
}

INVENTED_ID = re.compile(r"\b(?:FR-19|NFR-10)\b")


def main():
    errors = []
    for rel, needles in MUST_APPEAR.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"{rel} is missing freeze fact: {needle}")

    for path in [
        ROOT / "frontend" / "src",
        ROOT / "backend" / "cafe_fausse",
    ]:
        for file in path.rglob("*"):
            if file.suffix not in {".js", ".jsx", ".py", ".css"}:
                continue
            text = file.read_text(encoding="utf-8")
            if INVENTED_ID.search(text):
                errors.append(f"{file.relative_to(ROOT)} invents a requirement ID")

    if errors:
        print("SRS freeze fact check failed:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("SRS freeze facts present. No invented FR-19 / NFR-10 in app code.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

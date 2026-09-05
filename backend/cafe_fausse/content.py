"""Load the SRS freeze JSON. Do not invent menu items or prices (FR-5)."""

from __future__ import annotations

import json
from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
BACKEND_DIR = PACKAGE_DIR.parent
REPO_ROOT = BACKEND_DIR.parent
FREEZE_PATH = REPO_ROOT / "shared" / "freeze.json"
MENU_PRESENTATION_PATH = REPO_ROOT / "shared" / "menu-presentation.json"

freeze: dict = json.loads(FREEZE_PATH.read_text(encoding="utf-8"))
menu_presentation: dict = json.loads(MENU_PRESENTATION_PATH.read_text(encoding="utf-8"))

OFFICIAL_IMAGE_FILES = {img["file"] for img in freeze["officialImages"]}
SUPPLEMENTAL_MENU_IMAGE_FILES = {
    item["file"]
    for item in menu_presentation["items"].values()
        if item.get("kind") == "student-recovered" and item.get("file")
}
SERVED_IMAGE_FILES = OFFICIAL_IMAGE_FILES | SUPPLEMENTAL_MENU_IMAGE_FILES
TABLE_COUNT = int(freeze["tableCount"])
TIMEZONE_NAME = str(freeze["timezone"])

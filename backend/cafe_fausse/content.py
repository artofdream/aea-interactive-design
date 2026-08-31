"""Load the SRS freeze JSON. Do not invent menu items or prices (FR-5)."""

from __future__ import annotations

import json
from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
BACKEND_DIR = PACKAGE_DIR.parent
REPO_ROOT = BACKEND_DIR.parent
FREEZE_PATH = REPO_ROOT / "shared" / "freeze.json"

freeze: dict = json.loads(FREEZE_PATH.read_text(encoding="utf-8"))

OFFICIAL_IMAGE_FILES = {img["file"] for img in freeze["officialImages"]}
TABLE_COUNT = int(freeze["tableCount"])
TIMEZONE_NAME = str(freeze["timezone"])

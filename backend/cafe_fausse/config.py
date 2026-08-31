"""Runtime configuration. Missing DATABASE_URL is fail-closed (not a guessed yes)."""

import os

TABLE_COUNT = 30
RESTAURANT_TZ = "America/New_York"
MAX_GUESTS_PER_TABLE = 8


def database_url():
    """Return DATABASE_URL or None. Callers must fail closed when this is empty."""
    url = os.environ.get("DATABASE_URL", "").strip()
    return url or None

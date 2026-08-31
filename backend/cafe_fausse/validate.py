"""Shared input checks (FR-6, FR-15)."""

from __future__ import annotations

import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class InputError(Exception):
    def __init__(self, message: str, *, status: int = 400, code: str = "invalid"):
        super().__init__(message)
        self.status = status
        self.code = code


def validate_email(value: str) -> str:
    email = (value or "").strip().lower()
    if not email or not EMAIL_RE.match(email) or email.count("@") != 1:
        raise InputError("Please enter a valid email address.")
    if len(email) > 254:
        raise InputError("Please enter a valid email address.")
    return email

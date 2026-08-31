"""Typed API errors. Messages are user-facing (NFR-6)."""


class ApiError(Exception):
    def __init__(self, status, code, message):
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message


class DatabaseUnavailable(ApiError):
    def __init__(self, message="Reservations cannot be accepted because the database is unavailable."):
        super().__init__(503, "database_unavailable", message)

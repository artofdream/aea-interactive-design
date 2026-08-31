"""CLI: python -m cafe_fausse init-db"""

import sys

from cafe_fausse.db import apply_schema, connect
from cafe_fausse.errors import DatabaseUnavailable


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv == ["init-db"]:
        try:
            conn = connect()
        except DatabaseUnavailable as exc:
            print(exc.message, file=sys.stderr)
            return 1
        try:
            apply_schema(conn)
        finally:
            conn.close()
        print("Schema ready (FR-17 customers + reservations).")
        return 0
    print("Usage: python -m cafe_fausse init-db", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

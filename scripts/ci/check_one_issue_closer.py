#!/usr/bin/env python3
"""Fail closed if a pull-request body closes more than one GitHub issue.

One issue → one branch → one PR. A multi-item issue must be split first.
Keep this sensor; do not delete it to go green.
"""

from __future__ import annotations

import os
import re
import sys

CLOSER = re.compile(
    r"(?i)\b(?:closes?|fixes?|resolves?)\b"
)
ISSUE = re.compile(r"#(\d+)")


def closers_from_body(body: str) -> list[int]:
    found: list[int] = []
    for line in body.splitlines():
        if not CLOSER.search(line):
            continue
        for match in ISSUE.finditer(line):
            number = int(match.group(1))
            if number not in found:
                found.append(number)
    return found


def self_test() -> None:
    assert closers_from_body("Closes #12") == [12]
    assert closers_from_body("Closes #87. Closes #88.") == [87, 88]
    assert closers_from_body("See #89 and #108") == []
    assert closers_from_body("Fixes #1, #2") == [1, 2]


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        print("self-test OK")
        return 0
    body = os.environ.get("PR_BODY", "")
    numbers = closers_from_body(body)
    if len(numbers) > 1:
        print(
            "PR body closes more than one issue: "
            + ", ".join(f"#{n}" for n in numbers)
            + ". Split the items: one issue → one branch → one PR."
        )
        return 1
    print(f"closers={numbers or 'none'}; one-or-zero OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

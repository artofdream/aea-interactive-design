#!/usr/bin/env python3
"""Fail closed if a pull-request body closes more than one GitHub issue.

One issue → one branch → one PR. A multi-item issue must be split first.
Keep this sensor; do not delete it to go green.

Match GitHub-style closers: a keyword immediately followed by an issue
reference (#N or a github.com/.../issues/N URL). Do not treat every #N
on a line that merely contains the word "close".
"""

from __future__ import annotations

import os
import re
import sys

# Official GitHub closing keywords + the issue ref that follows them.
# close[sd]? = close / closes / closed; fix(?:es|ed)? = fix / fixes / fixed.
KEYWORD_REFS = re.compile(
    r"(?i)\b(?:close[sd]?|fix(?:es|ed)?|resolve[sd]?)\s+"
    r"(?P<refs>(?:#|https://github\.com/[^/\s]+/[^/\s]+/issues/)\d+"
    r"(?:\s*(?:,|and)\s*(?:#|https://github\.com/[^/\s]+/[^/\s]+/issues/)\d+)*)"
)
ISSUE_NUM = re.compile(r"(?:#|issues/)(\d+)")


def closers_from_body(body: str) -> list[int]:
    found: list[int] = []
    for match in KEYWORD_REFS.finditer(body):
        for num in ISSUE_NUM.finditer(match.group("refs")):
            number = int(num.group(1))
            if number not in found:
                found.append(number)
    return found


def self_test() -> None:
    assert closers_from_body("Closes #12") == [12]
    assert closers_from_body("Closes #87. Closes #88.") == [87, 88]
    assert closers_from_body("See #89 and #108") == []
    assert closers_from_body("Fixes #1, #2") == [1, 2]
    assert closers_from_body("Closed #3") == [3]
    assert closers_from_body("Fixed #4") == [4]
    assert closers_from_body("Resolved #5") == [5]
    assert closers_from_body(
        "Closes https://github.com/artofdream/aea-interactive-design/issues/113"
    ) == [113]
    assert closers_from_body("Mention close in passing. See #89.") == []
    assert closers_from_body("Closes #113. Do not mention #89.") == [113]


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

#!/usr/bin/env python3
"""Fail closed unless a pull-request body closes exactly one GitHub issue.

One issue → one branch → one PR. A multi-item issue must be split first.
Zero closers fails (a PR must name the issue it closes). Two or more fails.
Keep this sensor; do not delete it to go green.

Match GitHub closing keywords immediately followed by a reference:
close/closes/closed, fix/fixes/fixed, resolve/resolves/resolved, then
#N or https://github.com/owner/repo/issues/N (optional colon after the
keyword). Do not treat every #N on a line that merely contains those words.
"""

from __future__ import annotations

import os
import re
import sys

# Official GitHub forms: keyword (optional colon) immediately then a ref.
# Extra refs after one keyword may be joined with "," or "and" (Fixes #1, #2).
KEYWORD = re.compile(
    r"(?i)\b(?:close[sd]?|fix(?:es|ed)?|resolve[sd]?)\b:?"
)
REF = re.compile(
    r"(?:#|https://github\.com/[^/\s]+/[^/\s]+/issues/)(\d+)"
)
MORE_REFS = re.compile(r"\s*(?:,|and)\s*")


def closers_from_body(body: str) -> list[int]:
    found: list[int] = []
    for keyword in KEYWORD.finditer(body):
        after = body[keyword.end() :]
        space = re.match(r"\s+", after)
        if space is None:
            continue
        cursor = space.end()
        first = REF.match(after, cursor)
        if first is None:
            continue
        while first is not None:
            number = int(first.group(1))
            if number not in found:
                found.append(number)
            cursor = first.end()
            more = MORE_REFS.match(after, cursor)
            if more is None:
                break
            first = REF.match(after, more.end())
    return found


def self_test() -> None:
    assert closers_from_body("Closes #12") == [12]
    assert closers_from_body("Closed #12") == [12]
    assert closers_from_body("Fixed #12") == [12]
    assert closers_from_body("Resolved #12") == [12]
    assert closers_from_body("Closes #87. Closes #88.") == [87, 88]
    assert closers_from_body("See #89 and #108") == []
    assert closers_from_body("Fixes #1, #2") == [1, 2]
    assert closers_from_body("Closes #113 — do not close later; see #116") == [113]
    assert closers_from_body(
        "Closes https://github.com/artofdream/aea-interactive-design/issues/113"
    ) == [113]
    assert closers_from_body("Closes: #12") == [12]
    assert closers_from_body("Mention close in passing. See #89.") == []

    # Gate decision: exactly one closer passes; zero or two-plus fail closed.
    assert check("")[0] == 1
    assert check("   \n\n")[0] == 1
    assert check("## Summary\nNo closer here. See #89 and #108.")[0] == 1
    assert "no closing line" in check("")[1]
    assert check("Closes #225")[0] == 0
    assert check("## Summary\nFix the gate.\n\nCloses #225\n")[0] == 0
    assert check("Fixes: #225")[0] == 0
    assert check("Closes #225\nSee #113 for history.")[0] == 0
    assert check("Closes #1\nFixes #2")[0] == 1
    assert check("Fixes #1, #2")[0] == 1
    assert check("Resolves #1 and #2")[0] == 1
    assert "more than one issue" in check("Closes #1\nCloses #2")[1]


def check(body: str) -> tuple[int, str]:
    """Return (exit code, message) for a PR body. Exactly one closer passes."""
    numbers = closers_from_body(body)
    if not numbers:
        return 1, (
            "PR body has no closing line. Add exactly one line such as "
            "`Closes #N` (keywords: close/closes/closed, fix/fixes/fixed, "
            "resolve/resolves/resolved). One finding → one issue → "
            "one branch → one PR."
        )
    if len(numbers) > 1:
        return 1, (
            "PR body closes more than one issue: "
            + ", ".join(f"#{n}" for n in numbers)
            + ". Split the items: one issue → one branch → one PR."
        )
    return 0, f"closers=#{numbers[0]}; exactly-one OK"


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        print("self-test OK")
        return 0
    code, message = check(os.environ.get("PR_BODY", ""))
    print(message)
    return code


if __name__ == "__main__":
    raise SystemExit(main())

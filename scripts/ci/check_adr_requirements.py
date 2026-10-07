#!/usr/bin/env python3
"""Fail closed if an ADR cites a requirement ID that docs/srs.md does not define.

Every ADR in docs/adr/*.md (except README.md) must have exactly one line
starting with "Related requirements:". The value is either the single word
"none" or a comma-separated list of official IDs such as "FR-9, NFR-5".
Each ID must exist as a **FR-n:** / **NFR-n:** freeze entry in docs/srs.md.

Fail closed: a missing or unparsable docs/srs.md, a missing docs/adr/
directory, an ADR without the line, an unknown ID (FR-19, NFR-10, ...),
or a token that is not an ID all exit non-zero. Do not invent IDs.
Keep this sensor; do not delete it to go green.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SRS_PATH = Path("docs") / "srs.md"
ADR_DIR = Path("docs") / "adr"
INDEX_NAME = "README.md"

PREFIX = "Related requirements:"
# Freeze entries are written as **FR-n:** / **NFR-n:** (same marker CI's
# srs-present job requires). Substring matches like "FR-1..FR-18" do not count.
SRS_ENTRY = re.compile(r"\*\*((?:FR|NFR)-[1-9][0-9]*):\*\*")
ID_TOKEN = re.compile(r"^(?:FR|NFR)-[1-9][0-9]*$")


class CheckError(Exception):
    """A fail-closed finding."""


def srs_ids_from_text(text: str) -> set[str]:
    ids = set(SRS_ENTRY.findall(text))
    has_fr = any(i.startswith("FR-") for i in ids)
    has_nfr = any(i.startswith("NFR-") for i in ids)
    if not (has_fr and has_nfr):
        raise CheckError(
            "docs/srs.md has no **FR-n:** and **NFR-n:** freeze entries. "
            "Fail closed: cannot verify ADR requirement IDs."
        )
    return ids


def related_lines(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.startswith(PREFIX)]


def parse_related(line: str) -> list[str]:
    """Return cited IDs; [] for "none". Raise CheckError on bad syntax."""
    value = line[len(PREFIX) :].strip()
    if not value:
        raise CheckError("empty 'Related requirements:' value (write 'none' if none apply)")
    if value == "none":
        return []
    tokens = [t.strip() for t in value.split(",")]
    bad = [t for t in tokens if not ID_TOKEN.match(t)]
    if bad:
        raise CheckError(
            "not an official ID token: "
            + ", ".join(repr(t) for t in bad)
            + " (use e.g. 'FR-9, NFR-5' or 'none')"
        )
    return tokens


def check_adr_text(name: str, text: str, srs_ids: set[str]) -> list[str]:
    """Return a list of problems for one ADR (empty list = OK)."""
    lines = related_lines(text)
    if not lines:
        return [f"{name}: missing a line starting with '{PREFIX}'"]
    if len(lines) > 1:
        return [f"{name}: {len(lines)} '{PREFIX}' lines; keep exactly one"]
    try:
        cited = parse_related(lines[0])
    except CheckError as exc:
        return [f"{name}: {exc}"]
    unknown = [i for i in cited if i not in srs_ids]
    if unknown:
        return [
            f"{name}: ID(s) not defined in docs/srs.md: "
            + ", ".join(unknown)
            + ". Do not invent FR/NFR IDs."
        ]
    return []


def load_srs_ids(root: Path) -> set[str]:
    path = root / SRS_PATH
    if not path.is_file():
        raise CheckError("docs/srs.md is missing. Fail closed: no ID freeze, no ADR check.")
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise CheckError(f"docs/srs.md is unreadable ({exc}). Fail closed.") from exc
    return srs_ids_from_text(text)


def adr_files(root: Path) -> list[Path]:
    directory = root / ADR_DIR
    if not directory.is_dir():
        raise CheckError("docs/adr/ is missing. Fail closed: ADRs are required (#227).")
    files = sorted(p for p in directory.glob("*.md") if p.name != INDEX_NAME)
    if not files:
        raise CheckError("docs/adr/ has no ADR files. Fail closed.")
    return files


def run(root: Path) -> int:
    try:
        srs_ids = load_srs_ids(root)
        files = adr_files(root)
    except CheckError as exc:
        print(str(exc))
        return 1
    problems: list[str] = []
    cited_total: set[str] = set()
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            problems.append(f"{path.name}: unreadable ({exc})")
            continue
        found = check_adr_text(path.name, text, srs_ids)
        problems.extend(found)
        if not found:
            cited_total.update(parse_related(related_lines(text)[0]))
            print(f"{path.name}: {related_lines(text)[0]}")
    if problems:
        for problem in problems:
            print(problem)
        print(f"ADR requirement check FAILED ({len(problems)} problem(s)).")
        return 1
    print(
        f"adrs={len(files)} srs_ids={len(srs_ids)} cited_ids={len(cited_total)}; "
        "every Related requirements ID exists in docs/srs.md"
    )
    return 0


def _expect_error(fn, *args) -> str:
    try:
        fn(*args)
    except CheckError as exc:
        return str(exc)
    raise AssertionError(f"expected CheckError from {fn.__name__}{args!r}")


def self_test() -> None:
    srs = "- **FR-1:** a\n- **FR-9:** b\n- **NFR-5:** c\nRange FR-1..FR-18 and FR-19 prose.\n"
    ids = srs_ids_from_text(srs)
    assert ids == {"FR-1", "FR-9", "NFR-5"}, ids
    # Range or prose mentions are not freeze entries; FR-19 is not defined.
    assert "FR-19" not in ids
    assert "freeze entries" in _expect_error(srs_ids_from_text, "no entries, FR-1..FR-18")
    assert "freeze entries" in _expect_error(srs_ids_from_text, "- **FR-1:** only FR\n")

    assert parse_related("Related requirements: FR-9, NFR-5") == ["FR-9", "NFR-5"]
    assert parse_related("Related requirements: none") == []
    assert parse_related("Related requirements:FR-1") == ["FR-1"]
    assert "empty" in _expect_error(parse_related, "Related requirements:   ")
    assert "not an official ID" in _expect_error(parse_related, "Related requirements: FR9")
    assert "not an official ID" in _expect_error(parse_related, "Related requirements: FR-1 and FR-9")
    assert "not an official ID" in _expect_error(parse_related, "Related requirements: none, FR-1")
    assert "not an official ID" in _expect_error(parse_related, "Related requirements: FR-01")
    assert "not an official ID" in _expect_error(parse_related, "Related requirements: FR-1,")

    ok = "# ADR\n\nRelated requirements: FR-1, NFR-5\n"
    assert check_adr_text("a.md", ok, ids) == []
    assert check_adr_text("b.md", "Related requirements: none\n", ids) == []
    invented = check_adr_text("c.md", "Related requirements: FR-19, NFR-10\n", ids)
    assert invented and "FR-19" in invented[0] and "NFR-10" in invented[0], invented
    missing = check_adr_text("d.md", "# ADR\n**Related requirements:** FR-1\n", ids)
    assert missing and "missing" in missing[0], missing
    indented = check_adr_text("e.md", "  Related requirements: FR-1\n", ids)
    assert indented and "missing" in indented[0], indented
    twice = check_adr_text("f.md", "Related requirements: FR-1\nRelated requirements: FR-9\n", ids)
    assert twice and "exactly one" in twice[0], twice

    # Fail closed on a repo root with no docs/srs.md or no docs/adr/.
    empty_root = Path(__file__).resolve().parent / "__adr_self_test_no_such_dir__"
    assert "missing" in _expect_error(load_srs_ids, empty_root)
    assert "missing" in _expect_error(adr_files, empty_root)


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        print("self-test OK")
        return 0
    return run(REPO_ROOT)


if __name__ == "__main__":
    raise SystemExit(main())

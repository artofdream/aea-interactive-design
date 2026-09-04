#!/usr/bin/env python3
"""Build the knowledge site from Markdown. Stdlib only. Not a CMS."""

from __future__ import annotations

import html
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
OUT = ROOT / "_site"

NAV = [
    ("index.html", "Home"),
    ("brief.html", "Brief"),
    ("friday-plan.html", "Friday"),
    ("video-script.html", "Video"),
    ("presentation.html", "Talk"),
    ("presentation-sample.html", "Slides"),
    ("stack.html", "Stack"),
    ("srs.html", "SRS freeze"),
    ("coverage.html", "Coverage"),
    ("honesty.html", "Honesty"),
    ("future.html", "Future"),
]

REQUIRED = [
    ROOT / "index.md",
    ROOT / "brief.md",
    ROOT / "friday-plan.md",
    ROOT / "video-script.md",
    ROOT / "presentation.md",
    ROOT / "presentation-sample.md",
    ROOT / "stack.md",
    ROOT / "srs.md",
    ROOT / "coverage.md",
    ROOT / "honesty.md",
    ROOT / "future.md",
]

MERMAID_CDN = "https://cdn.jsdelivr.net/npm/mermaid@11.6.0/dist/mermaid.esm.min.mjs"
WIDE_PAGES = {"stack.html", "coverage.html", "friday-plan.html", "aws-schema-map.html", "presentation.html"}
SAFE_CLIP_RE = re.compile(r"^clips/[A-Za-z0-9][A-Za-z0-9._-]*\.mp4$")
VIDEO_OPEN_RE = re.compile(r"<video\b([^>]*)>", re.IGNORECASE)
VIDEO_SRC_RE = re.compile(r"""\bsrc\s*=\s*(['"])([^'"]+)\1""", re.IGNORECASE)
CLIP_REF_RE = re.compile(r"clips/[A-Za-z0-9][A-Za-z0-9._-]*\.mp4")


def fail(message: str) -> None:
    print(f"fail-closed: {message}", file=sys.stderr)
    raise SystemExit(1)


_LIST_ITEM_RE = re.compile(r"^([ \t]*)([-*]|\d+\.)[ \t]+(.*)$")


def _indent_width(ws: str) -> int:
    n = 0
    for ch in ws:
        n += 4 - (n % 4) if ch == "\t" else 1
    return n


def _line_indent(line: str) -> int:
    i = 0
    n = 0
    while i < len(line):
        if line[i] == " ":
            n += 1
        elif line[i] == "\t":
            n += 4 - (n % 4)
        else:
            break
        i += 1
    return n


def _is_blank(line: str) -> bool:
    return not line.strip()


def _parse_list_item(line: str) -> tuple[int, str, str] | None:
    m = _LIST_ITEM_RE.match(line)
    if not m:
        return None
    kind = "ul" if m.group(2) in "-*" else "ol"
    return _indent_width(m.group(1)), kind, m.group(3)


def _peek_nonblank(lines: list[str], i: int) -> int | None:
    while i < len(lines) and _is_blank(lines[i]):
        i += 1
    return i if i < len(lines) else None


def _is_interrupting_block(line: str) -> bool:
    s = line.lstrip()
    if s.startswith("```"):
        return True
    if re.match(r"^#{1,6}\s+", s):
        return True
    if re.match(r"^---+\s*$", s):
        return True
    if s.startswith("> "):
        return True
    return False


def _belongs_to_list(lines: list[str], i: int, base_indent: int) -> bool:
    """True if content at/after i still belongs to a list at base_indent.

    Blank lines do not end a list when the next non-blank line is a sibling
    item, a nested item, or an indented continuation of the current item.
    """
    j = _peek_nonblank(lines, i)
    if j is None:
        return False
    line = lines[j]
    if _is_interrupting_block(line) and _line_indent(line) <= base_indent:
        return False
    item = _parse_list_item(line)
    if item is not None:
        return item[0] >= base_indent
    return _line_indent(line) > base_indent


def _consume_indented_para(lines: list[str], i: int, min_indent: int) -> tuple[str, int]:
    buf: list[str] = []
    while i < len(lines):
        if _is_blank(lines[i]):
            break
        if _parse_list_item(lines[i]) is not None:
            break
        if _line_indent(lines[i]) < min_indent:
            break
        if _is_interrupting_block(lines[i]):
            break
        buf.append(lines[i].strip())
        i += 1
    text = " ".join(x for x in buf if x)
    return (f"<p>{inline(text)}</p>" if text else ""), i


def _consume_list(lines: list[str], i: int) -> tuple[str, int]:
    """Consume a markdown list, including nested lists and blank-line gaps."""
    first = _parse_list_item(lines[i])
    if first is None:
        raise ValueError("expected a list item")
    base_indent, kind, _ = first
    items: list[list[str]] = []

    while i < len(lines) and _belongs_to_list(lines, i, base_indent):
        if _is_blank(lines[i]):
            i += 1
            continue

        parsed = _parse_list_item(lines[i])
        if parsed is None:
            break

        indent, item_kind, text = parsed
        if indent < base_indent:
            break
        if indent > base_indent:
            nested, i = _consume_list(lines, i)
            if items:
                items[-1].append(nested)
            else:
                items.append([nested])
            continue
        if item_kind != kind:
            break

        i += 1
        parts: list[str] = [inline(text)] if text else []
        while i < len(lines):
            if _is_blank(lines[i]):
                # Stay in this item only for nested lists / indented continuations.
                if not _belongs_to_list(lines, i + 1, indent + 1):
                    break
                i += 1
                continue

            nested_item = _parse_list_item(lines[i])
            if nested_item is not None:
                nindent, _, _ = nested_item
                if nindent > indent:
                    nested, i = _consume_list(lines, i)
                    parts.append(nested)
                    continue
                break

            if _line_indent(lines[i]) > indent and not _is_interrupting_block(lines[i]):
                para, i = _consume_indented_para(lines, i, indent + 1)
                if para:
                    parts.append(para)
                continue
            break

        items.append(parts)

    lis = "".join(f"<li>{''.join(parts)}</li>" for parts in items)
    return f"<{kind}>{lis}</{kind}>", i


def md_to_html(src: str) -> str:
    lines = src.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    in_code = False
    code_lang = ""
    code_lines: list[str] = []

    def flush_para(buf: list[str]) -> None:
        if not buf:
            return
        text = " ".join(x.strip() for x in buf if x.strip())
        if text:
            out.append(f"<p>{inline(text)}</p>")
        buf.clear()

    para: list[str] = []

    while i < len(lines):
        line = lines[i]
        if in_code:
            if line.strip().startswith("```"):
                body = "\n".join(code_lines)
                if code_lang.lower() == "mermaid":
                    out.append(f'<pre class="mermaid">{html.escape(body)}</pre>')
                else:
                    lang = html.escape(code_lang)
                    cls = f' class="language-{lang}"' if lang else ""
                    out.append(f"<pre><code{cls}>{html.escape(body)}</code></pre>")
                in_code = False
                code_lines = []
                code_lang = ""
            else:
                code_lines.append(line)
            i += 1
            continue

        if line.strip().startswith("```"):
            flush_para(para)
            in_code = True
            code_lang = line.strip()[3:].strip()
            i += 1
            continue

        if re.match(r"^---+\s*$", line):
            flush_para(para)
            out.append("<hr>")
            i += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            flush_para(para)
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2).strip())}</h{level}>")
            i += 1
            continue

        if line.strip().startswith("> "):
            flush_para(para)
            quote: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                quote.append(lines[i].strip()[2:])
                i += 1
            out.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
            continue

        if line.lstrip().lower().startswith("<video"):
            flush_para(para)
            video_html, i = _consume_video_html(lines, i)
            out.append(video_html)
            continue

        if _is_table_start(lines, i):
            flush_para(para)
            table_html, i = _consume_table(lines, i)
            out.append(table_html)
            continue

        if _parse_list_item(line) is not None:
            flush_para(para)
            list_html, i = _consume_list(lines, i)
            out.append(list_html)
            continue

        if line.strip() == "":
            flush_para(para)
            i += 1
            continue

        para.append(line)
        i += 1

    flush_para(para)
    if in_code:
        fail("unclosed fenced code block")
    return "\n".join(out)


def _is_table_start(lines: list[str], i: int) -> bool:
    if i + 1 >= len(lines):
        return False
    if "|" not in lines[i]:
        return False
    return bool(re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]))


def _split_row(row: str) -> list[str]:
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    return [c.strip() for c in row.split("|")]


def _consume_table(lines: list[str], i: int) -> tuple[str, int]:
    header = _split_row(lines[i])
    i += 2
    rows: list[list[str]] = []
    while i < len(lines) and "|" in lines[i] and lines[i].strip():
        rows.append(_split_row(lines[i]))
        i += 1
    parts = ["<table>", "<thead><tr>"]
    parts.extend(f"<th>{inline(c)}</th>" for c in header)
    parts.append("</tr></thead><tbody>")
    for row in rows:
        parts.append("<tr>")
        parts.extend(f"<td>{inline(c)}</td>" for c in row)
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "".join(parts), i


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
EM_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")


def rewrite_href(href: str) -> str:
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return href
    if href.endswith(".md"):
        href = href[:-3] + ".html"
    if href == "docs/srs.md" or href.endswith("/docs/srs.md"):
        return "srs-full.html"
    return href


def inline(text: str) -> str:
    placeholders: list[str] = []

    def hold(fragment: str) -> str:
        placeholders.append(fragment)
        return f"\x00{len(placeholders) - 1}\x00"

    def images(match: re.Match[str]) -> str:
        alt, href = match.group(1), match.group(2)
        href = rewrite_href(href)
        path_only = href.split("?", 1)[0].split("#", 1)[0]
        if path_only.lower().endswith(".mp4"):
            return hold(_video_html(href, wrap=False))
        return hold(
            f'<img src="{html.escape(href, quote=True)}" alt="{html.escape(alt, quote=True)}">'
        )

    def links(match: re.Match[str]) -> str:
        label, href = match.group(1), match.group(2)
        if href == "../docs/srs.md" or href == "docs/srs.md":
            href = "srs-full.html"
        href = rewrite_href(href)
        return hold(
            f'<a href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
        )

    text = IMAGE_RE.sub(images, text)
    text = LINK_RE.sub(links, text)

    def codes(match: re.Match[str]) -> str:
        return hold(f"<code>{html.escape(match.group(1))}</code>")

    text = CODE_RE.sub(codes, text)
    text = html.escape(text)
    text = BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = EM_RE.sub(r"<em>\1</em>", text)
    for idx, fragment in enumerate(placeholders):
        text = text.replace(f"\x00{idx}\x00", fragment)
    return text


def title_from_md(src: str, fallback: str) -> str:
    for line in src.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def collect_pages() -> list[Path]:
    pages = []
    for path in sorted(ROOT.rglob("*.md")):
        pages.append(path)
    return pages


def rel_from_out(from_html: Path, name: str) -> str:
    depth = len(from_html.parent.relative_to(OUT).parts)
    return "/".join([".."] * depth + [name]) if depth else name


def rel_css(from_html: Path) -> str:
    return rel_from_out(from_html, "style.css")


def rel_nav_prefix(from_html: Path) -> str:
    depth = len(from_html.parent.relative_to(OUT).parts)
    return "/".join([".."] * depth) + "/" if depth else ""


FAVICON_FILES = (
    "favicon.ico",
    "favicon-32.png",
    "apple-touch-icon.png",
)


def copy_static_dir(name: str) -> None:
    src = ROOT / name
    if not src.is_dir():
        return
    dest = OUT / name
    for path in src.rglob("*"):
        if not path.is_file():
            continue
        target = dest / path.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())


def copy_static_assets() -> None:
    copy_static_dir("assets")
    copy_static_dir("clips")


def copy_favicons() -> None:
    for name in FAVICON_FILES:
        src = ROOT / name
        if not src.is_file():
            fail(f"missing knowledge/{name}")
        (OUT / name).write_bytes(src.read_bytes())


def assert_favicons_built() -> None:
    for name in FAVICON_FILES:
        path = OUT / name
        if not path.is_file() or path.stat().st_size < 32:
            fail(f"built site missing favicon {name}")
    index = (OUT / "index.html").read_text(encoding="utf-8")
    for needle in (
        'rel="icon"',
        "favicon.ico",
        "favicon-32.png",
        'rel="apple-touch-icon"',
        "apple-touch-icon.png",
    ):
        if needle not in index:
            fail(f"index.html missing favicon wiring ({needle})")
    nested = OUT / "future" / "schema.html"
    if nested.is_file():
        nested_html = nested.read_text(encoding="utf-8")
        if 'href="../favicon.ico"' not in nested_html:
            fail("nested page missing relative favicon path")


def assert_clip_refs() -> None:
    for md_path in sorted(ROOT.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        for rel in CLIP_REF_RE.findall(text):
            src = ROOT / rel
            if not src.is_file():
                fail(f"{md_path.relative_to(REPO)} references missing {rel}")


def _video_html(src: str, wrap: bool = True) -> str:
    if not SAFE_CLIP_RE.match(src):
        fail(f"video src must be clips/<file>.mp4, got {src!r}")
    esc = html.escape(src, quote=True)
    inner = (
        f'<video controls playsinline preload="metadata" src="{esc}">'
        f"Your browser does not play MP4. "
        f'<a href="{esc}">Download the clip</a>.'
        f"</video>"
    )
    if wrap:
        return f'<figure class="clip">{inner}</figure>'
    return inner


def _consume_video_html(lines: list[str], i: int) -> tuple[str, int]:
    buf: list[str] = []
    found_close = False
    while i < len(lines):
        buf.append(lines[i])
        if "</video>" in lines[i].lower():
            found_close = True
            i += 1
            break
        i += 1
    if not found_close:
        fail("unclosed video tag")
    raw = "\n".join(buf)
    open_m = VIDEO_OPEN_RE.search(raw)
    if open_m is None:
        fail("malformed video tag")
    src_m = VIDEO_SRC_RE.search(open_m.group(1))
    if src_m is None:
        fail("video tag missing src")
    return _video_html(src_m.group(2)), i


def page_shell_for(out_file: Path, title: str, body: str, current: str, extra_class: str) -> str:
    prefix = rel_nav_prefix(out_file)
    nav_bits = []
    for href, label in NAV:
        cls = ' class="is-current"' if href == current else ""
        nav_bits.append(f'<a href="{prefix}{href}"{cls}>{html.escape(label)}</a>')
    nav = "\n        ".join(nav_bits)
    css = rel_css(out_file)
    icon_ico = rel_from_out(out_file, "favicon.ico")
    icon_png = rel_from_out(out_file, "favicon-32.png")
    icon_apple = rel_from_out(out_file, "apple-touch-icon.png")
    future_note = ""
    if extra_class == "is-future" or current.startswith("future"):
        future_note = (
            '<p class="future-banner">Future / not-MVP — the assignment floor is the '
            "SRS freeze, not this page.</p>"
        )
    classes = extra_class.strip()
    if current in WIDE_PAGES or out_file.name in WIDE_PAGES:
        classes = f"{classes} is-wide".strip()
    mermaid_script = ""
    if 'class="mermaid"' in body:
        mermaid_script = f"""
  <script type="module">
    import mermaid from "{html.escape(MERMAID_CDN, quote=True)}";
    mermaid.initialize({{ startOnLoad: true, theme: "neutral", securityLevel: "strict" }});
  </script>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} — Café Fausse knowledge</title>
  <link rel="icon" href="{html.escape(icon_ico, quote=True)}" sizes="16x16 32x32 48x48">
  <link rel="icon" type="image/png" sizes="32x32" href="{html.escape(icon_png, quote=True)}">
  <link rel="apple-touch-icon" sizes="180x180" href="{html.escape(icon_apple, quote=True)}">
  <link rel="stylesheet" href="{css}">
</head>
<body class="{classes}">
  <header>
    <p class="eyebrow">Café Fausse knowledge map</p>
    <p class="sub">Not the restaurant. MVP = official SRS freeze.</p>
    <nav>
        {nav}
    </nav>
  </header>
  <main>
    {future_note}
    {body}
  </main>
  <footer>
    <p>Knowledge host <code>knowledge.cafe.artof.link</code>: HTTPS GET 200 this session
    (2026-09-02 Europe/Berlin); HTTP 301 to HTTPS. TLS VERIFY_OK, CN/SAN match. Pages
    <code>https_enforced=true</code>; cert approved for <code>knowledge.cafe.artof.link</code>.</p>
    <p>Restaurant hostname <code>cafe.artof.link</code> is <strong>not</strong> Café Fausse App
    (CNAME to an AWS ELB). Local MVP is in-repo. GitHub Actions → GitHub Pages. No GitLab.</p>
  </footer>{mermaid_script}
</body>
</html>
"""


def assert_coverage_freeze_ids(src: str) -> None:
    for n in range(1, 19):
        if f"| FR-{n} |" not in src:
            fail(f"coverage.md missing table row for FR-{n}")
    for n in range(1, 10):
        if f"| NFR-{n} |" not in src:
            fail(f"coverage.md missing table row for NFR-{n}")


def assert_svg_well_formed() -> None:
    assets = ROOT / "assets"
    if not assets.is_dir():
        return
    for path in sorted(assets.glob("*.svg")):
        raw = path.read_bytes()
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            fail(f"{path.relative_to(REPO)} is not UTF-8: {exc}")
        try:
            ET.fromstring(raw)
        except ET.ParseError as exc:
            fail(f"{path.relative_to(REPO)} is not well-formed SVG/XML: {exc}")


def main() -> None:
    for required in REQUIRED:
        if not required.is_file():
            fail(f"missing required knowledge page {required.relative_to(REPO)}")
    assert_coverage_freeze_ids((ROOT / "coverage.md").read_text(encoding="utf-8"))
    assert_svg_well_formed()
    assert_clip_refs()
    srs = REPO / "docs" / "srs.md"
    if not srs.is_file():
        fail("missing docs/srs.md")

    if OUT.exists():
        for child in OUT.rglob("*"):
            if child.is_file():
                child.unlink()
    OUT.mkdir(parents=True, exist_ok=True)

    css_src = ROOT / "style.css"
    if not css_src.is_file():
        fail("missing knowledge/style.css")
    (OUT / "style.css").write_text(css_src.read_text(encoding="utf-8"), encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    copy_static_assets()
    copy_favicons()
    clips_src = ROOT / "clips"
    if clips_src.is_dir():
        for clip in sorted(clips_src.glob("*.mp4")):
            dest = OUT / "clips" / clip.name
            if not dest.is_file() or dest.stat().st_size != clip.stat().st_size:
                fail(f"clip not copied to _site/clips/{clip.name}")

    for md_path in collect_pages():
        rel = md_path.relative_to(ROOT)
        out_name = rel.with_suffix(".html")
        if out_name.name == "index.html" and out_name.parent == Path("."):
            current = "index.html"
        else:
            current = str(out_name).replace("\\", "/")
        src = md_path.read_text(encoding="utf-8")
        body = md_to_html(src)
        title = title_from_md(src, md_path.stem)
        extra = "is-future" if "future" in current else ""
        html_out = page_shell_for(OUT / out_name, title, body, current if current in {n[0] for n in NAV} else ("future.html" if extra else current), extra)
        write(OUT / out_name, html_out)

    srs_src = srs.read_text(encoding="utf-8")
    srs_body = md_to_html(srs_src)
    write(
        OUT / "srs-full.html",
        page_shell_for(
            OUT / "srs-full.html",
            "Reconstructed SRS (full)",
            srs_body,
            "srs.html",
            "",
        ),
    )
    assert_favicons_built()
    print(f"built {OUT}")


if __name__ == "__main__":
    main()

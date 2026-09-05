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
    ("index.html", "Home", "home"),
    ("quantic.html", "Quantic", "quantic"),
    ("stack.html", "Stack", "stack"),
    ("srs.html", "SRS freeze", "srs"),
    ("coverage.html", "Coverage", "coverage"),
    ("honesty.html", "Honesty", "honesty"),
    ("glossary.html", "Glossary", "glossary"),
    ("future.html", "Future", "future"),
]

# Quantic delivery pages stay complete (#74 hub-only). They are not global nav (#79).
DELIVERY_ONLY_HREFS = (
    "brief.html",
    "friday-plan.html",
    "video-script.html",
    "must-film-shots.html",
    "presentation.html",
    "presentation-sample.html",
    "meeting-wednesday.html",
    "meeting-friday.html",
    "meeting-saturday.html",
    "meeting-sunday.html",
    "quantic-handoff.html",
)

# Stroke icons for in-page links and the page brand when the href is off NAV.
PAGE_ICONS = {
    "brief.html": "brief",
    "friday-plan.html": "friday",
    "video-script.html": "video",
    "must-film-shots.html": "video",
    "presentation.html": "talk",
    "presentation-sample.html": "slides",
    "glossary.html": "glossary",
    "meeting-wednesday.html": "brief",
    "meeting-friday.html": "friday",
    "meeting-saturday.html": "talk",
    "meeting-sunday.html": "slides",
    "quantic-handoff.html": "quantic",
}

# Stroke icons (viewBox 0 0 24 24). Labels stay the source of meaning.
ICONS = {
    "home": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M4 11.2 12 4l8 7.2V20h-5.2v-5.6H9.2V20H4z"/>'
    ),
    "quantic": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M4 10.2 12 6l8 4.2-8 4.2zM7.2 11.8v3.2c0 1.3 2.1 2.4 4.8 2.4s4.8-1.1 '
        '4.8-2.4v-3.2M19 10.8v6.4"/>'
    ),
    "brief": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M7 3.6h7.2L19 8.4V20.4H7zM14.2 3.6V8.4H19M9.2 12.2h5.6M9.2 15.6h5.6"/>'
    ),
    "friday": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M5 6.4h14v13.2H5zM5 10.6h14M9 4.2v4.2M15 4.2v4.2M8.2 14.2h1.8M12.1 14.2h1.8M16 14.2h.2"/>'
    ),
    "video": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 20.2a8.2 8.2 0 1 0 0-16.4 8.2 8.2 0 0 0 0 16.4zM10 8.8l5.4 3.2L10 15.2z"/>'
    ),
    "talk": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M5 5.6h13.2v8.4H9.4L5 17.8z"/>'
    ),
    "slides": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M4.4 7.2h12.4v10.4H4.4zM7.4 4.8h12.2v9.6"/>'
    ),
    "stack": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M4.4 15.8 12 19l7.6-3.2M4.4 12 12 15.2 19.6 12M12 5 4.4 8.2 12 11.4l7.6-3.2z"/>'
    ),
    "srs": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 5.2H6.2A2.2 2.2 0 0 0 4 7.4v11.2c.8-.8 1.9-1.2 3.2-1.2H12M12 5.2h5.8A2.2 2.2 0 0 1 20 7.4v11.2c-.8-.8-1.9-1.2-3.2-1.2H12V5.2z"/>'
    ),
    "coverage": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M4.6 6.2h14.8v12H4.6zM4.6 10.4h14.8M10.4 6.2v12"/>'
    ),
    "honesty": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 3.6 19.2 6.8v5.4c0 4.4-3.1 6.7-7.2 8.2-4.1-1.5-7.2-3.8-7.2-8.2V6.8zM8.8 12.2l2.3 2.3 4.2-4.4"/>'
    ),
    "glossary": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M5 5.2c1.8-.8 3.6-.8 5.4 0v13.2c-1.8-.8-3.6-.8-5.4 0zM19 5.2c-1.8-.8-3.6-.8-5.4 0v13.2c1.8-.8 3.6-.8 5.4 0z"/>'
    ),
    "future": (
        '<path fill="none" stroke="currentColor" stroke-width="1.75" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M12 20.2a8.2 8.2 0 1 0 0-16.4 8.2 8.2 0 0 0 0 16.4zM12 7.6l2.4 6.2L12 12l-2.4 1.8z"/>'
    ),
}

REQUIRED = [
    ROOT / "index.md",
    ROOT / "quantic.md",
    ROOT / "brief.md",
    ROOT / "friday-plan.md",
    ROOT / "video-script.md",
    ROOT / "must-film-shots.md",
    ROOT / "presentation.md",
    ROOT / "presentation-sample.md",
    ROOT / "meeting-wednesday.md",
    ROOT / "meeting-friday.md",
    ROOT / "meeting-saturday.md",
    ROOT / "meeting-sunday.md",
    ROOT / "quantic-handoff.md",
    ROOT / "stack.md",
    ROOT / "srs.md",
    ROOT / "coverage.md",
    ROOT / "honesty.md",
    ROOT / "glossary.md",
    ROOT / "future.md",
]

MERMAID_CDN = "https://cdn.jsdelivr.net/npm/mermaid@11.6.0/dist/mermaid.esm.min.mjs"
WIDE_PAGES = {
    "stack.html",
    "coverage.html",
    "friday-plan.html",
    "aws-schema-map.html",
    "presentation.html",
    "presentation-sample.html",
    "honesty.html",
    "glossary.html",
    "index.html",
    "brief.html",
    "video-script.html",
    "must-film-shots.html",
    "quantic-handoff.html",
}
SAFE_CLIP_RE = re.compile(r"^clips/[A-Za-z0-9][A-Za-z0-9._-]*\.mp4$")
VIDEO_OPEN_RE = re.compile(r"<video\b([^>]*)>", re.IGNORECASE)
VIDEO_SRC_RE = re.compile(r"""\bsrc\s*=\s*(['"])([^'"]+)\1""", re.IGNORECASE)
CLIP_REF_RE = re.compile(r"clips/[A-Za-z0-9][A-Za-z0-9._-]*\.mp4")
DIAGRAM_WRAP_RE = re.compile(r'(<div class="diagram-wrap"[^>]*>.*?</div>)', re.S)


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
        buf.clear()
        if not text:
            return
        # SVG figures emit a block .diagram-wrap; do not wrap that div in <p>
        # (browsers close the p and leave empty paragraphs on Stack HLD images).
        rendered = inline(text)
        for part in DIAGRAM_WRAP_RE.split(rendered):
            if not part:
                continue
            if DIAGRAM_WRAP_RE.fullmatch(part):
                out.append(part)
                continue
            leftover = part.strip()
            if leftover:
                out.append(f"<p>{leftover}</p>")

    para: list[str] = []

    while i < len(lines):
        line = lines[i]
        if in_code:
            if line.strip().startswith("```"):
                body = "\n".join(code_lines)
                if code_lang.lower() == "mermaid":
                    out.append(
                        '<div class="diagram-wrap" tabindex="0" role="region" '
                        'aria-label="Diagram">'
                        f'<pre class="mermaid">{html.escape(body)}</pre>'
                        "</div>"
                    )
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
            inner = inline(heading.group(2).strip())
            if level == 2:
                inner = (
                    '<span class="section-mark" aria-hidden="true"></span>'
                    f"{inner}"
                )
            out.append(f"<h{level}>{inner}</h{level}>")
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


_MD_DECOR_RE = re.compile(r"[*_`]")


def _cell_label(text: str) -> str:
    """Plain header text for mobile card data-label (no markdown markers)."""
    return _MD_DECOR_RE.sub("", text).strip()


def _consume_table(lines: list[str], i: int) -> tuple[str, int]:
    header = _split_row(lines[i])
    i += 2
    rows: list[list[str]] = []
    while i < len(lines) and "|" in lines[i] and lines[i].strip():
        rows.append(_split_row(lines[i]))
        i += 1
    labels = [_cell_label(c) for c in header]
    # 3+ columns overflow a phone column (12-slide outline is 4; 8-slide is 3).
    wide = " table-wide" if len(header) >= 3 else ""
    parts = [
        f'<div class="table-wrap{wide}" tabindex="0" role="region" '
        'aria-label="Data table">',
        "<table>",
        "<thead><tr>",
    ]
    parts.extend(f"<th>{inline(c)}</th>" for c in header)
    parts.append("</tr></thead><tbody>")
    for row in rows:
        parts.append("<tr>")
        for j, cell in enumerate(row):
            label = labels[j] if j < len(labels) else ""
            attr = f' data-label="{html.escape(label, quote=True)}"' if label else ""
            parts.append(f"<td{attr}>{inline(cell)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table></div>")
    return "".join(parts), i


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
EM_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")


def svg_icon(name: str, extra_class: str = "nav-icon") -> str:
    inner = ICONS.get(name)
    if inner is None:
        fail(f"missing icon {name}")
    return (
        f'<svg class="{html.escape(extra_class, quote=True)}" viewBox="0 0 24 24" '
        f'aria-hidden="true" focusable="false">{inner}</svg>'
    )


def icon_name_for_href(href: str) -> str | None:
    path = href.split("#", 1)[0].split("?", 1)[0]
    if path in PAGE_ICONS:
        return PAGE_ICONS[path]
    for nav_href, _label, icon in NAV:
        if path == nav_href:
            return icon
    return None


def icon_for_page_href(href: str) -> str:
    name = icon_name_for_href(href)
    if name is None:
        return ""
    return svg_icon(name, "inline-icon")


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
        if path_only.lower().endswith(".svg"):
            return hold(
                '<div class="diagram-wrap" tabindex="0" role="region" '
                'aria-label="Diagram">'
                f'<img class="diagram-img" src="{html.escape(href, quote=True)}" '
                f'alt="{html.escape(alt, quote=True)}">'
                "</div>"
            )
        return hold(
            f'<img src="{html.escape(href, quote=True)}" '
            f'alt="{html.escape(alt, quote=True)}">'
        )

    def links(match: re.Match[str]) -> str:
        label, href = match.group(1), match.group(2)
        if href == "../docs/srs.md" or href == "docs/srs.md":
            href = "srs-full.html"
        href = rewrite_href(href)
        icon = icon_for_page_href(href)
        cls = ' class="page-link"' if icon else ""
        return hold(
            f'<a href="{html.escape(href, quote=True)}"{cls}>{icon}{html.escape(label)}</a>'
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


def page_icon_name(current: str) -> str:
    name = icon_name_for_href(current)
    if name is not None:
        return name
    if current.startswith("future"):
        return "future"
    return "home"


def page_shell_for(out_file: Path, title: str, body: str, current: str, extra_class: str) -> str:
    prefix = rel_nav_prefix(out_file)
    nav_bits = []
    for href, label, icon in NAV:
        cls = ' class="is-current"' if href == current else ""
        nav_bits.append(
            f'<a href="{prefix}{href}"{cls}>{svg_icon(icon)}'
            f'<span>{html.escape(label)}</span></a>'
        )
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
    page_slug = current.replace(".html", "").replace("/", "-")
    classes = f"{classes} page-{page_slug}".strip()
    mermaid_script = ""
    if 'class="mermaid"' in body:
        mermaid_script = f"""
  <script type="module">
    import mermaid from "{html.escape(MERMAID_CDN, quote=True)}";
    mermaid.initialize({{ startOnLoad: true, theme: "neutral", securityLevel: "strict", flowchart: {{ useMaxWidth: true }} }});
  </script>"""
    brand_icon = svg_icon(page_icon_name(current), "page-icon")
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
  <a class="skip-link" href="#content">Skip to content</a>
  <header>
    <div class="brand">
      {brand_icon}
      <div>
        <p class="eyebrow">Café Fausse knowledge map</p>
        <p class="sub">Not the restaurant. MVP = official SRS freeze.</p>
      </div>
    </div>
    <nav aria-label="Knowledge pages">
        {nav}
    </nav>
  </header>
  <main id="content">
    {future_note}
    {body}
  </main>
  <footer>
    <p>Knowledge host <code>knowledge.cafe.artof.link</code>: HTTPS GET 200 this session
    (2026-09-05 Europe/Berlin); HTTP 301 to HTTPS.</p>
    <p>Prefer live share <code>https://cafe.artof.link/</code> (HTTPS GET 200 this session;
    Lightsail staging #57 — weekend recording window, not production forever).
    Interim backup <code>https://54-165-102-60.sslip.io/</code>. Local MVP is in-repo.
    GitHub Actions → GitHub Pages. No GitLab.</p>
  </footer>{mermaid_script}
</body>
</html>
"""


def _nav_block(html_text: str) -> str:
    match = re.search(r'<nav aria-label="Knowledge pages">(.*?)</nav>', html_text, re.S)
    if match is None:
        fail("missing Knowledge pages nav")
    return match.group(1)


def assert_coverage_freeze_ids(src: str) -> None:
    for n in range(1, 19):
        if f"| FR-{n} |" not in src:
            fail(f"coverage.md missing table row for FR-{n}")
    for n in range(1, 10):
        if f"| NFR-{n} |" not in src:
            fail(f"coverage.md missing table row for NFR-{n}")


def assert_ux_wiring() -> None:
    css = (OUT / "style.css").read_text(encoding="utf-8")
    for needle in (
        "@media",
        ".table-wrap",
        ".table-wide",
        ".nav-icon",
        ".section-mark",
        "max-width: 40rem",
        "min-width: 64rem",
        "max-width: 767px",
        "min-width: 768px",
        "attr(data-label)",
        "overflow-y: hidden",
        ".diagram-wrap",
        "grid-template-columns: repeat(2",
        "Swipe sideways for the full diagram",
    ):
        if needle not in css:
            fail(f"style.css missing readability rule ({needle})")
    if "min-width: 44rem" in css:
        fail("do not force table min-width 44rem — it clips when overflow-x fails")
    wrap_at = css.find(".table-wrap {")
    stack_at = css.find("@media (max-width: 767px)")
    if wrap_at == -1 or "overflow-y: hidden" not in css[wrap_at : wrap_at + 500]:
        fail("table-wrap must set overflow-y: hidden so overflow-x scrolls (WebKit)")
    if stack_at == -1 or "attr(data-label)" not in css[stack_at:]:
        fail("767px query must stack tables as cards via data-label")
    if stack_at == -1 or "grid-template-columns: repeat(2" not in css[stack_at:]:
        fail("767px query must use a two-column nav grid")
    if stack_at == -1 or ".diagram-wrap .diagram-img" not in css[stack_at:]:
        fail("767px query must keep HLD SVGs swipeable at a readable min-width")
    if stack_at == -1 or ".diagram-wrap .mermaid svg" not in css[stack_at:]:
        fail("767px query must keep mermaid diagrams swipeable at a readable min-width")
    if re.search(r"(html|body|header|main|footer)\s*\{[^}]*overflow:\s*hidden", css, re.S):
        fail("html/body/header/main/footer must not overflow:hidden (clips tables)")
    index = (OUT / "index.html").read_text(encoding="utf-8")
    for needle in (
        'class="nav-icon"',
        'aria-label="Knowledge pages"',
        'class="skip-link"',
        'id="content"',
        'class="section-mark"',
        'class="page-link"',
        'data-label="Team"',
        "table-wide",
    ):
        if needle not in index:
            fail(f"index.html missing UX wiring ({needle})")
    coverage = (OUT / "coverage.html").read_text(encoding="utf-8")
    if "table-wide" not in coverage:
        fail("coverage.html missing wide table wrap")
    if 'class="nav-icon"' not in coverage:
        fail("coverage.html missing nav icons")
    if 'data-label="Summary"' not in coverage:
        fail("coverage.html missing mobile card data-label")
    sample = (OUT / "presentation-sample.html").read_text(encoding="utf-8")
    if "table-wide" not in sample:
        fail("presentation-sample.html missing wide table wrap")
    if 'data-label="Say / show"' not in sample:
        fail("presentation-sample 12-slide table missing Say / show data-label")
    if 'data-label="Merge from the long outline"' not in sample:
        fail("presentation-sample 8-slide (3-col) table must also stack")
    if 'aria-label="Scrollable table"' in sample:
        fail("do not keep swipe-only aria on stacked tables")
    stack_html = (OUT / "stack.html").read_text(encoding="utf-8")
    if 'class="diagram-img"' not in stack_html:
        fail("stack.html missing swipeable HLD diagram images")
    if stack_html.count('class="diagram-wrap"') < 4:
        fail("stack.html must wrap mermaid and HLD SVGs in diagram-wrap")
    if re.search(r"<p>\s*<div class=\"diagram-wrap\"", stack_html):
        fail("stack.html must not wrap HLD diagram-wrap inside <p>")
    if "useMaxWidth: true" not in stack_html:
        fail("stack.html mermaid init must set useMaxWidth")
    for mermaid_page in ("friday-plan.html", "presentation.html"):
        built = (OUT / mermaid_page).read_text(encoding="utf-8")
        if 'class="diagram-wrap"' not in built or 'class="mermaid"' not in built:
            fail(f"{mermaid_page} missing wrapped mermaid diagram")
    honesty_md = (ROOT / "honesty.md").read_text(encoding="utf-8")
    if "Do not say NFR-1 / NFR-2 **met**" not in honesty_md:
        fail("honesty.md lost the NFR-1 / NFR-2 not-met line")
    quantic = OUT / "quantic.html"
    if not quantic.is_file():
        fail("missing built quantic.html")
    qhtml = quantic.read_text(encoding="utf-8")
    for needle in (
        "Navigation hub only",
        "Delivery / MSAIE",
        "not the Quantic pack",
        'href="brief.html"',
        'href="coverage.html"',
        'href="presentation.html"',
        'href="presentation-sample.html"',
        'href="video-script.html"',
        'href="must-film-shots.html"',
        'href="friday-plan.html"',
        'href="meeting-wednesday.html"',
        'href="meeting-friday.html"',
        'href="meeting-saturday.html"',
        'href="meeting-sunday.html"',
        'href="quantic-handoff.html"',
        'href="honesty.html"',
        'href="glossary.html"',
        'href="stack.html"',
        'href="future.html"',
        'href="index.html"',
        'class="nav-icon"',
        'class="is-current"',
    ):
        if needle not in qhtml:
            fail(f"quantic.html missing hub wiring ({needle})")
    if "<table" in qhtml:
        fail("quantic.html must stay table-light (issue #73 is a separate PR)")
    if "<video" in qhtml or 'class="mermaid"' in qhtml:
        fail("quantic.html must not embed clips or diagrams (nav hub only)")
    if 'href="quantic.html"' not in index:
        fail("index.html missing Quantic nav link")
    if 'href="glossary.html"' not in index:
        fail("index.html missing Glossary nav link")
    glossary_md = (ROOT / "glossary.md").read_text(encoding="utf-8")
    for term in ("Probe", "Unknown", "MVP"):
        if term not in glossary_md:
            fail(f"glossary.md missing term {term}")
    if "## Sources and links" not in glossary_md:
        fail("glossary.md must keep the #101 sources / links table")
    future_glossary = (ROOT / "future" / "glossary.md").read_text(encoding="utf-8")
    if "../glossary.md" not in future_glossary:
        fail("future/glossary.md must point at the first-class glossary")
    if "inline-icon" not in qhtml:
        fail("quantic.html delivery links must keep page icons")
    for page in (
        "index.html",
        "stack.html",
        "srs.html",
        "coverage.html",
        "honesty.html",
        "glossary.html",
        "future.html",
        "quantic.html",
        *DELIVERY_ONLY_HREFS,
    ):
        built = OUT / page
        if not built.is_file():
            fail(f"missing built {page}")
        nav = _nav_block(built.read_text(encoding="utf-8"))
        if 'href="quantic.html"' not in nav:
            fail(f"{page} global nav must keep Quantic hub")
        if 'href="glossary.html"' not in nav:
            fail(f"{page} global nav must keep first-class Glossary")
        for name in DELIVERY_ONLY_HREFS:
            if re.search(rf'href="(?:\.\./)*{re.escape(name)}"', nav):
                fail(f"{page} global nav must not include Quantic delivery {name}")
    brief_md = (ROOT / "brief.md").read_text(encoding="utf-8")
    video_md = (ROOT / "video-script.md").read_text(encoding="utf-8")
    stack_md = (ROOT / "stack.md").read_text(encoding="utf-8")
    if "clips/01-home-menu.mp4" not in brief_md or "clips/02-happy-book.mp4" not in brief_md:
        fail("brief.md must keep clip embeds (hub is nav-only; do not hollow source pages)")
    if "clips/01-home-menu.mp4" not in video_md or "clips/02-happy-book.mp4" not in video_md:
        fail("video-script.md must keep clip embeds (hub is nav-only; do not hollow source pages)")
    if "clips/03-zoom-dryrun-v2.mp4" not in video_md:
        fail("video-script.md must embed Zoom dry-run v2 prototype (issue #81)")
    if "must-film-shots.md" not in video_md:
        fail("video-script.md must link the must-film shot list (issue #83)")
    wed_md = (ROOT / "meeting-wednesday.md").read_text(encoding="utf-8")
    fri_md = (ROOT / "meeting-friday.md").read_text(encoding="utf-8")
    sat_md = (ROOT / "meeting-saturday.md").read_text(encoding="utf-8")
    sun_md = (ROOT / "meeting-sunday.md").read_text(encoding="utf-8")
    if "brief.md" not in wed_md:
        fail("meeting-wednesday.md must link the Brief (do not hollow it)")
    if "friday-plan.md" not in fri_md:
        fail("meeting-friday.md must link the Friday plan (do not hollow it)")
    if "presentation.md" not in sat_md or "video-script.md" not in sat_md:
        fail("meeting-saturday.md must link talk cuts and video script")
    if "must-film-shots.md" not in sat_md:
        fail("meeting-saturday.md must link the must-film shot list")
    if "America/New_York" not in sat_md or "Europe/Berlin" not in sat_md:
        fail("meeting-saturday.md must note America/New_York and Europe/Berlin")
    if "Unknown" not in sun_md or "to-be-filled" not in sun_md:
        fail("meeting-sunday.md must stay Unknown / to-be-filled until notes exist")
    handoff_md = (ROOT / "quantic-handoff.md").read_text(encoding="utf-8")
    for needle in (
        "https://github.com/artofdream/aea-interactive-design",
        "https://cafe.artof.link/",
        "https://knowledge.cafe.artof.link/",
        "quantic.html",
        "coverage.md",
        "honesty.md",
        "PROTOTYPE",
        "not FR-19",
        "NFR-1",
        "NFR-7",
        "to-be-filled",
    ):
        if needle not in handoff_md:
            fail(f"quantic-handoff.md missing required handoff fact ({needle})")
    if "<video" in handoff_md or "clips/" in handoff_md:
        fail("quantic-handoff.md must not embed clips (sister pages keep them)")
    for name, text in (
        ("meeting-wednesday.md", wed_md),
        ("meeting-friday.md", fri_md),
        ("meeting-saturday.md", sat_md),
        ("meeting-sunday.md", sun_md),
    ):
        if "quantic-handoff.md" not in text:
            fail(f"{name} must link the Quantic deliverable handoff")
    for name, text in (
        ("meeting-wednesday.md", wed_md),
        ("meeting-friday.md", fri_md),
        ("meeting-saturday.md", sat_md),
        ("meeting-sunday.md", sun_md),
    ):
        if "<video" in text or "clips/" in text:
            fail(f"{name} must not embed clips (sister pages keep them)")
    shots_md = (ROOT / "must-film-shots.md").read_text(encoding="utf-8")
    if "Do-not-say checklist" not in shots_md:
        fail("must-film-shots.md lost the do-not-say checklist")
    if "<video" in shots_md:
        fail("must-film-shots.md must not embed clips (video-script keeps them)")
    if "hld-aws-staging.svg" not in stack_md:
        fail("stack.md must keep AWS staging HLD (hub is nav-only; do not hollow source pages)")


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
    assert_ux_wiring()
    print(f"built {OUT}")


if __name__ == "__main__":
    main()

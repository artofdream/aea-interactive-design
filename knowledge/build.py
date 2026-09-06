#!/usr/bin/env python3
"""Build the knowledge site from Markdown. Stdlib only. Not a CMS."""

from __future__ import annotations

import html
import re
import struct
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
    "journal.html",
    "meeting-wednesday.html",
    "meeting-friday.html",
    "meeting-saturday.html",
    "meeting-sunday.html",
    "quantic-handoff.html",
    "meghna-cafe-demo.html",
    "meghna-materials.html",
    "meghna-voiceover.html",
    "parts-345-materials.html",
    "parts-345-notes.html",
    "parts-345-vo-notes.html",
    "parts-345-handoff-mapping.html",
    "part3-local-vs-aws.html",
    "part3-hld-flow-notes.html",
    "part4-coding-overview.html",
    "part3-variant-b-script.html",
    "part3-variant-b-voiceover.html",
    "part3-variant-b-script-natural.html",
    "part3-variant-b-voiceover-natural.html",
    "part4-variant-c-script.html",
    "part4-variant-c-voiceover.html",
    "part4-variant-c-script-natural.html",
    "part4-variant-c-voiceover-natural.html",
    "part5-shared-close-script.html",
    "part5-shared-close-voiceover.html",
    "part5-shared-close-script-natural.html",
    "part5-shared-close-voiceover-natural.html",
    "part3-present.html",
    "part4-present.html",
    "part5-present.html",
    "developer-system-map.html",
    "to-be.html",
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
    "journal.html": "brief",
    "meeting-wednesday.html": "brief",
    "meeting-friday.html": "friday",
    "meeting-saturday.html": "talk",
    "meeting-sunday.html": "slides",
    "quantic-handoff.html": "quantic",
    "meghna-cafe-demo.html": "video",
    "meghna-materials.html": "video",
    "meghna-voiceover.html": "talk",
    "parts-345-materials.html": "video",
    "parts-345-notes.html": "brief",
    "parts-345-vo-notes.html": "brief",
    "parts-345-handoff-mapping.html": "coverage",
    "part3-local-vs-aws.html": "stack",
    "part3-hld-flow-notes.html": "stack",
    "part4-coding-overview.html": "stack",
    "part3-variant-b-script.html": "talk",
    "part3-variant-b-voiceover.html": "talk",
    "part3-variant-b-script-natural.html": "talk",
    "part3-variant-b-voiceover-natural.html": "talk",
    "part4-variant-c-script.html": "talk",
    "part4-variant-c-voiceover.html": "talk",
    "part4-variant-c-script-natural.html": "talk",
    "part4-variant-c-voiceover-natural.html": "talk",
    "part5-shared-close-script.html": "talk",
    "part5-shared-close-voiceover.html": "talk",
    "part5-shared-close-script-natural.html": "talk",
    "part5-shared-close-voiceover-natural.html": "talk",
    "part3-present.html": "slides",
    "part4-present.html": "slides",
    "part5-present.html": "slides",
    "developer-system-map.html": "stack",
    "to-be.html": "future",
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
    ROOT / "stack.md",
    ROOT / "srs.md",
    ROOT / "coverage.md",
    ROOT / "honesty.md",
    ROOT / "glossary.md",
    ROOT / "future.md",
    ROOT / "journal.md",
]

MERMAID_CDN = "https://cdn.jsdelivr.net/npm/mermaid@11.6.0/dist/mermaid.esm.min.mjs"
WIDE_PAGES = {
    "to-be.html",
    "stack.html",
    "coverage.html",
    "friday-plan.html",
    "aws-schema-map.html",
    "presentation.html",
    "presentation-sample.html",
    "honesty.html",
    "index.html",
    "brief.html",
    "video-script.html",
    "must-film-shots.html",
    "glossary.html",
    "parts-345-handoff-mapping.html",
    "part3-local-vs-aws.html",
    "part3-hld-flow-notes.html",
    "part4-coding-overview.html",
    "part3-present.html",
    "part4-present.html",
    "part5-present.html",
    "developer-system-map.html",
}
SAFE_CLIP_RE = re.compile(r"^clips/[A-Za-z0-9][A-Za-z0-9._-]*\.mp4$")
VIDEO_OPEN_RE = re.compile(r"<video\b([^>]*)>", re.IGNORECASE)
VIDEO_SRC_RE = re.compile(r"""\bsrc\s*=\s*(['"])([^'"]+)\1""", re.IGNORECASE)
CLIP_REF_RE = re.compile(r"clips/[A-Za-z0-9][A-Za-z0-9._-]*\.mp4")
DIAGRAM_WRAP_RE = re.compile(r'(<div class="diagram-wrap"[^>]*>.*?</div>)', re.S)


def fail(message: str) -> None:
    print(f"fail-closed: {message}", file=sys.stderr)
    raise SystemExit(1)


def png_ihdr_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        fail(f"{path.relative_to(REPO)} is not a PNG")
    if data[12:16] != b"IHDR":
        fail(f"{path.relative_to(REPO)} missing PNG IHDR")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


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
                lang_tokens = code_lang.split()
                lang_name = lang_tokens[0].lower() if lang_tokens else ""
                lang_flags = {t.lower() for t in lang_tokens[1:]}
                if lang_name == "mermaid":
                    fit = "fit" in lang_flags
                    wrap_cls = "diagram-wrap diagram-fit" if fit else "diagram-wrap"
                    aria = "Stacked diagram" if fit else "Diagram"
                    safe = html.escape(body)
                    # Mermaid htmlLabels need a real <br>; keep the rest escaped.
                    safe = safe.replace("&lt;br/&gt;", "<br/>").replace("&lt;br&gt;", "<br>")
                    out.append(
                        f'<div class="{wrap_cls}" tabindex="0" role="region" '
                        f'aria-label="{html.escape(aria, quote=True)}">'
                        f'<pre class="mermaid">{safe}</pre>'
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
    mermaid.initialize({{ startOnLoad: true, theme: "neutral", securityLevel: "strict", flowchart: {{ useMaxWidth: true, wrappingWidth: 220, htmlLabels: true }} }});
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
        ".diagram-fit",
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
    if stack_at == -1 or ".diagram-wrap:not(.diagram-fit) .mermaid svg" not in css[stack_at:]:
        fail("767px query must keep wide mermaid swipeable at a readable min-width")
    if stack_at == -1 or ".diagram-wrap.diagram-fit .mermaid svg" not in css[stack_at:]:
        fail("767px query must fit compact mermaid at max-width 100%")
    mermaid_fit = css[stack_at:]
    fit_svg = mermaid_fit.find(".diagram-wrap.diagram-fit .mermaid svg")
    if fit_svg == -1 or "max-width: 100%" not in mermaid_fit[fit_svg : fit_svg + 180]:
        fail("compact mermaid svg must set max-width: 100% in the 767px query")
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
    if "wrappingWidth: 220" not in stack_html:
        fail("stack.html mermaid init must set wrappingWidth so labels wrap on phone")
    for mermaid_page in ("friday-plan.html", "presentation.html"):
        built = (OUT / mermaid_page).read_text(encoding="utf-8")
        if 'class="diagram-wrap"' not in built or 'class="mermaid"' not in built:
            fail(f"{mermaid_page} missing wrapped mermaid diagram")
    glossary = (OUT / "glossary.html").read_text(encoding="utf-8")
    if 'class="diagram-wrap diagram-fit"' not in glossary:
        fail("glossary.html status-word mermaid must use diagram-fit")
    if 'class="mermaid"' not in glossary:
        fail("glossary.html missing status-word mermaid")
    if "Yes: a command, HTTP GET, CI log, or committed file" in glossary:
        fail("glossary mermaid must not keep the long Yes edge label (clips on phone)")
    if "<br/>" not in glossary and "<br>" not in glossary:
        fail("glossary mermaid must use <br> so the status-word diamond wraps on phone")
    if "{&quot;Checked this" not in glossary and '{"Checked this' not in glossary:
        fail("glossary mermaid must keep the status-word diamond")
    # Ratchet #162: freeze.json why / how / scope on the glossary (not a DB menu).
    glossary_md = (ROOT / "glossary.md").read_text(encoding="utf-8")
    if "## freeze.json" not in glossary_md:
        fail("glossary.md must have a freeze.json section")
    for needle in (
        "**Purpose:**",
        "**How:**",
        "**Scope:**",
        "**Why not DB:**",
        "shared/freeze.json",
        "/api/menu",
        "/api/site",
        "/images/",
        "**not** in Postgres",
    ):
        if needle not in glossary_md:
            fail(f"glossary.md freeze.json entry must keep {needle}")
    if "reservations" not in glossary_md.lower() or "newsletter" not in glossary_md.lower():
        fail("glossary.md freeze.json entry must say Postgres holds reservations and newsletter")
    if "Aurora" in glossary_md:
        fail("glossary.md must not name another student's Aurora menu as ours")
    if 'class="diagram-wrap diagram-fit"' not in index:
        fail("index.html home mermaid must use diagram-fit")
    honesty_html = (OUT / "honesty.html").read_text(encoding="utf-8")
    if 'class="diagram-wrap diagram-fit"' not in honesty_html:
        fail("honesty.html status-word mermaid must use diagram-fit")
    if "{&quot;Checked this" not in honesty_html and '{"Checked this' not in honesty_html:
        fail("honesty.html mermaid must keep the status-word diamond")
    honesty_md = (ROOT / "honesty.md").read_text(encoding="utf-8")
    if "Do not say NFR-1 / NFR-2 **met**" not in honesty_md:
        fail("honesty.md lost the NFR-1 / NFR-2 not-met line")
    # Ratchet #123: NFR-1 met is the cited A36 Brave broadband cold Home.
    # Ratchet #125: NFR-2 met is the cited A36 Brave broadband reservation submit.
    coverage_md = (ROOT / "coverage.md").read_text(encoding="utf-8")
    for label, text in (("honesty.md", honesty_md), ("coverage.md", coverage_md)):
        if "Samsung A36" not in text:
            fail(f"{label} lost the Samsung A36 NFR-1 probe")
        if "Brave (not Chrome)" not in text:
            fail(f"{label} must name Brave (not Chrome) for the A36 NFR-1 take")
        if "466 ms" not in text:
            fail(f"{label} lost the A36 cold Home 466 ms")
        if "phonelink-a36-stopwatch.json" not in text:
            fail(f"{label} lost the cts-ai A36 NFR-1 report path (cite only)")
        if "233 ms" not in text:
            fail(f"{label} lost the A36 reservation submit 233 ms")
        if "phonelink-a36-submit2-stopwatch.json" not in text:
            fail(f"{label} lost the cts-ai A36 NFR-2 report path (cite only)")
        if "NFR-2 stays **Unknown**" in text:
            fail(f"{label} must not leave NFR-2 Unknown after the A36 submit probe")
        if "rog-device-stopwatch-issue-119.json" not in text:
            fail(f"{label} lost the separate ROG Wi-Fi evidence-note path")
    if "owner-claimed broadband" not in coverage_md:
        fail("coverage.md must say NFR-1 met is owner-claimed broadband + measured cold Home")
    if "Reservation confirmed. Table 27" not in coverage_md:
        fail("coverage.md lost the A36 NFR-2 success-frame cite")
    # Ratchet #127: home must not keep NFR-1 / NFR-2 stay Unknown after the A36 mets.
    index_md = (ROOT / "index.md").read_text(encoding="utf-8")
    if "NFR-1** / **NFR-2** stay **Unknown**" in index_md:
        fail("index.md must not say NFR-1 / NFR-2 stay Unknown after #123/#125")
    if "466 ms" not in index_md:
        fail("index.md lost the home NFR-1 466 ms cite")
    if "233 ms" not in index_md:
        fail("index.md lost the home NFR-2 233 ms cite")
    # Ratchet #131: home must not keep open #89 / Unknown to-be after #111.
    if "open [#89]" in index_md:
        fail("index.md must not call #89 open after that batch stayed CLOSED")
    if "/to-be.html` stays **Unknown**" in index_md:
        fail("index.md must not leave /to-be.html Unknown after #98/#111")
    if "to-be.md" not in index_md:
        fail("index.md lost the landed to-be page cite")
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
        'href="honesty.html"',
        'href="glossary.html"',
        'href="stack.html"',
        'href="future.html"',
        'href="index.html"',
        'href="journal.html"',
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
    shots_md = (ROOT / "must-film-shots.md").read_text(encoding="utf-8")
    if "Do-not-say checklist" not in shots_md:
        fail("must-film-shots.md lost the do-not-say checklist")
    if "<video" in shots_md:
        fail("must-film-shots.md must not embed clips (video-script keeps them)")
    if "hld-aws-staging.svg" not in stack_md:
        fail("stack.md must keep AWS staging HLD (hub is nav-only; do not hollow source pages)")
    meghna_md = (ROOT / "meghna-cafe-demo.md").read_text(encoding="utf-8")
    if "≥90s left" not in meghna_md:
        fail("meghna-cafe-demo.md happy-book extra must gate on ≥90s (do not start on 45s)")
    if "≥60s left" not in meghna_md:
        fail("meghna-cafe-demo.md newsletter extra must gate on ≥60s")
    # Ratchet #129: Talk cuts must not keep NFR-1 / NFR-2 Unknown after Coverage mets.
    presentation_md = (ROOT / "presentation.md").read_text(encoding="utf-8")
    if "NFR-1** / **NFR-2** stay **Unknown**" in presentation_md:
        fail("presentation.md must not say NFR-1 / NFR-2 stay Unknown after #123/#125")
    if "not claimed met" in presentation_md:
        fail("presentation.md must not keep NFR-1 / NFR-2 not-claimed-met after #123/#125")
    if "466 ms" not in presentation_md:
        fail("presentation.md lost the NFR-1 466 ms cite")
    if "233 ms" not in presentation_md:
        fail("presentation.md lost the NFR-2 233 ms cite")
    # Ratchet #133: Parts 3–5 keep silent + PROTOTYPE TTS; vo-notes stay site-relative.
    materials_345 = (ROOT / "parts-345-materials.md").read_text(encoding="utf-8")
    vo_notes = (ROOT / "parts-345-vo-notes.md").read_text(encoding="utf-8")
    for clip in (
        "clips/part3-variant-b-prototype-silent.mp4",
        "clips/part4-variant-c-prototype-silent.mp4",
        "clips/part5-shared-close-prototype-silent.mp4",
        "clips/part3-variant-b-prototype-vo.mp4",
        "clips/part4-variant-c-prototype-vo.mp4",
        "clips/part5-shared-close-prototype-vo.mp4",
    ):
        if clip not in materials_345:
            fail(f"parts-345-materials.md lost {clip}")
        clip_path = ROOT / clip
        if not clip_path.is_file():
            fail(f"missing {clip} (do not delete silent or VO clips)")
    if "PROTOTYPE TTS" not in materials_345 or "en-US-GuyNeural" not in materials_345:
        fail("parts-345-materials.md must label VO clips as PROTOTYPE TTS (en-US-GuyNeural)")
    if "not teammate" not in materials_345.lower() and "**not** teammate" not in materials_345:
        fail("parts-345-materials.md must say PROTOTYPE TTS is not teammate VO")
    if "Recorded teammate VO" not in materials_345 or "**Unknown**" not in materials_345:
        fail("parts-345-materials.md must keep recorded teammate VO Unknown")
    if "parts-345-vo-notes.md" not in materials_345:
        fail("parts-345-materials.md must link parts-345-vo-notes.md")
    if "/workspace/" in materials_345 or "/workspace/" in vo_notes:
        fail("Parts 3–5 materials/vo-notes must use site-relative paths (no /workspace/)")
    if "PROTOTYPE TTS" not in vo_notes or "en-US-GuyNeural" not in vo_notes:
        fail("parts-345-vo-notes.md must stay labeled PROTOTYPE TTS (en-US-GuyNeural)")
    if "Recorded teammate VO" not in vo_notes:
        fail("parts-345-vo-notes.md must keep recorded teammate VO Unknown")
    # Ratchet #139: natural spoken pack sits beside technical; mapping not spoken on camera.
    mapping_345 = (ROOT / "parts-345-handoff-mapping.md").read_text(encoding="utf-8")
    for clip in (
        "clips/part3-variant-b-prototype-vo-natural.mp4",
        "clips/part4-variant-c-prototype-vo-natural.mp4",
        "clips/part5-shared-close-prototype-vo-natural.mp4",
    ):
        if clip not in materials_345:
            fail(f"parts-345-materials.md lost natural clip {clip}")
        clip_path = ROOT / clip
        if not clip_path.is_file():
            fail(f"missing {clip} (do not delete natural VO clips)")
    if "Prefer natural" not in materials_345 and "prefer natural" not in materials_345:
        fail("parts-345-materials.md must prefer natural for camera")
    if "parts-345-handoff-mapping.md" not in materials_345:
        fail("parts-345-materials.md must link parts-345-handoff-mapping.md")
    if "PROTOTYPE TTS" not in materials_345 or "natural" not in materials_345:
        fail("parts-345-materials.md must label the natural pack as PROTOTYPE TTS natural")
    if "not spoken on camera" not in mapping_345.lower():
        fail("parts-345-handoff-mapping.md must say not spoken on camera")
    for name in (
        "part3-variant-b-script-natural.md",
        "part3-variant-b-voiceover-natural.md",
        "part4-variant-c-script-natural.md",
        "part4-variant-c-voiceover-natural.md",
        "part5-shared-close-script-natural.md",
        "part5-shared-close-voiceover-natural.md",
        "parts-345-handoff-mapping.md",
        "part3-local-vs-aws.md",
        "part3-hld-flow-notes.md",
        "part4-coding-overview.md",
        "developer-system-map.md",
        "quantic.md",
        "presentation.md",
        "quantic-handoff.md",
    ):
        text = (ROOT / name).read_text(encoding="utf-8")
        if "/workspace/" in text:
            fail(f"{name} must use site-relative paths (no /workspace/)")
        if "PARTS-345-HANDOFF-MAPPING.md" in text:
            fail(f"{name} must link parts-345-handoff-mapping.md (site-relative)")
        if "PART3-LOCAL-VS-AWS.md" in text:
            fail(f"{name} must link part3-local-vs-aws.md (site-relative)")
    presentation_md = (ROOT / "presentation.md").read_text(encoding="utf-8")
    quantic_md = (ROOT / "quantic.md").read_text(encoding="utf-8")
    handoff_md = (ROOT / "quantic-handoff.md").read_text(encoding="utf-8")
    for hub, label in (
        (presentation_md, "presentation.md"),
        (quantic_md, "quantic.md"),
        (handoff_md, "quantic-handoff.md"),
    ):
        if "part3-variant-b-script-natural.md" not in hub:
            fail(f"{label} must point speakers to the natural Part 3 script")
    if "parts-345-handoff-mapping.md" not in handoff_md:
        fail("quantic-handoff.md must link the Parts 3–5 handoff mapping")
    # Ratchet #141: MSAIE staging + architect deploy table on Stack; Pages-ready materials.
    local_vs_aws = (ROOT / "part3-local-vs-aws.md").read_text(encoding="utf-8")
    if "What was used" not in stack_md or "Explanation" not in stack_md:
        fail("stack.md must fold the local vs AWS table (what was used · explanation)")
    if "Rationale" not in stack_md or "Implementation" not in stack_md:
        fail("stack.md must fold the local vs AWS table (rationale · implementation)")
    if "73d202d" not in stack_md or "on-box Postgres" not in stack_md:
        fail("stack.md must keep the honest staging cut (on-box PG tip 73d202d)")
    if "not a shared RDS" not in stack_md:
        fail("stack.md must say MSAIE staging is not a shared RDS")
    if "part3-local-vs-aws.md" not in stack_md:
        fail("stack.md must link part3-local-vs-aws.md")
    if "store-only" not in stack_md and "Store-only" not in stack_md:
        fail("stack.md must keep newsletter store-only on the dual-env table")
    if "part3-local-vs-aws.md" not in materials_345:
        fail("parts-345-materials.md must link part3-local-vs-aws.md")
    if "MSAIE" not in materials_345 or "cafe.artof.link" not in materials_345:
        fail("parts-345-materials.md must keep MSAIE staging / cafe.artof.link wording")
    if "architecture why/how" not in materials_345.lower() and "Architecture why/how" not in materials_345:
        fail("parts-345-materials.md must keep the talk spine (architecture why/how)")
    if "UX/business" not in materials_345:
        fail("parts-345-materials.md must keep Part 2 UX/business on the talk spine")
    # Owner lock #143: same usecase, three depths (confirmed spine wording).
    for label, text in (
        ("stack.md", stack_md),
        ("parts-345-materials.md", materials_345),
        ("quantic.md", quantic_md),
    ):
        if "Same usecase, three depths" not in text:
            fail(f"{label} must keep the owner-locked Part 2→3→4 depth ladder")
        if "what Meghna shows" not in text:
            fail(f"{label} must say Part 2 UX = frontend view (what Meghna shows)")
        if "view behind it" not in text or "FE/BE flow" not in text:
            fail(f"{label} must say Part 3 Architecture = view behind it (HLDs + FE/BE flow)")
        if "how it is actually implemented" not in text:
            fail(f"{label} must say Part 4 Coding = how it is actually implemented")
        if "forms/functions/FE/BE/API/DB" not in text:
            fail(f"{label} must keep Part 4 as forms/functions/FE/BE/API/DB")
    if "behind the UX" not in stack_md:
        fail("stack.md must title Part 3 diagrams as behind the UX")
    if "implementation of that flow" not in stack_md:
        fail("stack.md must title Part 4 as implementation of that flow")
    if "UX/business" not in quantic_md:
        fail("quantic.md must cue Part 2 as UX/business why+how")
    if "part3-local-vs-aws.md" not in presentation_md:
        fail("presentation.md must point to part3-local-vs-aws.md")
    if "part3-local-vs-aws.md" not in handoff_md:
        fail("quantic-handoff.md must point to part3-local-vs-aws.md")
    # Ratchet #145: owner casting lock on Quantic / Parts 3–5 / talk pages.
    casting = "Meghna Part 2 UX · Claude Part 3 Architecture (Variant B) · Hiren Part 4 Coding (Variant C)"
    for label, text in (
        ("parts-345-materials.md", materials_345),
        ("quantic.md", quantic_md),
        ("presentation.md", presentation_md),
        ("quantic-handoff.md", handoff_md),
    ):
        if casting not in text:
            fail(f"{label} must stamp the owner casting lock")
        if "Claude or Hiren" in text:
            fail(f"{label} must not keep Claude or Hiren as an open speaker pick after #145")
        if "Hiren B vs C pick" in text or "Hiren B-vs-C lock" in text:
            fail(f"{label} must not keep the old Hiren B vs C Unknown after #145")
    # Ratchet #148: stamp Claude/Hiren Who on Part 3/4 NATURAL scripts (gap after #146).
    # Do not rewrite the #145 casting line. Do not reopen #145/#147.
    part3_natural = (ROOT / "part3-variant-b-script-natural.md").read_text(encoding="utf-8")
    part4_natural = (ROOT / "part4-variant-c-script-natural.md").read_text(encoding="utf-8")
    part3_vo_natural = (ROOT / "part3-variant-b-voiceover-natural.md").read_text(encoding="utf-8")
    part4_vo_natural = (ROOT / "part4-variant-c-voiceover-natural.md").read_text(encoding="utf-8")
    part3_tech = (ROOT / "part3-variant-b-script.md").read_text(encoding="utf-8")
    part4_tech = (ROOT / "part4-variant-c-script.md").read_text(encoding="utf-8")
    if "**Who:** **Claude** (owner lock 2026-09-06) — Architecture Part 3." not in part3_natural:
        fail("part3-variant-b-script-natural.md must lock Who to Claude")
    if "**Who:** **Hiren** (owner lock 2026-09-06) — Coding Part 4." not in part4_natural:
        fail("part4-variant-c-script-natural.md must lock Who to Hiren")
    if "**Who:** **Claude** (owner lock 2026-09-06) — Architecture Part 3." not in part3_vo_natural:
        fail("part3-variant-b-voiceover-natural.md must lock Who to Claude")
    if "**Who:** **Hiren** (owner lock 2026-09-06) — Coding Part 4." not in part4_vo_natural:
        fail("part4-variant-c-voiceover-natural.md must lock Who to Hiren")
    if "**Who:** **Claude** (owner lock 2026-09-06) — Architecture Part 3." not in part3_tech:
        fail("part3-variant-b-script.md must lock Who to Claude")
    if "**Who:** **Hiren** (owner lock 2026-09-06) — Coding Part 4." not in part4_tech:
        fail("part4-variant-c-script.md must lock Who to Hiren")
    for label, text in (
        ("part3-variant-b-script-natural.md", part3_natural),
        ("part4-variant-c-script-natural.md", part4_natural),
        ("part3-variant-b-voiceover-natural.md", part3_vo_natural),
        ("part4-variant-c-voiceover-natural.md", part4_vo_natural),
        ("part3-variant-b-script.md", part3_tech),
        ("part4-variant-c-script.md", part4_tech),
    ):
        if "Claude or Hiren" in text:
            fail(f"{label} must not keep Claude or Hiren as an open speaker pick after #148")
        if "the one not doing Architecture" in text:
            fail(f"{label} must not keep the open B-vs-C Who after #148")
        if "Hiren picks B vs C" in text:
            fail(f"{label} must not keep the Hiren B vs C pick after #148")
    if "MSAIE" not in local_vs_aws or "73d202d" not in local_vs_aws:
        fail("part3-local-vs-aws.md lost MSAIE staging or host tip 73d202d")
    # Ratchet #143: four Part 3/4 diagrams on Stack; notes site-relative; old HLDs stay archive.
    hld_notes = (ROOT / "part3-hld-flow-notes.md").read_text(encoding="utf-8")
    coding_notes = (ROOT / "part4-coding-overview.md").read_text(encoding="utf-8")
    for asset in (
        "hld-local.svg",
        "hld-local-720.png",
        "hld-aws-msaie.svg",
        "hld-aws-msaie-720.png",
        "flow-meghna-fe-be.svg",
        "flow-meghna-fe-be-720.png",
        "flow-coding-overview.svg",
        "flow-coding-overview-720.png",
    ):
        path = ROOT / "assets" / asset
        if not path.is_file():
            fail(f"missing knowledge/assets/{asset} (Part 3/4 diagram pack)")
        copied = OUT / "assets" / asset
        if not copied.is_file():
            fail(f"built site missing assets/{asset}")
    for label, text in (
        ("stack.md", stack_md),
        ("part3-hld-flow-notes.md", hld_notes),
    ):
        for needle in (
            "hld-local.svg",
            "hld-aws-msaie.svg",
            "flow-meghna-fe-be.svg",
        ):
            if needle not in text:
                fail(f"{label} must embed {needle}")
    if "flow-coding-overview.svg" not in stack_md:
        fail("stack.md must embed flow-coding-overview.svg")
    if "flow-coding-overview.svg" not in coding_notes:
        fail("part4-coding-overview.md must embed flow-coding-overview.svg")
    if "history / probe archive" not in stack_md:
        fail("stack.md must label older hld-as-is / hld-aws-staging as history / probe archive")
    if "hld-as-is.svg" not in stack_md:
        fail("stack.md must keep hld-as-is.svg as history (do not delete the archive HLD)")
    if "part3-hld-flow-notes.md" not in stack_md:
        fail("stack.md must link part3-hld-flow-notes.md")
    if "part4-coding-overview.md" not in stack_md:
        fail("stack.md must link part4-coding-overview.md")
    for label, text in (
        ("part3-hld-flow-notes.md", hld_notes),
        ("part4-coding-overview.md", coding_notes),
        ("stack.md", stack_md),
    ):
        if "/workspace/" in text:
            fail(f"{label} must use site-relative paths (no /workspace/)")
        if "PART3-HLD-FLOW-NOTES.md" in text or "PART4-CODING-OVERVIEW.md" in text:
            fail(f"{label} must use site-relative .md links (not ALL-CAPS pack names)")
        if "store-only" not in text and "Store-only" not in text:
            fail(f"{label} must keep newsletter store-only")
        if "/api/slots" not in text or "/api/reservations" not in text:
            fail(f"{label} must name GET /api/slots + POST /api/reservations for booking")
    if "MSAIE" not in hld_notes or "cafe.artof.link" not in hld_notes:
        fail("part3-hld-flow-notes.md must keep MSAIE staging / cafe.artof.link on camera")
    if "on-box Postgres" not in hld_notes and "on-box Postgres" not in stack_md:
        fail("Part 3 HLD notes or Stack must keep on-box Postgres")
    if "not a shared RDS" not in hld_notes and "not a shared RDS" not in stack_md:
        fail("Part 3 HLD notes or Stack must say not a shared RDS")
    # Ratchet #150: drop AEA RDS / aea-pilot-postgres from MSAIE-facing Knowledge pages.
    for name in (
        "stack.md",
        "part3-local-vs-aws.md",
        "part3-hld-flow-notes.md",
        "part3-variant-b-script.md",
        "part3-variant-b-voiceover.md",
        "part4-coding-overview.md",
        "developer-system-map.md",
        "parts-345-materials.md",
        "parts-345-handoff-mapping.md",
        "presentation.md",
        "honesty.md",
        "friday-plan.md",
        "future.md",
        "future/aws-schema-map.md",
    ):
        text = (ROOT / name).read_text(encoding="utf-8")
        if "AEA RDS" in text or "aea-pilot-postgres" in text:
            fail(f"{name} must not name AEA RDS / aea-pilot-postgres (use on-box Postgres / not a shared RDS)")
    if "PROTOTYPE" not in hld_notes or "PROTOTYPE" not in coding_notes:
        fail("Part 3/4 diagram notes must stay labeled PROTOTYPE")
    if "freeze" not in hld_notes.lower():
        fail("part3-hld-flow-notes.md must say static pages read the freeze")
    for hub, label in (
        (materials_345, "parts-345-materials.md"),
        (presentation_md, "presentation.md"),
        (quantic_md, "quantic.md"),
        (handoff_md, "quantic-handoff.md"),
        (local_vs_aws, "part3-local-vs-aws.md"),
    ):
        if "part3-hld-flow-notes.md" not in hub:
            fail(f"{label} must link part3-hld-flow-notes.md")
        if "part4-coding-overview.md" not in hub:
            fail(f"{label} must link part4-coding-overview.md")
    spoken_re = re.compile(r"“[^”]+”")
    for name in (
        "part3-variant-b-script-natural.md",
        "part3-variant-b-voiceover-natural.md",
        "part4-variant-c-script-natural.md",
        "part4-variant-c-voiceover-natural.md",
        "part5-shared-close-script-natural.md",
        "part5-shared-close-voiceover-natural.md",
    ):
        text = (ROOT / name).read_text(encoding="utf-8")
        for match in spoken_re.finditer(text):
            line_start = text.rfind("\n", 0, match.start()) + 1
            line_end = text.find("\n", match.end())
            line = text[line_start : line_end if line_end != -1 else None]
            if "avoid" in line.lower():
                continue
            if "weekend Lightsail" in match.group(0):
                fail(f"{name} spoken lines must not say weekend Lightsail on camera")
    # Ratchet #136: Future lists SES newsletter outbound #135; Coverage must not claim send.
    future_md = (ROOT / "future.md").read_text(encoding="utf-8")
    to_be_md = (ROOT / "to-be.md").read_text(encoding="utf-8")
    if "#135" not in future_md or "Amazon SES" not in future_md:
        fail("future.md must list Amazon SES newsletter outbound #135")
    if "store-only" not in future_md:
        fail("future.md must keep the SES grade floor as store-only")
    if "FR-19" not in future_md:
        fail("future.md must say SES outbound is not FR-19")
    if "#135" not in to_be_md:
        fail("to-be.md must keep the #135 SES Future pointer")
    if "Amazon SES" in coverage_md or re.search(r"#135\b", coverage_md):
        fail("coverage.md must not claim SES newsletter outbound (#135 is Future only)")
    # Ratchet #159: developer system map on Knowledge (stack, API, schema, FE/BE).
    map_md = (ROOT / "developer-system-map.md").read_text(encoding="utf-8")
    if "/workspace/" in map_md:
        fail("developer-system-map.md must use site-relative paths (no /workspace/)")
    if "73d202d" not in map_md:
        fail("developer-system-map.md must keep New Bot inventory tip 73d202d")
    if "Local (dev)" not in map_md or "Docker" not in map_md:
        fail("developer-system-map.md must name Local (dev) + Docker")
    if "cts-ai" in map_md:
        fail("developer-system-map.md must not name cts-ai as the product")
    if "on-box Postgres" not in map_md:
        fail("developer-system-map.md must keep on-box Postgres")
    if "not a shared RDS" not in map_md:
        fail("developer-system-map.md must say staging is not a shared RDS")
    if "AEA RDS" in map_md or "aea-pilot-postgres" in map_md:
        fail("developer-system-map.md must not name AEA RDS / aea-pilot-postgres")
    if "florist Path B" not in map_md:
        fail("developer-system-map.md must keep the no-florist-Path-B lock")
    if "Lily" in map_md:
        fail("developer-system-map.md must not name Lily's Florist")
    if "/api/gallery" not in map_md:
        fail("developer-system-map.md must name /api/gallery as missing")
    if "Does not exist" not in map_md and "does not exist" not in map_md:
        fail("developer-system-map.md must say /api/gallery does not exist")
    if "store-only" not in map_md:
        fail("developer-system-map.md must keep newsletter store-only")
    if "fail-closed" not in map_md.lower() and "Fail-closed" not in map_md:
        fail("developer-system-map.md must keep fail-closed")
    if "MSAIE" not in map_md:
        fail("developer-system-map.md must keep MSAIE staging camera wording")
    if "event bus" not in map_md.lower() and "HTTP only" not in map_md:
        fail("developer-system-map.md must say HTTP only / no event bus")
    if "/api/slots" not in map_md or "/api/reservations" not in map_md:
        fail("developer-system-map.md must name GET /api/slots + POST /api/reservations")
    if "@app.get" not in map_md or "@app.post" not in map_md:
        fail("developer-system-map.md must say routes are @app.get / @app.post")
    if "not Flask Blueprints" not in map_md and "not Flask Blueprint" not in map_md:
        fail("developer-system-map.md must say routes are not Flask Blueprints")
    if "developer-system-map.md" not in stack_md:
        fail("stack.md must link developer-system-map.md")
    if "developer-system-map.md" not in quantic_md:
        fail("quantic.md must link developer-system-map.md")
    if "developer-system-map.md" not in materials_345:
        fail("parts-345-materials.md must link developer-system-map.md")
    if "developer-system-map.md" not in handoff_md:
        fail("quantic-handoff.md must link developer-system-map.md")
    # Ratchet #165: Part 3 present uses SVG for architect diagrams; PNG-only beats stay >=1800px.
    present_md = (ROOT / "part3-present.md").read_text(encoding="utf-8")
    present_html = (OUT / "part3-present.html").read_text(encoding="utf-8")
    for svg in (
        "assets/flow-meghna-fe-be.svg",
        "assets/hld-local.svg",
        "assets/hld-aws-msaie.svg",
    ):
        if svg not in present_md:
            fail(f"part3-present.md must use {svg} (not the -720.png raster)")
        if svg not in present_html:
            fail(f"part3-present.html must reference {svg}")
    for raster in (
        "flow-meghna-fe-be-720.png",
        "hld-local-720.png",
        "hld-aws-msaie-720.png",
    ):
        if raster in present_md or raster in present_html:
            fail(f"part3-present must not use {raster}; use the matching .svg")
    if "still-reservation-720.png" in present_md or "still-reservation-720.png" in present_html:
        fail("part3-present must use still-reservation.png (2k), not still-reservation-720.png")
    for name in (
        "still-reservation.png",
        "fit-02-stack.png",
        "card-p3-boxes.png",
        "card-p3-sensors.png",
        "card-p3-staging.png",
        "card-p3-handoff.png",
    ):
        path = ROOT / "assets" / name
        if not path.is_file():
            fail(f"missing knowledge/assets/{name}")
        width, _height = png_ihdr_size(path)
        if width < 1800:
            fail(f"knowledge/assets/{name} must be >=1800px wide for 250% zoom (got {width})")
        copied = OUT / "assets" / name
        if not copied.is_file():
            fail(f"built site missing assets/{name}")
    msaie_svg = (ROOT / "assets" / "hld-aws-msaie.svg").read_text(encoding="utf-8")
    if "Out of cut" in msaie_svg or "Out of this cut" in msaie_svg:
        fail("hld-aws-msaie.svg must not show an Out of cut panel")
    if "AEA RDS" in msaie_svg or "aea-pilot-postgres" in msaie_svg:
        fail("hld-aws-msaie.svg must not name AEA RDS")
    if "on-box Postgres" not in msaie_svg:
        fail("hld-aws-msaie.svg must keep on-box Postgres")
    if "cafe.artof.link" not in msaie_svg:
        fail("hld-aws-msaie.svg must keep cafe.artof.link")
    # Ratchet #167: Part 3 present transition stills before each beat (recording splits).
    slides = (
        "slide-p3-00-title.svg",
        "slide-p3-01-boundaries.svg",
        "slide-p3-02-flow.svg",
        "slide-p3-03-deploys.svg",
        "slide-p3-04-quality.svg",
        "slide-p3-05-tradeoffs.svg",
        "slide-p3-06-handoff.svg",
        "slide-p3-07-teammate.svg",
    )
    last = -1
    for name in slides:
        path = ROOT / "assets" / name
        if not path.is_file():
            fail(f"missing knowledge/assets/{name}")
        copied = OUT / "assets" / name
        if not copied.is_file():
            fail(f"built site missing assets/{name}")
        needle = f"assets/{name}"
        if needle not in present_md:
            fail(f"part3-present.md must embed {needle}")
        pos = present_html.find(needle)
        if pos == -1:
            fail(f"part3-present.html must reference {needle}")
        if pos < last:
            fail(f"part3-present.html must keep transition stills in order (bad order at {name})")
        last = pos
    for before, after in (
        ("slide-p3-01-boundaries.svg", "still-reservation.png"),
        ("slide-p3-02-flow.svg", "flow-meghna-fe-be.svg"),
        ("slide-p3-03-deploys.svg", "hld-local.svg"),
        ("slide-p3-04-quality.svg", "card-p3-boxes.png"),
        ("slide-p3-05-tradeoffs.svg", "card-p3-staging.png"),
        ("slide-p3-06-handoff.svg", "card-p3-handoff.png"),
        ("slide-p3-06-handoff.svg", "slide-p3-07-teammate.svg"),
    ):
        if present_html.find(f"assets/{before}") > present_html.find(f"assets/{after}"):
            fail(f"part3-present.html must place {before} before {after}")
    teammate = (ROOT / "assets" / "slide-p3-07-teammate.svg").read_text(encoding="utf-8")
    if "teammate architecture" not in teammate:
        fail("slide-p3-07-teammate.svg must keep Hiren as teammate architecture")
    if "cafe.artof.link" not in teammate:
        fail("slide-p3-07-teammate.svg must keep cafe.artof.link")
    if "MSAIE staging" not in teammate:
        fail("slide-p3-07-teammate.svg must keep MSAIE staging")


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

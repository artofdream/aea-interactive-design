# Archify diagrams (Café Knowledge)

Documentation aids generated with [artofdream/archify](https://github.com/artofdream/archify) (fork of tt-a1i/archify). **Documented aid — not Live.** Same-origin host after Pages deploy: `https://knowledge.cafe.artof.link/archify/`.

Cite freeze-first / SRS MVP only (`docs/srs.md`, FR-1..18 / NFR-1..9). Do not invent FR-19 / NFR-10. Not Lily's Florist, Path B, 14 hats, 3DX Lab, or ctos QEMU content.

## Artifacts

| File | Kind | Topic |
|------|------|--------|
| [`cafe-knowledge-workflow.architecture.json`](./cafe-knowledge-workflow.architecture.json) + [`.html`](./cafe-knowledge-workflow.architecture.html) | architecture | Knowledge Pages ratchet: freeze → issue → PR → MRC COMMENT → New Bot → Pages → probe |
| [`index.html`](./index.html) | index | Thin listing of diagrams |

### Honesty

- Status wording: **Documented** aid (readable map). **Not Live.**
- Intended URLs after Pages deploy (ping-ready once parent probes post-merge):
  - `https://knowledge.cafe.artof.link/archify/`
  - `https://knowledge.cafe.artof.link/archify/cafe-knowledge-workflow.architecture.html`
  - `https://knowledge.cafe.artof.link/archify/cafe-knowledge-workflow.architecture.json`
- Do not claim Live / production status from this folder alone. A this-session HTTPS GET after merge closes the Pages probe.

### Open locally

```bash
xdg-open knowledge/archify/cafe-knowledge-workflow.architecture.html
# or: python3 -m http.server -d knowledge/archify 8765
```

### Regenerate

```bash
node /path/to/archify/bin/archify.mjs deliver architecture \
  knowledge/archify/cafe-knowledge-workflow.architecture.json \
  knowledge/archify/cafe-knowledge-workflow.architecture.html \
  --quality showcase
```

`knowledge/build.py` copies this directory to `_site/archify/` so GitHub Pages serves `/archify/`.

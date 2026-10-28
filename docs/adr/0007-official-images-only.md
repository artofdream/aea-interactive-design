# ADR-0007: Only the official four-image pack counts as official; student-recovered images are isolated and allowlisted

## Status

Accepted (retroactive, recorded 2026-10-07)

## Date

2026-08-31: the images were isolated and the pack hash pinned (PR #1), and the MVP served only official images (PR #9). 2026-09-05: the Menu allowlist was added (PR #71).

## Context

FR-3 asks for high-quality images and a consistent theme. FR-12 asks for a gallery covering the interior, menu dishes and special or behind-the-scenes events. The official Quantic image pack is a zip that contains exactly four webp files. Seventeen more images were recovered by filename from a public student mirror. They are not in the official zip.

## Decision

- The four official webps live in `assets/images/`. The zip and its SHA256 are pinned in CI ([ADR-0005](0005-srs-freeze-fail-closed-ci.md)) and documented in `assets/images/PROVENANCE.md`.
- The 17 student-recovered files live in `assets/images/supplemental-not-official/` with their own `PROVENANCE.md`. They are never presented as course-official.
- Flask's `/images/<file>` serves by **basename allowlist** only: the four official images (`freeze.officialImages`) plus the files that `shared/menu-presentation.json` maps as `student-recovered` for the Menu page. Nested paths and unmapped supplemental files return 404.
- The Gallery and Home pages use `freeze.officialImages`. `menu-presentation.json` never carries prices. Menu items with no image get a placeholder.

## Consequences

- The provenance of every image shown is auditable, and nothing unofficial passes as official.
- The gallery has only four images to cover FR-12's three categories.
- Showing another image means changing the allowlist JSON and passing `test_official_and_allowlisted_menu_images_served_unused_supplemental_blocked` and `test_frontend_does_not_reference_unmapped_supplemental_files`.

## Related requirements

Related requirements: FR-3, FR-12

## Evidence

- `e49f40c` docs: pin official PDF/zip SHA256 and isolate supplemental images (PR #1).
- `5603d85` feat: implement Café Fausse restaurant MVP (#7) (PR #9): official images only, with supplemental files not served.
- `566e400` feat(app): menu images, nav icons, and readable viewports (#68) (PR #71): `shared/menu-presentation.json` and the Menu allowlist.

## OPEN

- OPEN: The license or reuse terms of the 17 student-recovered images are not recorded. `PROVENANCE.md` records only where they came from.

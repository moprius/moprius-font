# Moprius Font Family — Audit Results

**Status: PASS**

Desktop fonts: 12

## Families

- Moprius Sans: 4 styles
- Moprius Mono: 4 styles
- Moprius Serif: 4 styles

## Checks

- Opened all TTF and OTF desktop fonts with FontTools.
- Verified all matching WOFF2 files and semantic cmap/glyph parity.
- Verified family/style naming, weight flags and embedding permissions.
- Verified Portuguese and publishing punctuation coverage.
- Verified fixed 600-unit width behavior in Moprius Mono.
- Rendered smoke-test text with RAQM/Pillow.
- Recompiled all TTX sources.
- Ran Fontconfig and subsetting smoke tests when available.

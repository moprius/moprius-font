# Moprius Fonts

Moprius is a two-family type system for desktop interfaces, long-form reading, terminals and source code.

- **Moprius Sans** — proportional family for UI and reading.
- **Moprius Mono** — monospaced family with a fixed 600-unit advance width for spacing glyphs.
- Styles: Regular, Italic, Bold and Bold Italic.
- Current font version: **1.437**.
- Formats: TTF and WOFF2.
- License: SIL Open Font License 1.1.

![Moprius specimen](specimen/Moprius-Specimen.png)

## Important naming note

Earlier development builds used the name “Moprius Source”. The public family names are now **Moprius Sans** and **Moprius Mono** because **Source** is a Reserved Font Name in the Adobe upstream license. The word “Source” is retained only in factual upstream attribution.

## Install on Linux

```bash
mkdir -p ~/.local/share/fonts/Moprius
cp fonts/ttf/*.ttf ~/.local/share/fonts/Moprius/
fc-cache -f
```

## Web use

Include `css/moprius.css`, then use `Moprius Sans` for text and `Moprius Mono` for code.

## Build

The `sources/ttx/` directory contains XML sources for all static fonts. Rebuild with:

```bash
python tools/build.py
```

## Coverage

Each font contains 1,216 glyphs and 1,183 mapped Unicode characters, including Latin Extended, Greek, Cyrillic, technical symbols, arrows, box drawing, Powerline separators and a project logo at `U+E000`.

## Upstream and license

Moprius is a Modified Version derived from OFL-licensed upstream work including Adobe Source Sans and Fantasque Sans Mono. Exact notices are preserved in `OFL.txt`, `LEGAL-NOTICES.md` and the embedded font metadata. Moprius is not endorsed by the upstream authors.

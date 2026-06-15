# Moprius Serif — Audit Results

Version: 1.000

## Status

**PASS — no blocking errors found.**

## Font files

| File | Glyphs | Unicode mappings | Style | Space | Italic angle |
|---|---:|---:|---|---:|---:|
| `MopriusSerif-Regular.otf` | 1414 | 907 | Regular | 245 | 0.0 |
| `MopriusSerif-Italic.otf` | 551 | 420 | Italic | 245 | -12.0 |
| `MopriusSerif-Bold.otf` | 1414 | 907 | Bold | 245 | 0.0 |
| `MopriusSerif-BoldItalic.otf` | 551 | 420 | Bold Italic | 245 | -12.0 |

## Checks performed

- OTF load, save and reopen with FontTools.
- WOFF2 load and semantic comparison.
- Public family, subfamily, full and PostScript names.
- Reserved name exclusion from user-facing primary names.
- CFF FontName, FamilyName and FullName consistency.
- OS/2 weight, style flags, embedding permissions, vendor ID and typographic metrics.
- Portuguese and common publishing punctuation coverage in all four styles.
- Consistent U+0020 and U+00A0 word-space advance widths.
- Fontconfig recognition.
- Pillow rasterization smoke test.
- FontTools subsetting with all layout features.
- TTX source import and binary round trip.
- Preservation of GSUB/GPOS OpenType feature tables.

## Coverage note

The upright styles inherit the broader Source Serif Pro character set. The italic styles inherit the Latin-focused italic set from the licensed base files available for this build. Portuguese, Western European text, publishing punctuation and the intended long-form reading use are covered in all four styles.

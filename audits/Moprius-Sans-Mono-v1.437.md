# Final audit result

Status: **PASS** after the v1.437 publication corrections.

Validated across all eight styles:

- 1,216 glyphs and 1,183 Unicode mappings per font;
- identical glyph order and character coverage;
- family/style naming, weight bits, italic bits and PostScript names;
- copyright, OFL metadata and unrestricted embedding (`fsType = 0`);
- fixed 600-unit advance width in Moprius Mono;
- glyph bounds within declared vertical metrics;
- no missing composite components;
- rendering of every mapped character at 8, 12, 16 and 32 px;
- NFC/NFD advance consistency for Latin, Vietnamese, Greek and Cyrillic samples;
- TTF/WOFF2 semantic parity;
- TTX rebuild round-trip;
- FontTools subsetting smoke tests;
- Fontconfig scanning;
- absence of stale TrueType hint-program values.

Publication corrections found in the final audit:

1. `Source` was being used in the public family name despite being an Adobe Reserved Font Name.
2. Upstream copyright statements were absent from the embedded copyright field and package header.
3. The project logo used `U+F8FF`, a PUA position widely associated with the Apple logo.
4. The unhinted fonts retained obsolete TrueType VM maxima in the `maxp` table.

All four points are corrected by `finalize_moprius.py`.

#!/usr/bin/env python3
from pathlib import Path
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "ttx"
TTF = ROOT / "fonts" / "ttf"
OTF = ROOT / "fonts" / "otf"
WOFF = ROOT / "fonts" / "woff2"
for d in (TTF, OTF, WOFF): d.mkdir(parents=True, exist_ok=True)

for xml in sorted(SRC.glob("*.ttx")):
    font = TTFont(recalcTimestamp=False)
    font.importXML(xml)
    is_cff = "CFF " in font or "CFF2" in font
    out = (OTF if is_cff else TTF) / (xml.stem + (".otf" if is_cff else ".ttf"))
    font.save(out, reorderTables=True)
    font.flavor = "woff2"
    font.save(WOFF / (xml.stem + ".woff2"), reorderTables=True)
    font.close()
    print(f"Built {out.name} and {xml.stem}.woff2")

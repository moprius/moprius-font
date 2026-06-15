#!/usr/bin/env python3
from pathlib import Path
from fontTools.ttLib import TTFont
from PIL import ImageFont
import tempfile, subprocess, shutil, sys, json

ROOT = Path(__file__).resolve().parents[1]
DESKTOP = sorted((ROOT/'fonts/ttf').glob('*.ttf')) + sorted((ROOT/'fonts/otf').glob('*.otf'))
WOFF = ROOT/'fonts/woff2'
SOURCES = ROOT/'sources/ttx'
EXPECTED = {
    'Moprius Sans': 4,
    'Moprius Mono': 4,
    'Moprius Serif': 4,
}
errors=[]; notes=[]; rows=[]

def err(s): errors.append(s)
def names(font, nid):
    vals=[]
    for n in font['name'].names:
        if n.nameID==nid:
            try: v=n.toUnicode()
            except Exception: continue
            if v not in vals: vals.append(v)
    return vals

def cmap(font):
    d={}
    for t in font['cmap'].tables:
        if t.isUnicode(): d.update(t.cmap)
    return d

if len(DESKTOP)!=12: err(f'Expected 12 desktop fonts, found {len(DESKTOP)}')
counts={k:0 for k in EXPECTED}
for p in DESKTOP:
    try: f=TTFont(p, recalcBBoxes=True, recalcTimestamp=False, checkChecksums=2)
    except Exception as e: err(f'{p.name}: cannot open: {e}'); continue
    fams=names(f,1); family=fams[0] if fams else ''
    if family not in EXPECTED: err(f'{p.name}: unexpected family {family!r}')
    else: counts[family]+=1
    public=' '.join(names(f,1)+names(f,2)+names(f,4)+names(f,6)+names(f,16)+names(f,17))
    if 'Moprius Source' in public: err(f'{p.name}: obsolete public family name present')
    if f['OS/2'].fsType != 0: err(f'{p.name}: embedding restriction fsType={f["OS/2"].fsType}')
    cm=cmap(f)
    required='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÁÂÃÇÉÊÍÓÔÕÚÜàáâãçéêíóôõúü0123456789“”‘’—–…€'
    missing=[c for c in required if ord(c) not in cm]
    if missing: err(f'{p.name}: missing required chars {missing}')
    style=(names(f,2) or [''])[0]
    bold='Bold' in style; italic='Italic' in style
    if f['OS/2'].usWeightClass != (700 if bold else 400): err(f'{p.name}: weight mismatch')
    if bool(f['head'].macStyle & 1)!=bold: err(f'{p.name}: macStyle bold mismatch')
    if bool(f['head'].macStyle & 2)!=italic: err(f'{p.name}: macStyle italic mismatch')
    if family=='Moprius Mono':
        if not f['post'].isFixedPitch: err(f'{p.name}: Mono not fixed pitch')
        bad=[(g,w) for g,(w,lsb) in f['hmtx'].metrics.items() if w not in (0,600)]
        if bad: err(f'{p.name}: non-600 Mono widths {bad[:5]}')
    # Render smoke test
    try:
        pf=ImageFont.truetype(str(p), 20, layout_engine=ImageFont.Layout.RAQM)
        for text in ('Moprius ação ciência órgão útil 0123456789', 'Italic Bold → ∑ {} [] ()'):
            pf.getmask(text)
    except Exception as e: err(f'{p.name}: render failed: {e}')
    # WOFF2 parity
    wp=WOFF/(p.stem+'.woff2')
    if not wp.exists(): err(f'{p.name}: missing {wp.name}')
    else:
        try:
            w=TTFont(wp)
            if w.getGlyphOrder()!=f.getGlyphOrder() or cmap(w)!=cm: err(f'{wp.name}: semantic mismatch')
            w.close()
        except Exception as e: err(f'{wp.name}: cannot open: {e}')
    # Fontconfig smoke test
    if shutil.which('fc-scan'):
        r=subprocess.run(['fc-scan','--format=%{family}|%{style}\n',str(p)],capture_output=True,text=True)
        if r.returncode or family not in r.stdout: err(f'{p.name}: fc-scan failed')
    rows.append({'file':p.name,'family':family,'style':style,'glyphs':len(f.getGlyphOrder()),'unicode':len(cm)})
    f.close()

for fam,n in EXPECTED.items():
    if counts[fam]!=n: err(f'{fam}: expected {n} styles, found {counts[fam]}')

# TTX round-trip
with tempfile.TemporaryDirectory() as td:
    td=Path(td)
    for xml in sorted(SOURCES.glob('*.ttx')):
        try:
            f=TTFont(recalcTimestamp=False); f.importXML(xml)
            ext='.otf' if ('CFF ' in f or 'CFF2' in f) else '.ttf'
            out=td/(xml.stem+ext); f.save(out,reorderTables=True); f.close()
            TTFont(out).close()
        except Exception as e: err(f'{xml.name}: round-trip failed: {e}')

# Subset smoke test
if shutil.which('pyftsubset'):
    with tempfile.TemporaryDirectory() as td:
        for p in DESKTOP:
            out=Path(td)/(p.stem+p.suffix)
            r=subprocess.run(['pyftsubset',str(p),f'--output-file={out}','--text=Hello Moprius ação ciência Καλημέρα Привет','--layout-features=*'],capture_output=True,text=True)
            if r.returncode or not out.exists(): err(f'{p.name}: subset failed: {r.stderr.strip()}')
else: notes.append('pyftsubset unavailable')

result={'status':'PASS' if not errors else 'FAIL','desktop_fonts':len(DESKTOP),'families':counts,'errors':errors,'notes':notes,'fonts':rows}
print(json.dumps(result,indent=2,ensure_ascii=False))
sys.exit(1 if errors else 0)

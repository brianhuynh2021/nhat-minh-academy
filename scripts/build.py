#!/usr/bin/env python3
"""Build a standalone static site and a deployable zip without dependencies."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text(encoding='utf-8')
css = (root / 'assets/styles.css').read_text(encoding='utf-8')
marker = '<link rel="stylesheet" href="assets/styles.css">'
if html.count(marker) != 1:
    raise SystemExit('Expected one stylesheet link in index.html')
bundled = html.replace(marker, '<style>\n' + css + '</style>')
out = root / 'dist'
out.mkdir(exist_ok=True)
(out / 'index.html').write_text(bundled, encoding='utf-8')
with ZipFile(out / 'nhat-minh-academy.zip', 'w', ZIP_DEFLATED) as archive:
    archive.writestr('index.html', bundled)
print('Built dist/index.html and dist/nhat-minh-academy.zip')

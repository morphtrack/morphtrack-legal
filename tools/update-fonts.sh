#!/usr/bin/env bash
# Refresh the self-hosted webfonts in fonts/ from the Google Fonts CSS2 API.
#
# The landing inlines its @font-face rules (see the top of the <style> block in
# index.html) and serves the .woff2 files itself, so there is no third-party
# font origin and no render-blocking font stylesheet. Run this only when the
# family/weight list changes — then paste the regenerated rules from
# build/fonts.css over the inlined block in index.html.
#
#   ./tools/update-fonts.sh
set -euo pipefail

cd "$(dirname "$0")/.."

# Keep this in sync with the inlined @font-face block.
FAMILIES="family=IBM+Plex+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap"
# The site is EN/RU — greek/vietnamese subsets are deliberately not shipped.
SUBSETS="latin latin-ext cyrillic cyrillic-ext"
# A modern desktop UA is what makes the API serve woff2 rather than ttf.
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

mkdir -p build fonts
curl -sSf -A "$UA" "https://fonts.googleapis.com/css2?${FAMILIES}" -o build/google-fonts.css

SUBSETS="$SUBSETS" node - <<'NODE'
const fs = require('fs');
const css = fs.readFileSync('build/google-fonts.css', 'utf8');
const keep = process.env.SUBSETS.split(/\s+/).filter(Boolean);
const out = [], dl = [];
for (const b of css.matchAll(/\/\* ([a-z-]+) \*\/\s*@font-face \{([\s\S]*?)\}/g)) {
  const [, subset, body] = b;
  if (!keep.includes(subset)) continue;
  const fam = (body.match(/font-family:\s*'([^']+)'/) || [])[1];
  const wt = (body.match(/font-weight:\s*(\d+)/) || [, '400'])[1];
  const st = (body.match(/font-style:\s*(\w+)/) || [, 'normal'])[1];
  const url = (body.match(/url\((https:\/\/fonts\.gstatic\.com\/[^)]+)\)/) || [])[1];
  const range = (body.match(/unicode-range:\s*([^;]+);/) || [])[1];
  if (!fam || !url) { console.error('skipping malformed block:', subset); continue; }
  const name = `${fam.replace(/\s+/g, '')}-${wt}-${st}-${subset}.woff2`;
  dl.push(`${url}|${name}`);
  out.push(`@font-face{font-family:"${fam}";font-style:${st};font-weight:${wt};` +
    `font-display:swap;src:url(fonts/${name}) format("woff2");unicode-range:${range};}`);
}
fs.writeFileSync('build/dl.txt', dl.join('\n') + '\n');
fs.writeFileSync('build/fonts.css', out.join('\n') + '\n');
console.log(`${out.length} @font-face rules -> build/fonts.css`);
NODE

while IFS='|' read -r url name; do
  [ -n "$url" ] && curl -sSf "$url" -o "fonts/$name"
done < build/dl.txt

# A truncated or error-page download would silently break the page.
for f in fonts/*.woff2; do
  head -c 4 "$f" | grep -q 'wOF2' || { echo "ERROR: $f is not a valid woff2" >&2; exit 1; }
done

echo "fonts/ now holds $(ls fonts/*.woff2 | wc -l | tr -d ' ') files"
echo "Now paste build/fonts.css over the inlined @font-face block in index.html."

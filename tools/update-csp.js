#!/usr/bin/env node
/**
 * Rewrite the CSP meta tag's script-src hashes in index.html.
 *
 * The policy allows inline <script> blocks by SHA-256 hash rather than
 * 'unsafe-inline' (which Lighthouse flags as an ineffective CSP). That means
 * ANY edit to an inline script — including the JSON-LD blocks — invalidates its
 * hash and the browser silently stops executing it.
 *
 * Run this after editing any inline script:
 *   node tools/update-csp.js
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const FILE = path.join(__dirname, '..', 'index.html');
const html = fs.readFileSync(FILE, 'utf8');

// Every script element WITHOUT a src attribute — CSP's script-src governs
// these, whatever their type (JSON-LD included). HTML comments are stripped
// first (by blanking them, so offsets stay put): a commented-out or merely
// *mentioned* tag is not executed, and counting it would hash the wrong bytes.
const scannable = html.replace(/<!--[\s\S]*?-->/g, (c) => ' '.repeat(c.length));
const inline = [...scannable.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)];
const hashes = inline.map(
  (m) => `'sha256-${crypto.createHash('sha256').update(m[1], 'utf8').digest('base64')}'`,
);

if (hashes.length === 0) {
  console.error('No inline scripts found — refusing to write an empty script-src.');
  process.exit(1);
}

// Swap just the hash list inside script-src, leaving the rest of the policy
// (host allowlists, other directives) exactly as authored.
const HASH_LIST = /(content="[^"]*script-src 'self' )('sha256-[^']*'(?: 'sha256-[^']*')*)( )/;

if (!HASH_LIST.test(html)) {
  console.error('CSP script-src hash list not found in index.html — not modified.');
  process.exit(1);
}

const updated = html.replace(
  HASH_LIST,
  (_full, head, _old, tail) => `${head}${hashes.join(' ')}${tail}`,
);

// Already current is success, not failure — this script is safe to re-run.
if (updated === html) {
  console.log(`CSP already up to date (${hashes.length} inline-script hashes).`);
  process.exit(0);
}

fs.writeFileSync(FILE, updated);
console.log(`Updated CSP with ${hashes.length} inline-script hashes:`);
hashes.forEach((h, i) => console.log(`  #${i + 1} ${h}`));

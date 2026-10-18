# MorphTrack website and legal documents

Source for [www.morphtrack.app](https://www.morphtrack.app/). Despite the repository name, this contains the landing page as well as legal documents. GitHub Pages publishes the root of `main` with Jekyll after each push.

## Where to edit

| Path | Purpose |
| --- | --- |
| `v2/`, `v2/ru/` | Current English and Russian Privacy Policy, Terms, Health Data Policy, deletion instructions and support. `/v2` is a stable URL prefix, not a requirement to maintain two active policies. |
| `v1/privacy-policy.md`, `v1/terms.md` | Historical documents. Keep readable, labelled as superseded and `noindex`. Do not rewrite their historical promises. |
| `archive/` | Prior published revisions of the current documents, with archive notices and links back to the current versions. |
| Root legal pages, `support.html`, `v1/delete-account.md`, `v2/index.html` | Compatibility redirects. Old app and store links depend on these addresses. |
| `src/page.html` | Landing-page source, styles and translation dictionary. Edit here. Excluded from the public site. |
| `index.html`, `ru/index.html` | Generated English and Russian landing pages. Commit both: GitHub Pages does not run the Python generator. |
| `_layouts/default.html` | Shared legal-page layout and navigation. |
| `tools/` | Landing generator, checks, CSP updater and optional font refresh. Not published. |
| `img/`, `fonts/`, `vendor/lenis-1.1.14.min.js` | Assets used by the landing pages. |
| `go/` | App Store / Google Play download redirects. |
| `CNAME`, `_config.yml`, `robots.txt`, `sitemap.xml` | Custom domain, publication rules and search indexing. |
| `google*.html` | Google ownership verification. Retain unless the corresponding Search Console/OAuth verification is confirmed obsolete. |

`_drafts/` contains local working notes only. It is ignored by Git and excluded from Jekyll. It is not a place to publish internal operational details or account data. `build/` holds disposable font-generation output.

## Update the landing

```sh
python3 tools/build-pages.py
node tools/update-csp.js index.html
node tools/update-csp.js ru/index.html
python3 tools/test_build_pages.py
git diff --check
```

Run these after editing `src/page.html` or the generator. The CSP hashes must match the generated inline scripts. `tools/update-fonts.sh` is only needed when changing font families or weights; do not run it for routine text edits.

## Publish legal changes

1. Check the wording against the deployed service and applicable requirements. A policy update does not deploy features, obtain consent, prove legal compliance or notify existing account holders by itself.
2. Update both languages and the actual publication/update date. Preserve the prior published Privacy Policy and Terms in `archive/`, retaining their original dates and marking them `noindex`.
3. Keep all existing legal URLs working. Link new pages from both landing-page footers and the legal layout. Only current canonical pages belong in `sitemap.xml`.
4. Check internal links, layout, generated pages and the Git diff. Commit only publication files; do not add local `_drafts/` material.
5. Push `main`, wait for the GitHub Pages build to succeed, then check the live pages, both languages, archive links and old redirects. Confirm that source/build files return 404.

Substantive Terms changes for existing accounts still require the applicable notice/agreement process. Publishing the site does not silently replace accepted terms or collect new health-data consent.

# MorphTrack landing page — design & build brief

Recreate the MorphTrack marketing landing page exactly as specified below. One self-contained HTML file, no frameworks, no build step. All motion is CSS transitions/animations driven by small vanilla-JS class toggles or scroll math.

Assets: use the 10 phone screenshots from `screens-for-site/` (status bars already cropped). Reference them as `assets/screen-*.png`. Photos of the model for the animated compare screen: two shots of the SAME person in the SAME framing (`assets/journey-5.png`, `assets/journey-9.png`), otherwise the slider seam looks broken.

---

## 1. Design system

**Tokens** (CSS custom properties on `:root`, oklch):

```
--bg oklch(0.978 0.004 250)      page background
--elev #fff                      cards, phone screens
--surface oklch(0.955 0.005 250) inset chips, segmented controls
--ink oklch(0.17 0.005 250)      primary text, dark blocks, CTA
--inkSoft oklch(0.34 0.006 250)  body copy
--muted oklch(0.56 0.006 250)    labels, meta
--border oklch(0.88 0.006 250)   dividers
--soft oklch(0.93 0.005 250)     card borders
--accent oklch(0.40 0.180 270)   indigo — links, charts, badges
--accentSoft oklch(0.94 0.026 265)
--plum oklch(0.45 0.12 320)      link hover
--green oklch(0.52 0.12 150)     "helping" state
--greenSoft oklch(0.95 0.03 150)
--tint oklch(0.945 0.028 280)    hero + footer wash (lavender)
--tintWarm oklch(0.96 0.02 70)   warm panel wash
```

**Type**
- UI/body: `"Helvetica Neue", Helvetica, system-ui, sans-serif`, antialiased.
- Accent italic: **Instrument Serif** italic 400, only inside `em.ser`, coloured `--accent`, used for the last phrase of most headings.
- Mono: **IBM Plex Mono** — eyebrows (12.5px, `letter-spacing:.18em`, uppercase), dates, counters, in-screen labels.
- `h1` `clamp(40px,5vw,70px)`, `line-height:1.02`, `letter-spacing:-.032em`, weight 700, `text-wrap:balance`.
- `h2` `clamp(28px,3.1vw,42px)`, `line-height:1.06`, `letter-spacing:-.026em`, weight 700.
- `.lead` 19px / 1.55, `--inkSoft`, `text-wrap:pretty`.

**Shape & depth**
- Radii: cards 20–22px, panels 28px, phone frames 40px, pills 999px, in-screen cards 16px.
- Shadows are wide, soft, low-opacity only: `0 24px 50px -34px oklch(0.17 0.02 260/.32)` for cards, `0 40px 80px -34px oklch(0.17 0.02 260/.42)` for phones. No hard drop shadows, no gradients on text, no emoji.
- Links: define `a` = `--accent`, `a:hover` = `--plum`.

**Layout**
- `.wrap` max-width 1240px, side padding 40px.
- Sections `padding:92px 0`; feature sections are a 2-column grid `minmax(0,1fr) minmax(0,1fr)` with `gap:72px`, alternating sides via a `.flip` class.
- Below 1080px: everything collapses to one column, nav links hide, the hero fan becomes a horizontally scrollable row.

---

## 2. Page structure (in order)

### Sticky header
Logo (34px rounded-square mark with a purple sphere + "MorphTrack" 21px/700) · nav links `What you can track / AI analysis / Privacy / FAQ` · EN|RU pill toggle (active = black pill) · black pill CTA "Get the app". Background `oklch(0.978 0.004 250/.86)` + `backdrop-filter:blur(12px)`, 1px bottom border.

### Hero — centred, lavender wash
Gradient `--tint → oklch(0.955 0.018 275) → --bg`, top-down.
1. Mono eyebrow: `Skin · acne · posture · body · hair`
2. H1: **Know what's worth your time — *before you waste months on it*.** (italic serif tail)
3. Lead, max 34em, centred: photograph what you're changing, tick off the routine, the AI reading says what moved and which habit moved it.
4. Two store buttons: black `border-radius:14px`, small "Download on the / Get it on" line + 18px bold store name, Apple + coloured Google Play glyph. Hover: `translateY(-2px)`, opacity .92.
5. **Phone fan** — five frames overlapping, centre one in focus:
   - widths 214px, `margin:0 -22px`
   - rotations/offsets: `-9deg/+46px/scale .9`, `-4.5deg/+18px/.96`, centre `translateY(-14px) scale(1.06)` and highest z-index, then mirrored `+4.5deg`, `+9deg`
   - contents left→right: photos-by-month · calendar · AI analysis · compare · connections+trend
6. Mono caption row under the fan naming each screen.

### Feature section 1 — "Track anything · free" (text left, screen right)
Eyebrow `Track anything · free`, H2 **Every habit you want to watch — *no limits*.**, lead about 8-second photos and 5-second routine ticks, then a chip cloud of real factors (Azelaic acid, Retinol, SPF 50, Dermatologist visit, Sleep 7 h+, Cycle day, Dairy-free, Gym, Evening stretching, Water 2 l) ending with a dashed chip `+ your own, unlimited`, then an accent pill: **Unlimited factors · unlimited photos · free**.
Screen: the calendar screen in a phone frame on a tinted panel (`.shot`, radius 28px, lavender gradient, phone width 252px).

### Feature section 2 — "Photos & compare" (flipped: text left, screens right, warm panel)
H2 **Every photo you take, *side by side*.** Lead: shoot as often as you like, photos group by month and tracker; pick any two dates — slider, side-by-side or overlay, aligned by angle and framing. Bulleted checklist (indigo check icons): three modes · any two dates · shot guide repeats angle and light · unlimited photos grouped by month.
Screens: **two phones** — the photos-grid screenshot sits behind (`position:absolute`, `rotate(-10deg)`, ~85% of the front phone's height, offset left) and the **animated compare screen** in front (`translateX(74px)`, higher z-index). Keep ~2/3 of the back phone visible.

### Feature section 3 — "AI reading" (`id="analysis"`, text left, screens right)
H2 **What changed — and *what changed it*.** Lead: comparable photos read zone by zone, result lined up against logged factors (helping / no clear effect / possibly hurting), whole category plotted as one trend line. Bullets: zone by zone · factor influence · plain words, never a beauty score · progress as one line, dips explained.
Screens: duo again — connections+trend screen behind (rotated, left), the AI-analysis screenshot in front. Any text on the back phone must fit its visible left ~60%; cap in-screen text blocks with `max-width:60%` so nothing is cut by the front phone.

### Free-tracking band — dark
Full-width `--ink` block, two columns: left eyebrow `The part nobody else gives you` + H2 **Routine tracking stays *free and unlimited*.** (italic tail in `oklch(0.82 0.11 292)`); right paragraph — add a hundred factors if the treatment needs it; photos, comparisons and calendar are free; you only pay for extra AI readings. Chip row on dark: No slot limits · No per-tracker fees · No ads · No data selling · dashed `Yes, really`.

### Privacy
Two columns, light. Eyebrow `Private by default`, H2 **Photos of your face deserve *real* rules.** Four green-check list items: stored in the EU, encrypted, visible only to you · location and EXIF stripped on upload · never sold, never used to train AI, no ads or analytics SDKs · delete everything in one tap.

### FAQ
Eyebrow `Straight answers`, H2 **Before you download.** Five `<details>` rows with 1px top borders, `+ / –` markers on the right, first one open: what you actually get · is it free (photos, comparisons, calendar and unlimited factors free; first AI reading free) · how many habits (no cap) · how long until useful (two comparable photos; 3–4 weeks for a trend) · not medical advice.

### Closing CTA + footer
Centred on a `--bg → --tint` gradient: eyebrow `Start with today's photo`, H2 **Stop guessing. *See* the answer.**, lead about eight seconds a day, the two store buttons, and a muted line `Photos shown with permission · yours stay private`. Footer on `--tint`: © 2026 MorphTrack · Privacy · FAQ · mail link.

---

## 3. Motion spec

**a) Reversible scroll reveals.** Every `[data-reveal]` block (feature copy, panels, dark band, privacy list) is driven by ONE scroll handler, not IntersectionObserver: `q = ease(clamp((innerHeight - rect.top - 40) / (innerHeight * 0.3)))`, then `opacity = q`, `transform = translateY(20*(1-q))`. Because it's pure scroll math it plays backwards when scrolling up. Add class `rv-on` to `<html>` from JS so a no-JS page stays fully visible. Skip entirely under `prefers-reduced-motion`.

**b) Animated compare screen** (in-frame HTML, not a video). Cycles every 4.6s through three modes by swapping a class on the root: `m-slider → m-side → m-ovl`, with the segmented control's active pill following it.
- `m-slider`: the "after" image's `clip-path: inset(0 0 0 X)` animates 24% → 78% → 24% over 4.4s `ease-in-out infinite`, with the white 1.5px handle and 22px knob riding the same keyframes.
- `m-side`: both halves pinned at 50%, knob hidden.
- `m-ovl`: `clip-path` removed, after-image opacity 0 → 1 → 0 over 4.4s, plus an `Overlay · 42 %` label.
Date stamps in dark translucent pills, top-left and top-right.

**c) Animated calendar** (in-frame HTML). On load the marked days fill in one by one (~170ms apart, `background`/`box-shadow` transition + icons scaling in with `cubic-bezier(.2,.9,.3,1.5)`), the "N days logged" counter tick up, then the loop restarts after ~8s. The final state is the DEFAULT (rendered before JS runs) so the screen is never blank.

---

## 4. In-frame mock screens (built in HTML, must match the real app)

Both hand-built screens live inside a phone frame and are authored at ONE fixed size, then scaled to whatever frame width they appear in:

```
.pf   → device: 7px solid oklch(0.20 0.012 275), radius 40px, overflow hidden
.scrn → position:relative; aspect-ratio:1280/2856; overflow:hidden; app gradient bg
.si   → position:absolute; width:238px; height:531px; transform-origin:top left;
        transform:scale(var(--sc,1)); display:flex; flex-direction:column
JS    → for each .scrn: si.style.setProperty('--sc', scrn.clientWidth / 238)
```
Never re-tune font sizes per frame; only `--sc` changes. Every screen must end with the app's bottom tab bar (Today / Photos / Calendar / Analyses / More, pill-shaped, blurred white) so it reads like a real screen and fills the frame.

**Calendar screen** (matches the app 1:1):
- Header row: `August 2026` 700 + mono counter `N days logged`.
- Legend: three outlined pills on ONE line — camera `photo`, sparkle `AI reading`, check `routine`. No coloured tracker dots.
- Weekday row Mon…Sun, mono 9.5px, `grid-template-columns:repeat(7,minmax(0,1fr))`.
- 6×7 grid, `grid-auto-rows:minmax(0,1fr)`, `aspect-ratio:7/6.1`, gap 3px. Cells: `width/height:100%`, radius 9px; leading/trailing days greyed; **logged** days become white cards with a soft shadow, a 10.5px day number and up to two 8.5px icons; today (17) is a `--ink` block with white number and a white check.
- `today Aug 17` row with a mono `✓ 4` counter on the right.
- `DAILY ROUTINE` label + `All factors` link; routine chips: done = filled `--ink` with white check-circle and white text (Azelaic Acid 10%, Repair Moisturizer, SPF 50, Sport), not-done = outlined (Cleanser).
- `ONGOING FACTORS` label + pill `∞ Retinol · Apr 1 — Sep 30`.

**Connections + trend screen**:
- Back arrow + `Skin condition`.
- Mono label `POSSIBLE CONNECTIONS`, then TWO compact cards: `ⓘ Noticed · not confirmed` (mono, muted) / factor name 12.5px 700 / one-line claim ("Skin tone improved with regular use.", "Aligns with more even tone.") / italic note chip `Correlation, not causation`. Keep each text block `max-width:60%`.
- `TREND` card: title `"Skin condition" dynamics`, stepped indigo line (6 dots, flat→up→flat→up) over an `--accentSoft` area fill, dashed Better / Neutral / Worse guides with mono axis labels, date range `Apr 1 → Aug 12`.

---

## 5. Copy rules
Plain, specific, no marketing fluff, no exclamation marks, no emoji. Never promise diagnosis — the AI "describes what is visible in your photos". Always frame factor links as correlation, not causation. State clearly and repeatedly that photos, comparisons, the calendar and an unlimited number of routine factors are free, and that only extra AI readings are paid.

## 6. Verification checklist
- Every `.si` mock screen: `scrollHeight === clientHeight` (content exactly fills the frame) at both frame widths it is used at.
- In every duo composition, no text on the back phone crosses the front phone's left edge.
- Compare slider: the two photos' eye lines and face widths match — the seam must run continuously through nose and lips.
- Scroll reveals play forwards AND backwards; nothing stays invisible if JS fails.
- No duplicate `id`s when a mock screen is cloned into a second frame — strip ids from the clone.
- No console errors; all images resolve; every referenced `var(--*)` is defined.

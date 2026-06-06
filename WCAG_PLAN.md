# Plan: Create WCAG_PLAN.md for Accessibility Remediation

# WCAG 2.2 Remediation Plan
# Beaver Works Assistive Technology — CRE[AT]E Challenge Website

**Source audit**: `wcag-audit.md`  
**Target conformance**: WCAG 2.2 Level AA  
**Files in scope**: `index.html`, `about.html`, `schedule.html`,
`getting-started.html`, `tips-for-teams.html`, `goals-of-the-challenge.html`,
`additional-resources.html`

---

## How to Use This Plan

Each **Agent Block** is self-contained and covers one or more HTML files.
Agents can work in parallel as long as they only touch their assigned files.
Within each block, follow the task order — CSS additions come before the HTML
changes that rely on those classes.

**Read the Shared Decisions and CSS Utilities section first** — every agent
must apply the shared CSS to their files before making structural HTML changes.

---

## Design Decisions (resolved at planning level)

| Decision | Choice | Reason |
|---|---|---|
| `<h1>` approach | Add visually hidden `<h1 class="sr-only">` per page | Pages are Google Sites embeds; visible h1 would duplicate the host-page heading |
| Link / label color | `#7a5500` | Achieves ≈4.7:1 on white (#fff) and ≈4.4:1 on gray (#f5f5f5), passing 4.5:1 AA for normal text |
| `.schedule-semester` heading level | `<h3>` | After adding hidden `<h1>` and keeping first visible `<h2>`, semesters become level 3 |
| `.notes-list__heading` heading level | `<h4>` | One level below the semester `<h3>` |
| `interest-band` element | `<section>` with `aria-label` | Promotes it to a landmark for screen reader navigation |
| Footer on minimal pages | Add copyright + MIT Accessibility + Privacy Policy links | Matches the full footer pattern from index.html/schedule.html |

---

## Dependency Map

```
Level 0 — Design decisions above (already resolved)
    │
    ▼
Level 1 — Add shared CSS utilities to each file's <style> block
          (sr-only, skip-link, focus-visible, color update)
          ← MUST happen before any HTML structural change in that file
    │
    ▼
Level 2 — Add skip link + <main> landmark (requires skip-link CSS)
          Add visually hidden <h1> (requires sr-only CSS)
          Update color values in HTML/inline styles
    │
    ▼
Level 3 — All remaining semantic / ARIA changes
          (interest-band, heading promotions, ARIA attributes, etc.)
    │
    ▼
Level 4 — File-specific fixes not dependent on structure
          (tag colors, frameborder removal, meta description, etc.)
```

No tasks in one Agent Block depend on any other Agent Block.
All inter-task dependencies are within the same block and are addressed by
the ordered task lists below.

---

## Shared CSS Utilities

Every agent must add the following CSS to the `<style>` block of each file
they are responsible for. Add it **once**, near the top of the style block,
after the `:root` variable definitions.

```css
/* ── Accessibility utilities ─────────────────────────────────────────── */

/* Screen-reader-only: visually hides element but keeps it in the a11y tree */
.sr-only {
  position: absolute; width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}

/* Skip link: hidden until focused, then slides into view */
.skip-link {
  position: absolute; top: -40px; left: 0;
  background: var(--mit-dark); color: var(--yellow);
  padding: 8px 16px; z-index: 100;
  font-weight: 700; text-decoration: none;
  border-radius: 0 0 4px 0;
}
.skip-link:focus { top: 0; }

/* Enhanced focus indicator (replaces thin browser default) */
a:focus-visible,
.btn:focus-visible {
  outline: 3px solid var(--yellow);
  outline-offset: 3px;
  border-radius: 2px;
}
```

Also update the **link and label color** wherever `#b8860b` appears in the
file's `<style>` block:

```css
/* Before: color: #b8860b; */
/* After:  color: #7a5500; */
```

This replacement targets at minimum:
- `a { color: ... }` or `a:not(.btn) { color: ... }`
- `.section__label { color: ... }`
- Any other selector using `#b8860b` as a text color

---

## Agent Block A — `index.html`

**Estimated effort**: 45–60 min  
**Dependencies within block**: Level 1 CSS → Level 2 structure → Level 3 ARIA

### A1 — Add shared CSS utilities (Level 1)
- Add the Shared CSS Utilities block to the `<style>` tag
- Change all `#b8860b` text-color usages to `#7a5500`
- Change `.team-map-subtitle { color: #888 }` → `color: var(--mit-gray)` (i.e., `#555`)

### A2 — Structural skeleton (Level 2, depends on A1)
Add skip link as the very first child of `<body>`:
```html
<a class="skip-link" href="#main-content">Skip to main content</a>
```
Wrap all content between the skip link and `</body>` (exclusive of `<footer>`) in:
```html
<main id="main-content">
  …existing sections…
</main>
```
Add a visually hidden h1 as the first element inside `<main>`:
```html
<h1 class="sr-only">CRE[AT]E Challenge — Home</h1>
```

### A3 — ARIA and semantic improvements (Level 3, depends on A2)

**Map container** — add role and label:
```html
<div id="team-map" role="img"
     aria-label="Map showing CRE[AT]E Challenge team locations across the U.S. See the state summary list below for team counts by state.">
```

**Team count badge** — add aria-live:
```html
<div class="team-count" id="teamCountBadge" aria-live="polite" aria-label="Total teams"></div>
```

**State pills** — convert flat divs to a semantic list. In the JavaScript that
generates pills (search for `statePills` or `state-pills` in the script block),
change the container tag to `<ul>` in HTML and each pill to `<li>`:
```html
<ul id="statePills" class="state-pills">
  <!-- each pill: <li class="state-pill">…</li> -->
</ul>
```
Update the JS accordingly (change `createElement('div')` calls to `'li'`).

**Interest band** — promote to landmark:
```html
<section class="interest-band" aria-label="Registration interest">
  …
</section>
```

### A4 — Minor / polish (Level 4)

**Inline footer styles** — move to the CSS block:
Remove `style="background: var(--mit-dark); border-top: 4px solid var(--yellow);"` from `<footer>` and ensure the CSS rule for `footer` already contains these declarations (add if absent):
```css
footer { background: var(--mit-dark); border-top: 4px solid var(--yellow); }
```

**Tap target padding** — add to callout card links:
```css
.callout-card__body a {
  display: inline-block;
  padding: 2px 0;
  min-height: 24px;
  line-height: 1.6;
}
```

---

## Agent Block B — `schedule.html`

**Estimated effort**: 45–60 min  
**Dependencies within block**: Level 1 CSS → Level 2 structure → Level 3 headings → Level 4 colors

### B1 — Add shared CSS utilities (Level 1)
- Add the Shared CSS Utilities block to the `<style>` tag
- Change all `#b8860b` text-color usages to `#7a5500`

### B2 — Structural skeleton (Level 2, depends on B1)
Add skip link as the very first child of `<body>`:
```html
<a class="skip-link" href="#main-content">Skip to main content</a>
```
Wrap sections in `<main id="main-content">…</main>` (exclude `<footer>`).
Add visually hidden h1 as first element inside `<main>`:
```html
<h1 class="sr-only">CRE[AT]E Challenge — Schedule</h1>
```

### B3 — Heading hierarchy (Level 3, depends on B2)

**Semester dividers** — change from `<div>` to `<h3>`:
```html
<!-- Before -->
<div class="schedule-semester">Fall Semester — September to December 2026</div>
<!-- After -->
<h3 class="schedule-semester">Fall Semester — September to December 2026</h3>
```
Apply to ALL `.schedule-semester` occurrences in the file.

**Assignment Notes heading** — change from `<div>` to `<h4>`:
```html
<!-- Before -->
<div class="notes-list__heading">Assignment Notes</div>
<!-- After -->
<h4 class="notes-list__heading">Assignment Notes</h4>
```

**Invalid ARIA role** — fix `role="note"`:
```html
<!-- Before -->
<div class="notes-list" role="note" aria-label="Assignment notes">
<!-- After -->
<div class="notes-list" role="region" aria-label="Assignment notes">
```

### B4 — Color contrast (Level 4, independent)

**Project tag** — darken text:
```css
.tag--project { background: #fef3cd; color: #6b3e00; }
```

**Schedule notes** — darken warning text:
```css
.schedule-note { color: #5c3500; }
/* or wherever .schedule-note color is set — change from #92600a to #5c3500 */
```

### B5 — Reflow test (320px, independent)
Manually verify or add responsive stacked layout for the schedule table:
```css
@media (max-width: 480px) {
  .schedule-table,
  .schedule-table tbody,
  .schedule-table tr,
  .schedule-table td { display: block; }
  .schedule-table thead { display: none; }
  .schedule-table td[data-label="Milestone"] {
    font-weight: 700; text-align: left;
  }
}
```

---

## Agent Block C — `about.html` + `getting-started.html`

**Estimated effort**: 30–45 min  
**Dependencies within block**: Level 1 CSS → Level 2 structure → Level 3/4 extras

### C1 — Add shared CSS utilities to BOTH files (Level 1)
For each file:
- Add the Shared CSS Utilities block to the `<style>` tag
- Change all `#b8860b` text-color usages to `#7a5500`

### C2 — Structural skeleton in BOTH files (Level 2, depends on C1)
For each file, add skip link and `<main id="main-content">` wrapper, plus visually hidden `<h1>`:
- `about.html`: `<h1 class="sr-only">CRE[AT]E Challenge — About</h1>`
- `getting-started.html`: `<h1 class="sr-only">CRE[AT]E Challenge — Getting Started</h1>`

### C3 — about.html extras (Level 3/4, depends on C2)

**Remove deprecated `frameborder` attribute** from all `<iframe>` elements:
```html
<!-- Before -->
<iframe ... frameborder="0" ...>
<!-- After -->
<iframe ... ...>
```
Add to the `<style>` block if not already present:
```css
.video-embed iframe, iframe { border: 0; }
```

**Tap target padding** for callout card links:
```css
.callout-card__body a {
  display: inline-block;
  padding: 2px 0;
  min-height: 24px;
  line-height: 1.6;
}
```

**Footer alignment** — ensure footer includes at minimum:
```html
<footer>
  <div class="footer__inner">
    <div class="footer__left">
      <p>&copy; 2026 MIT Beaver Works Institute. All rights reserved.</p>
      <nav aria-label="Footer links">
        <a href="https://accessibility.mit.edu" target="_blank" rel="noreferrer noopener">MIT Accessibility</a>
        <a href="https://accessibility.mit.edu/privacy" target="_blank" rel="noreferrer noopener">Privacy Policy</a>
      </nav>
    </div>
  </div>
</footer>
```
Match the structure and classes used in the full footer from `index.html` as closely as possible.

### C4 — getting-started.html extras (Level 3/4, depends on C2)

**Fix dual `.btn--red` buttons** — change the second one:
```html
<!-- Before -->
<a class="btn btn--red" href="...">Next section: Goals of the Challenge</a>
<!-- After -->
<a class="btn btn--outline" href="...">Next section: Goals of the Challenge</a>
```
(Locate in the final CTA / interest-band section at the bottom of the page.)

**Interest band** — if present, promote to `<section>` with `aria-label`.

**Footer alignment** — apply same footer fix as about.html if the footer is minimal.

---

## Agent Block D — `goals-of-the-challenge.html` + `tips-for-teams.html` + `additional-resources.html`

**Estimated effort**: 30–45 min  
**Dependencies within block**: Level 1 CSS → Level 2 structure → Level 3/4 extras

### D1 — Add shared CSS utilities to ALL THREE files (Level 1)
For each file:
- Add the Shared CSS Utilities block to the `<style>` tag
- Change all `#b8860b` text-color usages to `#7a5500`

### D2 — Structural skeleton in ALL THREE files (Level 2, depends on D1)
Add skip link, `<main id="main-content">` wrapper, and visually hidden `<h1>`:
- `goals-of-the-challenge.html`: `<h1 class="sr-only">CRE[AT]E Challenge — Goals of the Challenge</h1>`
- `tips-for-teams.html`: `<h1 class="sr-only">CRE[AT]E Challenge — Tips for Teams</h1>`
- `additional-resources.html`: `<h1 class="sr-only">CRE[AT]E Challenge — Additional Resources</h1>`

### D3 — additional-resources.html extras (Level 3/4, depends on D2)

**Add missing meta description** in `<head>`:
```html
<meta name="description" content="Tools, learning materials, and community resources for assistive technology design, used by Beaver Works AT students and alumni." />
```

**Tap target padding** for resource card list links:
```css
.resource-card__list a {
  display: inline-block;
  padding: 2px 0;
  min-height: 24px;
  line-height: 1.6;
}
```

**Footer alignment** — ensure footer matches full footer pattern.

### D4 — goals-of-the-challenge.html extras (Level 4)

**Interest band** — if present, promote `<div class="interest-band">` to
`<section class="interest-band" aria-label="…">` with a descriptive label.

### D5 — tips-for-teams.html extras (Level 4)

**Interest band** — same promotion as D4.

---

## Cross-Cutting Checklist (apply in every block)

After completing block-specific tasks, verify these on every file you touched:

- [ ] `<html lang="en">` present ✅ (was already correct — confirm not accidentally removed)
- [ ] `<a class="skip-link" href="#main-content">` is the **first child** of `<body>`
- [ ] `<main id="main-content">` wraps all page sections (not the footer)
- [ ] First element inside `<main>` is `<h1 class="sr-only">…</h1>`
- [ ] No `#b8860b` remains as a text color anywhere in the `<style>` block
- [ ] `.sr-only`, `.skip-link`, and `a:focus-visible` rules are present in `<style>`
- [ ] All `<div class="interest-band">` changed to `<section class="interest-band" aria-label="…">`
- [ ] Footer contains at minimum: copyright line, MIT Accessibility link, Privacy Policy link

---

## Issue-to-Block Traceability

| Audit # | Issue | WCAG | Block |
|---|---|---|---|
| 1 | Link/label color `#b8860b` → `#7a5500` | 1.4.3 AA | A, B, C, D (all) |
| 2 | Add `<main>` landmark | 2.4.1 A | A, B, C, D (all) |
| 3 | Add skip-to-main link | 2.4.1 A | A, B, C, D (all) |
| 4 | Add visually hidden `<h1>` | 1.3.1 A | A, B, C, D (all) |
| 5 | `.schedule-semester` / `.notes-list__heading` → semantic headings | 1.3.1 A | B |
| 6 | Fix `role="note"` → `role="region"` | 4.1.1 A | B |
| 7 | `.tag--project` / `.schedule-note` color darken | 1.4.3 AA | B |
| 8 | `.team-map-subtitle` color `#888` → `#555` | 1.4.3 AA | A |
| 9 | Map `role="img"` + `aria-label` | 1.1.1 A | A |
| 10 | State pills → `<ul>/<li>` list | 4.1.2 A | A |
| 11 | `aria-live="polite"` on team count badge | 4.1.2 A | A |
| 12 | `interest-band` div → `<section aria-label>` | 4.1.2 A | A, B, C, D |
| 13 | Focus-visible styles | 2.4.7 AA | A, B, C, D (all) |
| 14 | Tap target padding on small links | 2.5.8 AA | A, C, D |
| 15 | Add `<meta name="description">` | — | D |
| 16 | Align footer structure across all pages | 3.2.3 AA | C, D |
| 17 | Fix dual `.btn--red` → one `.btn--outline` | — | C |
| 18 | Remove `frameborder="0"` from iframes | 4.1.1 A | C |
| 19 | Move inline footer styles to CSS | — | A |
| 20 | Schedule table reflow at 320px | 1.4.10 AA | B |
```

---

## Execution Step

1. Write the above markdown content to `WCAG_PLAN.md` in the project root.
2. No other files are modified during plan creation.
3. Agents can then be spawned using the block assignments above.
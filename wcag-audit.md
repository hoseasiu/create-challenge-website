# WCAG Accessibility Audit Report
# Beaver Works Assistive Technology — CRE[AT]E Challenge Website

**Site**: Beaver Works Assistive Technology — CRE[AT]E Challenge  
**Files audited**: `index.html`, `about.html`, `schedule.html`, `getting-started.html`, `tips-for-teams.html`, `goals-of-the-challenge.html`, `additional-resources.html`  
**Date**: 2026-05-20  
**WCAG Version**: 2.2  
**Target Conformance Level**: AA  
**Scope**: All 7 HTML embed files in the repository

---

## Executive Summary

### Conformance Status
- **Level A**: ❌ Not Conformant (multiple issues)
- **Level AA**: ❌ Not Conformant (multiple issues)
- **Level AAA**: ⚪ Not Evaluated

### Issue Count
| Severity | Count |
|----------|-------|
| Critical | 4 |
| Serious | 6 |
| Moderate | 7 |
| Minor / Advisory | 5 |

### Top 3 Blockers
1. **No `<h1>` on any page** — all 7 pages start with `<h2>`, breaking heading hierarchy (WCAG 1.3.1, 2.4.6)
2. **Link and section-label color `#b8860b` fails contrast on both white and gray backgrounds** — affects every page (WCAG 1.4.3)
3. **No "skip to main content" link and no `<main>` landmark** — affects all 7 pages (WCAG 2.4.1)

### Estimated Remediation Effort
- **Quick fixes** (a few hours each): heading hierarchy fix, `<main>` landmark, skip link, `role="note"` correction, `<meta description>` on `additional-resources.html`
- **Medium effort** (CSS changes, some testing): link/label color contrast, tag contrast, map accessibility, focus indicators
- **Larger effort**: interactive map alternative text / accessible data table

---

## Detailed Findings by Principle

---

### 1. Perceivable

#### ❌ FAIL — 1.3.1 Info and Relationships (Level A)

**Severity**: Serious  
**Affects**: `schedule.html`, `goals-of-the-challenge.html`, all pages

**Issue 1 — Heading hierarchy: no `<h1>` on any page**

Every page uses `<h2>` as the first and primary heading. Since these pages are embedded in Google Sites (which provides its own top-level heading), this may be intentional — but from the perspective of each HTML document in isolation, there is no `<h1>`, which breaks the required heading hierarchy. Screen reader users who navigate by headings will start at level 2 with no top-level context.

- **Affected files**: All 7 pages
- **Recommendation**: Add a visually hidden `<h1>` that matches the page title, or change the first `<h2>` on each page to `<h1>` and adjust downstream heading levels accordingly. If embedding in Google Sites provides an `<h1>`, document this clearly and confirm the embedded iframe context is correctly handled.
- **Example fix**:
  ```html
  <!-- Visually hidden h1 for screen readers -->
  <h1 class="sr-only">CRE[AT]E Challenge — Schedule</h1>
  <h2 class="section__heading">Challenge Schedule</h2>
  ```
  Add to CSS:
  ```css
  .sr-only {
    position: absolute; width: 1px; height: 1px;
    padding: 0; margin: -1px; overflow: hidden;
    clip: rect(0,0,0,0); white-space: nowrap; border: 0;
  }
  ```

**Issue 2 — `.schedule-semester` divs are not semantic headings**

In `schedule.html`, semester labels ("Fall Semester — September to December 2026") are styled as headings using `<div class="schedule-semester">` but are plain `<div>` elements. Screen readers will not identify these as headings and users who navigate by headings will miss them.

- **Affected file**: `schedule.html`
- **Recommendation**: Change to `<h3>` (or `<h2>` if `<h1>` is added and section heading becomes `<h2>`).
  ```html
  <h3 class="schedule-semester">Fall Semester — September to December 2026</h3>
  ```

**Issue 3 — `.notes-list__heading` is not a semantic heading**

The "Assignment Notes" label in `schedule.html` uses a styled `<div>` rather than a heading element, so it is not discoverable by screen reader heading navigation.

- **Affected file**: `schedule.html`
- **Recommendation**: Change to `<h3>` or `<h4>` depending on finalized heading hierarchy.

---

#### ❌ FAIL — 1.4.3 Contrast (Minimum) (Level AA)

**Severity**: Critical  
**Affects**: All 7 pages

**Issue 1 — Link color `#b8860b` fails contrast on white and gray backgrounds**

The global link color `#b8860b` (dark gold) is used for all in-text links across every page. Its contrast ratios are:

| Background | Ratio | Required | Result |
|---|---|---|---|
| `#ffffff` | 3.54:1 | 4.5:1 | ❌ FAIL |
| `#f5f5f5` | 3.34:1 | 4.5:1 | ❌ FAIL |

This is the most widespread contrast failure on the site, affecting every linked word in body copy on all 7 pages.

- **Recommendation**: Darken the link color to at least `#7a5500` (which achieves ~4.7:1 on white) or use `#6b4a00` for a more comfortable margin. Then test the new color against both white and `#f5f5f5` backgrounds.
  ```css
  a { color: #7a5500; }  /* ≈ 4.7:1 on #fff */
  ```

**Issue 2 — Section label color `#b8860b` fails contrast**

The `.section__label` eyebrow text uses the same `#b8860b` color at 0.75rem / 700 weight. At this size it is normal text (not "large text" per WCAG, which requires 18pt/24px or 14pt/bold/~18.67px), so it requires 4.5:1.

- **Affected files**: All 7 pages
- **Recommendation**: Apply the same darkened link color fix — use `#7a5500` or darker for labels. Or use a separate token like `--label-color: #7a5500`.

**Issue 3 — `.tag--project` color fails contrast**

In `schedule.html`, the Project tag uses `#92600a` text on `#fef3cd` background: ratio ≈ 3.2:1, failing the 4.5:1 requirement.

- **Affected file**: `schedule.html`
- **Recommendation**: Darken the text to `#6b3e00` or similar (achieves ~4.8:1 on `#fef3cd`).
  ```css
  .tag--project { background: #fef3cd; color: #6b3e00; }
  ```

**Issue 4 — `.schedule-note` color `#92600a` fails contrast on white**

Same color used for warning notes — fails 4.5:1 on `#ffffff`.

- **Affected file**: `schedule.html`
- **Recommendation**: Darken to `#6b3e00` or `#5c3500`.

**Issue 5 — `.team-map-subtitle` color `#888` fails contrast**

In `index.html`, the map subtitle text uses `#888` on `#ffffff`: ratio ≈ 3.5:1, failing 4.5:1.

- **Affected file**: `index.html`
- **Recommendation**: Change to `#767676` minimum (4.54:1) or use `var(--mit-gray)` which is `#555` (7.4:1).

---

#### ❌ FAIL — 1.1.1 Non-text Content (Level A)

**Severity**: Serious  
**Affects**: `index.html`

**Issue 1 — Interactive map has no accessible text alternative**

The Leaflet map in `index.html` displays the geographic distribution of 86 teams across the U.S. This data is visually rich but entirely inaccessible to screen reader users. The map div (`#team-map`) has no `aria-label`, `aria-describedby`, role, or text alternative. Users who cannot see the map have no access to the information it presents.

- **Recommendation (minimal)**: Add `role="img"` and `aria-label` to the map container:
  ```html
  <div id="team-map" role="img" aria-label="Map showing CRE[AT]E Challenge team locations across the U.S. See the state summary list below for team counts by state."></div>
  ```
  The state pills below the map (`.state-pills`) provide a partial text alternative — make sure they are accessible (see 4.1.2 finding below).

- **Recommendation (ideal)**: Supplement with a visually hidden accessible summary table of the same team-count data by state.

**Issue 2 — Map markers are inaccessible**

Individual team markers are rendered as `<div class="custom-pin">` elements injected by Leaflet's `divIcon`. They have no text, no role, and no `aria-label`. While the number of individual pins is high (86), the popup content ("City, State") is not reachable by keyboard navigation in a meaningful way.

- **Recommendation**: This is largely a Leaflet limitation with custom icons. The state pills table is a better accessible alternative for the data — focus effort there.

---

#### ⚠️ ADVISORY — 1.4.10 Reflow (Level AA)

**Severity**: Moderate  
**Affects**: `schedule.html`

The schedule table uses `min-width: 140px` on the date column. At 320px viewport width (WCAG 1.4.10 requirement), a two-column table with a `min-width: 140px` date column and a milestone column containing long text and links may cause horizontal overflow.

- **Recommendation**: Test the schedule table at 320px. Consider removing `min-width` from the date column at small sizes, or switching the table to a stacked card layout below 500px using CSS.
  ```css
  @media (max-width: 480px) {
    .schedule-table, .schedule-table tbody, .schedule-table tr, .schedule-table td {
      display: block;
    }
    .schedule-table thead { display: none; }
    .schedule-table td:last-child {
      text-align: left;
      font-weight: 700;
    }
  }
  ```

---

### 2. Operable

#### ❌ FAIL — 2.4.1 Bypass Blocks (Level A)

**Severity**: Serious  
**Affects**: All 7 pages

No page provides a "skip to main content" link. No page uses a `<main>` landmark element — all content is inside `<section>` and `<div>` elements with no wrapping `<main>`. Without a `<main>` landmark or skip link, keyboard-only and screen reader users must tab through all content on every page load.

- **Recommendation**: Wrap the page's primary content in `<main>` and add a visually hidden skip link at the top of each page:
  ```html
  <body>
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content">
      <!-- sections here -->
    </main>
    <footer>...</footer>
  </body>
  ```
  ```css
  .skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: var(--mit-dark);
    color: var(--yellow);
    padding: 8px 16px;
    z-index: 100;
    font-weight: 700;
    text-decoration: none;
  }
  .skip-link:focus { top: 0; }
  ```

---

#### ❌ FAIL — 2.4.6 Headings and Labels (Level AA)

**Severity**: Serious  
**Affects**: All 7 pages

Covered in detail under 1.3.1 above. No page has an `<h1>`, and in `schedule.html` the semester dividers are non-semantic `<div>` elements. This means heading navigation (a primary way screen reader users scan pages) is degraded on every page.

---

#### ⚠️ ADVISORY — 2.4.7 Focus Visible (Level AA)

**Severity**: Moderate  
**Affects**: All 7 pages

No custom focus styles are defined. The site relies on browser-default focus indicators. While not a direct violation (browsers do provide default focus rings), default focus outlines are often very thin or low-contrast and do not meet the enhanced WCAG 2.2 focus appearance guidance. Given that this site serves a community that includes people with disabilities — many of whom may use keyboard navigation — enhanced focus styles are strongly recommended.

- **Recommendation**: Add explicit focus styles to all interactive elements:
  ```css
  a:focus-visible,
  .btn:focus-visible {
    outline: 3px solid var(--yellow);
    outline-offset: 3px;
    border-radius: 2px;
  }
  ```

---

#### ❌ FAIL — 2.5.8 Target Size Minimum (Level AA, WCAG 2.2)

**Severity**: Moderate  
**Affects**: `index.html`, `about.html`, `additional-resources.html`

Arrow links inside `.callout-card__body` (e.g., "View 2026 projects →", "See the mentor page →") and resource links inside `.resource-card__list` are short inline text links with no padding. At `0.95rem` font size these render at approximately 15–18px tall, well below the WCAG 2.2 minimum of 24×24 CSS pixels for interactive targets.

- **Affected elements**: All `<a>` tags inside `.callout-card__body` and `.resource-card__list li`
- **Recommendation**: Add vertical padding to these inline links, or ensure their line-height provides at least 24px of clickable height:
  ```css
  .callout-card__body a,
  .resource-card__list a {
    display: inline-block;
    padding: 2px 0;
    min-height: 24px;
    line-height: 1.6;
  }
  ```

---

### 3. Understandable

#### ✅ PASS — 3.1.1 Language of Page (Level A)

All 7 pages correctly declare `<html lang="en">`.

---

#### ✅ PASS — 3.2.3 Consistent Navigation (Level AA)

Footer is structurally consistent across pages. `page-nav` links are present where appropriate. No unexpected context changes occur on focus or input.

---

### 4. Robust

#### ❌ FAIL — 4.1.1 Parsing (Level A)

**Severity**: Moderate  
**Affects**: `schedule.html`, `additional-resources.html`

**Issue 1 — Invalid ARIA role: `role="note"`**

In `schedule.html` the notes callout uses `role="note"`:
```html
<div class="notes-list" role="note" aria-label="Assignment notes">
```
`note` is not a valid ARIA landmark or widget role. This will be silently ignored or misinterpreted by assistive technologies.

- **Recommendation**: Use `role="region"` with the `aria-label`, or simply remove the role and let the section be read as a regular content block:
  ```html
  <div class="notes-list" role="region" aria-label="Assignment notes">
  ```

**Issue 2 — `frameborder` is a deprecated HTML attribute**

In `about.html`, `<iframe>` elements use `frameborder="0"`. This attribute was deprecated in HTML5.

- **Recommendation**: Remove `frameborder="0"` and use CSS instead:
  ```css
  .video-embed iframe { border: 0; }
  ```

---

#### ❌ FAIL — 4.1.2 Name, Role, Value (Level A)

**Severity**: Serious  
**Affects**: `index.html`

**Issue 1 — State pills list has no accessible role or structure**

The dynamically generated `.state-pills` container lists states and team counts but is a flat `<div>` containing more `<div>` elements. There is no semantic list markup, no ARIA role, and screen readers will announce the content as a stream of text with no grouping.

- **Recommendation**: Generate the pills as a `<ul>` with `<li>` items:
  ```javascript
  const pillContainer = document.getElementById('statePills');
  pillContainer.tagName // change to <ul> in HTML
  // each pill becomes an <li>
  ```
  Or add `role="list"` to the container and `role="listitem"` to each pill.

**Issue 2 — Team count badge has no accessible label**

The `#teamCountBadge` `<div>` is populated dynamically by JS with text like "86 teams" but has no `aria-label` and does not use an `aria-live` region, so the update is not announced to screen readers.

- **Recommendation**: Add `aria-live="polite"` to the badge element in the HTML:
  ```html
  <div class="team-count" id="teamCountBadge" aria-live="polite" aria-label="Total teams"></div>
  ```

**Issue 3 — `interest-band` divs lack landmark roles**

On pages where `<div class="interest-band">` is used, the element is a `<div>` with no landmark role. Users navigating by landmarks will skip over this CTA section.

- **Recommendation**: Wrap as a `<section>` with an `aria-label`:
  ```html
  <section class="interest-band" aria-label="Registration interest">
    ...
  </section>
  ```

---

### 5. Cross-Cutting / Consistency Issues

#### ⚠️ ADVISORY — Missing `<meta name="description">` on `additional-resources.html`

`additional-resources.html` is the only page without a `<meta name="description">` tag. All other pages have one.

- **Recommendation**: Add a description:
  ```html
  <meta name="description" content="Tools, learning materials, and community resources for assistive technology design, used by Beaver Works AT students and alumni." />
  ```

#### ⚠️ ADVISORY — Inconsistent footer structure across pages

Some pages (`about.html`, `getting-started.html`, `additional-resources.html`) have minimal footers missing the yellow top border, social icons, copyright year, and accessibility links that appear in the full footers on `index.html`, `schedule.html`, `tips-for-teams.html`, and `goals-of-the-challenge.html`. This affects WCAG 3.2.3 (Consistent Navigation) and 3.2.4 (Consistent Identification) at a minor level.

- **Recommendation**: Align footers across all pages to include, at minimum: copyright line, MIT Accessibility link, and Privacy Policy link.

#### ⚠️ ADVISORY — Two `.btn--red` buttons side by side in `getting-started.html`

In `getting-started.html`, the final CTA section places two `.btn--red` (yellow-background) buttons next to each other. The style guide specifies pairing `.btn--red` with `.btn--outline` on light backgrounds. Two visually identical buttons can be confusing to some users.

- **Recommendation**: Change the second button to `.btn--outline`:
  ```html
  <a class="btn btn--outline" href="...">Next section: Goals of the Challenge</a>
  ```

#### ⚠️ ADVISORY — `index.html` footer uses inline `style` attribute

The footer in `index.html` has `<footer style="background: var(--mit-dark); border-top: 4px solid var(--yellow);">` as an inline style, while all other pages apply these styles via the CSS class or the footer element selector. This is an inconsistency that could cause maintenance issues.

- **Recommendation**: Move the inline styles to the footer CSS rule in `index.html`.

---

## Prioritized Remediation Plan

### Phase 1 — Critical / High Impact (estimate: 2–4 hours total)

| # | Issue | File(s) | WCAG | Effort |
|---|-------|---------|------|--------|
| 1 | Darken link and label color from `#b8860b` to `#7a5500` | All | 1.4.3 AA | 30 min |
| 2 | Add `<main>` landmark wrapper | All | 2.4.1 A | 30 min |
| 3 | Add skip-to-main link with focus style | All | 2.4.1 A | 30 min |
| 4 | Add `<h1>` (visually hidden or restructure headings) | All | 1.3.1 A | 1 hr |
| 5 | Fix `.schedule-semester` and `.notes-list__heading` to semantic headings | schedule.html | 1.3.1 A | 15 min |
| 6 | Fix `role="note"` → `role="region"` | schedule.html | 4.1.1 A | 5 min |
| 7 | Darken `.tag--project` and `.schedule-note` colors | schedule.html | 1.4.3 AA | 15 min |
| 8 | Darken `.team-map-subtitle` color | index.html | 1.4.3 AA | 5 min |

### Phase 2 — Serious / Moderate (estimate: 2–4 hours total)

| # | Issue | File(s) | WCAG | Effort |
|---|-------|---------|------|--------|
| 9 | Add `role="img"` + `aria-label` to map container | index.html | 1.1.1 A | 15 min |
| 10 | Convert state pills to semantic `<ul>/<li>` list | index.html | 4.1.2 A | 20 min |
| 11 | Add `aria-live="polite"` to team count badge | index.html | 4.1.2 A | 5 min |
| 12 | Wrap `interest-band` divs as `<section aria-label="...">` | All | 4.1.2 A | 20 min |
| 13 | Add explicit focus-visible styles | All | 2.4.7 AA | 30 min |
| 14 | Add padding to small inline links for 24px tap target | Multiple | 2.5.8 AA | 20 min |

### Phase 3 — Minor / Advisory (estimate: 1–2 hours total)

| # | Issue | File(s) | WCAG | Effort |
|---|-------|---------|------|--------|
| 15 | Add `<meta name="description">` | additional-resources.html | — | 5 min |
| 16 | Align footer structure across all pages | All | 3.2.3 AA | 45 min |
| 17 | Fix two `.btn--red` buttons side by side | getting-started.html | — | 5 min |
| 18 | Remove `frameborder="0"` deprecated attr from iframes | about.html | 4.1.1 A | 5 min |
| 19 | Move inline footer styles to CSS class | index.html | — | 5 min |
| 20 | Test schedule table at 320px width; add stacked layout if needed | schedule.html | 1.4.10 AA | 45 min |

---

## Summary by File

| File | Critical | Serious | Moderate | Notes |
|------|----------|---------|----------|-------|
| `index.html` | 2 (link contrast, no h1) | 3 (no skip/main, map, state pills) | 2 (tap targets, team badge) | Most complex page; map needs most attention |
| `about.html` | 1 (link contrast) | 1 (no skip/main) | 2 (no h1, footer) | iframes titled ✅; frameborder deprecated |
| `schedule.html` | 2 (link contrast, tag contrast) | 2 (no skip/main, semantic headings) | 2 (no h1, role="note") | Best overall structure after fixes |
| `getting-started.html` | 1 (link contrast) | 1 (no skip/main) | 2 (no h1, dual red buttons) | |
| `tips-for-teams.html` | 1 (link contrast) | 1 (no skip/main) | 1 (no h1) | Cleanest page structurally |
| `goals-of-the-challenge.html` | 1 (link contrast) | 1 (no skip/main) | 1 (no h1) | Good use of h3 subheadings |
| `additional-resources.html` | 1 (link contrast) | 1 (no skip/main) | 2 (no h1, no meta desc) | Minimal footer needs alignment |

---

## What's Done Well ✅

- All pages declare `<html lang="en">` (3.1.1 ✅)
- Semantic `<section>`, `<footer>`, `<nav>`, `<blockquote>`, `<table>`, `<ul>`/`<ol>` used appropriately throughout
- Schedule tables use `aria-label` attributes ✅
- `page-nav` elements use `<nav aria-label="Page navigation">` ✅
- Video iframes in `about.html` have descriptive `title` attributes ✅
- Social icon images have `alt` text ✅ and social links have `aria-label` on most pages ✅
- BWSI logo image has meaningful `alt` text ✅
- Body text contrast (`#555` on white and gray) passes comfortably ✅
- Button text contrast (yellow on dark, dark on yellow) passes ✅
- Footer link contrast (near-white on very dark) passes ✅
- Most color tags (`tag--course`, `tag--event`, `tag--deadline`) pass contrast ✅
- Responsive grid layouts using `auto-fit` handle most reflow cases well ✅
- No `outline: none` suppressions on interactive elements ✅
- External links use `target="_blank" rel="noreferrer noopener"` where appropriate ✅

---

## Recommended CSS Additions (consolidated)

Add these to a shared stylesheet or to the `<style>` block in each page:

```css
/* Screen-reader-only utility */
.sr-only {
  position: absolute; width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}

/* Skip link */
.skip-link {
  position: absolute; top: -40px; left: 0;
  background: var(--mit-dark); color: var(--yellow);
  padding: 8px 16px; z-index: 100;
  font-weight: 700; text-decoration: none;
  border-radius: 0 0 4px 0;
}
.skip-link:focus { top: 0; }

/* Enhanced focus indicator */
a:focus-visible,
.btn:focus-visible {
  outline: 3px solid var(--yellow);
  outline-offset: 3px;
  border-radius: 2px;
}

/* Fix link/label color contrast (replaces #b8860b) */
a, .section__label { color: #7a5500; }
a:hover { text-decoration: underline; }
```

---

*Report generated: 2026-05-20 | Auditor: Claude (AI accessibility review) | Methodology: Manual code inspection against WCAG 2.2 success criteria. This report should be validated with automated tools (axe, WAVE, Lighthouse) and user testing with assistive technology users.*

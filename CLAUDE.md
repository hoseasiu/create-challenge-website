# Beaver Works AT — Site Style Guide

This document describes the visual language for the Beaver Works Assistive Technology website. Follow these conventions when adding new pages or components so everything stays consistent.

---

## Color Palette

| Token          | Value     | Usage |
|----------------|-----------|-------|
| `--yellow`     | `#ffce10` | Primary accent — backgrounds, highlights, CTA buttons, left-border accents |
| `--yellow-dk`  | `#e6b800` | Darker yellow for hover states or subtle contrast |
| `--mit-dark`   | `#1a1a1a` | Primary dark — footer background, dark CTA button, body text |
| `--mit-gray`   | `#555`    | Secondary body text, card body copy |
| `--mit-light`  | `#f5f5f5` | Alternating section background (gray sections) |
| `--border`     | `#e0e0e0` | Card and component borders |
| `--white`      | `#ffffff` | Page background, card backgrounds |
| Link color     | `#b8860b` | In-text links (dark gold); also used for section labels |

All colors are declared as CSS custom properties on `:root`. Always reference them via `var(--token)` rather than hard-coding hex values.

---

## Typography

**Font stack:** `'Segoe UI', Arial, sans-serif`

**Base body:** `font-size: 1rem`, `line-height: 1.65`, `color: var(--mit-dark)`

| Element            | Size                          | Weight | Notes |
|--------------------|-------------------------------|--------|-------|
| Section heading    | `clamp(1.4rem, 3.5vw, 2rem)`  | 800    | `line-height: 1.2` |
| Section label      | `0.75rem`                     | 700    | Uppercase, `letter-spacing: 0.12em`, gold color `#b8860b` |
| Section body copy  | `1rem`                        | 400    | `color: var(--mit-gray)`, `max-width: 680px` |
| Card title         | `1rem`                        | 700    | |
| Card body          | `0.875rem`                    | 400    | `color: var(--mit-gray)` |
| Footer text        | `0.85rem`                     | 400    | |

Section labels (the small uppercase eyebrow text above headings) always use gold `#b8860b` and all-caps + tracked letterforms. They provide context for the heading that follows.

---

## Layout

**Max content width:** `960px`, centered with `margin: 0 auto` via `.section__inner`.

**Standard section padding:** `60px 24px` (vertical/horizontal).

Sections alternate between white and light-gray backgrounds using `.section` and `.section.section--gray`. This creates visual rhythm without adding borders or heavy dividers.

---

## Buttons

All buttons use the `.btn` base class, with a variant modifier.

```html
<a class="btn btn--white" href="...">Primary Action</a>
<a class="btn btn--outline" href="...">Secondary Action</a>
<a class="btn btn--red" href="...">CTA on dark background</a>
<a class="btn btn--outline-dark" href="...">Secondary on dark background</a>
```

| Variant           | Background          | Text color        | Border |
|-------------------|---------------------|-------------------|--------|
| `.btn--white`     | `var(--mit-dark)`   | `var(--yellow)`   | none |
| `.btn--outline`   | transparent         | `var(--mit-dark)` | `2px solid rgba(0,0,0,0.35)` |
| `.btn--red`       | `var(--yellow)`     | `var(--mit-dark)` | none |
| `.btn--outline-dark` | transparent      | `var(--white)`    | `2px solid rgba(255,255,255,0.5)` |

Hover behavior: `opacity: 0.88` and `translateY(-1px)` — subtle lift, no color change. Transition: `0.15s opacity, 0.1s transform`.

On light backgrounds, pair a primary `.btn--white` with a secondary `.btn--outline`. On dark backgrounds, pair `.btn--red` with `.btn--outline-dark`.

---

## Components

### Feature Cards (`.feature-card`)

Used in a responsive grid (`repeat(auto-fit, minmax(200px, 1fr))`). White background, `1px solid var(--border)` border, `border-radius: 8px`, `padding: 28px 22px`. Each card has an emoji icon, a bold title, and short body copy.

```html
<div class="features">
  <div class="feature-card">
    <div class="feature-card__icon">📚</div>
    <div class="feature-card__title">Card Title</div>
    <div class="feature-card__body">Short description.</div>
  </div>
</div>
```

### Callout Cards (`.callout-card`)

Used in a responsive two-or-three column grid (`repeat(auto-fit, minmax(280px, 1fr))`). Yellow left-border accent (`4px solid var(--yellow)`), white background, light border on the other three sides, `border-radius: 0 8px 8px 0`. Contains a bold title, body copy, and usually one or more arrow links (`→`).

```html
<div class="callouts">
  <div class="callout-card">
    <div class="callout-card__title">Card Title</div>
    <div class="callout-card__body">
      Description text.
      <br><br>
      <a href="...">Link text →</a>
    </div>
  </div>
</div>
```

### Interest Band (`.interest-band`)

A full-width dark band (`var(--mit-dark)` background) used to break up the page and draw attention to a primary CTA. Text is centered and white. Heading uses the standard `clamp(1.4rem, 3.5vw, 2rem)` / weight-800 style.

```html
<div class="interest-band">
  <h2 class="interest-band__heading">Heading</h2>
  <p class="interest-band__body">Supporting text.</p>
  <div class="interest-band__ctas">
    <a class="btn btn--red" href="...">Primary CTA</a>
    <a class="btn btn--outline-dark" href="...">Secondary CTA</a>
  </div>
</div>
```

### Sections (`.section`)

Standard content sections use:

```html
<section class="section">           <!-- white background -->
<section class="section section--gray">  <!-- light gray background -->
  <div class="section__inner">
    <p class="section__label">Eyebrow label</p>
    <h2 class="section__heading">Heading</h2>
    <p class="section__body">Body copy...</p>
    <!-- component content below -->
  </div>
</section>
```

The `section__label` is optional but recommended when a heading benefits from extra context.

### Footer

Dark background (`var(--mit-dark)`) with a `4px solid var(--yellow)` top border. Two-column flex layout: copyright/links on the left, social icons on the right. Social icons are white-filtered (`filter: brightness(0) invert(1)`). Footer links use `rgba(255,255,255,0.8)`.

---

## Page Structure

Since these pages are embedded in Google Sites (which provides its own navigation header), individual pages should **not** include a nav bar or hero. The standard page structure is:

1. Content sections (`.section`, alternating white/gray)
2. Interest band — if there's a primary CTA to surface
3. Footer

---

## Site Snapshot Lookup

When a question is about a particular website page, first search the `site-snapshot` folder for that page's file. Use the snapshot copy as the authoritative summary source before making any content or format changes.

If you convert a Google Sites page into an HTML embed or otherwise update its published form, also update the corresponding file inside `site-snapshot` and revise the snapshot date to keep the archive aligned with the live site.

---

## Google Sites to HTML Embed Workflow

When a page is converted from the Google Sites version to a standalone full-page HTML embed, follow this workflow:

1. Review the live Google Sites page online first under beaver-works-assistive-tech.mit.edu/.
2. Compare it with the corresponding `site-snapshot` markdown file.
3. If there are major content or structural differences, pause and ask for clarification before editing.
4. If the snapshot is simply out of date, update the `site-snapshot/*.md` content to match the current published page.
5. Add or update snapshot metadata to document the source HTML file (for example, `source_html: index.html`).
6. Build the new HTML embed using the site style guide and accessibility guidelines.
7. Update the corresponding `site-snapshot` markdown file and snapshot date to keep the archive current.

This workflow ensures the published version, the snapshot archive, and the markup all stay synchronized.

---

## Naming Conventions

CSS follows a loose BEM convention: `.block`, `.block__element`, `.block--modifier`. Component-level class names are descriptive (`.feature-card`, `.callout-card`, `.interest-band`) rather than generic.

---

## Accessibility

This site should follow basic web accessibility principles to make content usable for people with diverse needs.

- Use semantic HTML whenever possible: headings (`h1`–`h6`), paragraphs, lists, buttons, links, forms, and landmarks.
- Ensure heading hierarchy is logical and sequential; avoid skipping levels.
- Provide meaningful link text that describes the destination or action, not just "click here."
- Include descriptive `alt` text for images and icons, or `alt=""` for decorative assets.
- Maintain strong contrast between text and background colors, especially for body copy, headings, buttons, and links.
- Make interactive elements keyboard-accessible and visible when focused.
- Keep content structure clear with spacing, readable line length, and responsive layout for different screen sizes.
- Use visible labels and supporting text for forms or inline inputs, and associate labels with fields.
- Avoid conveying information by color alone; pair color with text, iconography, or other indicators.
- Make page sections and cards easy to scan with clear headings, concise body copy, and consistent visual grouping.

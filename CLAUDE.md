# Beaver Works AT — Site Style Guide

This document describes the visual language for the Beaver Works Assistive Technology website. Follow these conventions when adding new pages or components so everything stays consistent.

---

## Cowork vs. Claude Code: who may edit this repo

**Only a local Claude Code session may edit, create, or delete files in this repository.** Running git against this working directory from both a Cowork session and a local Claude Code session at the same time causes `.git/index.lock` contention and has already caused null-byte corruption of `.git/config` once (see "Cowork Session Limitations" below).

**If a Cowork session is asked to edit anything in this repo — HTML/CSS files, `CLAUDE.md`, `website-update-status.md`, anything — it must refuse and tell Hosea to make the change from Claude Code instead.** This applies even to small or "quick" edits; there's no exception for size. Cowork may still read files here freely (to answer questions, review content, check `website-update-status.md`, or look things up in `site-snapshot/`) — the restriction is on writes only.

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
| Link color     | `#7a5500` | In-text links (dark brown-gold); also used for section labels — meets WCAG AA contrast on both white and light-gray backgrounds |

All colors are declared as CSS custom properties on `:root`. Always reference them via `var(--token)` rather than hard-coding hex values.

---

## Typography

**Font stack:** `'Segoe UI', Arial, sans-serif`

**Base body:** `font-size: 1rem`, `line-height: 1.65`, `color: var(--mit-dark)`

| Element            | Size                          | Weight | Notes |
|--------------------|-------------------------------|--------|-------|
| Section heading    | `clamp(1.4rem, 3.5vw, 2rem)`  | 800    | `line-height: 1.2` |
| Section label      | `0.75rem`                     | 700    | Uppercase, `letter-spacing: 0.12em`, gold color `#b8860b` |
| Section body copy  | `1rem`                        | 400    | `color: var(--mit-gray)`, `max-width: 680px` only on pages with card grids (see note below) |
| Card title         | `1rem`                        | 700    | |
| Card body          | `0.875rem`                    | 400    | `color: var(--mit-gray)` |
| Footer text        | `0.85rem`                     | 400    | |

Section labels (the small uppercase eyebrow text above headings) always use gold `#b8860b` and all-caps + tracked letterforms. They provide context for the heading that follows.

**`max-width: 680px` on body copy — when to apply it:** The 680px cap on `.section__body` (and on `.section__callout`, `.schedule-block`, and similar prose containers) is only appropriate when a page also has wide card grids (feature cards, callout cards, project cards) that fill the remaining horizontal space. On those pages the narrow intro text is balanced by the wide grids below it. On **prose-only pages** — any page whose sections contain only text, tables, or lists with no card grids — do **not** apply `max-width: 680px` to any content containers, so they fill the full 960 px `section__inner`. Course pages (under `/create-course/`) are always prose-only and are already covered by the course-page rules below. Non-course prose-only pages (e.g. `technical-mentors.html`, `schedule.html`) follow the same rule: omit the cap.

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

**Link targets in iframe embeds (corrected 2026-07-12 — see Cowork Session Limitations below):** Google Sites sandboxes embedded iframes and silently blocks `target="_top"` navigation — clicks do nothing, while Ctrl+click (opens new tab) works. Never use `target="_top"`.

An earlier version of this guide over-generalized that finding into "always use `target="_blank"` for internal links too." That's wrong and has been corrected: a plain link with **no `target` attribute** (default `_self`) navigates correctly in place — confirmed live on `index.html`, whose links have always lacked `target="_blank"` and work perfectly. `target="_top"` was the specific thing that broke; omitting `target` entirely is not the same as using it, and does not hit that bug.

**Current rule:**
- **Internal links** (anywhere on `beaver-works-assistive-tech.mit.edu`) — use a plain `<a href="...">` with **no `target` attribute**. This matches the homepage's proven behavior and avoids spawning a new tab for ordinary site navigation.
- **External links** (Google Forms, `giving.mit.edu`, `accessibility.mit.edu`, social media, `bwsi.mit.edu`, etc.) — keep `target="_blank" rel="noreferrer noopener"`, per normal web convention for leaving the site.
- **Never** use `target="_top"` anywhere in this repo.

---

## Course Pages

Course content pages (under `/create-challenge/create-course/`) are text-heavy and follow a prose-first layout. Keep these rules in mind:

- **Course pages use the full 960px content width.** Unlike non-course pages where `max-width: 680px` narrows body copy (because card grids fill the remaining space), course pages have all-prose layouts and look awkwardly narrow if that cap is applied. Do not add `max-width: 680px` to `.prose`, `.section__body`, `.prose-heading`, `.video-stack`, `.resource-list`, or `.reflect-box` on course pages — let them fill the `section__inner` (960px).
- **Videos are always one per row.** Never place two or more video embeds side by side in a course section. Use the `.video-stack` component (flex column) so each video takes its own full row. The `.video-grid` (multi-column) class is for non-course pages only.
- **`video-embed` aspect-ratio trap.** The `padding-bottom: 56.25%` trick on `.video-embed` is calculated against the *parent element's* width, not the element's own width. Never apply `max-width` directly to a `.video-embed` div — the height will be wrong. If a video needs to be narrower than its parent, wrap it in a plain `<div style="max-width: ...">` first, then put `.video-embed` inside that wrapper.
- Use the `.quiz-banner` (yellow background, bold dark text, full-width) after each major section to prompt Edly users to take the section quiz.
- **Module navigation buttons follow a book convention.** In the interest band at the bottom of each course page, the left button goes back (previous module or course overview) and the right button goes forward (next module). The forward/right button is the primary action and uses the highlighted style (`.btn--red`); the back/left button is secondary (`.btn--outline-dark`).

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

## Local-to-Live Sync Workflow

**Standard update flow, in order:**

1. Update the HTML page locally in this repo.
2. Push the change to GitHub.
3. Update the corresponding HTML embed on the live Google Site.
4. Update local documentation (e.g. `website-update-status.md`, TODO notes in the vault) to remove any TODO items tied to that update.

Full-page HTML embeds are edited locally in this repo, then manually pasted into the matching embed block on the live Google Site — there is no automated deploy. [website-update-status.md](website-update-status.md) is the handoff log between the editing step (Claude Code) and the publishing step (Claude in Chrome, or the user pasting by hand). Keep it current:

1. **After editing a local HTML embed (Claude Code):** mark that page's row in `website-update-status.md` as 🔄 **Needs sync**, and add a one-line note on what changed. Do this even for small edits — the whole point of the log is that nothing gets pushed live silently.
2. **Before pushing an update (Claude in Chrome or the user):** check `website-update-status.md` for pages marked 🔄 Needs sync or ❓ Unknown to know what's stale on the live site.
3. **After pushing an update:** flip the row to ✅ **Synced** and set "Last synced" to the date it was confirmed live. If Claude in Chrome performs the push, it should verify the live page reflects the change (reload and check) before marking it synced.
4. **New embed pages:** when a page is converted from Google Sites to a local HTML embed for the first time (see the workflow above), add it to the table in `website-update-status.md` rather than leaving it in the "not yet converted" list.
5. `website-update-status.md` tracks push status only. `site-snapshot/` remains the separate content archive — keep updating snapshot dates per the workflow above regardless of sync status.

Never assume a local edit is live until `website-update-status.md` says so.

---

## Cowork Session Limitations (learned 2026-07-12)

A few things that don't work the way you'd hope in a Cowork session on this repo — check here before re-discovering them the hard way. See also "Cowork vs. Claude Code: who may edit this repo" at the top of this file — as of 2026-07-12, Cowork no longer edits this repo at all, specifically because of the lock/corruption issues documented below.

**`git push` doesn't work from the Cowork sandbox.** The sandboxed shell has no SSH access to github.com (DNS resolution fails, no SSH keys configured). Don't attempt `git push`/`git fetch` over SSH from Cowork's bash tool — it will fail. Make all local commits as normal, but tell the user the push step needs to happen from their own machine (or set up an HTTPS remote with a token if that becomes available). Don't silently skip this step either — flag it explicitly so it doesn't get missed.

**`.git/config` can get silently corrupted with null bytes**, which breaks every git command with `fatal: bad config line N in file .git/config` and looks unrelated to anything you did. If git commands mysteriously fail at the very start of a session, check `.git/config` for null bytes (`sed -n 'Np' .git/config | cat -A` around the failing line) before assuming something else is wrong — stripping null bytes (`tr -d '\000'`) fixes it.

**The bash sandbox's view of this folder can go stale and lag well behind what `Edit`/`Write`/`Read` actually wrote — don't use bash (`cat`, `python3 open(...)`, `check-styles.py`, etc.) to verify a write that was just made with `Edit` or `Write`.** On 2026-07-12, bash reads of several files (including this `CLAUDE.md`) showed content cut off mid-sentence or mid-tag well after `Edit`/`Write` had reported success — in one case bash still showed a stale, truncated snapshot even several minutes and many tool calls later, while the `Read` tool (and presumably the user's own OneDrive-synced copy) showed the file complete and correct the whole time. Bash's own writes-then-reads within the same tool (e.g. a Python script that both edits and re-reads a file) were reliable; the staleness only showed up when bash tried to read something `Edit`/`Write` had just changed. **Practical rule: after using `Edit` or `Write`, verify the result with the `Read` tool, not bash.** If bash output disagrees with what `Edit`/`Write` reported, trust `Edit`/`Write`/`Read` over bash. This also means: don't assume a `check-styles.py` run via bash reflects an edit you just made with `Edit`/`Write` — re-run it, or verify manually via `Read`, if the timing is close. Separately, because the user's own local OneDrive sync can lag the same way, if a live-paste attempt right after an edit comes out truncated, the fix is usually to wait a bit and re-copy rather than assume the source file is broken — check the actual file with `Read` first before doing surgery on it.

**Caution when using the git-diff technique above:** a diff against `git show HEAD:<file>` can also surface *intentional* uncommitted content changes from earlier sessions, not just corruption — confirm with the user before "restoring" anything that looks like a deletion. (The `create-course.html` "Classroom guides" feature card was deliberately removed by the user in an earlier, uncommitted session and got wrongly re-added during a 2026-07-12 corruption sweep; it had to be removed again.)

**Don't try to push large HTML embeds into the Google Sites editor via Claude in Chrome + JS injection.** The "Embed from the web" dialog is a plain textarea with no file-upload or URL option, so the only way to get content into it is to have the content already exist somewhere fetchable (it doesn't, pre-push) or to transmit it through chat. Reliable single-call size for that transmission is roughly 9,000 characters of base64 — anything past that risks a silent mid-string truncation that breaks the JS (this happened when trying to push `index.html`, a 27KB file, in one shot). Chunking around that limit works but costs multiple round trips per page and duplicates the file's content in the conversation both as bash output and as the tool call payload — for a repo where several pages run 20–90KB, pushing all of them this way is impractically expensive. Default to finishing and verifying the local HTML files, then handing the user a clear list (via `website-update-status.md`) of which pages changed and why, and let them paste manually. Only attempt the Chrome-based push for a single small, already-agreed-upon page, and say upfront that it'll take several tool calls.

**A stuck `.git/index.lock` may not be deletable from the Cowork sandbox at all.** On 2026-07-12 a leftover `index.lock` (0 bytes, no owning process) resisted `rm`, `os.unlink`/`os.remove`, `find -delete`, `mv`, and `chmod` — all failed with `Operation not permitted`, and `chmod` didn't even silently take effect (permissions stayed `0700`). This looks like the OneDrive-backed mount itself refusing deletion from the sandbox side, not a normal permissions problem. Workaround: point git at a scratch index instead of fighting the lock — `GIT_INDEX_FILE=/tmp/git_index_alt git status` (copy `.git/index` to that path first) works fine and avoids ever touching the stuck file, since git's lock naming follows the index file path. The real fix is for the user to delete `.git\index.lock` directly from their own machine, where they have normal OS-level file access.

**Re-verify "synced" status before trusting it — don't take a prior sync record at face value.** `maker-skills.html` was marked ✅ Synced from a June push, but a fresh `check-styles.py` run in July found 3 drift issues on it that the earlier push apparently missed or predated. When doing a style/content audit, always run the actual check script in full and read its complete output rather than assuming a page is fine because a status file says so or because an earlier partial read of the output looked clean.

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

---

## Testing

When asked to create or check a particular page, ensure that any links are valid by attempting to reach them if you have access to the right tools.

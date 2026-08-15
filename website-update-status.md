# Website Update Status

This file tracks which full-page HTML embeds in this repo are **in sync with the live Google Site**. It is the working handoff point between two tools:

- **Claude Code** edits the HTML files in this repo.
- **Claude in Chrome** (or the user, manually) pastes the updated HTML into the matching embed block on the live Google Site.

See the "Local-to-Live Sync Workflow" section of [CLAUDE.md](CLAUDE.md) for the full process. `site-snapshot/` remains the separate content archive of record — this file is purely about push status.

## How to read the table

| Column | Meaning |
|---|---|
| Local file | HTML file in the repo root |
| Live URL | The embed's page on beaver-works-assistive-tech.mit.edu |
| Last local edit | Date of the most recent commit touching the local file |
| Sync status | ✅ Synced · 🔄 Needs sync · ❓ Unknown |
| Last synced | Date someone confirmed the live embed matches the local file |

**Sync status meanings:**
- ✅ **Synced** — the live embed matches this local file as of "Last synced."
- 🔄 **Needs sync** — local file has changed since it was last pushed; live site is stale.
- ❓ **Unknown** — sync status has never been confirmed either way; treat as needs-sync until checked.

---

## Pages with a local HTML embed

The rows below were seeded on 2026-07-12 by comparing each file's last local-edit date against its `site-snapshot` entry's `snapshot_date`. Per the existing [Google Sites to HTML Embed Workflow](CLAUDE.md#google-sites-to-html-embed-workflow), `snapshot_date` should be bumped every time an embed is pushed live — so a local edit dated *after* `snapshot_date` means the live site is very likely stale. This is an inference, not a confirmed check; do one pass to verify each row, then keep it current going forward.

| Local file | Live URL | Last local edit | Sync status | Last synced | Notes |
|---|---|---|---|---|---|
| [index.html](index.html) | [/home](https://beaver-works-assistive-tech.mit.edu/home) | 2026-07-12 | ✅ Synced | 2026-07-12 | Style-guide drift fixes (body font-size, `.section__body` margin, `.interest-band__body` opacity, `.features`/`.feature-card`/`.callout-card` spacing) + added missing `<meta name="description">`. Pasted live and confirmed by user 2026-07-12. |
| [about.html](about.html) | [/create-challenge/about](https://beaver-works-assistive-tech.mit.edu/create-challenge/about) | 2026-07-12 | ✅ Synced | 2026-07-12 | Added missing `body { font-size: 1rem }` (style-guide drift fix), then removed `target="_blank"` from 1 internal link (Getting Started) per the corrected link-target rule in CLAUDE.md. Rebuilt 2026-07-12 from the last git commit after an earlier truncated paste; re-pasted live and confirmed by user 2026-07-12. |
| [additional-resources.html](additional-resources.html) | [/additional-resources](https://beaver-works-assistive-tech.mit.edu/additional-resources) | 2026-07-12 | ✅ Synced | 2026-07-12 | Style-guide drift fixes (body font-size, `.section__body` margin, callout-card spacing) and a new Interest Band section added before the footer (previously had none) — copy is placeholder-quality ("Ready to put these tools to use?" linking to Getting Started and the Course); revisit wording if it doesn't read right live. Then removed `target="_blank"` from 2 internal links (Getting Started, the Course). Pasted live and confirmed by user 2026-07-12. |
| [create-course.html](create-course.html) | [/create-challenge/create-course](https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course) | 2026-07-12 | ✅ Synced | 2026-07-12 | Fixed link underline/hover-opacity to match style guide, then removed `target="_blank"` from 11 internal links (module nav, maker-skills sub-links). Pasted live and confirmed by user 2026-07-12. |
| [course-introduction.html](course-introduction.html) | [/create-challenge/create-course/introduction](https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course/introduction) | 2026-07-12 | ✅ Synced | 2026-07-12 | Aligned unused `.video-grid` CSS and `.video-embed` border-radius to reference values (no layout change — page uses `.video-stack`), then removed `target="_blank"` from 2 internal links. Pasted live and confirmed by user 2026-07-12. |
| [maker-skills.html](maker-skills.html) | [/create-challenge/create-course/maker-skills](https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course/maker-skills) | 2026-08-15 | 🔄 Needs sync | — | Added a new "Artificial Intelligence" section card (icon, description, link to `/create-challenge/create-course/maker-skills/artificial-intelligence`) after the Wearables card. Previously synced 2026-07-12; this is a new local change not yet pasted live. |
| [technical-mentors.html](technical-mentors.html) | [/create-challenge/technical-mentors](https://beaver-works-assistive-tech.mit.edu/create-challenge/technical-mentors) | 2026-07-12 | ✅ Synced | 2026-07-12 | Style-guide drift fixes (body font-size, `.section__body`/`.section__list` spacing, `.interest-band__body` opacity, `.section__list` color, `.schedule-block` margin). Pasted live and confirmed by user 2026-07-12. No internal links needed the target fix — all its links are already external. |
| [tips-for-teams.html](tips-for-teams.html) | [/create-challenge/tips-for-teams](https://beaver-works-assistive-tech.mit.edu/create-challenge/tips-for-teams) | 2026-07-12 | ✅ Synced | 2026-07-12 | Style-guide drift fixes (`.section__list` spacing, `.section__ctas` margin, `.callouts`/`.callout-card` spacing). Pasted live and confirmed by user 2026-07-12. Already had no `target="_blank"` links — no further change needed. |
| [2026-projects.html](2026-projects.html) | [/past-projects/2026-projects](https://beaver-works-assistive-tech.mit.edu/past-projects/2026-projects) | 2026-07-12 | ✅ Synced | 2026-07-12 | Removed stray `'DM Sans'` from body font-family, added missing `<meta name="description">`, then removed `target="_blank"` from 2 internal links (Past Projects index, Getting Started). Pasted live and confirmed by user 2026-07-12. |
| [schedule.html](schedule.html) | [/create-challenge/schedule](https://beaver-works-assistive-tech.mit.edu/create-challenge/schedule) | 2026-07-12 | ✅ Synced | 2026-07-12 | Additional style-guide drift fixes made after the prior June push (body font-size, `.section__body` margin, `.interest-band__body` opacity), then fixed the duplicate `<h1>` issue (visible "Challenge Schedule" heading was `<h1>` alongside the sr-only `<h1>`; demoted to `<h2>` to match every other page's pattern). Pasted live and confirmed by user 2026-07-12. |
| [faq.html](faq.html) | [/create-challenge/faq](https://beaver-works-assistive-tech.mit.edu/create-challenge/faq) | 2026-08-15 | 🔄 **Needs sync** | — | New HTML embed (first conversion from Google Sites — page was previously listed under "Not yet converted"). Built to resolve [issue #19](https://github.com/hoseasiu/create-challenge-website/issues/19): fixed heading hierarchy (every question is now a consistently-leveled `<h3>` under its section's `<h2>`; previously a mix of `<h2>`s and plain text, with one question mis-nested as a false section header), unified the team-number scheme everywhere it's mentioned (2 digits = middle school, 3 = high school, 4 = college — previously inconsistent between "three-digit" and "3- or 4-digit" and omitted middle school entirely), stated the middle school policy plainly (contact us to see what's possible; assigned 2-digit numbers if they join), and added a jump-links section index at the top. All FAQ content is otherwise verbatim from the live page as of 2026-08-15. Not yet pasted live. |
| [idea-to-ink.html](idea-to-ink.html) | [/create-challenge/create-course/idea-to-ink](https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course/idea-to-ink) | 2026-08-15 | 🔄 **Needs sync** | — | New HTML embed (first conversion from Google Sites — Module 3 of the CRE[AT]E Course, previously listed under "Not yet converted"). Built following the `course-introduction.html` pattern (full 960px prose width, `.video-stack`/`.video-embed`, quiz banner, module-nav interest band). Content — storyboarding, sketching for physical products and software/UI, and raster vs. vector digital drawing — is verbatim from the live page as of 2026-08-15. The two storyboard example images (Cheryl Platz's Echo Look frames, Veronica Spencer's Instructables paint-booth example) were downloaded locally by the user into `website-images/` and are referenced via `raw.githubusercontent.com` URLs, matching the pattern used for the logo in `index.html` — these won't resolve until this commit is pushed to `main`. Both embedded YouTube videos and both external resource links (Medium, Instructables) were checked and resolve correctly. `check-styles.py` passes with zero drift. Not yet pasted live. |

## Local drafts not yet linked to a snapshot

These HTML files exist in the repo but their `site-snapshot` entry has no `source_html` field and is still marked `content_status: stub` — meaning it's unclear whether this embed was ever pushed to the live site at all. Confirm live status before relying on the sync table above for these.

| Local file | Live URL | Last local edit | Notes |
|---|---|---|---|
| [getting-started.html](getting-started.html) | [/create-challenge/getting-started](https://beaver-works-assistive-tech.mit.edu/create-challenge/getting-started) | 2026-07-12 | Style-guide drift fixes (`.section__list` spacing, `.feature-card__body` font-size), then removed `target="_blank"` from 1 internal link (Goals of the Challenge). Pasted live and confirmed by user 2026-07-12. `site-snapshot` entry still needs its `source_html` field added per the workflow in CLAUDE.md. |
| [goals-of-the-challenge.html](goals-of-the-challenge.html) | [/create-challenge/goals-of-the-challenge](https://beaver-works-assistive-tech.mit.edu/create-challenge/goals-of-the-challenge) | 2026-08-15 | 🔄 **Needs sync** — wrapped the "most important learning objective" sentence in `<strong>` in the Learning Objectives section (2026-08-15), not yet pasted live. Style-guide drift fixes (`.section__list` spacing) were pasted live and confirmed by user 2026-07-12, prior to this change. `site-snapshot` entry still needs its `source_html` field added per the workflow in CLAUDE.md. |

## Not yet converted to an HTML embed

These pages are still native Google Sites content with no local HTML embed. Not "out of sync" — just not started. Listed for backlog visibility only; move a page out of this list and into the table above once it gets a local HTML embed.

- Alumni Division, Registration Process, Current Forms
- CRE[AT]E Course modules: Design Processes, Documentation and Presentation
- Maker Skills sub-pages: Electronics, Mechanical Making, Software, Wearables
- CRE[AT]E Project and sub-pages: Co-Designer Interviews, Design Reviews, Finding a Co-Designer, Project Brainstorming, Scoping a Project, Simplify
- Final Event: 2023, 2024, 2025, 2026
- Past Projects: 2023, 2024, 2025 (2026 is already an embed — see table above)
- Challenge Dashboard
- Previous Programs: Design for Education Aids (Crash Course, Projects), Design of AT (2021 Documentation, 2022 Assignments, 2022 Documentation, About Design of AT, Final Prototype, Initial Prototype, Product Requirements)

---

*Last reviewed: 2026-07-12. All 12 pages pass `check-styles.py` with zero drift against `reference-style.css`. All pages, including the further local fixes made to `about.html`, `additional-resources.html`, `create-course.html`, `course-introduction.html`, `maker-skills.html`, `2026-projects.html`, `getting-started.html`, and `schedule.html` (internal link targets and/or the duplicate-`<h1>` fix), have been pasted live and confirmed synced as of 2026-07-12. Update this file whenever a local HTML embed changes or whenever a push to the live site is confirmed — see the workflow in [CLAUDE.md](CLAUDE.md).*

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
| [index.html](index.html) | [/home](https://beaver-works-assistive-tech.mit.edu/home) | 2026-07-12 | 🔄 Needs sync | — | Snapshot dated 2026-05-11; local file edited after (WCAG contrast/focus fixes, link target fixes; removed "Funding for Your Project" feature card). |
| [about.html](about.html) | [/create-challenge/about](https://beaver-works-assistive-tech.mit.edu/create-challenge/about) | 2026-06-11 | 🔄 Needs sync | — | Snapshot dated 2026-05-11; local file edited after (iframe link-target fix, WCAG fixes). |
| [additional-resources.html](additional-resources.html) | [/additional-resources](https://beaver-works-assistive-tech.mit.edu/additional-resources) | 2026-06-11 | 🔄 Needs sync | — | Snapshot dated 2026-05-11; local file edited after (new resource categories + search filter added). |
| [create-course.html](create-course.html) | [/create-challenge/create-course](https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course) | 2026-06-11 | 🔄 Needs sync | — | Snapshot dated 2026-06-06; local file edited after (minor corrections, link-target fix). |
| [course-introduction.html](course-introduction.html) | [/create-challenge/create-course/introduction](https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course/introduction) | 2026-06-11 | 🔄 Needs sync | — | Snapshot dated 2026-06-06; local file edited after (link-target fix). |
| [maker-skills.html](maker-skills.html) | [/create-challenge/create-course/maker-skills](https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course/maker-skills) | 2026-06-13 | ✅ Synced | 2026-06-13 | Local edit date matches snapshot date. Verify this still holds before trusting it. |
| [technical-mentors.html](technical-mentors.html) | [/create-challenge/technical-mentors](https://beaver-works-assistive-tech.mit.edu/create-challenge/technical-mentors) | 2026-06-11 | 🔄 Needs sync | — | Snapshot dated 2026-06-06; local file edited after (small corrections, max-width fix). |
| [tips-for-teams.html](tips-for-teams.html) | [/create-challenge/tips-for-teams](https://beaver-works-assistive-tech.mit.edu/create-challenge/tips-for-teams) | 2026-06-06 | 🔄 Needs sync | — | Snapshot dated 2026-05-11; local file edited after (WCAG fixes, link fixes, nav consistency). |
| [2026-projects.html](2026-projects.html) | [/past-projects/2026-projects](https://beaver-works-assistive-tech.mit.edu/past-projects/2026-projects) | 2026-06-11 | 🔄 Needs sync | — | Snapshot dated 2026-06-06; local file edited after (iframe link-target fix). |
| [project-funding.html](project-funding.html) | [/create-challenge/project-funding](https://beaver-works-assistive-tech.mit.edu/create-challenge/project-funding) | 2026-08-05 | 🔄 Needs sync | — | New page created for issue #18 (canonical funding mechanism); not yet pushed live — this URL does not exist on the live site yet. |

## Local drafts not yet linked to a snapshot

These HTML files exist in the repo but their `site-snapshot` entry has no `source_html` field and is still marked `content_status: stub` — meaning it's unclear whether this embed was ever pushed to the live site at all. Confirm live status before relying on the sync table above for these.

| Local file | Live URL | Last local edit | Notes |
|---|---|---|---|
| [getting-started.html](getting-started.html) | [/create-challenge/getting-started](https://beaver-works-assistive-tech.mit.edu/create-challenge/getting-started) | 2026-06-11 | Snapshot never updated with `source_html`; verify whether this was ever pushed live. |
| [goals-of-the-challenge.html](goals-of-the-challenge.html) | [/create-challenge/goals-of-the-challenge](https://beaver-works-assistive-tech.mit.edu/create-challenge/goals-of-the-challenge) | 2026-06-06 | Snapshot never updated with `source_html`; verify whether this was ever pushed live. |
| [schedule.html](schedule.html) | [/create-challenge/schedule](https://beaver-works-assistive-tech.mit.edu/create-challenge/schedule) | 2026-06-11 | Snapshot never updated with `source_html`; verify whether this was ever pushed live. |

## Not yet converted to an HTML embed

These pages are still native Google Sites content with no local HTML embed. Not "out of sync" — just not started. Listed for backlog visibility only; move a page out of this list and into the table above once it gets a local HTML embed.

- Alumni Division, Registration Process, Current Forms, FAQ
- CRE[AT]E Course modules: Design Processes, Documentation and Presentation, Idea to Ink
- Maker Skills sub-pages: Electronics, Mechanical Making, Software, Wearables
- CRE[AT]E Project and sub-pages: Co-Designer Interviews, Design Reviews, Finding a Co-Designer, Project Brainstorming, Scoping a Project, Simplify
- Final Event: 2023, 2024, 2025, 2026
- Past Projects: 2023, 2024, 2025 (2026 is already an embed — see table above)
- Challenge Dashboard
- Previous Programs: Design for Education Aids (Crash Course, Projects), Design of AT (2021 Documentation, 2022 Assignments, 2022 Documentation, About Design of AT, Final Prototype, Initial Prototype, Product Requirements)

---

*Last reviewed: 2026-07-12. Update this file whenever a local HTML embed changes or whenever a push to the live site is confirmed 
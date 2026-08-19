# Design Processes / Idea to Ink — Verbatim Text Audit (2026-08-19)

## Why this file exists

Following the same audit pattern established in [maker-skills-verbatim-audit.md](maker-skills-verbatim-audit.md), [design-processes.html](design-processes.html) and [idea-to-ink.html](idea-to-ink.html) were checked paragraph-by-paragraph against their live Google Sites originals. Both pages were far closer to verbatim than the original Maker Skills sub-pages, but each had real deviations — including one fabricated paragraph on Design Processes.

**Source of truth used:** the original Google-Sites-native pages, still reachable (hidden from nav, not deleted) at their renamed URLs — `.../create-challenge/create-course/old-design-processes` and `.../create-challenge/create-course/old-idea-to-ink`. Text was extracted directly from each live page's rendered `document.body.innerText`.

**Status: both pages fixed.** `check-styles.py` passes with zero drift across all 28 pages after the edits below.

---

## Design Processes ([design-processes.html](design-processes.html))

Source: `.../create-course/old-design-processes`

| Location | Was | Fixed to (verbatim) |
|---|---|---|
| Module overview | **Invented paragraph not present in the source at all**: *"This module covers the engineering design process you'll use throughout the CRE[AT]E Challenge. You'll learn what it means to work with a co-designer, walk through a general design process for hardware products, practice turning user needs into measurable product specifications, and follow a real case study of iterative prototyping for an assistive technology device."* | Removed. The source goes straight from the page title into the "Co-Designers" heading — no overview paragraph exists. |
| Activity intro sentence | Reworded: *"Below are 5 statements that were gathered in a user interview with Kenzie's mom."* | Restored exact original (admittedly awkward) phrasing: *"In the below 5 activities are some statements that are gathered in a user interview with Kenzie's mom."* |
| Prototyping 2 Decision Point | Reworded: *"...and prioritizes the ones...design: the sharpness of the clamp's edges and the weight of the object."* | Restored exact original: *"...design: edges of the clamp sharpness and the weight of the object."* |
| Prototyping Round 2, clamp paragraph | Word swap: *"metal working expertise **on** the team"* | Restored original: *"metal working expertise **in** the team"* — not a clear error, just a wording preference change that shouldn't have been made silently |
| 4 case-study figcaptions (system-components, CAD rendering, updated rendering, final photo) | **Invented figcaptions** describing each image, not present in the source (the source has no captions on these images at all) | Removed. Images keep their existing descriptive `alt` text for accessibility; no reader-facing caption text was added back since none exists in the source. |

**Unlogged-but-in-scope objective fixes found already baked into the page** (kept as-is, logging now per the fix-and-log rule):
- "CREA[AT]E Challenge" → "CRE[AT]E Challenge" (misspelled program name)
- "user needs statement(s)" → "user need statement(s)" (×3, consistent with the term used throughout the rest of the page)
- "nice-to haves" → "nice-to-haves"
- "table and chairs" → "tables and chairs" (Armon Edero paragraph)
- "each devices" → "each device" (Review section)
- "real life scenario" → "real-life scenario"
- "user needs where understood" → "user needs were understood" (where/were)
- "y-axes" → "y-axis" (Performance Requirements — a single rotation, singular axis)
- Roughly a dozen missing-article / missing-comma / subject-verb-agreement fixes throughout (e.g. "Agile have been shown" → "Agile, have been shown"; "For hardware the processes...is used" → "For hardware processes...are used"; "attribute that address" → "...addresses"; "Armon Edero which" → "Armon Edero, which"; "3 people have tried," → "...tried it,"; "so must be able" → "so it must be able"; "referred to as feasibility prototype" → "...as a feasibility prototype"; "clamp and ball joint and arm cuff" → "clamp, ball joint, and arm cuff"; "and skipped for this prototype" → "and is skipped..."; "the requirements the team defines" → "...defined")

## Idea to Ink ([idea-to-ink.html](idea-to-ink.html))

Source: `.../create-course/old-idea-to-ink`

| Location | Was | Fixed to (verbatim) |
|---|---|---|
| Storyboarding resource list, Cheryl Platz item | Condensed, dropping content: *"Cheryl Platz, a designer for Microsoft and Amazon, describes the motivation..., and provides tips for creating your own storyboards."* | Restored full original wording: *"...who has been a designer for Microsoft and Amazon, very articulately describes the motivation..., and provides tips for creating your own storyboards in the context of designing user experiences."* (kept the descriptive link title "Half the Blank Page: Storyboarding for Product Design" in place of the source's non-descriptive "This Medium article," since that's an accessibility fix, not a wording change) |
| Storyboarding resource list, Veronica Spencer item | Condensed: *"another approach, by product designer Veronica Spencer."* | Restored: *"another approach by product designer Veronica Spencer, focused on storyboarding for product design."* (same treatment — descriptive link title kept, dropped clause restored) |
| 2 storyboard image figcaptions | **Invented captions** with detail not in the source: *"Credit: Cheryl Platz — frames from the first Echo Look storyboards."* / *"Credit: Veronica Spencer — New Invention Studio paint booth storyboard example, via Instructables."* | Restored the source's literal terse captions: *"Credit to Cheryl Platz"* / *"Credit to Veronica Spencer"* |

**Unlogged-but-in-scope objective fixes found already baked into the page** (kept as-is, logging now):
- "the way **then** envisioned" → "the way **they** envisioned" (typo)
- "CAD **had** a tendency" → "CAD **has** a tendency" (tense fix — the surrounding paragraph is present-tense)

No content fabrication was found on Idea to Ink beyond the resource-list condensing and the two figcaptions above — the sketching, physical-product-drawing, paper-prototyping, and raster/vector sections all checked out as genuinely verbatim.

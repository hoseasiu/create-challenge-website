# Maker Skills — Verbatim Text Audit (2026-08-19)

## Why this file exists

When the four original Maker Skills pages (Mechanical, Electronics, Software, Wearables) were converted from Google Sites to local HTML embeds on 2026-08-15, the wording was substantially reworded, condensed, and in a few places had new claims/links added — despite [website-update-status.md](website-update-status.md) recording the content as "verbatim from the live page." Hosea caught this by comparing the live site against the local files and asked for a full revert to verbatim source text, restructured only where needed to fit the site's HTML components (prose blocks, lists, reflect-boxes), with a written record of every change.

**Source of truth used:** the original Google-Sites-native pages, still reachable (hidden from nav, not deleted) at their renamed URLs — e.g. `.../maker-skills/old-mechanical`. Text was extracted directly from each live page's server-rendered HTML.

**Status: 4 of 4 sub-pages fixed and reverted to verbatim text.** The Maker Skills index page still could not be checked — see "Not yet resolved" below.

---

## Mechanical ([maker-skills-mechanical.html](maker-skills-mechanical.html))

Source: `.../maker-skills/old-mechanical`

| Location | Was (reworded) | Fixed to (verbatim) |
|---|---|---|
| Module overview | Invented paragraph not present in the source at all: *"This section covers the physical fabrication skills behind building an assistive technology device — machine tools and shops, 3D printing, and computer-aided design (CAD). Mechanical is one of four Maker Skills sections; if your project involves mechanical fabrication, complete this section along with one other that fits your project."* | Removed. The source has no overview paragraph before "Machine Tools and Shops" — the section now shows only the title. |
| Machine Tools intro | Condensed/reworded, dropped "the making of products by" and changed "such as" → "like" | Restored full original sentence, including its original dashes and phrasing |
| StuffMadeHere video | Original explanatory paragraph replaced with an invented one-line caption *("A shop tour from StuffMadeHere, included to give you a sense of what tools are commonly available in a well-equipped machine shop.")*, dropping "particularly for one person" and "many prototyping shops, including the Beaver Works shop, have a similar mix of tools" | Restored full original two-sentence paragraph before the video; removed the invented caption |
| Matterport tour | Paragraph reworded and the specific questions ("What machines do you see? And importantly, what safety equipment do you see?") dropped entirely | Restored full original text, including the questions |
| Makerspace activity | Original prose (with its definition sentence "Maker spaces are community prototyping shops...", the "(including ones in your school!)" aside, and the closing "If you don't have one nearby..." sentence) was rewritten into a 3-item bullet list, dropping all of that | Restored as the original flowing prose, verbatim, inside the reflect-box |
| 3D Printing intro | Reworded/condensed, dropped "It can be used to create a large variety of different objects designed in software, using various materials" and added an unsourced claim: *"it will likely be one of the most useful tools available to your team"* | Restored full original paragraph |
| 3D Printing comprehension question #5 | Reworded/shortened: *"(Hint: think about a lever printed lying horizontal vs. standing vertical — how does the layering direction affect strength?)"* | Restored full original wording |
| Reflect-box label | "Comprehension Check" (invented) | "Questions" — the source's own label text |
| CAD section heading | "Computer-Aided Design (CAD)" | "Computer-Aided Design" — source has no "(CAD)" |
| CAD intro paragraph | Entire "napkin sketch" paragraph explaining why CAD matters was deleted | Restored in full |
| Onshape intro paragraph | Reworded and shortened; **added an unsourced claim**: *"built for collaboration, so your whole team can work in the same document at once"* — this sentence does not exist anywhere in the source | Restored original paragraph (no collaboration claim) |
| Onshape signup instructions | Reworded into a numbered how-to list, dropped "using the 'Get Started' button" and "You are, of course, free to do more if you would like!" | Restored as the original two prose paragraphs |

**Judgment calls flagged, not silently decided:**
- The Matterport link's visible text is literally "here" in the source (a known accessibility anti-pattern flagged elsewhere in this repo's own style guide). Kept verbatim per your instruction rather than rewriting it to something more descriptive — let me know if you'd rather I fix just the link text here.
- The source's "learn.onshape.com" link actually points to a stale internal Edly courseware URL (`courses.bwsix.edly.io/.../Winter_2022/.../learn.onshape.com`), not to `learn.onshape.com` itself. I kept the link pointing directly at `https://learn.onshape.com` (what the visible text says, and almost certainly what was intended) rather than restoring the apparently-broken original href, since this is a link target, not wording. Flag if you want the literal original href restored instead.

---

## Electronics ([maker-skills-electronics.html](maker-skills-electronics.html))

Source: `.../maker-skills/old-electronics`

| Location | Was (reworded) | Fixed to (verbatim) |
|---|---|---|
| Intro | Condensed two original paragraphs into one, reworded throughout | Restored both original paragraphs in full |
| "Popular Platforms" heading | Invented — source has no sub-heading here | Removed; content now flows as prose under "Circuits and Microcontrollers," matching the source structure |
| Arduino/Feather/Pi paragraph | Rewritten from two flowing paragraphs into a 3-item bullet list, reworded line by line | Restored as the original two prose paragraphs |
| "Simulator First" heading | Invented | Removed |
| Tinkercad paragraph | Reworded into a 3-step numbered list; moved the "free account" note to a confusing final "step" | Restored as the original single prose paragraph, in original order |
| "Additional Learning Resources" heading | Invented | Removed |
| Resource links (Arduino/Adafruit/Sparkfun) | Link text shortened, dropped "the" and "page"/"Center" article structure | Restored exact original link text ("the Arduino tutorials page," "the Adafruit Learning Center," "the Sparkfun Learn page") |
| Closing paragraphs | Reworded ("Adafruit and SparkFun are also retailers...", "See also the Additional Resources page.") | Restored exact original wording |

No unsourced claims were added on this page — the issue here was condensing/paraphrasing, not fabrication.

---

## Software ([maker-skills-software.html](maker-skills-software.html))

Source: `.../maker-skills/old-software` — this page had the most extensive rewording and the two clearest content fabrications.

| Location | Was (reworded) | Fixed to (verbatim) |
|---|---|---|
| Intro list intro sentence | Dropped "Software projects in the assistive tech space can vary widely, though" | Restored |
| Intro list items | Reworded into "Label — description" fragments; **the "Mobile app" item added "— iOS or Android," a detail not present in the source at this point in the page** | Restored the four original list sentences verbatim |
| Intro framing paragraphs | Two full paragraphs dropped entirely: *"We will refer to the above as web, desktop, mobile, and MCU/SBC for the purposes of this page."* and *"In the sections below, version control and user interface / front-end development will be relevant to all types of development. After those sections, we will discuss some issues that are specific to the type of development that you are doing or are considering."* | Restored both |
| Version Control | First paragraph (defining version control) dropped entirely; second paragraph reworded/condensed | Restored both original paragraphs in full, including the source's own "the the use of" typo (kept verbatim per your instruction — flag if you'd like this specific typo corrected) |
| UI/Front-End Development | 5 original paragraphs condensed to 2; the whole "you must first figure out what the interaction will look like..." paragraph was dropped | Restored all 4 original body paragraphs |
| Web Development | Source is literally two `TODO` placeholder lines ("TODO - learning resources" / "TODO - simulating mobile viewports"). These were replaced with **invented finished-sounding prose**: *"This section is still being developed — check back for additional learning resources. In the meantime, if you're testing a mobile-first design, Chrome DevTools device mode is a useful way to simulate a mobile viewport..."* | Restored the literal "TODO" placeholder text (the Chrome DevTools link itself is real and was already correctly attached to "simulating mobile viewports" in the source — only the surrounding TODO framing was fabricated away) |
| Desktop Dev intro | Reworded | Restored exact original sentence |
| Packaging paragraph | Reworded; dropped the second sentence ("Packaging ensures that all necessary parts are included so the app runs reliably on another machine.") | Restored in full |
| "Why packaging matters" heading | Reworded from source's actual heading, "Why do we need packaging?" | Restored exact original heading |
| Packaging bullets (4 items) | All 4 shortened/reworded, dropping detail from each | Restored full original text for all 4, including original punctuation/typos |
| Mobile Dev intro | Dropped entirely | Restored |
| iOS section | Numbered list items reworded slightly; final paragraph reworded | Restored exact original wording, including the source's "iOS development development" and "willing the pay" typos (kept verbatim) |
| Android section heading | "Android Development" | "Android development" (matches source capitalization) |
| Android paragraph | Reworded | Restored, with "guide to getting started" as the exact original link text (was previously "Android Developers getting-started guide") |
| "Visual Programming for Mobile: MIT App Inventor" heading | Reworded from source's actual heading | Restored exact original heading: "Visual Programming Environment for Mobile Apps" |
| App Inventor intro paragraph | **Dropped a full sentence with a real link**: *"There are a few examples on the About Us page that share some teams that used App Inventor to create assistive tech already."* | Restored, with the "About Us page" link restored (`appinventor.mit.edu/about-us`) |
| App Inventor bullets (2 items) | Both heavily condensed — dropped "These apps can range from simple utilities to more complex, interactive applications like games, social networking apps, and tools that interact with hardware or online services" and the entire ThingSpeak/Android-app-choice sentence from the second bullet | Restored both bullets in full |
| Software Accessibility section | Rewritten from 5 flowing paragraphs into 2 sentences + a 4-item resource list, dropping most of the explanatory text (what screen-reader accessibility is, the "important to keep a few principles in mind" framing, etc.) | Restored as the original 5 prose paragraphs, with links attached to their original anchor text |
| Firefox colorblindness note | This one was *not* actually a fabrication — I initially misread it as an invented link, but the YouTube link (`youtube.com/watch?v=eBefjaWud-M`) **is** in the original, attached to "built-in colorblindness simulator." Restored the exact original sentence and link placement. |
| AI/ML section intro | Dropped 2 of 3 original paragraphs, including the one that introduces the video ("First, let's take a look at the 'machine learning life cycle'...") | Restored all 3 original paragraphs |
| HuggingFace paragraph | Reworded | Restored exact original wording |
| Data Bias and Disability | Both original paragraphs (long, detailed — including the full neurotypical-vs-neurodivergent explanation and the OpTECHs example) condensed into 2 short sentences plus an invented "Rule of Thumb" reflect-box | Restored both original paragraphs in full as prose; removed the invented reflect-box (its content was a paraphrase, not a verbatim excerpt) |
| Training Models | Dropped "or want to go through the process to learn it" and "(and more general ML training)"; reworded throughout | Restored both original paragraphs in full |
| Other Resources | Reworded ("If you're using App Inventor, see...") | Restored exact original sentence |

**Judgment call flagged:** the source mixes straight and curly apostrophes inconsistently (e.g. "doesn't" vs. "doesn't"/"what's"). I matched this exactly where I directly verified character codes against the source, but did not do an exhaustive character-by-character audit of every apostrophe/quote/dash on this page — let me know if you want a stricter typographic pass.

---

## Wearables ([maker-skills-wearables.html](maker-skills-wearables.html))

Source: `.../maker-skills/old-wearables` (URL supplied by Hosea — my earlier guessed URLs were all wrong).

| Location | Was (reworded) | Fixed to (verbatim) |
|---|---|---|
| Module overview | Both intro paragraphs condensed/reworded into a single `section__body` sentence plus one shortened prose paragraph | Restored both original paragraphs in full |
| Section heading | "Electronic Wearables — Components" (added "— Components," not in source) | "Electronic Wearables" |
| Components list | Reworded into shorter fragments; **"Blufruit" (the source's own spelling/typo) was silently corrected to "Bluefruit"** | Restored all 4 items verbatim, including the source's "Blufruit" spelling (flagging this as a likely typo, not fixing it) |
| "Form Factor & Ergonomics" | Original lead sentence plus 2 sub-bullets ("Minimizing discomfort during use," "Donning and doffing," each with full explanatory text) condensed into a single generic paragraph, dropping the two-part structure and most of the detail | Restored the lead sentence and both sub-bullets in full, matching the source's nested-list structure |
| "Measuring for Wearables" | Reworded intro sentence; all 4 sub-bullets (Bodies are flexible/move/change/need hygiene) shortened, dropping explanatory detail from each (e.g. "look up videos or resources on anatomical measurements for accuracy" was dropped from the first) | Restored intro sentence and all 4 bullets verbatim |
| "Aesthetics" | Condensed into one sentence, dropping the closing "By considering these factors, you'll create wearables that are comfortable, practical, and functional for the user." sentence entirely | Restored the bold "Aesthetics:" lead-in plus both full original paragraphs, including the closing sentence |
| AFFOA paragraph 1 | Reworded/shortened, dropping "is fortunate to" and "share their wearable technology and functional fabric curriculum with students," and condensing AFFOA's mission statement | Restored in full |
| AFFOA paragraph 2 / curriculum link | Reworded; link text changed from the source's "here" to a constructed "curriculum.affoa.org/EDP" | Restored original wording and the source's own "here" link text (flagging the non-descriptive link text the same way as Mechanical's Matterport link, below) |

**Judgment call flagged:** same as Mechanical's Matterport link — the AFFOA curriculum link's visible text is literally "here" in the source. Kept verbatim; let me know if you'd rather that one link's text specifically be fixed for accessibility.

`check-styles.py` passes with zero drift, and the rebuilt page's text was verified to match the source exactly (including the "Blufruit" typo and the curly vs. straight apostrophes checked against the source's actual character codes: "It's", "you'll", and "AFFOA's" are curly (’) in the source; "user's," "co-designer's," and "Adafruit's" are straight (') — both preserved as found).

## Not yet resolved

**Maker Skills index page** ([maker-skills.html](maker-skills.html)) — same situation. Tried `old-maker-skills` under `/create-challenge/create-course/` — 404. I have not touched this page's wording pending confirmation either way. Its current callout-card descriptions (for Mechanical, Software, Electronics, Wearables, Artificial Intelligence) are short original summaries rather than lifted from the sub-pages, so they may not have the same problem — but I haven't verified this against a source page.

**Artificial Intelligence** ([maker-skills-artificial-intelligence.html](maker-skills-artificial-intelligence.html)) — not audited. Unlike the other four, this page's own history note says it was built directly from the *live* page (not a since-hidden old version) on 2026-08-19, so the same rewording risk may not apply — but this hasn't been independently checked against source text the way the other four were.

---

## 2026-08-19 follow-up: misspellings and formatting errors corrected

The verbatim pass above deliberately preserved every typo/error found in the source, flagging rather than fixing them. Hosea then asked to go back and fix the genuine errors (not just note them). These are actual corrections to the source's own mistakes, not "rewording" — the underlying meaning is unchanged in every case:

| Page | Was (source error) | Fixed to |
|---|---|---|
| Software | "consider the the use of version control" | "consider the use of version control" (duplicated word) |
| Software | "Apple keeps iOS development development behind" | "Apple keeps iOS development behind" (duplicated word) |
| Software | "unless you are willing the pay the costs" | "unless you are willing to pay the costs" (wrong word) |
| Software | "or to help with decide what clothes to wear" | "or to help decide what clothes to wear" (grammar) |
| Software | "packaging bundles what's missing ." | "packaging bundles what's missing." (stray space before period) |
| Software | "Arduino, Beagle Bone, etc" | "Arduino, BeagleBone, etc" (product name is one word) |
| Software | "be familiar with Swift or Objective C" | "be familiar with Swift or Objective-C" (language name is hyphenated) |
| Electronics | "the Sparkfun Learn page" / "Adafruit and Sparkfun are retailers" | "the SparkFun Learn page" / "Adafruit and SparkFun are retailers" (brand name is SparkFun, capital F) |
| Wearables | "Adafruit's lines of Lilypad, Blufruit, and Feather boards" | "...Lilypad, Bluefruit, and Feather boards" (Adafruit's actual product line is "Bluefruit") |

**Not touched:** the two non-descriptive "here" links (Mechanical's Matterport tour link, Wearables' AFFOA curriculum link) — fixing those would mean adding/changing words to make the link text descriptive, which is a copy/accessibility improvement rather than a correction of an objective error, so I left them as flagged rather than deciding unilaterally. Say the word if you want those fixed too. Also not touched: a couple of borderline awkward-but-not-wrong constructions in the source (e.g. Software's "Although, there are also other platforms like ThingSpeak..." — a sentence that starts oddly but isn't a clear-cut error) — flagging here rather than guessing whether you'd count that as in scope.

`check-styles.py` passes with zero drift on all 4 pages after these fixes.

## Next steps

- `website-update-status.md` has been updated for all 4 fixed pages (flipped to 🔄 Needs sync, wording revert noted) — see that file.
- `check-styles.py` passes with zero drift on all 4 edited pages.
- Once the Maker Skills index page's old-version URL is confirmed (or its absence confirmed), repeat this same process for it.

---
name: design-quality
description: One skill for designing and reviewing websites, landing pages, app and SaaS screens, dashboards, forms, interactive tools (calculators, configurators), lists with filters, data tables, sign-up, pricing, navigation, print and slides. Mode create builds from the first decision on; modes audit and fix check and improve what exists. All modes share the same rules (surfaces not lines, no side accent bars, WCAG 2.2 AA, no dark patterns, brand colors fixed, libraries such as shadcn/ui and Tailwind used as intended), so building and reviewing arrive at the same result. Use whenever something is designed, built, redesigned, extended, reviewed, polished, made less generic or AI-looking, converts poorly, feels cluttered or cheap, or needs an accessibility or UI/UX check, even if the user only says "build", "make", "design" or "check".
---

# Design Quality

Good and generic interfaces often use the same components. The difference lies in focus, order, a few details, and how well the screen helps people decide. This skill holds one set of rules and uses it in three ways: to decide and build (create), to check (audit) and to improve (fix). Because all modes use the same rules, a page built here and a page reviewed here should end up alike. Keep only what carries the decision; improving usually means removing, not adding.

Design for the system, not for one screenshot: every check asks whether the screen still works with other content, other images and other items. Screens fail less often because they look bad than because they ignore how people perceive and decide. Layout fixes rarely mean rebuilding; usually one deliberate shift does more, and the moves from print design (posters, magazines, packaging) apply to the web as well.

Fixed rules and the accessibility block are hard requirements. Everything else is a principle: numbers in it are examples, and the right means depends on the brand and context.

## Modes

- **create**: a new page, screen, component or section, or a redesign from scratch. Decide, build with the sections as build rules, then run the audit on the rendered result and fix until it passes.
- **audit**: check only, report with scores.
- **fix**: improve following the fix order, then audit again.
- **Choose the mode from the request.** A request to build or extend selects create for the requested scope (adding a field to an existing form is create for that field, followed by an audit of the changed form, not an audit only). A request to inspect selects audit. A request to improve an existing result selects fix, beginning with a baseline audit. No mode given: something to build means create; for an ambiguous existing artifact, audit first, then ask whether to fix.

## Fixed rules (override everything below)

1. **Everything shown is true.** Progress counts only real steps the user did or confirmed, result counts are real, deadlines exist, losses are the user's actual loss. No invented numbers, ratings, logos, testimonials or scarcity presented as real. Missing content, in this order: use what was given; ask for what is missing; in drafts fill neutral content (names, sample records, body copy) with realistic demo content, marked once as example content. Proof is never invented, not even as demo: testimonials, ratings, client logos, certificates and counts (customers, projects, years) that were not given get a visibly marked slot each and are listed as open at the end. Prices, package contents and other values a draft needs to work are not proof: when they were not given, use realistic example values so the draft calculates and compares, mark them once as example values and list them as open. In drafts and mockups, placeholder functionality (controls that don't work yet) is not flagged; only the believability of the content is checked.
2. **No dark patterns.** Declining stays easy and neutrally worded; no shaming labels, no hidden close buttons, no invented countdowns or scarcity. Defaults serve the user, never the business at the user's expense. Never preselect consent, newsletters, paid extras, a priced package, data sharing or longer contracts. In consent banners, declining is as easy and visible as accepting. Cancelling is as easy as signing up; the full price with all mandatory fees is shown before commitment; a declined prompt does not return on every visit. These principles work because they match real behavior; used to deceive, they become dark patterns, cost trust and in many markets break consumer or privacy law. A premium feel comes from respect for the visitor's time and intelligence, not from tricks. The way out is visible and plainly worded (for example "Nicht jetzt", "Ohne Upgrade weiter").
3. **Surfaces, not lines.** Cards, tiles, chips, tags, outlined secondary buttons and stat groups get no thin border lines or hairline dividers between them (a secondary button takes a calm tinted fill instead); separate with surfaces and spacing, shadows optional and soft. Borders only on inputs and controls. A transparent outline is allowed as a fallback for forced colors (high contrast mode).
4. **No side accent bars.** Never mark a card, row, alert, quote or selected item with a thicker colored edge on one side (left or right border, inset shadow, pseudo-element stripe); it is the most typical generic AI pattern. Mark state through the surface itself (a tinted background), weight, an icon, a dot or a label. A selected or flagged state uses at least two cues (tinted surface plus check icon, label or weight), never a tint alone, because a tint alone rarely reaches 3:1 against the unselected state. A selectable card is a control: a full outline or ring for focus and selection is allowed under rule 3; a one-sided edge is not. In audits, an existing side bar is a rule violation; in fixes, replace it.
5. **Brand and look are fixed.** A given palette, corporate colors, type and component style are kept: invent no new hues and no new style for one section or tool; how the existing colors are used is decided, reviewed and changed freely. Two things differ completely here: a new color or color scheme is forbidden; giving an element a different color from the existing palette is a normal fix. Recoloring a button, dimming a loud alert, turning an outlined accent button neutral, reserving the accent for the main action, or giving a status its existing caution token instead of the fault color is applying the palette, not changing the brand. Tints, shades and status colors derived from the palette are fine; meaning never rests on color alone. Palette changes may only be recommended when the whole site or product is in scope, as a marked suggestion with the reason (for example contrast), never applied.
6. **Content stays in fix mode.** Preserve visible wording, facts, demo data, discoverability and decision-time disclosures. Decoration is not content: eyebrow kickers, decorative badges, repeated labels, glows and filler that rule 8 or A1 remove are removed directly and listed in the report. Move, group or regroup content while keeping it available at the point of use; a disclosure moved below the decision it belongs to counts as removed, even if every word stays in the markup. Action and status microcopy may change directly where a rule calls for it: a button or decline label that names its result, a progress line, a price reference, a state label, and error, sending and success messages, including a message the fix has made untrue. List each such change in the report with its old and new wording, so the user can confirm or revert it. All other shortening, rewriting, removing or hiding of visible content is only proposed, never done silently: present it as a before/after suggestion with the reason, and apply it after the user explicitly approves that change. Markup may change for accessibility while preserving the displayed meaning. Decorative duplicates (for example a repeated label) may be hidden with CSS only when equivalent information remains available, including to assistive technology; they stay in the markup. Edits use the project's copy conventions; German copy follows `copy-rules` if available.
7. **Signature elements** the user names (for example a hero effect) stay untouched, in every place they appear.
8. **No generic AI look.** No gradient headlines, glows, glass for its own sake, decorative badges, stat or status pills with dots, oversized outline wordmarks, emoji icons, rows of identical feature cards, stat strips without a source, or everything centered by default.
9. No em or en dashes in copy.
10. **Reuse before inventing.** Start with the project's existing tokens, components, variants, global classes and conventions; they come before new values, and changes use the installed framework's supported extension points. Component libraries and utility frameworks (for example shadcn/ui on Tailwind, or blocks built on them) are used as intended, with their components, variants, theme variables, utility classes and conventions; adaptations go through their theme tokens, variants or classes, never `!important` or other specificity overrides, hard-coded ad hoc values or forked copies. In shadcn/ui the installed component source belongs to the project: when a change belongs to every instance, editing the one canonical component or adding a shared variant there is the intended way; a second parallel copy, or a wrapper that only exists to avoid editing the canonical component, is not. In Tailwind, use the project's theme and utilities: theme variables map design tokens to utilities, so a token change belongs in the theme, not in scattered values. A given configuration (theme, Tailwind config, tokens) is reused exactly: adapt through classes or variants, and change the shared config only when the user asks or the library documents that as the way; before changing a shared token or component, verify the affected variants, states and other consumers. A library default that conflicts with a rule here (for example a card with a border) is solved once, at the appropriate scope, in the theme or a variant.

## When rules meet

**Conflicting fixed rules.** First try a permitted implementation: a different pairing of existing brand colors, a shade derived from the same hue, a neutral surface, a non-color state cue or an accessible equivalent for a signature effect. Preserve the named signature and palette. If the conflict persists, report the exact element and the user consequence as unresolved, give the smallest approval-dependent option and withhold a passing result for that check (it stays Fail, or Unverified if not yet tested, never Pass); create and fix stop at this approval boundary instead of looping. The cases below are the common ones.

- **Brand color fails contrast** (rule 5 against X1): change the use, not the color. Text and controls take a shade derived from the same hue, or a different pairing of existing brand colors; the original stays for surfaces and marks.
- **Brand elements and rule 8:** only signature elements the user names stay (rule 7). Every other gradient, glow, eyebrow kicker, tight tracking or extra font family is removed by rule 8 and A4, on existing elements as well as new ones; the palette itself stays (rule 5).
- **Equal cards:** rule 8 bans the filler row of look-alike feature cards, not equal cards for comparable items such as products, plans or people (A3, C2, G4).
- **Text over images:** only when the image is fixed and chosen for it (G3), and every supported crop and state keeps measured contrast (X1). Where images vary or are uploaded, text sits beside or below (A7, C2).
- **Simple against decidable:** remove what competes, never hide what a decision depends on. Looking simpler is not deciding more easily (B2, C4, C5 win over A2).
- **Equal choices:** where choices require equal visibility, such as accept and decline in a consent banner, the alternatives get equal prominence and effort; the quieter style for secondary actions (A1) does not apply to them (rule 2, W2).
- **Labels:** A8 removes repeated labels on static values, never the visible label of a form field (X3).
- **Sticky elements** (B5, B7, F2, I): on small screens they leave most of the view to content: one bar at the top, one at the bottom at most, and never over the focus (X2).

## What is on the screen (all modes)

**Context** sets priorities, not which sections apply:

| Context | Weigh more |
| --- | --- |
| Website (marketing, company, service) | First impression, clarity of message, trust, reading flow, the website duties in W |
| Product (app, SaaS, tool, portal) | Efficiency, density, control, states (empty, loading, error), consistency across screens; use W4 and the responsive checks (W5) for consequential web app tasks as well |
| Print, poster, slides | Composition, viewing distance, series |

**Building blocks** decide the sections. A website with a cost calculator gets section B; an app screen with a result list gets section C.

| If the screen has … | Apply |
| --- | --- |
| anything | **A Foundation**, **X Accessibility** |
| a public website or landing page | **W Website duties** and **G Composition** |
| forms, interactive tools, calculators, configurators, requirement catalogs, product selection with variants, quantity or an add to cart action, booking or checkout steps, filter and search panels | **B Forms and tools** |
| lists, cards, catalogs, search, filters, sorting | **C Lists, search and filters** |
| sign-up, onboarding, gated results, multi-step flows such as wizards or checkout | **D Sign-up and onboarding** |
| prices, plans, upgrade or paywall | **E Pricing and upgrade** |
| app or tool screens with data that can be empty, loading or fail, or actions that change data, or a long detail page whose title or main action scrolls out of view (F2) | **F States and actions** |
| data tables, bulk actions, AI features | **J Product tools** |
| a main navigation (bottom tab bar, top bar, side navigation, website menu) | **I Navigation** |
| print, posters, slides, a page judged as a composition, any image series or card row (G4), any edges that nearly touch (G2) | **G Composition** |
| several pages of one site | **H Multi-page** |
| long content on one page (article, guide, documentation, legal text) | **H3**, even on a single page |

**Select only applicable checks.** Identify the medium, the user task and the evidence available. Read the fixed rules and the relevant mode. Start with A and X, then use the building-block table as an index, and apply clauses only when their feature is present. Triggers that are easy to miss:
- Long content on one page triggers H3.
- An editable filter triggers the relevant B checks (B2 to B5) as well as C.
- A public page with interactive states or writes (a form that sends, a booking, an account) triggers F.
- A price shown as a fact triggers price clarity (E2); plan comparison and upgrade rules (E1, E3) require those actual decisions.
- Static media (print, posters, a single image or slide) use composition (G), legibility and real viewing distance (G3); record the medium and viewing condition, and evaluate a supplied digital companion separately.
- Browser and keyboard procedures (render widths, keyboard pass, reflow, zoom) require an interactive digital surface.

**Use the IDs.** State the route once, as context or medium · mode · applicable IDs, for example "Product · fix · A, X, B2 to B6, C, F" or "Website · audit · A, X, W, G, B, H": in the decision block in create, and in the report directly below the accessibility line. Within the selected sections use the test first (the pass line or the rule), then its rationale, typical mistakes and fixes as needed. Optional enhancements (UX upgrades) do not affect scores.

## Mode create: steps

1. **Decide before building.** Write a short decision block (in the reply or as a comment) before any markup:
   - **Context** and **building blocks** as in the tables above, so the matching sections are known.
   - **Job of the screen:** who arrives, what they want, the one next step, and the one feeling of the first view.
   - **Information order:** what is needed to decide, in which order; what waits; what is left out.
   - **Content:** as in rule 1. Use what was given, ask for what is missing, fill neutral content with realistic demo content marked once as example content; proof that was not given (testimonials, ratings, client logos, certificates, counts) gets a visibly marked slot each and is listed as open; missing prices and package contents get realistic example values, marked once and listed as open.
   - **Look:** if anything exists (a site, an app, a brand, neighbouring sections, a component library), the new part inherits its colors, type, radii, spacing, imagery and component style so it looks as if it had always been there. Only when nothing exists, keep it calm and conventional: one neutral sans-serif family (the system stack is fine), neutrals plus one accent, one radius family, one spacing scale, a few type sizes; no decorative or display typefaces, no second font, no invented logo or masthead styling. Character comes from order, proportion and one honest highlight, not from effects.
2. **Build with the sections as rules.** Every check in A, X and the sections that apply is a build rule, not something to check later. The fixed rules are the floor, not the goal.
3. **Self-check (required).** The build is not done until it has been looked at as a finished page, the way a reviewer would:
   - Render it at about 1280, 768, 375 and 320 px, full page, in every theme offered and in its important states (empty, selected, error, success). Code search alone misses what only shows on the rendered page. For print and other static media, check at real size and viewing distance instead (G3).
   - If nothing can be rendered here, say so in the self-check line, audit from the code and mark each result as checked in code, not rendered.
   - Run the audit steps below on the rendered result.
   - Fix and repeat until there is no blocking finding and every observed, in-scope failure that can be fixed under the fixed rules without inventing content has been corrected and retested. Polish counts: spacing, type, color, details, the footer and the designed states (A3 to A6, A9, F1, W1) are checks, not optional extras. What needs facts from the client stays as a marked suggestion or a marked slot (rule 1) and is listed as open, together with remaining failures, unverified behavior and the evidence or decision each one needs. An unresolved fixed-rule conflict stops at the approval boundary ("When rules meet").

If the audit would still change something, the build is not finished. Only items listed as UX upgrades are optional.

## Mode audit: steps

1. Look at the screen: desktop and mobile screenshots plus HTML/CSS; the first view without scrolling; for flows also the step before and after; for scroll effects judge end states. For print, a full view and a detail; for composition, a view scaled to real size (G3) and a blurred squint view (A3).
2. Name the purpose of the screen, the one feeling the first view should create, the one action it wants, and the moment people might leave.
3. Name context or medium and building blocks (see "What is on the screen"), write the route line, then apply the matching sections and clauses.
4. Stress test: a bright and a busy image, a long or translated title, other content, few and many results, dark mode if offered; look for text and values that wrap onto short lines in narrow columns or panels (a failed A3, fixed by stacking or widening).
5. Walk the path in reading order and mark the decision points (A8). Define one representative task and its observable success condition (for example "books a slot for Tuesday and sees the confirmation"). Distinguish the reviewer's walkthrough from observed user behavior. For an unresolved usability claim, name the task to test, the audience and the observation that would settle it.
6. Record the evidence available for each applicable check: seen (visual inspection), checked (inspected markup or code), operated (observed interaction), measured, or judgment. Keyboard pass on interactive digital surfaces: tab through the screen once in both directions, watching order, focus visibility and traps. For an interactive flow, operate it with the keyboard, including activation, widget keys, dismissal and focus return. Inspect names, roles and states in the accessibility tree. Test announcements and recovery with assistive technology where available. A screenshot supports visual observations only; record runtime behavior (focus, names, announcements, submission) as unverified until exercised.
7. Rate each applicable check Pass, Fail, Unverified or N/A with concrete evidence (element, value, selector) and its evidence label. A confirmed failure in any applicable clause fails the check. Otherwise, any unverified applicable clause makes the check Unverified. N/A requires an absent feature or an inapplicable condition, never missing evidence. For checks written as blocks, rate the pass line; failed sub-points are its evidence, not extra checks. Score each section Pass / (Pass + Fail), counting only applicable checks; show the Unverified and N/A counts separately, neither counts against the score. If nothing in a section was assessed, show "unscored". Compare before and after on the same scope and the same applicable checks.
8. Check the fixed rules; any violation goes into the report.
9. Note the UX upgrades that fit, one line each with the reason.
10. If available, run a contrast or accessibility checker (for example axe) and a design linter (for example `npx impeccable detect <file or url>`) and map their findings to the checks; neither replaces the keyboard pass. Map glows and gradients to A5, kickers and icon tiles to A1, contrast to X1, radius and shadows to A6.
11. Output the report.

## Report format (keep it short)

```
Accessibility: 1 observed blocker, 1 unverified check
Website · audit · A, X, W, G, B, H
A 5/9 · X 4/5 (1 unverified) · W 4/5 · G 3/4 · B 2/7 (1 N/A) · H 2/3

| Check | Result | Evidence | Fix |
|---|---|---|---|
| X1 Contrast | Fail (measured) | Gray body text 3.1:1 | Darken to 4.6:1 within the palette |
| A1 Focus | Fail (judgment) | Hero holds three badges and four buttons | One message, one button, badges below |
| B5 Consequence | Fail (checked) | Calculator shows the price only after "Berechnen" | Live total, button "Angebot für 2.400 € anfragen" |
| X2 Keyboard and focus | Unverified (seen) | Screenshot only; focus return of the dialog not exercised | Operate the dialog by keyboard |
...
Rules: no issues
```

- The whole report, including the table headers, the results (Pass, Fail, Unverified, N/A), the evidence labels (seen, checked, operated, measured, judgment; for example "Erfüllt/Nicht erfüllt/Ungeprüft/Entfällt" in a German request) and the "Rules:" line, is written in the language of the user's request. The template above is English only as an example; German sample labels and euro amounts are localization examples, new examples follow the interface language and locale.
- The report starts with one accessibility line: "Accessibility: [observed blockers], [unverified checks]" (in fix mode before and after on that same line). When coverage is incomplete and no blocker was seen, it says "No blockers observed in the checks performed", never just "no blockers"; "nothing unverified" only when keyboard operation and announcements were actually exercised. Then the route line (context or medium, mode, applicable IDs) and the section scores, as in the example; no further status lines in the head. Confirmed blockers and fixed-rule breaches lead the table.
- Only failed checks and consequential unverified checks as rows, at most twelve, sorted by impact; every further failure is named by ID in one line below the table, not as extra bullets; for each consequential unverified check, name the missing evidence; passed and N/A checks are counted, not listed. These limits apply to how findings are shown, never to what is checked: run every applicable check in full first, then present about twenty findings in all. Blockers are always shown, whatever the count; a page without a viewport meta element fails X6 on real phones even when an emulator shows no sideways scrolling.
- Judgments that only real users can settle are marked "test with users".
- UX upgrades that fit follow in one line each with the reason (`Upgrades: ...`).
- At most one closing sentence: the biggest lever.

## Mode fix: steps

Keep the look: palette, type and content stay, and components keep their style; how much color and weight each element gets is part of the fix (A1, A2, A5): an accent used on many secondary buttons, an alert louder than its importance or secondary actions as loud as the primary one fail and are corrected within the palette; controls that fail B8 are restyled in that same style. The layout may change where a failed check needs it, and everything else in the layout structure stays as it is (for example a summary that must stay visible while choosing, or options that are hard to compare side by side); keep one content container with the same left edge for header, sections and footer. Change existing tokens, components and library variants where a system exists; use a separate CSS layer on top of the original only when there is none, so it stays comparable.

1. Accessibility blockers (X).
2. Focus, first view and information order (A1, A2, A8): what is shown, where and in which order, before any polish; one message, one primary action, the rest moved down or grouped; removals only proposed.
3. Spacing, alignment, composition (A3, G), before type, color and details because everything else sits on them: keep layout moves as small as possible (shift, align, overlap, group); within composition, work on comprehension first (A8 decision points, G3), then calm (weight, G2), then character and order (G1, G4, same place).
4. Typography, color, details (A4 to A6).
5. Content and navigation (A7, C1, C2, I, W, H).
6. Sections B to F and J: defaults, controls, consequence before commit, filters, gates, prices, states, safe actions, tables.
7. Feedback, motion and ending (A9).
8. UX upgrades only when agreed.

Then check the fixed rules, audit again and report before/after scores.

## Output

- create: start with the short decision block, then the build; end with one line on the self-check (widths rendered, audit scores, what remains open or unverified and why).
- audit and fix: the report as above.
- Keep replies short, one point per reply; the report itself is the exception.
- Always output code changes complete and copy-ready in one piece.
- Provide created files or pages as clickable links.

## Rule book

The sections below are the rule book. Apply A and X to everything, clause by clause where the feature is present, and only the other sections in your route line. Checks written as blocks have one pass line; rate the pass line. Failed sub-points are its evidence, not extra checks.

## A Foundation (always)

### A1 Focus and first impression

Pass when: the first view carries one message, one feeling and one primary action where the task has one (per view on websites, per task area in products), and the purpose of the screen is its most obvious element, the largest and highest in contrast.

Includes:
- Name the purpose of the screen and make it the most obvious element; give it room and the best material.
- Secondary actions (newsletter, cancel, back, a second hero action) use a quieter style than the primary action: a text link, not a second button or pill. A header button for the same action stays quieter while the hero button is in view, so the first view never shows two filled primary buttons.
- For a reading, monitoring or status screen, the focal point may be information. Add a primary action only when it serves the task; an article does not need an invented button.
- Where choices require equal visibility, including accept and decline in consent, give the alternatives equal prominence and effort.
- At most one honest highlight among options: a recommendation marked as such and naming who it fits, never preselected; claims about how many people choose it, such as "most chosen" or "for most", only with real data.
- Competing stat bars, badges and kickers are turned down or moved.
- Badges say the minimum ("20% off", not "20% off discount" plus an icon).

Why: the first impression colors everything after it (search term: halo effect); badges must be understood at a glance and must not steal focus.

Typical mistake: badges, gradient headline, two equal buttons, stats and feature cards all compete, sliders, weak or generic imagery, an unclear message.

### A2 Low effort and order

Pass when: a first-time visitor sees the order of importance and the next step without effort.

Includes:
- One primary goal per section.
- Short, predictable navigation.

Why: what is easy to process feels calmer and more trustworthy; effort feels like risk (search term: cognitive fluency).

Typical mistake: many equal elements, long menus, several goals per section, dense text.

### A3 Spacing and alignment

Pass when: one consistent spacing system and one grid hold the screen together, related things sit closer than unrelated ones, and visual weight is spread, not piled in one corner.

Includes:
- One consistent spacing system (for example steps of 4 or 8, or fluid values).
- Related things closer than unrelated ones; spacing is tighter inside a section than between sections; a label sits close to its input.
- One margin and grid for the screen: header, sections and footer on the same container width with the same left and right edge (for example, content always 24 px from the edge). A new section added to an existing page takes its neighbours' width; a shorter line length for text is set inside, not by narrowing the section. Within one screen, a reading column, navigation rail, data workspace or full-bleed image may differ in width when its task requires it, as long as related regions share the grid; this does not loosen the neighbours'-width rule for added sections.
- The main content (the list, table, form or article the screen exists for) comes first and stays visible in the first view. A secondary panel (detail, summary, inspector, filters) sits beside it, or opens as a drawer or sheet; it never moves above the main content when space runs short. When a table does not fit beside its panel, drop, merge or wrap secondary columns, or narrow the panel, before moving the panel.
- Columns only where each keeps a comfortable line length, otherwise stacked rows.
- Steps of a flow run top to bottom in one column of one width.
- Elements of the same kind share size, height and alignment.
- Watch the eye flow: an object pointing at an element must not lead the eye into an overloaded corner where it gets stuck; when it does, move the target element so the eye can continue and the weight spreads across the area.
- Judge the hero by weight, not only by direction, and never stack call to action, badge and image in one corner.
- A squint test (blurred view) shows where mass bunches up.

Why: white space shows relationships, not quantity; misalignment feels untrustworthy even when people can't say why.

Typical mistake: same padding everywhere, elements a few pixels off, too much space between related blocks, narrow side-by-side columns that wrap words or values onto short lines.

### A4 Typography

Pass when: the hierarchy is clear with means that fit the brand (weight, color, spacing, line height, size), with few families and comfortable reading.

Includes:
- One family, two at most.
- Comfortable body line height (for example 1.5 to 1.7, denser in tables) and a comfortably short line length.
- Hierarchy preferably through weight and color rather than size alone: in product screens and inside cards, titles only slightly larger but darker and heavier; the headline of a website's first view takes a clear size step (A1, G3).
- The title stands out without shouting, neither too big, too heavy nor too weak for its role.
- Secondary text in a softer tone that still keeps 4.5:1; paragraphs stay slightly calmer than headlines, within 4.5:1.
- Labels in sentence case, existing ones too: small uppercase labels, tags and captions (also inside mockups and illustrations) become sentence case unless the user names them as a signature element; then slight positive letter spacing stops them looking cramped.
- Headings keep the typeface's default letter spacing, no tighter tracking on headings.

Why: fewer styles give a stronger foundation; the title tells people what they are looking at; headlines attract attention and paragraphs support understanding.

Typical mistake: ever bigger headings, many sizes and styles, hierarchy made by lowering text contrast, cramped small uppercase labels.

### A5 Color

Pass when: the screen is mostly neutrals (tinted toward the brand), with saturation and accent only where attention belongs.

Includes:
- Contrast as in X1.
- The accent goes to the primary button, the focus state and links.
- Repeated or secondary actions (resume, start, edit in every row) stay neutral: a calm neutral fill, the accent at most on hover; the accent belongs to the one main action.
- Several alerts or notices on one screen share one calm tone; severity is carried by icon, label and order, and a strong status color is kept for the one alert that blocks work. An alert is never louder than its importance.
- Decorative gradients on backgrounds, buttons and badges, colored glows and halos are removed.
- A highlight color in text (a colored word in a headline, colored plus signs, tags) is used once per page, at the one place it carries the message; repeated, it stops leading.

Why: too many loud elements kill hierarchy; gradients and glows pull attention to places that do not deserve it.

Typical mistake: gradients and glows everywhere, loud accents on unimportant things.

### A6 Details and consistency

Pass when: one shape language, one shadow style and one icon style run through the screen, with no rendering defects.

Includes:
- One shape language (radius, nested elements slightly smaller).
- Shadows soft and layered, if any, never one heavy blur.
- One icon style, size and stroke; icons in one or two colors with tight spacing, optically on the line of their text; an icon section never dominates the content.
- Subtle or no dividers (tables may need them); dividers stay soft.
- No rendering defects: overlaps, clipped text, bands not reaching the edge, empty grid columns.

Why: icons share one visual logic or become noise; separation should feel smooth, not fenced.

Typical mistake: square and round mixed, heavy dividers, mixed filled and outlined icons, default body margin, harsh edges, one heavy blurred shadow.

### A7 Content and imagery

Pass when: content is specific and believable, and images show what is offered with a clear focal point, sized for their job.

Includes:
- Missing content as in rule 1: use what was given; when real content is missing, ask for it instead of inventing it; in drafts realistic demo content for neutral content instead of bracket placeholders, marked once as example content; proof (testimonials, ratings, client logos, certificates, counts) is never invented, not even as demo, and gets a visibly marked slot listed as open; missing prices and package contents get realistic example values, marked once and listed as open. In fix mode, too, missing facts become clearly marked suggestions.
- Images sized for their job (to recognize or to create desire).
- The image shows the item itself, not hands, and exactly what is offered (one item when it is sold by weight misleads); honest, natural styling. Hands may show use or scale as long as the product stays the focal point.
- One shared look in background, light and angle across a set; compare the series side by side and choose each crop for what it must reveal (G4).
- Text that must always be readable sits beside the photo, not on it. For a controlled composition (a fixed image chosen for it), text may share a focal point with the image if every supported crop and state keeps measured contrast (X1, G3).
- Controls over images get their own container with enough contrast and a subtle outline, tested with a bright and a busy image.
- On service and offer pages, problems may be illustrations and solutions product views in the same style.
- Real photos or references instead of mockups that promise the customer's result.
- Decorative filler images add nothing, content does.

Why: images change and controls must survive every one; an image never lives alone but sits next to others.

Typical mistake: generic stock, mockups promising a result, tiny thumbnails where desire matters, icons readable only on dark photos, pages full of [placeholder] brackets, John Doe, round numbers, vague features, invented testimonials or logos labelled as demo.

### A8 Information order and trust

Pass when: decision-relevant information sits at or before the decision, and the same question is answered in the same place for every item.

Includes:
- The deciding facts (what it is, how good, how much) come early.
- People act step by step, and a note after the action is seen too late: walk through the screen in the user's order and, at every point where they form an opinion or choose, check that they have seen everything that could change it (format requirements at the upload field, variant notes before the add to cart button).
- Answers to the same question (price, date, duration, status) sit in a shared column or row, on the same line as their item, so people can browse or take the shortcut through the same rows; a comparison table instead of facts buried in copy.
- Trust signals sit next to the claim they support.
- No labels the content already explains; a label kept on one item is kept on all comparable items.
- Titles don't contain variable attributes; variants and quantity live in the selection area, not in the title.

Why: late or misleading information creates doubt at the decision point; every extra word slows scanning; people ask "what is it, and can I trust it?" in one look.

Typical mistake: shipping costs after the button, rating far from the title, "Price:" before a price, "Email:" above a field that is already labeled.

### A9 Feedback, motion and ending

Pass when: every action gets quiet feedback, focus is always clearly visible, and every flow ends on purpose.

Includes:
- Every action gets quiet feedback (hover, validation, saved), while focus is always clearly visible.
- Inspect feedback at three moments where it carries information: on page load (what appears first and in which order), while scrolling (reveals, sticky changes, progress) and after an action (confirmation, changed state, the next step).
- Motion starts where the user acted, short and easing out, opening a little slower than closing.
- Menus and dropdowns grow from their trigger, notifications slide in from the edge and stack, sheets follow the finger.
- Movement animates transform and opacity; color and shadow may transition on state changes; layout properties are not animated for movement.
- Positive moments at key points (first success, completion) where the brand carries them.
- Every flow ends on purpose: what happened, what comes next, one useful next step.

Why: people remember an experience by its best moments and its end (search term: peak-end rule).

Typical mistake: static controls, everything fading up the same way, forms ending in a bare "Gesendet".

Calibration: a calm product homepage with one headline and one button (A1), a checkout form with tight, grouped fields (A3), a mostly neutral workspace app with one accent (A5), a notification with matching radius and shadow (A6), a bottom sheet that follows the finger (A9).

## X Accessibility (always; WCAG 2.2 AA for web)

Screen for barriers on the supplied surface. For web work, WCAG 2.2 AA is the target. These are hard minimums: a confirmed violation is a blocking finding, whatever the score elsewhere. The six checks are a screening, not a conformance claim: a claim of conformance requires assessment of all applicable A and AA criteria across the full pages and complete processes in scope. Record the criterion for each standards failure, and record the stricter house requirements of this skill separately (labelled as house rule); both block. For a static print artifact, assess the applicable visual properties (contrast, legibility at viewing distance) and state the medium. Legal frames that require it may be named as context.

| # | Check | Rule |
| --- | --- | --- |
| X1 | **Contrast** | Measure normal text at least 4.5:1 and large text at least 3:1 (large means at least 18 pt regular or 14 pt bold, or equivalent); hierarchy never goes below that. Non-text contrast of at least 3:1 against adjoining colors applies to the visual information needed to identify a control or its state, to focus indicators, to icons that carry meaning and to chart lines. A control whose text label already identifies it needs no visible boundary: a text chip, segment, option card or button on a light tint passes, and a secondary button takes a tinted fill, not an outline ring. Never add outlines or darker borders, and never force dark fills on resting chips, only to reach 3:1. Text inputs keep a boundary of at least 3:1, because an empty field has no other cue. A selected or checked state differs from the unselected state by 3:1 or by a second cue that does not rely on color (a check icon, weight, a label). Only inactive (disabled) controls and logotypes are exempt; check actual surfaces, image crops and states, in every theme offered; in dark themes surfaces separate by lightness, because shadows do not read; meaning conveyed by color keeps a second cue |
| X2 | **Keyboard and focus** | Everything works by keyboard in a sensible order; exercise the task in both directions, including activation and widget keys; focus is clearly visible and never hidden by sticky bars, banners or overlays: keeping the whole indicator visible is the house rule, while WCAG 2.4.11 fails a focused component entirely hidden by author-created content; an active modal dialog or sheet contains focus, Escape dismisses it, and focus returns to the invoker or the logical next step; non-modal panels (a persistent filter panel, an inspector) don't trap focus and stay reachable and escapable in normal page navigation |
| X3 | **Structure and names** | Page title and page language set; real headings in a sensible order and landmarks; a way past repeated navigation; alt text or alternatives for meaningful images; persistent visible labels for data-entry fields (a placeholder is not a label); accessible names for controls and icon buttons, matching the visible wording; programmatic state (expanded, selected, current); validation and status messages announced; media alternatives where applicable |
| X4 | **Operation** | Pointer targets at least 24 × 24 CSS px or a documented WCAG 2.5.8 exception, including adequate spacing (the floor; frequent touch actions and touch bars aim higher, I5); dragging has a single-pointer alternative where required; data already given in the same process isn't asked again; an accessible route through sign-in, without puzzles; nothing essential appears on hover only; inputs declare type and autocomplete so they can be filled automatically; password managers, autofill and paste are never blocked |
| X5 | **Motion and media** | Reduced motion respected and nothing flashes (house rules); qualifying content that moves, blinks or scrolls automatically for more than 5 s, and qualifying auto-updating content, can be paused, stopped or hidden, so no autoplay longer than 5 s without pause; audio that starts automatically and lasts more than 3 s can be paused or stopped or has independent volume control; supplied media have captions, descriptions or alternatives |
| X6 | **Reflow and text resize** | Usable at 320 CSS px width (equivalent to 400 % zoom on a 1280 CSS px viewport) without loss of content or sideways scrolling for vertical content; horizontally flowing content tested at 256 CSS px height; necessary two-dimensional layouts such as maps or comparison tables scroll within their own region; separately, text resized to 200 % (200 % zoom) and user text-spacing overrides lose nothing; sticky controls tested at these sizes |

## W Website duties

| # | Check | Rule |
| --- | --- | --- |
| W1 | **Mandatory links and required information** | Imprint and privacy (provider information and other required disclosures) are reachable from every page, usually in the footer and in the other relevant places (for example at a form that sends data); identify the operator and markets where that changes what is required. In drafts the footer and its links exist, with marked placeholder targets when the URLs are not given; an unresolved legal scope is marked for confirmation and listed as open, never a reason to leave the footer out |
| W2 | **Consent** | Where the service requests consent: banner as in rule 2, declining as visible and easy as accepting, later changes discoverable (for example a footer link), keyboard operable, doesn't cover focus or the main action; the behavior behind each choice is checked when a working implementation is available; a site without a consent request has no banner to style, and an unnecessary banner is friction |
| W3 | **Contact path** | A clear way to get in touch or take the next step, reachable from every page |
| W4 | **Media weight and performance** | Check the real entry view and a key interaction; hero images, videos and web fonts are sized and reserved so they don't delay the first view or shift the layout; the visible primary asset is prioritized and font loading preserves layout; with field data, report the 75th percentile for mobile and desktop: LCP at most 2.5 s, INP at most 200 ms, CLS at most 0.1; lab observations, missing field data and suspected causes are labelled separately; deeper measured values belong to `launch-check` or another specialist launch audit, if available |
| W5 | **Both widths, responsive use** | Checked on mobile and desktop; neither is an afterthought; the first view and the key task tested at mobile and desktop sizes, at the width where a component changes, and with zoom or a virtual keyboard where relevant; for supported locales, long labels, directional layout and formatted numbers, dates and currencies verified; the widths, states and devices actually checked are recorded |

## B Forms and tools

### B1 Smart defaults

Pass when: likely neutral choices are pre-filled, options are cut to what matters, and what can wait is asked later.

Includes:
- A sensible default reads as a recommendation and most people keep it (for example the next free slot already filled in).
- Never prefill consent, paid extras, term, a priced package or plan, or a quantity above the smallest sensible unit (one piece is a neutral default).
- A recommendation may be marked, not preselected; a preselected priced option breaks rule 2.

Why: every open choice is effort and many choices lead to none (search terms: default effect, choice overload).

Typical mistake: empty fields, long option lists, every field a decision.

| # | Check | Rule | Typical mistake |
| --- | --- | --- | --- |
| B2 | **Connected decisions together** | Choices that influence each other are visible at the same time | One page per setting, previous choices invisible |
| B3 | **Right control for the value** | Known values as direct options (tap "3+"; a handful of short choices as chips or segments, not hidden in a select), ranges as slider plus exact input, steppers only for nudging an existing value; "3+" means at least three, and where people are flexible a range between two options is possible; distinguish exactly N, at least N and a bounded range when those meanings change the result, and show which interpretation is active | Steppers to reach a known number, free text where a choice fits |
| B4 | **The user's own terms** | Ask in the terms people know (monthly rate and deposit instead of maximum price, problem instead of product name) and do the conversion for them | Asking for a value people must first calculate |

### B5 Consequence before commit

Pass when: the result updates while choosing and stays in view, and the button names the result.

Includes:
- Where a choice has costs or consequences, the live result and an in-reach action are required; a simple form without a calculated result can pass with an in-flow action and needs consent only when the task requires it.
- The result stays in view while choosing: on wide screens a sticky summary beside the choices, on small screens a compact bar.
- Before anything is chosen it says so instead of showing 0 as a price.
- The button names the result ("41 Angebote anzeigen", "Termin am Di um 9:30 buchen").
- A short total may sit in or beside the button, estimates marked as approximate.
- Button labels stay on one line at every width; a long result detail (price, dates) sits next to or under the button, not inside it.

Why: the button confirms what people are about to do, because they choose first and then act.

Typical mistake: "Absenden", "Berechnen", outcome only after the click, a button label that wraps onto two lines on small screens.

| # | Check | Rule | Typical mistake |
| --- | --- | --- | --- |
| B6 | **Errors and help in place** | Validation inline at the field, help and conditions where the question is asked; each message says what went wrong and how to correct it and is associated with its field; valid entries are kept on failure; long forms may add an error summary that moves focus to it; on a failed multi-field submission, focus moves to a useful destination (the summary or the first field needing attention) and each summary entry links to its field; the primary action stays enabled: if something is missing, clicking it shows the error at the field and moves focus there, instead of a greyed out button that looks dead | Errors only in a list, conditions in a footnote, a disabled submit button with no hint why, entries cleared after a failed submit |

### B7 Presets and action grouping

Pass when: the primary action sits next to its related controls and stays reachable, and a form ends in its reading flow with its own consent and submit.

Includes:
- Where a choice has costs or consequences, the live result and an in-reach action are required; a simple form without a calculated result can pass with an in-flow action and needs consent only when the task requires it.
- One-tap presets for common values next to the custom control; presets come ideally from real usage data (for example 500 g, 1 kg, 2 kg).
- Units sit inside the selector.
- The primary action sits next to its related controls and stays reachable; a sticky action area helps.
- A form ends in its reading flow with its own consent and submit, inside the last section or card of the form, not floating outside it; a sticky summary may repeat the action but never replaces it.
- The primary action stays enabled, as in B6.
- The primary button is refined, never shouting (no all caps, not oversized).

Why: a sticky action area helps because people often decide only after reading further.

Typical mistake: quantity far from the button, action out of view after scrolling, a shouting button in all caps, consent and submit floating below the form card.

### B8 Controls in the system

Pass when: every control shares the page's shape language, sizes and states, and each kind of choice uses one option pattern across the page.

Includes:
- Every control (checkbox, radio, switch, select, date and time fields, file upload, buttons) shares the page's shape language, sizes and states (hover, focus, checked, disabled, error).
- A native control passes when its purpose, states, contrast, target and operation fit the system and it is styled consistently with the page's designed components. It must not look like a raw browser default next to styled components: where the page styles its own components, untouched browser defaults fail this check. A page made only of browser defaults has no style to match: in create and fix its controls get a deliberate style from the given palette and type, as part of the A3 to A6 fixes.
- Replace a native control with a custom widget only for a demonstrated need; styling it needs no such reason. Preserve native semantics and platform behavior (keyboard, mobile pickers) where possible, and test keyboard, touch and forced colors after customization.
- A few short options are shown directly as chips or segments (a select only for long lists).
- Options with details such as a price or description sit each on its own surface with a large target, the extra info aligned to the right and a visible selected state (at least two cues, rule 4).
- One pattern per kind of choice: not bare boxes in one group, chips in another and cards in a third.

Why: the same kind of choice in different shapes reads as different kinds of choice, and raw defaults next to styled parts make the page look unfinished.

Typical mistake: a styled form with a raw file button, default checkboxes and unstyled date fields; three different option patterns for the same kind of choice.

## C Lists, search and filters

| # | Check | Rule | Typical mistake |
| --- | --- | --- | --- |
| C1 | **Worth continuing** | The first items are good enough to make people scroll; images sized for their job; in data tools density is the goal | Tiny thumbnails to fit more items |
| C2 | **Scannable cards** | One clear order per card (name, then the deciding facts, then the rest); details beside or below the image so every card looks consistent whatever image is uploaded | Everything one size and gray, text on photos |
| C3 | **Key filters visible** | The most used filters visible (chips, a bar or a side panel), the rest behind one button, sort beside it; applied filters stay visible and can be removed one by one or all at once; an empty result says which filter to loosen | Filters and sort hidden in drop-downs |
| C4 | **Filters keep results in mind** | Filters open over or beside the results (a sheet on mobile, often a side panel on desktop), all in one scroll; the controls inside follow B2 to B5 | Full-page filter, one page per filter |
| C5 | **Show what a choice costs** | Total count visible, as matches out of the relevant total where that helps ("41 von 312"); counts per option (the predicted count) before choosing; distribution behind range sliders, for the current selection and with its median where it helps; the user's own limit drawn into it if known; label the population and the assumptions behind a personal threshold (for example the interest rate behind an affordable monthly rate); when the trade-off matters and data is available, choose the smallest amount of context that helps the next decision; an unavailable count stays unknown, never estimated as fact | Choose, apply, see nothing left, go back |
| C6 | **Control where no default fits** | When there is no right choice for everyone (cards or compact list, sort order), let people choose | One view forced on all |
| C7 | **Search says what it finds** | Placeholder names what can be searched ("Orte, Gerichte oder Küchen"), plus a visible label or accessible name | "Suchen …" |
| C8 | **Helpers stay quieter than content** | Category, navigation and filter elements are calmer than the items and don't repeat their imagery; a "best match" highlight only when it rests on real data about the user, saying why | Category photos competing with the result photos |
| C9 | **Enough, not everything** | Each added piece of context must help the decision; remove what only adds noise | Every number shown because it exists |

## D Sign-up and onboarding

| # | Check | Rule |
| --- | --- | --- |
| D1 | **Give before you ask** | Where possible, a real, useful part of the result comes before any account or email; the account is offered to save or get more. Gating is fine if it says honestly what people get; receiving something real creates a wish to give back (search term: reciprocity); asking first feels like a wall. Typical mistake: results locked behind sign up, "enter your email to continue" before any value |
| D2 | **Head start** | Visible progress that counts real completed steps, never fake progress or unconfirmed defaults; people speed up the closer they feel to a goal (search term: goal gradient), and the starting line can be set: show where they are and how little is left. Count what the user really did as the first step (the sign-up just completed, the choice just made); if nothing is done yet, show how short the path is instead of an empty meter. Zero is a valid, honest starting point before any step is completed. Typical mistake: progress at 0 % although a real step is already done, a long list of empty steps, the account treated as something before the journey |
| D3 | **Let them build** | Users make a useful choice or create something of their own before the account step when the task permits it. Explain what will be saved, whether an account is required and what happens if they leave. The account step saves their work and is labelled clearly as account creation before the commitment (for example "Konto erstellen und Entwurf speichern" rather than a bare "Weiter" or "Speichern" that hides the account). Preserve work across the transition where feasible and keep the exit visible. People value what they made, and leaving then means abandoning it; two effects differ here: valuing the effort put in (search term: IKEA effect) and valuing what already feels owned (search term: endowment effect). Use both by letting people keep or recover their work, never by raising the cost of leaving. Typical mistake: a sign up screen with nothing of the user's own on it, account creation disguised as "Weiter", work lost on leaving |

## E Pricing and upgrade

| # | Check | Rule |
| --- | --- | --- |
| E1 | **Show what is at stake** | In products, where acting really matters, name the user's concrete loss or limit in their terms (their files, their deadline); on websites avoid fear appeals; the decline stays neutral; losing weighs more than gaining (search term: loss aversion). Where declining an upgrade has no adverse consequence, describe the existing entitlement accurately and allow a neutral exit. Typical mistake: an upgrade screen that only lists features, and nothing changes when it is ignored |
| E2 | **Anchor the cost** | Show the amount payable, currency, payment period, minimum commitment, total commitment and material conditions at the decision; identify mandatory charges and the status of any estimate. Every price stands next to an honest reference with comparable periods, quantities and inclusions: what it covers, per day or unit (a unit or reference price), today's cost, the larger purchase it belongs to; every number is judged against the one seen just before (search term: anchoring). A monthly fee compared with a one-off purchase needs the total fee over the stated term. If no honest comparison helps, the payable price and terms are sufficient. Typical mistake: a price alone on its own screen without terms or reference, a cost without any reference, a monthly fee set against a one-off price |
| E3 | **Clear choice** | One recommended plan at most, comparable rows, everything included listed, no fine print |

## F States and actions

| # | Check | Rule |
| --- | --- | --- |
| F1 | **States designed** | Empty, loading, error and success states exist and say what to do next; for consequential writes also a pending state that blocks repeat activation, a send failure that keeps all input and offers a retry without duplicates, and a success view that confirms what happened and the next step; unsent, in progress, partially completed and saved are distinguishable. Without a backend, build these states and simulate them, marked once as simulated (rule 1); behavior against the real service is listed as unverified, the design itself is not left open |
| F2 | **Context kept** | Title or key context and current selections stay in reach while scrolling, by any means (a sticky header is one option) that never hides focus; one option: content sits in a soft card that slides over the hero image on scroll, and once the image leaves, the title moves into a sticky top bar |
| F3 | **Same function, same form** | The same task looks and works the same on every screen |
| F4 | **Safe actions** | Reversible actions offer undo instead of a dialog; irreversible, legal or financial ones get a review and confirm step that names the consequence; destructive actions look distinct and sit apart from the main action |

## J Product tools

| # | Check | Rule |
| --- | --- | --- |
| J1 | **Data tables** | Numbers right-aligned with tabular figures, units in the header, sorting and the current sort visible, key columns stay in view, readable density; each value keeps its relationship to its row and column headers for assistive technology; the table is named where needed; sorting is keyboard operable and the active sort is exposed programmatically; labels, units and key actions tested in the narrow layout |
| J2 | **Bulk actions** | Selection count visible, actions appear where the selection is, select all says whether it means this page or everything |
| J3 | **AI features** | Say what the feature does; AI output and AI conversation partners are marked as such; show its relevant inputs or sources where they exist, its material limitations and what the user should verify; say how sure it is only with a confidence figure that is validated and helps this decision, never an invented confidence badge; let people stop generation, inspect, edit and undo; distinguish a draft from an external action and interrupted work from completed work; ask for informed confirmation before anything is sent, saved or executed on their behalf, showing the scope and consequence first, then the actual result, with recovery or undo where supported |

## I Navigation

| # | Check | Rule |
| --- | --- | --- |
| I1 | **Only the top level** | The main navigation holds the most important, frequently used destinations; tab bars about three to five; side and site menus may be longer if grouped; rare items (help, sign out, legal) live in a profile or menu; the same destinations in the same order when navigation changes form with width (bar, rail, side navigation) |
| I2 | **Familiar patterns** | Elements keep their usual place (no back or forward button or logo in a bottom bar); one frequent core action may sit prominently in the centre |
| I3 | **Labels for the audience** | Icons alone only for audiences that know the pattern, always with an accessible name; otherwise short, single-line labels, never too small to read |
| I4 | **Clear active state** | At least two visible changes (for example colour plus filled icon, weight or a pill indicator); inactive text keeps 4.5:1 |
| I5 | **Reachable and safe** | Targets at least 24 × 24 px, about 44 × 44 recommended for touch, whatever the icon size; touch targets in a bar about 44 × 44 or more, because 24 × 24 (X4) is the floor, not the goal; the bar sits above system gesture areas and never covers them or the focus; compact enough not to crowd content; tested on two or three widths and a real device |
| I6 | **Calm and consistent** | Familiar, simple icons in one family and visual weight; filled or outlined base sets are both valid (for example outlined, with filled only for the active item); the active destination is distinguishable through two cues, at least one independent of colour, and is exposed programmatically; neutral colours, no colour per destination, the accent only for the active item and the main action; top and bottom navigation share one palette; no boxes around items |
| I7 | **Set apart from content** | Through its own surface or a very soft shadow, not a line |
| I8 | **Badges sparingly** | Only for what really needs attention, small but legible; a dot for presence, a real count when quantity helps; positioned consistently at the icon's upper trailing edge, distinguishable from both the icon and the bar, its meaning exposed in the accessible name or description |
| I9 | **Creative only if usable** | Unusual shapes or positions are fine as long as orientation and operation don't suffer; motion as in A9; consider three events separately: a tap answers at once (colour, scale or ripple), the active marker moves to the new tab, screens change with a short fade or slide; orientation is preserved and reduced motion respected |

## G Composition

| # | Check | Rule |
| --- | --- | --- |
| G1 | **Break the grid on purpose** | Only where two things should visibly interact; accidental outliers corrected; a consistent grid sets an expectation, so the spot that breaks it gets noticed: for example a product reaching into the next area, or an image crossing a section edge or card |

### G2 No near tangencies

Pass when: edges either have clear space or clearly overlap, never almost touch.

Includes:
- On the web, watch images almost touching the viewport edge, a section edge, the header or a neighbour, and near collisions at breakpoints.
- In print, mind binding and bleed.
- For example, an image ending 6 px short of an edge either crosses it clearly or gets clear space.

Why: the thin strip of a near tangency grabs more attention than intended.

Typical mistake: an image or card that ends a few pixels short of an edge or a neighbour, often only at one breakpoint.

### G3 Viewing distance

Pass when: at real size (phone, thumbnail, poster distance) the key message lands in the first second together with the key information, without breaking hierarchy.

Includes:
- Decide what can wait.
- Check the mobile view and the thumbnail and social preview.
- If two things must register at once, give them a shared focal point (for example a date set over a calm, dark area of the photo).
- Text set over an image sits only on a calm area of it, and only on an image that is fixed and chosen for it (see "When rules meet").

Why: at 45 cm on a monitor small things look refined but are unreadable in real use, and enlarging everything breaks hierarchy.

Typical mistake: small type that only works at desk distance; everything enlarged until nothing leads.

| # | Check | Rule |
| --- | --- | --- |
| G4 | **Series** | Fixed constants (type position, baseline, accent), individual crops per image; identical crops look consistent but strip each image of what makes it special; place the series side by side and choose each crop for what it must reveal; this applies to card rows, team photos and case studies |

## H Multi-page

| # | Check | Rule |
| --- | --- | --- |
| H1 | **Same function, same form** | Sections with the same task look the same on every page; readers recognize the pattern and find their way faster |
| H2 | **Sub pages go deeper** | What the main page summarizes isn't repeated as its own section on a sub page |
| H3 | **Long content scannable** | Structure visible at a glance, readers jump to what concerns them |

## UX upgrades (after the checks)

UX upgrades go beyond fixing and make the task easier, not just the screen prettier. Suggest only those that fit, for example a sticky action area (B7), presets for common choices (B7), or a content card over the hero (F2). List them in the report in one line each with the reason (for example: sticky action area, the button leaves the viewport after 900 px) and apply them only when agreed.

## Related

- Logos and brand marks: `logo-design`. Technical launch checks and measured performance: `launch-check`. Copy: `copy-rules`. Charts: a data visualization skill, if installed.
- Motion: dedicated animation and transition skills, if installed. Deeper measurable checks: Impeccable (detect, critique, audit) or Hallmark (sloplint).
- The original visual, refinement, layout and psychology guidance is integrated in A to J, W and X; all required decisions and tests are defined in this file. Named tools and specialist skills are optional.
- Single-topic deep dives remain available where installed: `ui-principles`, `ui-refinement`, `layout-refinement`, `ux-psychology`. This skill replaces them as the rule set; where they differ, this one is right.

---
name: design-quality
description: One skill for designing and reviewing websites, landing pages, app and SaaS screens, dashboards, forms, interactive tools (calculators, configurators, requirement catalogs), lists with search and filters, data tables, sign-up, onboarding, pricing, navigation, and print or slides. Mode create guides a new page, screen, component or section from the first decision on; modes audit and fix check and improve what already exists. All modes use the same fixed rules (surfaces not lines, no side accent bars, WCAG 2.2 AA, no dark patterns, brand and corporate colors fixed, component libraries such as shadcn/ui and Tailwind used as intended) and the same sections per building block, so building and reviewing arrive at the same result. Use this skill whenever something is designed, built, redesigned, extended with a new section, reviewed, polished, made less generic or AI-looking, converts poorly, feels cluttered or cheap, or needs an accessibility or UI/UX check, even if the user only says "build", "make", "design" or "check" and names no principle.
---

# Design Quality

Good and generic interfaces often use the same components. The difference lies in focus, order, a few details, and how well the screen helps people decide. This skill holds one set of rules and uses it in three ways: to decide and build (create), to check (audit) and to improve (fix). Because all modes use the same rules, a page built here and a page reviewed here should end up alike. Keep only what carries the decision; improving usually means removing, not adding.

Fixed rules and the accessibility block are hard requirements. Everything else is a principle: numbers in it are examples, and the right means depends on the brand and context.

## Modes

- **create**: a new page, screen, component or section, or a redesign from scratch. Decide, build with the sections as build rules, then run the audit on the rendered result and fix until it passes.
- **audit**: check only, report with scores.
- **fix**: improve following the fix order, then audit again.
- No mode given: something to build means create; something existing means audit first, then ask whether to fix.

## Fixed rules (override everything below)

1. **Everything shown is true.** Progress counts only real steps the user did or confirmed, result counts are real, deadlines exist, losses are the user's actual loss. No invented numbers, ratings, logos, testimonials or scarcity presented as real; in drafts, realistic demo content is fine when it is marked once as example content.
2. **No dark patterns.** Declining stays easy and neutrally worded; no shaming labels, no hidden close buttons, no invented countdowns or scarcity. Never preselect consent, newsletters, paid extras, a priced package, data sharing or longer contracts. In consent banners, declining is as easy and visible as accepting.
3. **Surfaces, not lines.** Cards and tiles get no thin border lines; separate with surfaces and spacing, shadows optional and soft. Borders only on inputs and controls. A transparent outline is allowed as a fallback for forced colors (high contrast mode).
4. **No side accent bars.** Never mark a card, row, alert, quote or selected item with a thicker colored edge on one side (left or right border, inset shadow, pseudo-element stripe); it is the most typical generic AI pattern. Mark state through the surface itself (a tinted background), weight, an icon, a dot or a label. In audits, an existing side bar is a rule violation; in fixes, replace it.
5. **Brand and look are fixed.** A given palette, corporate colors, type and component style are kept: invent no new hues and no new style for one section or tool; only how the colors are used is decided or reviewed. Tints, shades and status colors derived from the palette are fine; meaning never rests on color alone. Palette changes may only be recommended when the whole site or product is in scope, as a marked suggestion with the reason (for example contrast), never applied.
6. **Content stays.** In fix mode, move, group or shorten; removing visible content is only proposed, never done silently. Microcopy a rule is about (button and decline labels, a progress line, a price reference, a confirmation) may change, and markup may change for accessibility. German copy follows `copy-rules` if available.
7. **Signature elements** the user names stay untouched.
8. **No generic AI look.** No gradient headlines, glows, glass for its own sake, decorative badges, emoji icons, rows of identical feature cards, stat strips without a source, or everything centered by default.
9. No em or en dashes in copy.
10. **Reuse before inventing.** Existing tokens, components and global classes come before new values. Component libraries and utility frameworks (for example shadcn/ui on Tailwind, or blocks built on them) are used as intended, with their components, variants, theme variables, utility classes and conventions; adaptations go through their theme tokens, variants or classes, never `!important` overrides, hard-coded values or forked copies. A library default that conflicts with a rule here (for example a card with a border) is solved once in the theme or a variant.

## What is on the screen (all modes)

**Context** sets priorities, not which sections apply:

| Context | Weigh more |
| --- | --- |
| Website (marketing, company, service) | First impression, clarity of message, trust, reading flow, the website duties in W |
| Product (app, SaaS, tool, portal) | Efficiency, density, control, states (empty, loading, error), consistency across screens |
| Print, poster, slides | Composition, viewing distance, series |

**Building blocks** decide the sections. A website with a cost calculator gets section B; an app screen with a result list gets section C.

| If the screen has … | Apply |
| --- | --- |
| anything | **A Foundation**, **X Accessibility** |
| a public website | **W Website duties** |
| forms, interactive tools, calculators, configurators, requirement catalogs, booking or checkout steps | **B Forms and tools** |
| lists, cards, catalogs, search, filters, sorting | **C Lists, search and filters** |
| sign-up, onboarding, gated results | **D Sign-up and onboarding** |
| prices, plans, upgrade or paywall | **E Pricing and upgrade** |
| app or tool screens with data that can be empty, loading or fail, or actions that change data | **F States and actions** |
| data tables, bulk actions, AI features | **J Product tools** |
| a main navigation (bottom tab bar, top bar, side navigation, website menu) | **I Navigation** |
| print, posters, slides, or a page judged as a composition | **G Composition** |
| several pages of one site | **H Multi-page** |

Name the context and the sections you apply in one line at the top of the report or the decision block.

## A Foundation (always)

| # | Check | Rule | Typical mistake |
| --- | --- | --- | --- |
| A1 | **Focus and first impression** | The first view carries one message, one feeling and one primary action (per view on websites, per task area in products); secondary actions (newsletter, cancel, back) use a quieter style than the primary action; at most one honest highlight among options (a recommendation marked as such and naming who it fits, never preselected; claims about how many people choose it, such as "most chosen" or "for most", only with real data); the first impression colors everything after it | Badges, gradient headline, two equal buttons, stats and feature cards all compete |
| A2 | **Low effort and order** | A first-time visitor sees the order of importance and the next step without effort; one primary goal per section; short, predictable navigation | Many equal elements, long menus, several goals per section |
| A3 | **Spacing and alignment** | One consistent spacing system (for example steps of 4 or 8, or fluid values); related things closer than unrelated ones; one margin and grid for the screen, header, sections and footer on the same container width with the same left and right edge (a new section added to an existing page takes its neighbours' width; a shorter line length for text is set inside, not by narrowing the section); visual weight spread, not piled in one corner; columns only where each keeps a comfortable line length, otherwise stacked rows; steps of a flow run top to bottom in one column of one width; elements of the same kind share size, height and alignment | Same padding everywhere, elements a few pixels off, too much space between related blocks, narrow side-by-side columns that wrap words or values onto short lines |
| A4 | **Typography** | Clear hierarchy with means that fit the brand (weight, color, spacing, size); few families; comfortable body line height (for example 1.5 to 1.7, denser in tables) and a comfortably short line length | Ever bigger headings, many sizes and styles, hierarchy made by lowering text contrast |
| A5 | **Color** | Mostly neutrals (tinted toward the brand), saturation and accent only where attention belongs; contrast as in X1 | Gradients and glows everywhere, loud accents on unimportant things |
| A6 | **Details and consistency** | One shape language (radius, nested elements slightly smaller), soft shadows if any, one icon style, size and stroke, icons optically on the line of their text, subtle or no dividers (tables may need them), no rendering defects (overlaps, clipped text, bands not reaching the edge) | Square and round mixed, heavy dividers, mixed filled and outlined icons, default body margin |
| A7 | **Content and imagery** | Specific, believable content; in drafts realistic demo content instead of bracket placeholders, marked once as example content; images show what is offered with a clear focal point, sized for their job (to recognize or to create desire); one shared look across a set; controls over images get their own contrasting container; text that must always be readable sits beside the photo, not on it | Generic stock, mockups promising a result, tiny thumbnails where desire matters, icons readable only on dark photos, pages full of [placeholder] brackets |
| A8 | **Information order and trust** | Decision-relevant information sits at or before the decision; the same question is answered in the same place for every item; trust signals sit next to the claim they support; no labels the content already explains; titles don't contain variable attributes | Shipping costs after the button, rating far from the title, "Price:" before a price |
| A9 | **Feedback, motion and ending** | Every action gets quiet feedback (hover, validation, saved), while focus is always clearly visible; motion starts where the user acted, short and easing out, opening a little slower than closing; positive moments at key points (first success, completion) where the brand carries them; every flow ends on purpose: what happened, what comes next, one useful next step | Static controls, everything fading up the same way, forms ending in a bare "Gesendet" |

## X Accessibility (always, WCAG 2.2 AA)

Hard minimums. A violation is a blocking finding, whatever the score elsewhere. Legal frames that require it may be named as context.

| # | Check | Rule |
| --- | --- | --- |
| X1 | **Contrast** | Text at least 4.5:1, large text and meaningful UI parts (controls, focus, icons, chart lines) at least 3:1; hierarchy never goes below that; only disabled items are exempt |
| X2 | **Keyboard and focus** | Everything works by keyboard in a sensible order; focus is clearly visible and never hidden by sticky bars, banners or overlays; dialogs and sheets trap and return focus, Escape closes |
| X3 | **Structure and names** | Real headings and landmarks, page language set, alt text for meaningful images, visible labels (a placeholder is not a label), accessible names for icon buttons, status messages announced |
| X4 | **Operation** | Targets at least 24 × 24 px; dragging has a single-pointer alternative; data already given isn't asked again; sign-in without puzzles |
| X5 | **Motion** | Reduced motion respected; no autoplay longer than 5 s without pause; nothing flashes |
| X6 | **Reflow** | Usable at 320 px width and 200 % zoom without loss of content or sideways scrolling |

## W Website duties

| # | Check | Rule |
| --- | --- | --- |
| W1 | **Mandatory links** | Imprint and privacy are reachable from every page |
| W2 | **Consent** | Banner as in rule 2, keyboard operable, doesn't cover focus or the main action |
| W3 | **Contact path** | A clear way to get in touch or take the next step, reachable from every page |
| W4 | **Media weight** | Hero images, videos and web fonts are sized and reserved so they don't delay the first view or shift the layout; measured values belong to `launch-check` |
| W5 | **Both widths** | Checked on mobile and desktop; neither is an afterthought |

## B Forms and tools

| # | Check | Rule | Typical mistake |
| --- | --- | --- | --- |
| B1 | **Smart defaults** | Likely neutral choices are pre-filled, options cut to what matters, what can wait is asked later; never prefill consent, paid extras, term, a priced package or plan, or price-relevant quantities (a recommendation may be marked, not preselected; a preselected priced option breaks rule 2) | Empty fields, long option lists, every field a decision |
| B2 | **Connected decisions together** | Choices that influence each other are visible at the same time | One page per setting, previous choices invisible |
| B3 | **Right control for the value** | Known values as direct options (tap "3+"; a handful of short choices as chips or segments, not hidden in a select), ranges as slider plus exact input, steppers only for nudging an existing value; "3+" means at least three, and where people are flexible a range between two options is possible | Steppers to reach a known number, free text where a choice fits |
| B4 | **The user's own terms** | Ask in the terms people know (monthly rate and deposit instead of maximum price, problem instead of product name) and do the conversion for them | Asking for a value people must first calculate |
| B5 | **Consequence before commit** | The result updates while choosing and stays in view while choosing (on wide screens a sticky summary beside the choices, on small screens a compact bar); before anything is chosen it says so instead of showing 0 as a price; the button names the result ("41 Angebote anzeigen", "Termin am Di um 9:30 buchen"); a total may sit in or beside the button, estimates marked as approximate | "Absenden", "Berechnen", outcome only after the click |
| B6 | **Errors and help in place** | Validation inline at the field, help and conditions where the question is asked; long forms may add an error summary that moves focus to it | Errors only in a list, conditions in a footnote |
| B7 | **Presets and action grouping** | One-tap presets for common values next to the custom control; the primary action sits next to its related controls and stays reachable; a form ends in its reading flow with its own consent and submit, and a sticky summary may repeat the action but never replaces it | Quantity far from the button, action out of view after scrolling |
| B8 | **Controls in the system** | Every control (checkbox, radio, switch, select, date and time fields, file upload, buttons) shares the page's shape language, sizes and states (hover, focus, checked, disabled, error); where the page styles its own components, untouched browser defaults fail this check. Selectable options use one pattern per kind of choice across the page: a few short options are shown directly as chips or segments (a select only for long lists), options with details such as a price or description sit each on its own surface with a large target, the extra info aligned to the right and a visible selected state; not bare boxes in one group, chips in another and cards in a third | A styled form with a raw file button, default checkboxes and unstyled date fields; three different option patterns for the same kind of choice |

## C Lists, search and filters

| # | Check | Rule | Typical mistake |
| --- | --- | --- | --- |
| C1 | **Worth continuing** | The first items are good enough to make people scroll; images sized for their job; in data tools density is the goal | Tiny thumbnails to fit more items |
| C2 | **Scannable cards** | One clear order per card (name, then the deciding facts, then the rest); details beside or below the image so every card looks consistent whatever image is uploaded | Everything one size and gray, text on photos |
| C3 | **Key filters visible** | The most used filters visible (chips, a bar or a side panel), the rest behind one button, sort beside it | Filters and sort hidden in drop-downs |
| C4 | **Filters keep results in mind** | Filters open over or beside the results (a sheet on mobile, often a side panel on desktop), all in one scroll | Full-page filter, one page per filter |
| C5 | **Show what a choice costs** | Total count visible; counts per option before choosing; distribution behind range sliders; the user's own limit drawn into it if known | Choose, apply, see nothing left, go back |
| C6 | **Control where no default fits** | When there is no right choice for everyone (cards or compact list, sort order), let people choose | One view forced on all |
| C7 | **Search says what it finds** | Placeholder names what can be searched ("Orte, Gerichte oder Küchen"), plus a visible label or accessible name | "Suchen …" |
| C8 | **Helpers stay quieter than content** | Category, navigation and filter elements are calmer than the items and don't repeat their imagery; a "best match" highlight only when it rests on real data about the user, saying why | Category photos competing with the result photos |
| C9 | **Enough, not everything** | Each added piece of context must help the decision; remove what only adds noise | Every number shown because it exists |

## D Sign-up and onboarding

| # | Check | Rule |
| --- | --- | --- |
| D1 | **Give before you ask** | Where possible, a real, useful part of the result comes before any account or email; the account is offered to save or get more. Gating is fine if it says honestly what people get |
| D2 | **Head start** | Visible progress that counts real completed steps, never fake progress or unconfirmed defaults |
| D3 | **Let them build** | Users make choices of their own before the account step; the account step saves their work ("Weiter", "Speichern") |

## E Pricing and upgrade

| # | Check | Rule |
| --- | --- | --- |
| E1 | **Show what is at stake** | In products, where acting really matters, name the user's concrete loss or limit in their terms (their files, their deadline); on websites avoid fear appeals; the decline stays neutral |
| E2 | **Anchor the cost** | Every price stands next to an honest reference: what it covers, per day or unit, today's cost, the larger purchase it belongs to |
| E3 | **Clear choice** | One recommended plan at most, comparable rows, everything included listed, no fine print |

## F States and actions

| # | Check | Rule |
| --- | --- | --- |
| F1 | **States designed** | Empty, loading, error and success states exist and say what to do next |
| F2 | **Context kept** | Title or key context and current selections stay in reach while scrolling, by any means (a sticky header is one option) that never hides focus |
| F3 | **Same function, same form** | The same task looks and works the same on every screen |
| F4 | **Safe actions** | Reversible actions offer undo instead of a dialog; irreversible, legal or financial ones get a review and confirm step that names the consequence; destructive actions look distinct and sit apart from the main action |

## J Product tools

| # | Check | Rule |
| --- | --- | --- |
| J1 | **Data tables** | Numbers right-aligned with tabular figures, units in the header, sorting and the current sort visible, key columns stay in view, readable density |
| J2 | **Bulk actions** | Selection count visible, actions appear where the selection is, select all says whether it means this page or everything |
| J3 | **AI features** | Say what the feature does and how sure it is, show sources or inputs where they exist, let people stop, edit and undo, and ask before anything is sent, saved or executed on their behalf |

## I Navigation

| # | Check | Rule |
| --- | --- | --- |
| I1 | **Only the top level** | The main navigation holds the most important, frequently used destinations; tab bars about three to five; side and site menus may be longer if grouped; rare items (help, sign out, legal) live in a profile or menu |
| I2 | **Familiar patterns** | Elements keep their usual place (no back button or logo in a bottom bar); one frequent core action may sit prominently in the centre |
| I3 | **Labels for the audience** | Icons alone only for audiences that know the pattern, always with an accessible name; otherwise short, single-line labels, never too small to read |
| I4 | **Clear active state** | At least two visible changes (for example colour plus filled icon, weight or a pill indicator); inactive text keeps 4.5:1 |
| I5 | **Reachable and safe** | Targets at least 24 × 24 px, about 44 × 44 recommended for touch, whatever the icon size; the bar sits above system gesture areas and never covers them or the focus; compact enough not to crowd content; tested on two or three widths and a real device |
| I6 | **Calm and consistent** | Familiar, simple icons in one style (filled only for the active item); neutral colours, no colour per destination, the accent only for the active item and the main action; top and bottom navigation share one palette; no boxes around items |
| I7 | **Set apart from content** | Through its own surface or a very soft shadow, not a line |
| I8 | **Badges sparingly** | Only for what really needs attention, small but legible |
| I9 | **Creative only if usable** | Unusual shapes or positions are fine as long as orientation and operation don't suffer; motion as in A9 |

## G Composition

| # | Check | Rule |
| --- | --- | --- |
| G1 | **Break the grid on purpose** | Only where two things should visibly interact; accidental outliers corrected |
| G2 | **No near tangencies** | Edges either have clear space or clearly overlap, never almost touch |
| G3 | **Viewing distance** | At real size (phone, thumbnail, poster distance) the key message lands in the first second without breaking hierarchy |
| G4 | **Series** | Fixed constants (type position, baseline, accent), individual crops per image |

## H Multi-page

| # | Check | Rule |
| --- | --- | --- |
| H1 | **Same function, same form** | Sections with the same task look the same on every page |
| H2 | **Sub pages go deeper** | What the main page summarizes isn't repeated as its own section on a sub page |
| H3 | **Long content scannable** | Structure visible at a glance, readers jump to what concerns them |

## Mode create: steps

1. **Decide before building.** Write a short decision block (in the reply or as a comment) before any markup:
   - **Context** and **building blocks** as in the tables above, so the matching sections are known.
   - **Job of the screen:** who arrives, what they want, the one next step.
   - **Information order:** what is needed to decide, in which order; what waits; what is left out.
   - **Look:** if anything exists (a site, an app, a brand, neighbouring sections, a component library), the new part inherits its colors, type, radii, spacing, imagery and component style so it looks as if it had always been there. Only when nothing exists, keep it calm and conventional: one neutral sans-serif family (the system stack is fine), neutrals plus one accent, one radius family, one spacing scale, a few type sizes; no decorative or display typefaces, no second font, no invented logo or masthead styling. Character comes from order, proportion and one honest highlight, not from effects.
2. **Build with the sections as rules.** Every check in A, X and the sections that apply is a build rule, not something to check later. The fixed rules are the floor, not the goal.
3. **Self-check (required).** The build is not done until it has been looked at as a finished page, the way a reviewer would:
   - Render it at about 1280, 375 and 320 px, full page, and in its important states (empty, selected, error, success). Code search alone misses what only shows on the rendered page.
   - Run the audit steps below on the rendered result.
   - Fix and repeat until there is no blocking finding and no failed check that can be fixed without inventing content. What needs facts from the client stays as a marked suggestion.

If the audit would still change something, the build is not finished.

## Mode audit: steps

1. Look at the screen: desktop and mobile screenshots plus HTML/CSS; the first view without scrolling; for flows also the step before and after; for scroll effects judge end states.
2. Name context and building blocks (see "What is on the screen"), then apply the matching sections.
3. Stress test: a bright and a busy image, a long or translated title, other content, few and many results, dark mode if offered; look for text and values that wrap onto short lines in narrow columns or panels (a failed A3, fixed by stacking or widening).
4. Keyboard pass: tab through the screen once, watching order, focus visibility and traps.
5. Rate each applicable check Yes, No or n/a with concrete evidence (element, value, selector), marked as measured, checked or judgment.
6. Check the fixed rules; any violation goes into the report.
7. If available, run a contrast or accessibility checker (for example axe) and a design linter (for example `npx impeccable detect <file or url>`) and map their findings to the checks; neither replaces the keyboard pass.
8. Output the report.

## Report format (keep it short)

```
Website · A, X, W, B, H
A11y: 1 blocking

# A 5 / 9 · X 5 / 6 · W 4 / 5 · B 2 / 7 · H 2 / 3

| Check | Result | Evidence | Fix |
|---|---|---|---|
| X1 Contrast | No (measured) | Gray body text 3.1:1 | Darken to 4.6:1 within the palette |
| A1 Focus | No (judgment) | Hero holds three badges and four buttons | One message, one button, badges below |
| B5 Consequence | No (checked) | Calculator shows the price only after "Berechnen" | Live total, button "Angebot für 2.400 € anfragen" |
...
Rules: no issues
```

- The line `A11y: n blocking` comes first; blocking findings lead the table.
- Only failed checks as rows, at most twelve, sorted by impact; further failures are named in one line below the table; passed and n/a checks are counted, not listed. The new sections make the report more complete, not longer.
- Judgments that only real users can settle are marked "test with users".
- At most one closing sentence: the biggest lever.

## Mode fix: steps

Keep the look: colors, type and content stay, and components keep their style; controls that fail B8 are restyled in that same style. The layout may change where a failed check needs it (for example a summary that must stay visible while choosing, or options that are hard to compare side by side); keep one content container with the same left edge for header, sections and footer. Change existing tokens, components and library variants where a system exists; use a separate CSS layer on top of the original only when there is none, so it stays comparable.

1. Accessibility blockers (X).
2. Focus and first view (A1, A2): one message, one primary action, the rest moved down or grouped; removals only proposed.
3. Spacing, alignment, composition (A3, G).
4. Typography, color, details (A4 to A6).
5. Content, information order and navigation (A7, A8, C1, C2, I, W).
6. Sections B to F and J: defaults, controls, consequence before commit, filters, gates, prices, states, safe actions, tables.
7. Feedback, motion and ending (A9).

Then check the fixed rules, audit again and report before/after scores.

## Output

- create: start with the short decision block, then the build; end with one line on the self-check (widths rendered, audit scores, what remains open and why).
- audit and fix: the report as above.
- Keep replies short, one point per reply; the report itself is the exception.
- Always output code changes complete and copy-ready in one piece.
- Provide created files or pages as clickable links.

## Related

- Logos and brand marks: `logo-design`. Technical launch checks and measured performance: `launch-check`. Copy: `copy-rules`.
- Single-topic deep dives remain available: `ui-principles`, `ui-refinement`, `layout-refinement`, `ux-psychology`.

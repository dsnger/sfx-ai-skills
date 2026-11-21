---
name: design-review
description: One combined review and refinement of websites, landing pages, app and SaaS screens, forms, interactive tools (calculators, configurators, requirement catalogs), lists with search and filters, data tables, sign-up and onboarding, pricing and upgrade screens, navigation, and print or slides. Always checks the foundation and accessibility (WCAG 2.2 AA), then detects which building blocks are on the screen and applies only the matching sections, prioritized by context (website or product), honestly and without dark patterns, with a score per section and one merged short report. Use this skill whenever a page or screen should be reviewed, polished, made less generic or AI-looking, converts poorly, feels cluttered or cheap, needs an accessibility check, or a design check, UI/UX review or audit is requested, even if no principle is named.
---

# Design Review

Good and generic interfaces often use the same components. The difference lies in focus, order, a few details, and how well the screen helps people decide. This skill reviews a screen in one pass: it looks at what is actually on it and applies only what fits. Keep only what carries the decision; improving usually means removing, not adding.

Fixed rules and the accessibility block are hard requirements. Everything else is a principle: numbers in it are examples, and the right means depends on the brand and context.

## Modes

- **audit**: check only, report with scores.
- **fix**: improve following the fix order, then audit again.
- No mode given: audit first, then ask whether to fix.

## Fixed rules (override everything below)

1. **Everything shown is true.** Progress counts only real steps the user did or confirmed, result counts are real, deadlines exist, losses are the user's actual loss. Missing facts become placeholders, never inventions.
2. **No dark patterns.** Declining stays easy and neutrally worded; no shaming labels, no hidden close buttons, no invented countdowns or scarcity. Never preselect consent, newsletters, paid extras, a priced package, data sharing or longer contracts. In consent banners, declining is as easy and visible as accepting.
3. **Surfaces, not lines.** Cards and tiles get no thin border lines; separate with surfaces and spacing, shadows optional and soft. Borders only on inputs and controls. A transparent outline is allowed as a fallback for forced colors (high contrast mode).
4. **No side accent bars.** Never mark a card, row, alert, quote or selected item with a thicker colored edge on one side (left or right border, inset shadow, pseudo-element stripe); it is the most typical generic AI pattern. Mark state through the surface itself (a tinted background), weight, an icon or a label. In audits, an existing side bar is a rule violation; in fixes, replace it.
5. **Brand palette is fixed** if one is given: invent no new hues; only the use of the colors is reviewed. When the whole site or product is reviewed, palette changes may be recommended as a marked suggestion with the reason (for example contrast), never applied. Tints, shades and status colors derived from the palette are fine; meaning never rests on color alone.
6. **Content stays.** Demo content is fine in drafts (A7 checks that it is believable, not that it is real). In fix mode, move, group or shorten; removing visible content is only proposed, never done silently. Microcopy a rule is about (button and decline labels, a progress line, a price reference, a confirmation) may change, and markup may change for accessibility. German copy follows `copy-rules` if available.
7. **Signature elements** the user names stay untouched.
8. No em or en dashes in copy.
9. **Reuse before inventing.** Existing tokens, components and global classes come before new values. Component libraries and utility frameworks (for example shadcn/ui on Tailwind) are used as intended; fixes go through their theme tokens, variants or classes, never `!important` overrides or forked copies.

## Step 1: What is on the screen?

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

Name the context and the sections you apply in one line at the top of the report.

## A Foundation (always)

| # | Check | Rule | Typical mistake |
| --- | --- | --- | --- |
| A1 | **Focus and first impression** | The first view carries one message, one feeling and one primary action (per view on websites, per task area in products); secondary actions (newsletter, cancel, back) use a quieter style than the primary action; the first impression colors everything after it | Badges, gradient headline, two equal buttons, stats and feature cards all compete |
| A2 | **Low effort and order** | A first-time visitor sees the order of importance and the next step without effort; one primary goal per section; short, predictable navigation | Many equal elements, long menus, several goals per section |
| A3 | **Spacing and alignment** | One consistent spacing system (for example steps of 4 or 8, or fluid values); related things closer than unrelated ones; one margin and grid for the screen, header, sections and footer on the same container width and left edge; visual weight spread, not piled in one corner; columns only where each keeps a comfortable line length, otherwise stacked rows | Same padding everywhere, elements a few pixels off, too much space between related blocks, narrow side-by-side columns that wrap words or values onto short lines |
| A4 | **Typography** | Clear hierarchy with means that fit the brand (weight, color, spacing, size); few families; comfortable body line height (for example 1.5 to 1.7, denser in tables) and a comfortably short line length | Ever bigger headings, many sizes and styles, hierarchy made by lowering text contrast |
| A5 | **Color** | Mostly neutrals (tinted toward the brand), saturation and accent only where attention belongs; contrast as in X1 | Gradients and glows everywhere, loud accents on unimportant things |
| A6 | **Details and consistency** | One shape language (radius, nested elements slightly smaller), soft shadows if any, one icon style, size and stroke, icons optically on the line of their text, subtle or no dividers (tables may need them), no rendering defects (overlaps, clipped text, bands not reaching the edge) | Square and round mixed, heavy dividers, mixed filled and outlined icons, default body margin |
| A7 | **Content and imagery** | Specific, believable content; images show what is offered with a clear focal point, sized for their job (to recognize or to create desire); one shared look across a set; controls over images get their own contrasting container; text that must always be readable sits beside the photo, not on it | Generic stock, mockups promising a result, tiny thumbnails where desire matters, icons readable only on dark photos |
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
| B3 | **Right control for the value** | Known values as direct options (tap "3+"), ranges as slider plus exact input, steppers only for nudging an existing value; "3+" means at least three, and where people are flexible a range between two options is possible | Steppers to reach a known number, free text where a choice fits |
| B4 | **The user's own terms** | Ask in the terms people know (monthly rate and deposit instead of maximum price, problem instead of product name) and do the conversion for them | Asking for a value people must first calculate |
| B5 | **Consequence before commit** | The result updates while choosing and stays in view while choosing (on wide screens a sticky summary beside the choices, on small screens a compact bar); before anything is chosen it says so instead of showing 0 as a price; the button names the result ("41 Angebote anzeigen", "Termin am Di um 9:30 buchen"); a total may sit in or beside the button, estimates marked as approximate | "Absenden", "Berechnen", outcome only after the click |
| B6 | **Errors and help in place** | Validation inline at the field, help and conditions where the question is asked; long forms may add an error summary that moves focus to it | Errors only in a list, conditions in a footnote |
| B7 | **Presets and action grouping** | One-tap presets for common values next to the custom control; the primary action sits next to its related controls and stays reachable | Quantity far from the button, action out of view after scrolling |

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

## Audit: steps

1. Look at the screen: desktop and mobile screenshots plus HTML/CSS; the first view without scrolling; for flows also the step before and after; for scroll effects judge end states.
2. Do step 1: context and building blocks, then the sections that apply.
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

## Fix: steps

Keep the look: colors, type, components and content stay. The layout may change where a failed check needs it (for example a summary that must stay visible while choosing, or options that are hard to compare side by side); keep one content container with the same left edge for header, sections and footer. Change existing tokens, components and library variants where a system exists; use a separate CSS layer on top of the original only when there is none, so it stays comparable.

1. Accessibility blockers (X).
2. Focus and first view (A1, A2): one message, one primary action, the rest moved down or grouped; removals only proposed.
3. Spacing, alignment, composition (A3, G).
4. Typography, color, details (A4 to A6).
5. Content, information order and navigation (A7, A8, C1, C2, I, W).
6. Sections B to F and J: defaults, controls, consequence before commit, filters, gates, prices, states, safe actions, tables.
7. Feedback, motion and ending (A9).

Then check the fixed rules, audit again and report before/after scores.

## Output

- Keep replies short, one point per reply; the report itself is the exception.
- Always output code changes complete and copy-ready in one piece.
- Provide created files or pages as clickable links.

## Related

- Logos and brand marks: `logo-design`. Technical launch checks and measured performance: `launch-check`. Copy: `copy-rules`.
- Single-topic deep dives remain available: `ui-principles`, `ui-refinement`, `layout-refinement`, `ux-psychology`.

---
name: design-quality
description: 'Audits, refines, improves and fixes websites, landing pages, mockups, app screens, product pages, posters, presentations, print, forms, sign-up and onboarding flows, upgrade dialogs, paywalls and pricing, with scores: 7 principles of good UI, detail-level UI/UX mistakes, 7 layout techniques, 9 principles of how people perceive and decide, honestly and without dark patterns. Suggests UX upgrades (sticky actions, presets). Use whenever a page looks AI-generated or generic, a screen needs polish, feels cluttered or "almost right", a layout feels off, busy, unbalanced or hard to scan, a site feels cheap or untrustworthy, a flow converts poorly, users drop off, a product or detail page, form, onboarding, sign-up, upgrade or checkout is designed or reviewed, a UI check, design review, visual polish or composition review is requested, or someone asks what is wrong with a UI or about UX psychology, conversion, "premium feel" or "why don''t users finish this", even if no principle, technique or "refinement" is named.'
---

# Design Quality

Run all four blocks one after another and finish each block completely before starting the next.

## Modes

- **audit**: `ui-principles`, `ui-refinement`, `ux-psychology`: check only, report with score. `layout-refinement`: check the layout, report with score x / 7.
- **fix**: `ui-principles`: refine following the sequence in "Fix: steps (`ui-principles`)" below; `ui-refinement`: apply the fixes; `layout-refinement`: apply the moves; `ux-psychology`: improve following the principles. Each block then audits again.
- No mode given: each block audits first, then asks whether to fix.

Before designing anything, find what already exists for this surface and build from the most real source in reach (its code, else the running page), in a copy that leaves the product untouched; a screenshot is only evidence, never the thing to rebuild from. Say in one line what you start from before you build.

## Shared rules (all blocks)

These apply in every block, next to each block's own fixed constraints.

- **Existing look:** if anything exists (a site, an app, a brand, neighboring sections, a component library), the new part inherits its colors, type, radii, spacing, imagery and component style so it looks as if it had always been there. A given type and component style are kept as well: no new style for one section.
- **Palette:** tints, shades and status colors derived from the palette are fine; meaning never rests on color alone. Palette changes may only be recommended when the whole site or product is in scope, as a marked suggestion with the reason (for example contrast), never applied.
- **Brand color fails contrast:** change the use, not the color. Text and controls take a shade derived from the same hue, or a different pairing of existing brand colors; the original stays for surfaces and marks.
- **Conflicting fixed constraints:** first try a permitted implementation: a different pairing of existing brand colors, a shade derived from the same hue, a neutral surface, a non-color state cue or an accessible equivalent for a signature effect. If the conflict remains, report the element and the consequence for the user as unresolved, name the smallest option that needs approval, keep the check at No, and stop instead of looping.
- **Working on a system:** existing tokens, components, variants and conventions come before new values. No `!important` or other specificity overrides, ad hoc values or forked copies. A library default that conflicts with a rule here is solved once, in the theme or a variant. In the copy, change existing tokens, components and library variants where a system exists; use a separate CSS layer on top of the original only when there is none, so it stays comparable. Before changing a shared token or component, verify its other consumers.
- **No side accent bars.** Never mark a card, row, alert, quote or selected item with a thicker colored edge on one side (left or right border, inset shadow, pseudo-element stripe); it is the most typical generic AI pattern. Mark state through the surface itself (a tinted background), weight, an icon, a dot or a label. In audits, an existing side bar is a violation; in fixes, replace it.
- **Selected states:** a selected or flagged state uses at least two cues (tinted surface plus check icon, label or weight), never a tint alone. A selectable card is a control: a full outline or ring for focus and selection is allowed under "Surfaces, not lines"; a one-sided edge is not.
- **No decoration for its own sake:** no glass for its own sake, no emoji as icons, not everything centered by default. A filler row of look-alike feature cards fails; equal cards for comparable items (products, plans, people) are fine.
- **Kickers:** a kicker stays when it tells the reader something the heading does not, such as which part of the page or which topic the section opens. It goes when it is filler: a label put on every section by habit, a word that only repeats the heading, or styling for its own sake (mono caps, accent color, a dot or glow). This is what "kickers" means wherever a block says to hide them.
- **Simple against decidable:** remove what competes, never hide what a decision depends on. Looking simpler is not deciding more easily.
- **Proof is never invented, not even as demo:** testimonials, ratings, client logos, certificates and counts (customers, projects, years) that were not given get a visibly marked slot each and are listed as open at the end.
- **Changing content:** apart from what the blocks themselves allow (hiding decoration and the competing elements they name, and the microcopy a `ux-psychology` principle is about), any shortening, rewriting, removing or hiding of visible content is proposed as before/after with the reason and applied only after the user approves that change. Markup may change for accessibility while preserving the displayed meaning. Edits use the project's copy conventions.
- **Labels:** check 13 of `ui-refinement` removes repeated labels on static values, never the visible label of a form field.
- **Images:** images are sized for their job: to recognize or to create desire. Text that must always be readable sits beside the photo, not on it. Text over images only when the image is fixed and chosen for it and every supported crop and state keeps measured contrast; where images vary or are uploaded, text sits beside or below.
- **Feedback:** inspect feedback at three moments where it carries information: on page load (what appears first and in which order), while scrolling (reveals, sticky changes, progress) and after an action (confirmation, changed state, the next step).
- **Same kind, same form:** elements of the same kind share size, height and alignment.

## Evidence (all audits)

- Extend the stress test of `ui-refinement` with a busy image, a translated title, few and many results where a list exists, and dark mode if offered.
- Define one representative task and its observable success condition. Distinguish the reviewer's walkthrough from observed user behavior. For an unresolved usability claim, name the task to test, the audience and the observation that would settle it; judgments that only real users can settle are marked "test with users".
- State in the evidence cell how a result was established: seen, checked in code, operated, measured or judgment. A screenshot supports visual observations only; behavior that was not operated (focus, names, announcements, submission) is named as not exercised in one line below the block reports, next to "Accessibility:", and is never reported as passing on that basis.
- Keyboard pass on interactive digital surfaces: tab through the screen once in both directions, watching order, focus visibility and traps.
- If available, run a contrast or accessibility checker (for example axe) and map its findings to the checks; it does not replace the keyboard pass.
- If nothing can be rendered, say so, audit from the code and mark each result as checked in code, not rendered.
- A rule in the sections below the four blocks applies only when its feature is on the screen. Browser and keyboard procedures need an interactive digital surface. For a static print artifact, assess the applicable visual properties (contrast, legibility at viewing distance) and state the medium.

## Block `ui-principles`: the 7 principles (score 0 to 7)

Good and AI-generated interfaces often use the same components. The difference comes down to seven things. Improving usually means removing, not adding.

### Fixed constraints (`ui-principles`, override the 7 principles of this block)

1. **Surfaces, not lines:** cards and tiles get no thin border lines. Separate them with surfaces, spacing and soft shadows. Borders only on inputs and controls.
2. **Brand palette is fixed:** if the client provides primary, secondary and accent colors, invent no new hues. Principle 4 then only governs how the colors are used.
3. **Demo content is fine:** for drafts and mockups, demo data and placeholder functionality are not flagged; proof is the exception (see "Shared rules"). Principle 5 then only checks that the demo data feels believable and specific.
4. **Content stays:** in fix mode, do not delete or rewrite visible text. Hide decorative labels with CSS if needed, never remove them from the markup, unless the user asks.
5. **Signature elements** the user names (e.g. a hero effect) stay untouched.
6. No em or en dashes in copy.

### The 7 principles

| # | Principle | Rule | Typical AI mistake | Fix |
| --- | --- | --- | --- | --- |
| 1 | Focal point | One element draws the eye first, everything else is quieter | Badge, gradient headline, two equal buttons, stat bar and three feature cards all compete | Name the screen's purpose, make that the biggest and highest-contrast element, turn the rest down or remove it |
| 2 | Spacing | Fixed scale in multiples of 4 or 8 px; proximity shows what belongs together | Same padding everywhere, nothing feels grouped | Gaps on 8, 16, 24, 32 (etc.), label close to its input, tighter inside a section than between sections |
| 3 | Typography | Hierarchy through weight and color, not size | Ever bigger headings, many sizes on one card | One typeface, two at most. Titles only slightly larger but darker and heavier. Secondary text in a softer gray. Slightly tighter tracking on headings. Short line lengths |
| 4 | Color | Mostly neutrals, one accent only where it matters | Purple gradient on background, headline, buttons and badges | Remove gradients, grays slightly tinted toward the brand color, accent only on the primary button, focus state and links |
| 5 | Content | Real, product-specific content | John Doe, round numbers, vague features | Real names, numbers, features, quotes (for demos: believable demo data; never invented proof) |
| 6 | Details | Radius, shadows and icons consistent everywhere | Harsh edges, one heavy blur shadow, icons a few pixels off | Consistent radius, nested elements slightly smaller than their container, soft layered shadows, icons same size and stroke on the text baseline, shared edges |
| 7 | Motion | Motion starts where the user acted | No transitions, or everything fades up the same way | Dropdowns grow from their button, opening slightly slower than closing, notifications slide in from the edge and stack, sheets follow the finger, short ease-out animations |

Calibration examples: a calm product homepage with one headline and one button (focal point), a checkout form with tight, grouped fields (spacing), a mostly neutral workspace app with one accent (color), a phone notification with matching radius and shadow (details), a bottom sheet that follows the finger (motion).

### Audit: steps (`ui-principles`)

1. Look at the page: desktop and mobile screenshots, plus read the HTML/CSS. For scroll animations, judge the end states, not intermediate frames.
2. Check for real rendering defects too: elements overlapping on mobile, full-width bands not reaching the edge (e.g. default body margin), clipped text, empty grid columns. These count under principle 6.
3. If available, run `npx impeccable detect <file or url>` and map the findings to the principles (glows and gradients to 4, kickers and icon tiles to 1, contrast to 3/4, radius and shadows to 6). If the tool is missing, continue without it.
4. Answer each of the 7 check questions with Yes or No and concrete evidence (selector, text, value).
5. Output the report.

### Check questions (`ui-principles`)

1. What is this screen for, and is that the most obvious thing on it?
2. Does every gap follow a fixed scale?
3. Does hierarchy come from weight and color rather than size alone?
4. Is the accent color used only where it matters?
5. Is every piece of content real (or believable, for demos)?
6. Do radius, surfaces and shadows match everywhere, with no rendering defects?
7. Does every animation start where the user acted?

### Report format (`ui-principles`, keep it short)

Score large at the top, then one table, nothing else:

```
# 4 / 7

| # | Principle | Result | Evidence | Fix |
|---|---|---|---|---|
| 1 | Focal point | No | Two equal buttons in the hero | Turn the second button into a text link |
...
```

At most one closing sentence: the biggest lever.

### Fix: steps (`ui-principles`)

Keep this order; components and layout structure stay the same. Work in the copy as in "Shared rules" (system first, otherwise a separate CSS layer on top of the original so it stays comparable).

1. **Focus:** exactly one primary button where the task has one (a reading, monitoring or status screen may focus on information; add no invented button), everything else secondary (text link); hide competing elements such as stat bars, badges and kickers.
2. **Spacing:** move every gap onto the scale, group related items more tightly.
3. **Typography:** one typeface, headings heavier rather than bigger, gray for supporting text, labels in sentence case.
4. **Color:** remove gradients, colored glows and halos; tinted neutrals; accent only on the primary button and links. Text contrast at least 4.5:1.
5. **Content:** replace placeholders with real (or believable demo) content. If real content is missing, ask the user instead of inventing it.
6. **Details:** align radii, smaller radii for nested elements, replace card borders with surfaces, soft layered shadows, align edges, fix rendering defects.
7. **Motion:** menus grow from their trigger, notifications stack, all animations short with ease-out, movement animates only `transform` and `opacity` (color and shadow may transition on state changes; layout properties are not animated for movement), respect `prefers-reduced-motion`.

Then run the audit again and report the before/after score.

## Block `ui-refinement`: the 15 checks and UX upgrades (score counts only applicable checks)

A screen can have the right components and still feel cheap because of many small decisions. This block walks through 15 common detail mistakes, then looks for UX upgrades that make the task easier, not just the screen prettier. The guiding idea: design for the system, not for one screenshot. Every check asks "does this still work with other content, other images, other products?"

### Fixed constraints (`ui-refinement`)

- Content and demo data stay. Hide or restyle, don't rewrite, unless a check is explicitly about wording (6, 13, 14) and the user agrees.
- A given brand palette stays; check 4 then governs saturation and usage, not new hues.
- Surfaces over lines: no thin borders on cards and tiles. Dividers only where they truly separate, and then subtle (check 11).
- Signature elements the user names stay untouched.
- No em or en dashes in copy.

### The 15 checks

| # | Check | Mistake | Fix | Why |
| --- | --- | --- | --- | --- |
| 1 | Controls over images | Icons or buttons sit directly on a photo and are only readable because this photo is dark | Give overlay controls their own background container, enough contrast and a subtle outline; test with a bright and a busy image | Images change; controls must survive every one of them |
| 2 | Imagery | Busy frame without focal point, hands instead of product, image showing something other than what is sold (one item vs. sold by weight), artificial styling, every image styled differently | Clear focal point on the item itself, honest and natural styling, one shared look (background, light, angle) across the catalog or set. For service and offer pages: problems as illustrations, solutions as product views in the same style; no mockups that promise what the customer's result will look like (use real photos or references); decorative filler images add no material, content does | An image never lives alone; it sits in grids next to others |
| 3 | Alignment | Text, icons, prices and buttons start at slightly different x positions | One margin and grid for the whole screen (e.g. content always 24 px from the edge) | Users feel misalignment as untrustworthy even if they can't name it |
| 4 | Color | Too bright, too saturated, accents on unimportant things | Calmer, softer palette that supports the content; saturation only where attention belongs | Too many loud elements kill hierarchy |
| 5 | Typography | Many font styles mixed | One family; hierarchy through size, weight, color and line height | Fewer styles give a stronger foundation |
| 6 | Labels and badges | Cramped small caps labels; badges with redundant words and icons ("20% off discount" plus icon) | Add letter spacing to small uppercase labels; badges say the minimum ("20% off") | Badges must be understood in a glance and must not steal focus |
| 7 | Title | Bold but unbalanced: too big, too heavy or too weak for its role | Tune size and weight so it stands out without shouting | The title tells users what they are looking at |
| 8 | Body text | Tight line height, full-contrast paragraphs fighting the headline | More line height (about 1.5 to 1.7), slightly reduced contrast (still at least 4.5:1) | Headlines attract attention, paragraphs support understanding |
| 9 | Trust signals | Rating, reviews or certifications far away from what they qualify | Place them next to the title or the claim they support | Users ask "what is it, and can I trust it?" in one look |
| 10 | Icon sets | Mixed filled and outlined icons, different weights, many colors, loose spacing, section dominates | One icon style and stroke weight, one or two colors, tighter spacing | Icons share one visual logic or they become noise |
| 11 | Dividers | Dark, heavy lines chop the page into harsh blocks | Soften them strongly or replace them with spacing and surfaces | Separation should feel smooth, not fenced |
| 12 | Spacing balance | Too much white space between related sections | Tighten gaps between related blocks; keep larger gaps only between unrelated ones | White space is about relationships, not quantity |
| 13 | Redundant labels | "Price:" in front of "€4.99", "Email:" above a field already labeled | Remove labels the content already explains; if you keep one, label comparable items consistently | Every extra word slows scanning |
| 14 | Information order | Title contains a variable attribute (e.g. "1 kg" while quantity is selectable); key facts like price appear late | Title describes the item; variants and quantity live in the selection area; show the decisive facts (what, how good, how much) early | Misleading or late information creates doubt at the decision point |
| 15 | Primary action | Button shouts (all caps, oversized) and sits far from its related controls; unclear what clicking costs | Refined button, related controls grouped (quantity right next to the button), units inside the selector, the total inside the button ("Add to cart · €9.98") | Users choose, then act; the button should confirm what they are about to do |

Mark a check **n/a** when the screen has no such element (e.g. no images over controls). The score counts only applicable checks.

### UX upgrades (after the 15 checks)

These are optional and go beyond fixing. Suggest only those that fit the screen.

1. **Content card over the hero:** content sits in a soft, rounded card that slides over the hero image on scroll; once the image leaves, the title moves into a sticky top bar so context is never lost.
2. **Sticky action area:** keep the primary action (and its controls) visible at the bottom while users scroll, because they often decide only after reading further.
3. **Presets for common choices:** offer one-tap options for the most common values (e.g. 500 g, 1 kg, 2 kg, ideally from real usage data) and keep the custom control for flexibility.

### Audit: steps (`ui-refinement`)

1. Look at the screen: desktop and mobile screenshots plus HTML/CSS. For scroll effects judge end states.
2. Stress test the system: mentally (or actually) swap in a bright image, a long title, a different product. Note what breaks (checks 1, 2, 7, 14).
3. Rate each check Yes / No / n/a with concrete evidence (selector, text, value).
4. List which UX upgrades would fit, if any.
5. Output the report.

### Report format (`ui-refinement`, keep it short)

Score large at the top, then one table, then upgrades in one line each:

```
# 9 / 13

| # | Check | Result | Evidence | Fix |
|---|---|---|---|---|
| 6 | Labels and badges | No | Badge "20% off discount" + icon | Shorten to "20% off", drop the icon |
...

Upgrades: sticky action area (button leaves viewport after 900 px)
```

At most one closing sentence: the biggest lever.

### Fix: steps (`ui-refinement`)

Work in the copy as in "Shared rules" (system first, otherwise a separate CSS layer on top of the original so it stays comparable), plus minimal markup changes where unavoidable. Order: alignment and spacing (3, 12) first because everything else sits on them, then type (5, 7, 8, 6), then color and icons (4, 10, 11, 1), then information order and action (9, 13, 14, 15), then upgrades if agreed. Audit again and report before/after.

## Block `layout-refinement`: the 7 techniques (score 0 to 7)

Small layout moves with a big effect. The techniques come from graphic design (posters, magazines, packaging) and apply just as well to websites. It is rarely about rebuilding, usually about one deliberate shift.

### Fixed constraints (`layout-refinement`)

- Content, palette and signature elements named by the user stay untouched. Move, scale and regroup; do not rewrite.
- No thin border lines on cards and tiles; surfaces instead of lines.
- No em or en dashes in copy.

### The 7 techniques

| # | Technique | What to look for | Fix | On the web |
| --- | --- | --- | --- | --- |
| 1 | Break the grid on purpose | A consistent grid sets an expectation. When an element breaks it, that exact spot gets noticed | Break it only where two things should visibly interact (product reaching into the next area, image overlapping a section edge). Correct accidental outliers | An image, mockup or object deliberately crosses a section boundary or card instead of sitting neatly in its box |
| 2 | Balance visual weight | Eye flow (an object pointing at an element) often ends in an overloaded corner where the eye gets stuck. Squint test: where does mass bunch up? | Move the target element so the eye can continue and weight spreads across the area | Don't stack CTA, badge and image in the same corner; check hero composition for weight, not just direction |
| 3 | Avoid near tangencies | Two edges that almost touch create a thin strip that grabs more attention than intended | Decide: give clear space (separate) or clearly overlap (connected). Never just short of it. For print, consider binding and bleed | Images almost touching the viewport edge, section edge, header or a neighbor; elements nearly colliding at breakpoints |
| 4 | Viewing distance | At 45 cm on a monitor, small things look refined; in real use they are unreadable. Simply enlarging everything creates a hierarchy problem | Shrink the design to its real-world size. Decide what must land in the first second and what can wait. If two things must register at once, give them a shared focal point (e.g. a date set over a calm, dark area of the photo) | Check the mobile view and thumbnail/social preview; key message plus key info in the first second; text over images only on calm image areas of a fixed image (see "Shared rules", Images) |
| 5 | Series: constants and variation | Cropping every image the same looks consistent but strips each image of what makes it special | Decide what repeats (type position, baseline, color accent) and lock it to the grid. Choose each crop by what that image needs to show | Card rows, team photos, case studies: fixed layout constants, individual crops instead of identical centered ones |
| 6 | Same question, same place | When the same question applies to several items (opening time, price, status), nobody should have to hunt for it in body text | Align the answers in a shared column or row that sits on the same line as its item. Two routes: browsing (image, text) and shortcut (column), using the same rows | Prices, dates, durations, status always in the same position and on one line in cards; comparison tables instead of info buried in copy |
| 7 | Information at the decision point | People act step by step. A note that comes after the action is seen too late | Walk through the layout in the user's order. At every point where they form an opinion or make a choice: have they seen everything that could change it? If not, move that info right there | Conditions, notes and options inside the step, not below it: shipping costs next to the price, format requirements at the upload field, variant notes before the add-to-cart button |

### Multi-page and content-heavy layouts

- **Same function, same form.** Sections with the same content and task look the same on every page of a site. Readers recognize the pattern and find their way faster.
- **Sub pages go deeper, not wider.** What the main page already summarizes is not repeated as its own section on a sub page.
- **Long content stays scannable.** However long a block gets, readers can see its structure at a glance and jump to what concerns them.

### Audit: steps (`layout-refinement`)

1. Look at the layout: desktop and mobile screenshots (for print: full view and detail). Add a scaled-down view at real-world size (technique 4) and a blurred squint view (technique 2).
2. Walk the user's path in reading order and mark the decision points (technique 7).
3. Rate each technique Yes or No with concrete evidence (element, position, distance). Techniques 5 and 6 count as Yes if there is no series or no recurring question.
4. Output the report.

### Check questions (`layout-refinement`)

1. Is the grid broken only where two things are meant to interact?
2. Is visual weight spread out instead of piling up in one corner?
3. Are there no edges that almost, but not quite, touch?
4. At real-world size, does the most important thing land in the first second without breaking the hierarchy?
5. Does a series repeat the right things and vary the right things?
6. Do answers to the same question sit in the same place and on one line?
7. Is every decision-relevant piece of information before or at the decision, not after it?

### Report format (`layout-refinement`, keep it short)

Score large at the top, then one table, nothing else:

```
# 5 / 7

| # | Technique | Result | Evidence | Fix |
|---|---|---|---|---|
| 3 | Near tangency | No | Hero image ends 6 px short of the section edge | Pull the image 40 px across the edge or give it 48 px of space |
...
```

At most one closing sentence: the biggest lever.

### Fix: steps (`layout-refinement`)

Keep moves as small as possible: shift, align, overlap, group. Work in the copy as in "Shared rules" (system first, otherwise a separate CSS layer on top of the original so it stays comparable). Order by impact: first 7 and 4 (comprehension), then 2 and 3 (calm), then 1, 5 and 6 (character and order). Then run the audit again and report the before/after score.

## Block `ux-psychology`: the 9 principles (score 0 to 9)

Screens fail less often because they look bad than because they ignore how people perceive and decide. People judge a whole site by its first view, trust what is easy to process, remember the best moment and the end, avoid effort, speed up near a goal, return favors, value what they made, weigh losses more than gains and judge every number against the last one. This block applies that to a screen, honestly.

### Honesty comes first (`ux-psychology`, overrides the 9 principles of this block)

These principles work because they match real behavior. Used to deceive, they turn into dark patterns, cost trust and in many markets break consumer or privacy law. Premium feel comes from respect for the visitor's time and intelligence, not from tricks. So:

1. **Everything shown is true.** Result counts are real, deadlines exist, losses are the user's actual loss. Progress counts only steps the user did or confirmed; a pre-filled default the user hasn't looked at is not progress. A missing fact becomes a placeholder, never an invention.
2. **Declining stays easy and neutral.** The way out is visible and worded plainly ("Nicht jetzt", "Ohne Upgrade weiter"). No shaming labels, no hidden close buttons.
3. **Defaults serve the user, never the business at the user's expense.** Never preselect consent, newsletters, paid extras, data sharing or longer contracts.
4. **No fake pressure.** No invented countdowns, scarcity or "only 2 left" without data behind it.
5. **Brand palette, signature elements and content stay** as in other design work. Microcopy that a principle is about (button labels, decline labels, a progress line, a price reference, a confirmation message) may change. German copy follows `copy-rules` if available.

### The 9 principles

#### How it feels (perception)

| # | Principle | Why it works | Typical mistake | Fix |
| --- | --- | --- | --- | --- |
| 1 | **First impression** | The first view is judged in a moment and colors the judgment of everything after it (halo effect) | First screen crowded with badges, several buttons, sliders, weak or generic imagery, unclear message | Decide the one feeling and one message the first view must carry, give it room and the best material, move everything else below |
| 2 | **Low effort to understand** | What is easy to process feels better, calmer and more trustworthy (cognitive fluency); effort feels like risk | Competing elements, long navigation, several goals per section, dense text | One primary goal per section, clear order of importance, short predictable navigation, room around content. Remove before adding. For the visual execution use `ui-principles` and `layout-refinement` |
| 3 | **Peaks and a good ending** | People remember an experience by its best moments and by how it ended (peak-end rule) | Static controls without feedback, forms that end in a bare "Gesendet", flows that stop without a next step | Give every action quiet feedback (hover, focus, validation, saved state), and at a few key moments (first success, completion) a small deliberate positive moment in the brand's tone. Design the end of every flow on purpose: confirm what happened, what comes next, and give one useful next step |

#### What people do (decisions)

| # | Principle | Why it works | Typical mistake | Fix |
| --- | --- | --- | --- | --- |
| 4 | **Smart defaults** | Every open choice is effort; many choices at once lead to no choice. A sensible default reads as a recommendation, and most people keep it | Empty forms, every field a decision, long option lists, a button that only says "Submit" | Pre-fill each field with the most common or most likely choice, cut options, ask later what can wait. The button names the result ("12 freie Termine anzeigen") |
| 5 | **Head start** | People speed up the closer they feel to a goal, and the starting line can be set | Progress at 0 %, a long list of empty steps, account creation treated as something before the journey | Count what the user has really done as the first step, show where they are and how little is left |
| 6 | **Give before you ask** | Receiving something real creates a wish to give back; asking first feels like a wall | Results locked behind sign-up, "enter your email to continue" before any value | Deliver a real, useful part first, then offer the account as a way to save or get more |
| 7 | **Let them build** | People value what they made or chose themselves; leaving then means abandoning it | Sign-up screen with nothing of the user's own on it | Let users create or configure something before the account step. Before it, say what is saved, whether an account is required and what happens on leaving; the account step saves their work and is labeled clearly as account creation |
| 8 | **Show what is at stake** | Losing weighs more than gaining; people protect what they have | Upgrade screens that only list features, nothing changes when ignored | Where acting really matters, name the user's concrete loss or limit in their own terms (their files, their data, their deadline). Keep the decline neutral |
| 9 | **Anchor the cost** | Every number is judged against the one seen just before | A price alone on its own screen, a cost without any reference | Show the cost next to the honest reference it belongs to: what it protects, today's cost, the per unit or per day amount, the larger purchase it is part of |

A principle that does not apply to the screen (no price, no sign-up, no flow) is **n/a** and does not count against the score.

### Audit: steps (`ux-psychology`)

1. Look at the screen or flow: screenshots or the HTML, the first view without scrolling, and the step before and after if they exist.
2. Name the one feeling the first view should create, the one action the screen wants, and the moment the user might leave.
3. Answer the nine check questions with Yes, No or n/a and concrete evidence (element, label, value).
4. Check the honesty rules. Any violation goes into the report even if it scores well.
5. Output the report.

### Check questions (`ux-psychology`)

1. Does the first view carry one clear message and feeling, with nothing competing?
2. Can a first-time visitor see the order of importance and the next step without effort?
3. Does every action get feedback, and does every flow end on purpose with a next step?
4. Are the likely choices already made for the user, and does the button name the result?
5. Does the user start with visible progress that counts only real steps?
6. Does the user get something real before being asked for anything?
7. Does the user own something on this screen before the account step?
8. Where acting matters, does the screen name the user's concrete loss, with a neutral way out?
9. Is every cost shown next to an honest reference?

### Report format (`ux-psychology`, keep it short)

Score large at the top (counting only applicable principles), then one table, nothing else:

```
# 3 / 6

| # | Principle | Result | Evidence | Fix |
|---|---|---|---|---|
| 1 | First impression | No | Hero holds badge, slider and three buttons | One message, one button, slider below the fold |
| 4 | Smart defaults | No | Five empty fields, button "Absenden" | Pre-fill date and time with the next free slot, button "3 freie Termine anzeigen" |
| 9 | Anchor the cost | n/a | No price on this screen | |
...
Honesty: no issues
```

At most one closing sentence: the biggest lever.

### Fix: steps (`ux-psychology`)

Work in this order, keep layout and components, change only what a principle is about.

1. **First view:** one message, one feeling, one primary action where the task has one, the best material; everything else moves down.
2. **Remove effort:** fewer competing elements and navigation items, defaults, fewer options, defer what can wait, result-naming buttons.
3. **Set the starting line:** count real completed steps, show remaining steps.
4. **Move value forward:** show the real part of the result before any gate.
5. **Give ownership:** let the user make choices of their own before the account step.
6. **Make stakes concrete** where it matters, with a neutral decline.
7. **Anchor costs** with an honest reference.
8. **Peaks and ending:** feedback on every control, a designed confirmation with what happens next.

Then check the honesty rules, audit again and report the before/after score. Facts the screen needs but you don't have (real numbers, the user's items) become clearly marked placeholders.

## Accessibility floor (all blocks, unscored)

Run this screening last, after the four blocks, on their result. Screen for barriers on the supplied surface; for web work, WCAG 2.2 AA is the target. These are hard minimums: a confirmed violation goes into a line "Accessibility: …" below the block reports, like "Honesty:", and is fixed first, whatever the scores. This is a screening, not a conformance claim; record the criterion for each standards failure; record this skill's stricter requirements separately, labeled as house rule.

1. **Contrast:** text at least 4.5:1, large text at least 3:1 (at least 18 pt regular or 14 pt bold); hierarchy never goes below that. Non-text contrast of at least 3:1 for what identifies a control or its state, focus indicators, icons that carry meaning and chart lines. Check real surfaces, image crops, states and every theme offered; in dark themes surfaces separate by lightness, because shadows do not read.
2. **Keyboard and focus:** everything works by keyboard in a sensible order; focus is clearly visible and never hidden by sticky bars, banners or overlays (keeping the whole indicator visible is the house rule; WCAG 2.4.11 fails a focused component entirely hidden by author-created content); an active modal dialog or sheet contains focus, Escape dismisses it, and focus returns to the invoker or the logical next step; non-modal panels don't trap focus and stay reachable and escapable in normal page navigation.
3. **Structure and names:** page title and page language set; real headings in a sensible order and landmarks; a way past repeated navigation; alt text or alternatives for meaningful images; persistent visible labels for data-entry fields (a placeholder is not a label); accessible names for controls and icon buttons, matching the visible wording; programmatic state (expanded, selected, current); validation and status messages announced.
4. **Operation:** pointer targets at least 24 × 24 CSS px or a documented WCAG 2.5.8 exception, including adequate spacing; dragging has a single-pointer alternative where required; data already given in the same process isn't asked again; an accessible route through sign-in, without puzzles; nothing essential appears on hover only; inputs declare type and autocomplete; password managers, autofill and paste are never blocked.
5. **Motion and media:** reduced motion is respected and nothing flashes (house rules); content that moves, blinks or scrolls automatically for more than 5 s, and auto-updating content, can be paused, stopped or hidden; audio that starts automatically and lasts more than 3 s can be paused or stopped or has independent volume control; supplied media have captions, descriptions or alternatives.
6. **Reflow and text resize:** usable at 320 CSS px width without loss of content or sideways scrolling for vertical content; necessary two-dimensional layouts such as maps or comparison tables scroll within their own region; text resized to 200 % and user text-spacing overrides lose nothing; sticky controls are tested at these sizes.

## Lists, filters and search (where present, unscored)

- The first items are good enough to make people scroll; in data tools density is the goal.
- One clear order per card (name, then the deciding facts, then the rest).
- The most used filters stay visible, the rest behind one button, sort beside it; applied filters stay visible and can be removed one by one or all at once; an empty result says which filter to loosen.
- Filters open over or beside the results (a sheet on mobile, often a side panel on desktop), all in one scroll.
- Show what a choice costs before it is made: the total count visible, as matches out of the relevant total where that helps; counts per option (the predicted count) before choosing; distribution behind range sliders where it helps; an unavailable count stays unknown, never estimated as fact.
- When there is no right choice for everyone (cards or compact list, sort order), let people choose.
- The search placeholder names what can be searched, plus a visible label or accessible name.
- Category, navigation and filter elements are calmer than the items and don't repeat their imagery; a "best match" highlight only when it rests on real data about the user, saying why.
- Each added piece of context must help the decision; remove what only adds noise.

## Data tables (where present, unscored)

- Numbers right-aligned with tabular figures, units in the header, sorting and the current sort visible, key columns stay in view, readable density; each value keeps its relationship to its row and column headers for assistive technology; the table is named where needed; sorting is keyboard operable and the active sort is exposed programmatically; labels, units and key actions tested in the narrow layout.
- Bulk actions: selection count visible, actions appear where the selection is, "select all" says whether it means this page or everything.

## Navigation (where present, unscored)

- The main navigation holds the most important, frequently used destinations; tab bars about three to five; side and site menus may be longer if grouped; rare items (help, sign out, legal) live in a profile or menu; the same destinations in the same order when navigation changes form with width.
- Elements keep their usual place (no back or forward button or logo in a bottom bar); one frequent core action may sit prominently in the center.
- Icons alone only for audiences that know the pattern; otherwise short, single-line labels, never too small to read.
- The active destination follows "Selected states". An outlined set with a filled icon only for the active item is a state cue, not mixed icon styles.
- Touch targets in a bar about 44 × 44 px or more (24 × 24 is the floor, not the goal); the bar sits above system gesture areas and never covers them; compact enough not to crowd content.
- Familiar, simple icons; neutral colors, no color per destination, the accent only for the active item and the main action; top and bottom navigation share one palette; no boxes around items.
- Set apart from content through its own surface or a very soft shadow, not a line.
- Badges only for what really needs attention, small but legible, a dot for presence, a real count when quantity helps, positioned consistently, their meaning in the accessible name.
- Unusual shapes or positions only if orientation and operation don't suffer; a tap answers at once, the active marker moves to the new tab, screens change with a short fade or slide.

## Websites: loading and widths (where present, unscored)

- Hero images, videos and web fonts are sized and reserved so the first view neither waits nor shifts.
- Test the first view and the key task at mobile and desktop sizes, at the width where a component changes, and with zoom or a virtual keyboard where relevant; for supported locales, verify long labels, directional layout and formatted numbers, dates and currencies. Lab observations, missing field data and suspected causes are labeled separately.

## Self-check before reporting (fix mode)

Check the result against these rules and fix every miss before the report:

- No colored glows, halos, gradients or glass for its own sake, except on signature elements the user named. If none is named, nothing is exempt.
- Exactly one filled primary button per view where the task has one; a button in the header counts.
- No thin borders on cards and tiles, no side accent bars.
- No em or en dashes in copy.

Then add one line below the block reports, next to "Accessibility:": "Self-check:" followed by each rule above with ok, or what was corrected. A run without this line is not finished.

## Output

- Keep replies short, one point per reply.
- Always output code changes complete and copy-ready in one piece.
- Provide created files or pages as clickable links.

## Related and further reading

- `ui-principles`: Motion: dedicated animation and transition skills, if installed.
- `ui-principles`: For deeper, measurable checks: Impeccable (`detect`, `critique`, `audit`) or Hallmark (`sloplint`).
- `ui-principles`: For composition and layout: the `layout-refinement` block.
- `ui-refinement`: `ui-principles` for the big picture (focal point, spacing scale, color, motion).
- `ui-refinement`: `layout-refinement` for composition (grid breaks, balance, near tangencies, decision points).
- `layout-refinement`: For surface quality (focal point, spacing, typography, color, details, motion), use the `ui-principles` block; the two complement each other.
- `ux-psychology`: Visual quality: `ui-principles`, `ui-refinement`, `layout-refinement`.
- `ux-psychology`: Wording of buttons, prices, decline labels and confirmations: `copy-rules`.

---
name: design-create
description: Guides the creation of new websites, landing pages, app and SaaS screens, dashboards, forms, interactive tools, lists with filters, sign-up and pricing screens, and print or slides from the first decision on, so the result is focused, accessible, honest and free of generic AI patterns before any review is needed. Sets context, message and information order first, then builds with fixed rules (surfaces not lines, no side accent bars, WCAG 2.2 AA, no dark patterns, existing tokens and component libraries such as shadcn/ui and Tailwind used as intended) and principles per building block, and ends with a short self-check. Use this skill whenever a page, screen, component, mockup, prototype or layout is designed, built, redesigned from scratch or extended with a new section, even if the user only says "build", "make" or "design" and names no principle. For reviewing something that already exists, use design-review.
---

# Design Create

Generic and good interfaces use the same components. The difference is decided before the first line of code: what the screen is for, what people need to decide, and what can be left out. This skill makes those decisions first, then builds within clear limits, then checks itself. Fewer, better decided elements beat more elements.

Numbers below are examples unless marked as a minimum. The right means depends on the brand and context.

## Fixed rules (never broken)

1. **Everything shown is true.** No invented numbers, ratings, logos, testimonials, deadlines or scarcity presented as real. In drafts, realistic demo content is fine when it is marked once as example content.
2. **No dark patterns.** Declining is as easy and neutral as accepting; never preselect consent, newsletters, paid extras, data sharing or longer terms; no shaming labels, hidden close buttons or fake countdowns.
3. **Surfaces, not lines.** Cards and tiles are separated by surface, spacing and at most a soft shadow, never by thin border lines. Borders only on inputs and controls; a transparent outline is fine as a forced-colors fallback.
4. **No side accent bars.** Never mark a card, row, alert, quote or selected item with a thicker colored edge on one side (left or right border, inset shadow, pseudo-element stripe). Mark state with a tinted surface, weight, an icon, a dot or a label.
5. **Accessible by default (WCAG 2.2 AA).** Text at least 4.5:1, large text and meaningful UI parts at least 3:1; visible labels (a placeholder is not a label); accessible names for icon buttons; real headings and landmarks; full keyboard use with a clearly visible focus that nothing covers; targets at least 24 × 24 px; reduced motion respected; usable at 320 px width.
6. **Brand and system first.** A given palette, type, tokens, components and global classes are used before anything new; tints and status colors derive from the palette; meaning never rests on color alone.
7. **Work with the library, not against it.** When a project uses a component library or utility framework (for example shadcn/ui on Tailwind, or blocks built on them), use its components, variants, theme variables and utility classes as intended, and keep its conventions (composition, accessibility props, focus styles). Adapt it to these rules through the library's own means: theme tokens, variants or a class on the component, never `!important` overrides, hard-coded values or forked copies. Where a library default conflicts with a rule here (for example a card with a border), solve it in the theme or a variant, once, for the whole project.
8. **No generic AI look.** No gradient headlines, glows, glass for its own sake, decorative badges, emoji icons, rows of identical feature cards, stat strips without a source, or everything centered by default.
9. No em or en dashes in copy. German copy follows `copy-rules` if available.

## Step 1: Decide before building

Write these down in a few lines (in the reply or as a comment) before any markup:

1. **Context.** Website (message, trust, reading flow), product (efficiency, density, states), or print and slides (composition, viewing distance).
2. **Job of the screen.** Who arrives, what they want, what they should do next. One primary action per view on websites, one per task area in products.
3. **Information order.** What is needed to decide, in which order; what can wait for a second view; what is left out.
4. **Building blocks.** Which of the blocks below are on the screen; apply only those.
5. **System and look.** If anything already exists (a site, an app, a brand, neighbouring sections, a component library), the new part inherits it: colors, type, radii, spacing, imagery and component style, so it looks as if it had always been there. Never introduce a new color mood or style for one section or tool. Corporate design colors are fixed: work with how they are used (which color for text, surfaces, accent; contrast-safe tints and shades derived from them), never replace them. Only when the whole site or product is in scope may color changes be recommended, as a clearly marked suggestion with the reason (for example contrast), not applied. Only when nothing exists, choose a visual direction in one line (mood, palette from neutrals plus one accent, type pairing, one distinctive element) and a small system: one spacing scale, a few type sizes, one radius family. The fixed rules are the floor, not the goal: the result should have character, not just pass checks.
6. **Layout order.** One clear reading direction. Steps of a flow run top to bottom in one column of one width; elements of the same kind share size, height and alignment; a side summary only where there is room for both columns without cramping either.

## Step 2: Build with these principles

### Always

- **Focus.** The first view carries one message and one primary action; everything else is visibly secondary.
- **Order and spacing.** Related things sit closer than unrelated ones; one grid and margin; one consistent spacing scale; visual weight spread.
- **Type.** Hierarchy through weight, size and spacing that fit the brand, never by lowering text contrast; few families; comfortable line height and line length.
- **Color.** Mostly neutrals tinted toward the brand; the accent only where attention belongs.
- **Details.** One shape language, one icon style and stroke, icons optically aligned with their text, soft shadows if any.
- **Content.** Specific and believable; in drafts use realistic demo content instead of bracket placeholders, and note once (in the reply or a single quiet line) which facts are examples to replace; never present demo figures, ratings or quotes as real. Images show what is offered and are sized for their job; text that must stay readable sits beside photos, not on them.
- **Emphasis.** One honest highlight where it helps the decision (for example a recommended option, marked as such), not several competing ones.
- **Feedback and ending.** Hover, focus, validation and saved states exist; motion is short and starts where the user acted; every flow ends with what happened and the one useful next step.

### Website

- Imprint and privacy reachable from every page; a clear contact path; consent banner with equal decline.
- Hero media and fonts sized and reserved so they don't delay the first view or shift the layout.
- Designed for mobile and desktop alike.

### Forms and interactive tools

- Pre-fill only neutral, likely values; ask what can wait later.
- Choices that affect each other are visible together; the right control for each value (direct options for known values, slider plus input for ranges).
- Ask in the user's terms and convert for them.
- Show the consequence before commit: a live total or count, and a button that names the result.
- Errors and help at the field; long forms may add an error summary that moves focus.

### Lists, search and filters

- The first items are worth scrolling for; cards have one clear order (name, deciding facts, rest).
- Key filters visible, the rest behind one button; filters open over or beside the results; counts before choosing.
- Search says what it finds and has a label.
- Helpers stay quieter than the content.

### Sign-up, onboarding, pricing

- Give a real part of the result before asking for an account, where possible; progress counts only real steps.
- Every price stands next to an honest reference; one recommended plan at most; everything included listed.

### Product screens

- Empty, loading, error and success states designed from the start.
- Context and selections stay in reach while scrolling.
- Reversible actions offer undo; irreversible ones get a review step naming the consequence; destructive actions sit apart.
- Tables: numbers right-aligned with tabular figures, units in the header, visible sort.
- Bulk actions show the selection count and say what "select all" covers.
- AI features say what they do and how sure they are, and ask before anything is sent or executed.
- Navigation: tab bars about three to five items; side menus grouped; active state shown by at least two changes.

### Print and slides

- Break the grid only on purpose; edges clearly apart or clearly overlapping; the key message lands at real viewing distance; series share fixed constants.

## Step 3: Self-check before handing over

Run `design-review` in audit mode if it is available. Otherwise check at least:

- Fixed rules 1 to 9, with a search of the CSS for one-sided borders, inset side shadows and thin card borders.
- Contrast of body text, muted text and the accent on its surface.
- Keyboard order and visible focus.
- 320 px width and a long title.
- One primary action per view.
- The new part matches the existing look, and the layout reads in one clear direction.

Fix what fails, then hand over.

## Output

- Start with the short decision block from step 1, then the build.
- Code complete and copy-ready in one piece; files as clickable links.
- End with one line on the self-check (passed, or what remains open and why).
- Keep the reply short, one point per reply.

## Related

- Review and refinement of existing screens: `design-review`.
- Logos and brand marks: `logo-design`. Copy: `copy-rules`. Launch checks: `launch-check`.

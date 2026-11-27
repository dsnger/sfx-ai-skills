---
name: app-ui-system
description: Rules for building and changing the interface of a web app, including its phone widths, so every screen stays coherent with the others, on whatever component library and style the project uses (asked once and saved, never assumed). Covers how to work with the product owner, the style system, pages and overlays, lists and their toolbars, record pages and forms, phone layouts, wording and accessibility. Use it before building or changing any app screen, list, table, toolbar, dialog, drawer, form, navigation or UI wording, when setting up the UI foundation of a new app, and before reporting UI work as done, even if the user only says "add a page", "build the list view" or "make it work on mobile".
---

# App UI system

This skill keeps an app's interface coherent across all its screens. It states principles; the concrete values (library, style, sizes, radii, spacing, fonts, colors, terms) live in the project's UI profile, which you create once with the user and then follow.

For auditing or polishing a finished screen against general design quality, use `design-quality` if it is available. This skill is for building.

This skill does not teach a library's API or its theme setup. For correct component usage (installed components, props, primitives) and for setting up tokens, theme and dark mode, use the library's own skill if one is installed (for example the official `shadcn` skill, or a Tailwind theme skill); otherwise read the library's documentation. Where such a skill and this one differ on how the interface should look or behave, this skill and the profile win.

## Before anything: the UI profile

Look for the project's UI profile (by default `ui-profile.md` at the repository root; the user may name another place).

- **Profile exists:** read it and build within it. It wins over anything in this skill where they differ, because it holds decisions the owner already made.
- **No profile:** create one before building, and do not build before the owner has seen it. Read `references/profile.md`, take everything you can from the code (package manifest, component library config, tokens, existing screens), and ask the owner only what the code does not answer, as one question with your recommendation per open point. Never assume a library, a style or a value because it is common.

Keep the profile current: when the owner decides something that applies beyond one screen, add it there.

## 1. How to work with the owner

These come first.

1. **What the owner says is built.** Each thing they ask for becomes a task and is built unless they say no. No reviewer, second opinion or other agent overrules it; at most you ask them.
2. **Build exactly their point.** Nothing beside it; your own ideas go into one short "Suggestions" line. Never widen or narrow what they said ("for example today" is not "only today"). Quote them verbatim and mark your own reading as yours.
3. **Fix the system, never one value.** No single-place fixes and no fallbacks: change the one defining place (a token, a shared component, a constant) so every screen follows. A value the profile does not have yet (a color, a size, a breakpoint) goes into the profile as a proposal and is used only after the owner approves it; until then, build with existing values and name the open point.
4. **Do not ask about details a rule already settles.** Given a principle, decide the details yourself and say what you chose. Ask only real choices, with a recommendation, ideally as a picture or a built variant.
5. **Coherent and DRY.** The same thing uses the same component, shows the same information in the same place, has the same form and the same way of entering data, everywhere. A difference needs a stated reason.
6. **Do not invent; copy proven patterns.** Take the library's own blocks and the patterns of established products (the profile names them). Take a reference product for its scope and function, not for its look.
7. **Design for every case:** the longest word, many values, everything set at once, empty, loading, failed, every theme the app has, every width.
8. **Range first, then form.** Before building or changing a list, toolbar or form:
   a. Record its full range: number of items, filters and values, every combination, and the cases none, one and many.
   b. From that range, choose one designed form per width, not from the demo data and not by squeezing the desktop view. A form changes only at a fixed, named width, never because a value was chosen. The one exception: a count on a filter may push what follows.
   c. Record the decision as a short table (place × width × case → form) in the profile and measure it.

   The profile lists every width at which a form changes, for the whole app, in one place. A decision that changes the range (a new field, filter, status, option or role) re-opens the table: update the range and the table, and check every affected place again at every width before reporting done.
9. **Approved screens stay.** The profile names the reference screen(s). They never change as a side effect. Before changing a shared component, name the approved screens it touches. Nothing a person saw before disappears without the owner's rule.
10. **Variants only for what is undecided.** Once the owner chooses, build the choice in and remove the alternatives and any switch between them.
11. **The interface decides first.** What the backend lacks becomes an issue draft with acceptance criteria, never a faked figure.
12. **Done means checked:** the code, the tests against the base (only new failures count), a measurement, and the picture looked at, at the widths and themes the profile lists. Report in a few lines, in the owner's language, what visibly changed on which screen, and what was not checked. Every round trip costs the owner.
13. **A blocker is the owner's to remove.** When a tool or an access is missing, ask; then go the planned way. No workaround guess.

## 2. Style system

- **The library as it ships**, in the style the profile names. Deviate only on purpose, at the one defining place, with the reason in a comment.
- **One size per row.** Controls in a page head or toolbar take the library's default control size; never two sizes in one row. Buttons inside list rows are the small size. Larger touch targets only on coarse pointers.
- **Radius from one source** (the profile names it): a fixed scale from surface to notice to control and floating panel to choice and menu item to badge, avatar and dot (round) to checkbox. Nested is smaller than its container. The outer radius defines the shape, so neighbours in one row share it (for example a tab group's frame takes the radius of the buttons beside it); record such deviations in the profile.
- **Spacing on one base unit.** Shared rhythms (such as list row padding) are tokens derived from the base. Never change the base to fix one place.
- **Surfaces, not lines.** No card borders; separate by surfaces and spacing. Buttons are quiet surface buttons, not outlines; inputs keep their border. No card inside a card and no list inside a card (double padding). These are deliberate deviations from the library, set once at the defining place.
- **No browser controls:** one app date picker and the app's own select and combobox (search, hover, keyboard highlight); no native select or date input.
- **Color:** mostly neutrals; one filled main action per view in the accent; the accent also marks the one main number of a page. An exceeded or over-limit state uses the status color the profile names, never the brand accent. A tint that marks a state: the hue says which kind (for example whose), the strength says the state is active; without the state there is no tint.
- **Type:** the profile's typefaces, self-hosted, no remote font requests. Identifiers such as ticket numbers in the system monospace with a visible border.
- **Focus ring only on keyboard use**, around the whole element including its icon.
- **Motion:** short, ease-out, transform and opacity only, reduced motion respected. A command shows a busy state at its own size; results apply at once (an item moves to its new group immediately).

## 3. What to read next

Read the reference file for what you are building, before you build it:

| You are building or changing | Read |
|---|---|
| A page, a page head, a dialog, a drawer, a record page, a create or edit form, time or date input | `references/pages-and-overlays.md` |
| A list or table, its rows, totals, grouping, bulk actions, or the list toolbar (search, filters, sort, group, columns, export) | `references/lists.md` |
| Anything at phone width, or a bottom tab bar | `references/phone.md` |
| Labels, button texts, messages, terms; accessibility of any of the above | `references/words-and-access.md` |
| A new app's UI foundation, or a missing profile | `references/profile.md` |

## 4. Self-check before "done"

Check these before you report, fix every miss, and say in the report what you checked:

- **Approved screens unchanged:** compare every approved screen before and after, at every width the profile lists. A shared change that alters one of them is scoped to the new screen, or left out and named as an open point.
- **Only approved values used:** nothing that stands in the profile only as a proposal, and no value the profile does not have, is used in the build.
- **States built:** every list and view you touched has its empty, loading and failed state.

## 5. Report

When you finish, report briefly:

- what visibly changed, per screen;
- what you decided yourself under a rule, and which rule;
- what was not checked (width, theme, state);
- open questions as real choices with your recommendation;
- one "Suggestions" line for ideas beyond the task, if any.

## Reversed decisions

Keep a "Reversed" list in the profile: each rule the owner replaced, with the replacement and the date. Before building, check it, so nobody revives a version the owner already turned down.

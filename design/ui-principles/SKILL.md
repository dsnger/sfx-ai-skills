---
name: ui-principles
description: Audits and refines websites, landing pages, mockups and app screens against 7 principles of good UI (focal point, spacing, typography, color, content, details, motion) and gives a score from 0 to 7. Use this skill whenever a page looks AI-generated or generic, or a UI check, design review or visual polish is requested, even if the 7 principles are not mentioned.
---

# UI Principles

Good and AI-generated interfaces often use the same components. The difference comes down to seven things. Improving usually means removing, not adding.

## Modes

- **audit**: check only, report with score.
- **fix**: refine following the sequence below, then audit again.
- No mode given: audit first, then ask whether to fix.

## Fixed constraints (override the principles)

1. **Surfaces, not lines:** cards and tiles get no thin border lines. Separate them with surfaces, spacing and soft shadows. Borders only on inputs and controls.
2. **Brand palette is fixed:** if the client provides primary, secondary and accent colors, invent no new hues. Principle 4 then only governs how the colors are used.
3. **Demo content is fine:** for drafts and mockups, demo data and placeholder functionality are not flagged. Principle 5 then only checks that the demo data feels believable and specific.
4. **Content stays:** in fix mode, do not delete or rewrite visible text. Hide decorative labels with CSS if needed, never remove them from the markup, unless the user asks.
5. **Signature elements** the user names (e.g. a hero effect) stay untouched.
6. No em or en dashes in copy.

## The 7 principles

| # | Principle | Rule | Typical AI mistake | Fix |
| --- | --- | --- | --- | --- |
| 1 | Focal point | One element draws the eye first, everything else is quieter | Badge, gradient headline, two equal buttons, stat bar and three feature cards all compete | Name the screen's purpose, make that the biggest and highest-contrast element, turn the rest down or remove it |
| 2 | Spacing | Fixed scale in multiples of 4 or 8 px; proximity shows what belongs together | Same padding everywhere, nothing feels grouped | Gaps on 8, 16, 24, 32 (etc.), label close to its input, tighter inside a section than between sections |
| 3 | Typography | Hierarchy through weight and color, not size | Ever bigger headings, many sizes on one card | One typeface, two at most. Titles only slightly larger but darker and heavier. Secondary text in a softer gray. Slightly tighter tracking on headings. Short line lengths |
| 4 | Color | Mostly neutrals, one accent only where it matters | Purple gradient on background, headline, buttons and badges | Remove gradients, grays slightly tinted toward the brand color, accent only on the primary button, focus state and links |
| 5 | Content | Real, product-specific content | John Doe, round numbers, vague features | Real names, numbers, features, quotes (for demos: believable demo data) |
| 6 | Details | Radius, shadows and icons consistent everywhere | Harsh edges, one heavy blur shadow, icons a few pixels off | Consistent radius, nested elements slightly smaller than their container, soft layered shadows, icons same size and stroke on the text baseline, shared edges |
| 7 | Motion | Motion starts where the user acted | No transitions, or everything fades up the same way | Dropdowns grow from their button, opening slightly slower than closing, notifications slide in from the edge and stack, sheets follow the finger, short ease-out animations |

Calibration references: Linear homepage (focal point), Stripe Checkout (spacing), Notion (color), iPhone notification (details), Apple Maps bottom sheet (motion).

## Audit: steps

1. Look at the page: desktop and mobile screenshots, plus read the HTML/CSS. For scroll animations, judge the end states, not intermediate frames.
2. Check for real rendering defects too: elements overlapping on mobile, full-width bands not reaching the edge (e.g. default body margin), clipped text, empty grid columns. These count under principle 6.
3. If available, run `npx impeccable detect <file or url>` and map the findings to the principles (glows and gradients to 4, kickers and icon tiles to 1, contrast to 3/4, radius and shadows to 6). If the tool is missing, continue without it.
4. Answer each of the 7 check questions with Yes or No and concrete evidence (selector, text, value).
5. Output the report.

### Check questions

1. What is this screen for, and is that the most obvious thing on it?
2. Does every gap follow a fixed scale?
3. Does hierarchy come from weight and color rather than size alone?
4. Is the accent color used only where it matters?
5. Is every piece of content real (or believable, for demos)?
6. Do radius, surfaces and shadows match everywhere, with no rendering defects?
7. Does every animation start where the user acted?

### Report format (keep it short)

Score large at the top, then one table, nothing else:

```
# 4 / 7

| # | Principle | Result | Evidence | Fix |
|---|---|---|---|---|
| 1 | Focal point | No | Two equal buttons in the hero | Turn the second button into a text link |
...
```

At most one closing sentence: the biggest lever.

## Fix: steps

Keep this order; components and layout structure stay the same. Ideally add a separate CSS layer on top of the original so it stays comparable.

1. **Focus:** exactly one primary button, everything else secondary (text link); hide competing elements such as stat bars, badges and kickers.
2. **Spacing:** move every gap onto the scale, group related items more tightly.
3. **Typography:** one typeface, headings heavier rather than bigger, gray for supporting text, labels in sentence case.
4. **Color:** remove gradients, colored glows and halos; tinted neutrals; accent only on the primary button and links. Text contrast at least 4.5:1.
5. **Content:** replace placeholders with real (or believable demo) content. If real content is missing, ask the user instead of inventing it.
6. **Details:** align radii, smaller radii for nested elements, replace card borders with surfaces, soft layered shadows, align edges, fix rendering defects.
7. **Motion:** menus grow from their trigger, notifications stack, all animations short with ease-out, animate only `transform` and `opacity`, respect `prefers-reduced-motion`.

Then run the audit again and report the before/after score.

## Output

- Keep replies short, one point per reply.
- Always output code changes complete and copy-ready in one piece.
- Provide created files or pages as clickable links.

## Further reading

- Motion: "transitions" and Emil Kowalski's animation skills.
- For deeper, measurable checks: Impeccable (`detect`, `critique`, `audit`) or Hallmark (`sloplint`).
- For composition and layout: the `layout-refinement` skill.

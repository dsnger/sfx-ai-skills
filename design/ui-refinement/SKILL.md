---
name: ui-refinement
description: Finds and fixes the detail-level UI and UX mistakes on product pages, landing pages and app screens (overlay contrast, imagery, alignment, color, type, labels, badges, trust signals, icon sets, dividers, spacing, redundant labels, primary action) and suggests UX upgrades like sticky actions and presets. Use this skill whenever a screen needs polish, feels cluttered or "almost right", a product or detail page is being designed or reviewed, or the user asks what is wrong with a UI, even if they don't say "refinement".
---

# UI Refinement

A screen can have the right components and still feel cheap because of many small decisions. This skill walks through 15 common detail mistakes, then looks for UX upgrades that make the task easier, not just the screen prettier. The guiding idea: design for the system, not for one screenshot. Every check asks "does this still work with other content, other images, other products?"

## Modes

- **audit**: check only, report with score.
- **fix**: apply the fixes, then audit again.
- No mode given: audit first, then ask whether to fix.

## Fixed constraints

- Content and demo data stay. Hide or restyle, don't rewrite, unless a check is explicitly about wording (6, 13, 14) and the user agrees.
- A given brand palette stays; check 4 then governs saturation and usage, not new hues.
- Surfaces over lines: no thin borders on cards and tiles. Dividers only where they truly separate, and then subtle (check 11).
- Signature elements the user names stay untouched.
- No em or en dashes in copy.

## The 15 checks

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

## UX upgrades (after the 15 checks)

These are optional and go beyond fixing. Suggest only those that fit the screen.

1. **Content card over the hero:** content sits in a soft, rounded card that slides over the hero image on scroll; once the image leaves, the title moves into a sticky top bar so context is never lost.
2. **Sticky action area:** keep the primary action (and its controls) visible at the bottom while users scroll, because they often decide only after reading further.
3. **Presets for common choices:** offer one-tap options for the most common values (e.g. 500 g, 1 kg, 2 kg, ideally from real usage data) and keep the custom control for flexibility.

## Audit: steps

1. Look at the screen: desktop and mobile screenshots plus HTML/CSS. For scroll effects judge end states.
2. Stress test the system: mentally (or actually) swap in a bright image, a long title, a different product. Note what breaks (checks 1, 2, 7, 14).
3. Rate each check Yes / No / n/a with concrete evidence (selector, text, value).
4. List which UX upgrades would fit, if any.
5. Output the report.

### Report format (keep it short)

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

## Fix: steps

Work as a separate CSS layer (plus minimal markup changes where unavoidable) on top of the original so it stays comparable. Order: alignment and spacing (3, 12) first because everything else sits on them, then type (5, 7, 8, 6), then color and icons (4, 10, 11, 1), then information order and action (9, 13, 14, 15), then upgrades if agreed. Audit again and report before/after.

## Output

- Keep replies short, one point per reply.
- Always output code changes complete and copy-ready in one piece.
- Provide created files or pages as clickable links.

## Related

- `ui-principles` for the big picture (focal point, spacing scale, color, motion).
- `layout-refinement` for composition (grid breaks, balance, near tangencies, decision points).

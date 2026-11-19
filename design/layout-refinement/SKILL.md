---
name: layout-refinement
description: Audits and improves layouts of websites, landing pages, posters, presentations and print against 7 layout techniques (breaking the grid on purpose, balancing visual weight, near tangencies, viewing distance, series consistency, aligning answers to the same question, information at the decision point) with a score from 0 to 7. Use this skill whenever a layout feels off, busy, unbalanced or hard to scan, or a composition review is requested, even if the techniques are not mentioned.
---

# Layout Refinement

Small layout moves with a big effect. The techniques come from graphic design (posters, magazines, packaging) and apply just as well to websites. It is rarely about rebuilding, usually about one deliberate shift.

## Modes

- **audit**: check the layout, report with score x / 7.
- **fix**: apply the moves, then audit again.
- No mode given: audit first, then ask whether to fix.

## Fixed constraints

- Content, palette and signature elements named by the user stay untouched. Move, scale and regroup; do not rewrite.
- No thin border lines on cards and tiles; surfaces instead of lines.
- No em or en dashes in copy.

## The 7 techniques

| # | Technique | What to look for | Fix | On the web |
| --- | --- | --- | --- | --- |
| 1 | Break the grid on purpose | A consistent grid sets an expectation. When an element breaks it, that exact spot gets noticed | Break it only where two things should visibly interact (product reaching into the next area, image overlapping a section edge). Correct accidental outliers | An image, mockup or object deliberately crosses a section boundary or card instead of sitting neatly in its box |
| 2 | Balance visual weight | Eye flow (an object pointing at an element) often ends in an overloaded corner where the eye gets stuck. Squint test: where does mass bunch up? | Move the target element so the eye can continue and weight spreads across the area | Don't stack CTA, badge and image in the same corner; check hero composition for weight, not just direction |
| 3 | Avoid near tangencies | Two edges that almost touch create a thin strip that grabs more attention than intended | Decide: give clear space (separate) or clearly overlap (connected). Never just short of it. For print, consider binding and bleed | Images almost touching the viewport edge, section edge, header or a neighbor; elements nearly colliding at breakpoints |
| 4 | Viewing distance | At 45 cm on a monitor, small things look refined; in real use they are unreadable. Simply enlarging everything creates a hierarchy problem | Shrink the design to its real-world size. Decide what must land in the first second and what can wait. If two things must register at once, give them a shared focal point (e.g. a date set over a calm, dark area of the photo) | Check the mobile view and thumbnail/social preview; key message plus key info in the first second; text over images only on calm image areas |
| 5 | Series: constants and variation | Cropping every image the same looks consistent but strips each image of what makes it special | Decide what repeats (type position, baseline, color accent) and lock it to the grid. Choose each crop by what that image needs to show | Card rows, team photos, case studies: fixed layout constants, individual crops instead of identical centered ones |
| 6 | Same question, same place | When the same question applies to several items (opening time, price, status), nobody should have to hunt for it in body text | Align the answers in a shared column or row that sits on the same line as its item. Two routes: browsing (image, text) and shortcut (column), using the same rows | Prices, dates, durations, status always in the same position and on one line in cards; comparison tables instead of info buried in copy |
| 7 | Information at the decision point | People act step by step. A note that comes after the action is seen too late | Walk through the layout in the user's order. At every point where they form an opinion or make a choice: have they seen everything that could change it? If not, move that info right there | Conditions, notes and options inside the step, not below it: shipping costs next to the price, format requirements at the upload field, variant notes before the add-to-cart button |

## Multi-page and content-heavy layouts

- **Same function, same form.** Sections with the same content and task look the same on every page of a site. Readers recognize the pattern and find their way faster.
- **Sub pages go deeper, not wider.** What the main page already summarizes is not repeated as its own section on a sub page.
- **Long content stays scannable.** However long a block gets, readers can see its structure at a glance and jump to what concerns them.

## Audit: steps

1. Look at the layout: desktop and mobile screenshots (for print: full view and detail). Add a scaled-down view at real-world size (technique 4) and a blurred squint view (technique 2).
2. Walk the user's path in reading order and mark the decision points (technique 7).
3. Rate each technique Yes or No with concrete evidence (element, position, distance). Techniques 5 and 6 count as Yes if there is no series or no recurring question.
4. Output the report.

### Check questions

1. Is the grid broken only where two things are meant to interact?
2. Is visual weight spread out instead of piling up in one corner?
3. Are there no edges that almost, but not quite, touch?
4. At real-world size, does the most important thing land in the first second without breaking the hierarchy?
5. Does a series repeat the right things and vary the right things?
6. Do answers to the same question sit in the same place and on one line?
7. Is every decision-relevant piece of information before or at the decision, not after it?

### Report format (keep it short)

Score large at the top, then one table, nothing else:

```
# 5 / 7

| # | Technique | Result | Evidence | Fix |
|---|---|---|---|---|
| 3 | Near tangency | No | Hero image ends 6 px short of the section edge | Pull the image 40 px across the edge or give it 48 px of space |
...
```

At most one closing sentence: the biggest lever.

## Fix: steps

Keep moves as small as possible: shift, align, overlap, group. Ideally add a separate CSS layer on top of the original so it stays comparable. Order by impact: first 7 and 4 (comprehension), then 2 and 3 (calm), then 1, 5 and 6 (character and order). Then run the audit again and report the before/after score.

## Output

- Keep replies short, one point per reply.
- Always output code changes complete and copy-ready in one piece.
- Provide created files or pages as clickable links.

## Related

For surface quality (focal point, spacing, typography, color, details, motion), use the `ui-principles` skill; the two complement each other.

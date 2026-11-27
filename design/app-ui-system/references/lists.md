# Lists and the list toolbar

## The base row

- The profile names one reference list. Its row is the base of every list of the same kind of item: the same information in the same place. Other lists add, leave out or vary only with a reason.
- **Row anatomy** (adapt the parts to the domain, keep the order and the idea): who or what (a picture, with the name on hover and focus; phone rows show the name) · title · its context line · an identifier as its own column after the title from the width the profile sets, inline below it on narrower screens · a state light right before the main value · the main values · commands at the right edge. No separate status column; marks stand under the title.
- **Only controls react.** The title opens the item, a chevron expands it; the row area does nothing and has no hover. No extra "Open" button or icon.
- **The expanded part** is the same in every list of that item (facts, order, spacing). It repeats nothing the row shows, ends in one status line behind a fine rule with one link at the right, and shows a chevron only where there is something to expand. No label without a value.
- **Same kind, same commands.** An item in the same state carries the same commands on every screen, with the same icons and meanings everywhere (the profile lists them). A close icon only closes. Row actions: up to two as icon buttons with tooltip and accessible name; a "⋯" menu only from three items.

## Columns

- **No drift.** At one width no column moves when the period, tab or filter changes, and no column comes and goes with the rows. Where a list has a date column, it is always shown; today reads "Today" (in the app's language); a date links to that day's view where one exists. Column labels align like their cells.
- **The title column keeps its width.** Other columns give way first, in an order the profile states. Below the width the profile sets, compact rows replace a squeezed table. When room is short, commands go before text is cut. No word breaks inside a word; no page scrolls sideways at any supported width.

## Loading, grouping, tabs, totals

- **No pages:** load the first batch (the profile sets its size), then "Load more", keeping place and focus. No "rows per page".
- **Grouping** as in the domain's proven tools, up to two levels; a group head shows name, count and its totals.
- **Tabs** keep a list homogeneous (for example finished | active). The profile sets the default tab. A tab offers no control that makes no sense for it.
- **Totals** stand in a row under the list, under their own columns, in the table's type size; a full-width bar fixed at the bottom only while that row is out of view. The list, its total, its tab count and its export always agree. Counts say what they count.
- **Plain values:** one value per meaning (no near-duplicate columns); a value that does not apply shows "–"; no "at least" and no footnotes; notes go behind an info icon. If the app shows time spans: durations in words for finished items, a ticking clock for running ones; seconds only where they decide.

## Actions and states

- **Delete acts at once** with "Undo" for a few seconds (the profile sets how long); what cannot be undone asks first.
- **Bulk actions** wherever several records can be acted on, with the same bar everywhere.
- **States:** empty says what is empty and offers the next step; "not loaded" never looks like 0 or "–"; a failure says so, with a retry.

## The list toolbar (one shared component)

- **One schema for every list**, two groups with fixed places:
  - *narrowing:* search, period, filters, reset;
  - *arranging:* tabs, select, group, sort, columns, export, reload.
- **Search first,** at the left, at one fixed width the profile sets (never stretched); the rest at the right. Below the breakpoint the profile sets it fills its row.
- **Rows align at both edges.** No reserved empty slots, no gaps without a reason, never a second row that starts halfway. Two designed forms only: expanded (filters open) and compact ("Filters (n)"). The form changes at the one width the profile sets, found by measuring the full range, never by what currently fits; the phone uses the compact form.
- **Filters:** several values where the data allows; each as narrow as its label; once set, only a number badge (a status filter shows its word instead; whether that word may push or keeps the width of its longest word is decided per place from its range). The number widens the filter and pushes what follows.
- **Reset** clears filters only: a plain ✕ right after the last filter, shown only while a filter is set. The search clears itself with its own ✕.
- **Sorting and grouping** are their own controls, not styled like filters; as wide as their label (up to the maximum the profile sets); a dot when not at the default; a separate switch shows and reverses the direction; their menus end with "Remove sorting" / "Remove grouping" once changed; a second grouping level appears only after a first.
- **Settings are icons in the bar** (columns, export, reload), never hidden in a "⋯".
- **Periods:** a period menu lists choices only (the profile lists them); a custom range shows its two fields when chosen.
- **Long periods:** if the backend reads in windows, read window by window; refuse a period beyond the limit the profile sets, with the reason.
- **Messages never push the layout:** they stand inside the field or float.

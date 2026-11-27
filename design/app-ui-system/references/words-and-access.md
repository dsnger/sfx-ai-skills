# Words and accessibility

## Words

- **Words explain themselves.** One term per thing, everywhere, in the form of address the profile sets.
- **Fixed terms live in the profile's glossary** (the term, and the words it replaces). Use them exactly; add new ones there when the owner decides.
- No filler words and no placeholders; no internal ids (such as a database id) in the interface; no concepts the domain does not have.
- No status sentences under buttons. Reasons go behind an info icon with a tooltip.

## Accessibility

- State never by color alone: a state light has a name, icons carry words or tooltips.
- Hover content is also available on focus and on tap.
- Every icon button has an accessible name and a tooltip.
- Run an automated checker (for example axe) with 0 violations in every theme, at a wide and a phone width.
- Check the Tab order in both directions.

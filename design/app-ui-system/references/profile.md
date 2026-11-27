# The UI profile

The profile holds every concrete value and decision for one app. The rules in this skill refer to it. Create it before the first build; keep it current after every decision that applies beyond one screen.

## How to create it

1. Read what the code already answers: the package manifest, the component library's config and CLI (the library's own skill knows which), the CSS or theme tokens, fonts, existing screens.
2. Ask the owner only what is still open, one question per point, each with your recommendation and the reason. Offer the library's own options where it has them (for example the styles of the library's style generator) instead of inventing values.
3. Write the profile and show it. Do not build before the owner has seen it.

Never assume a library, a style or a value because it is common.

## Template

```markdown
# UI profile: <app>

## Stack
- Framework:
- Component library and version:
- Style / theme of the library (as chosen in its generator or config):
- CSS approach (for example Tailwind and version):
- Table / data grid library:

## Values
- Control size in heads and toolbars: (library default: …) · in rows: …
- Touch target on coarse pointers:
- Radius source (file/token) and scale: surface · notice · control/floating panel · choice/menu item · badge/avatar/dot · checkbox
- Recorded radius deviations:
- Spacing base unit: · shared rhythms (for example row padding):
- Typefaces (self-hosted): · monospace for identifiers:
- Accent color and its uses: · status color(s) and their meaning:
- Search width in the list toolbar: · max width of sort and group controls:
- First batch size before "Load more":
- Period choices · custom range allowed:
- Breakpoints: identifier column from … · search fills its row below … · compact rows below … · stacked record pages below … · narrow fallbacks below … · smallest supported width …
- Forms per width for the whole app (each width a parameter; orientation values from one reference project, to adapt): open filters from (~1536) · identifier column from (~1440) · table from (~1280), compact rows below · edge-to-edge with a phone head below (~768) · two-column pages stack below (~1280)
- Range tables (place × width × case → form): one per list, toolbar and form, with its range (items, filters, values, combinations, none/one/many)
- Widths and themes to check before "done":
- Smallest overlay viewport:
- Undo window after delete:
- Period limit and read window (if the backend reads in windows):

## Screens
- Reference screen(s) that stay as approved:
- Main working view:
- Records that are pages · items that open in a drawer:
- Reference list (the base row):
- Order in which columns give way:
- Default tab per list:

## Patterns
- Proven products to copy (function, not look):
- Command icons and their meanings (for example create, close):

## Words
- Language and form of address:
- Glossary (term · replaces):

## Reversed (do not revive)
- <old rule> → <new rule> (date)

## Open
- <decision still pending>
```

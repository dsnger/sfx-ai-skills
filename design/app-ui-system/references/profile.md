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
- Forms per width for the whole app, only here (each width is a parameter; bracketed px values are orientation from one reference project, not defaults: measure your own, they count as proposals until the owner approves): open filters from … (~1536) · identifier column from … (~1440) · table from …, compact rows below (~1280) · list with breakdown stacks below … (~1280) · search fills its row below … · phone layout below … (~768) · narrow fallbacks below … · smallest supported width …
- Range tables (place × width × case → form): one per place (for example list, toolbar, input form), with its range (items, filters, values, combinations, empty/one/many)
- Widths and themes to check before "done":
- Smallest overlay viewport:
- Undo window after delete:
- Period limit and read window (if the backend reads in windows):

## Screens
- Reference screen(s) that stay as approved:
- Main working view:
- Records that are pages · items that open in a drawer:
- Reference list (the base row):
- Order in which columns give way, and the named width for each step:
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
- <decision or proposed value still pending; proposals are not used in the build>
```

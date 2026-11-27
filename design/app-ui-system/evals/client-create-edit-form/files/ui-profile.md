# UI profile: Fieldbook

## Stack
- Framework: static HTML prototype (later React)
- Component library: own components in app.css
- CSS approach: plain CSS with tokens in tokens.css
- Icon set: placeholder glyphs

## Values
- Control size in heads and toolbars: 36 px (--control-h) · in rows: 32 px (--control-h-sm)
- Radius source: tokens.css --radius 12 · surface 16.8 · control 9.6 · menu item 7.2 · badge/avatar/dot round · checkbox 4
- Spacing base unit: 4 px · row padding --row-pad = 16 px
- Typeface: Inter (self-hosted in production) · monospace: system
- Accent: #0f6e5c, only the one filled main action per view · warning #9a5b00 · error #b4232a
- Content max width: 1320 px · form page width: 48rem
- Search width in the list toolbar: 276 px
- Breakpoints: compact rows below 1024 px
- Widths to check: 1440 / 1024 / 390 / 320, light only
- Smallest overlay viewport: 360 × 600
- Undo window after delete: 10 s

## Screens
- Reference screen: Clients list (clients.html)
- Reference list (the base row): Clients
- Order in which columns give way: Revenue, then Open jobs, then Contact · City
- Records that are pages: clients, jobs · entries that open in a drawer: time entries

## Words
- Language: English, plain
- Glossary: "Client" (not "Customer") · "Job" (not "Project") · "Close / Closed / Reopen" (not "Lock")

## Reversed (do not revive)
- Row click opens the client → the title opens, the row area does nothing (2026-11-10)

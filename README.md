# SFX AI Skills

Agent skills by SmileFX in the open SKILL.md format. Works with Claude, Codex, Gemini CLI, Cursor and other agents that read skills.

## Design

### Which design skill when

- **Building or changing app screens** (lists, forms, dialogs, navigation in a web app): use **app-ui-system**. On first use it sets up the project's UI profile, then every screen is built within it.
- **Reviewing or improving a finished page or screen** (website, landing page, app screen, poster): use **design-quality**. It already contains the four single skills below as blocks, so do not run it together with them.
- **Only one aspect** of an existing page or screen: use the matching single skill.
  - **ui-principles:** the page looks generic or AI-made.
  - **ui-refinement:** the screen is almost right and needs detail polish.
  - **layout-refinement:** the composition feels off; also for print, posters and slides.
  - **ux-psychology:** a flow converts poorly or users drop off.
- **Logos:** use **logo-design**. It is independent of the others.

**Order when combining:**

1. **app-ui-system** while building.
2. **design-quality** afterwards, as audit or fix of the built result.
3. If you use the single skills instead of design-quality, run them in this order: ui-principles, ui-refinement, layout-refinement, ux-psychology.

### Skills

- **[design-quality](design/design-quality/SKILL.md)**
  Audits and fixes pages, screens and components in one run of four blocks (UI principles, detail mistakes, layout techniques, UX psychology), with shared rules, an accessibility floor and a self-check. Fixes go into a copy of the real source; decisions come back as visual variants.
- **[app-ui-system](design/app-ui-system/SKILL.md)**
  Builds app interfaces that stay coherent across every screen, on whatever stack the project uses. Stack, style and values are asked once and kept in a per-project UI profile.
- **[ui-principles](design/ui-principles/SKILL.md)**
  Audits and refines websites and app screens against principles of good UI (focal point, spacing, typography, color, content, details, motion).
- **[ui-refinement](design/ui-refinement/SKILL.md)**
  Finds and fixes 15 detail-level UI/UX mistakes and suggests UX upgrades.
- **[layout-refinement](design/layout-refinement/SKILL.md)**
  Audits and improves layouts against 7 layout techniques from graphic design.
- **[ux-psychology](design/ux-psychology/SKILL.md)**
  Audits and improves screens and flows against 9 principles of how people perceive and decide, without dark patterns.
- **[logo-design](design/logo-design/SKILL.md)**
  Guides logo work from brief to handover and reviews logos against 12 principles.

## Copy

- **[copy-rules](copy/copy-rules/SKILL.md)**
  Rules for German marketing and business copy: stance, sentence rules, banned AI patterns, value-driven wording, sentence checker script.
- **[sales-page-copy](copy/sales-page-copy/SKILL.md)**
  Sales pages, landing pages and pitch presentations end to end: instruction checklist, reader chain, copy, review rounds, hand-off.
- **[copy-review-panel](copy/copy-review-panel/SKILL.md)**
  Independent reviewer panel for copy: personas, sales psychology expert, client reviewer, behavior test, debate with referee.

## Business

- **[client-offboarding](business/client-offboarding/SKILL.md)**
  Project handover and end-of-service documents for web projects, in the name of any sender (own brand, agency, white label).
- **[website-report](business/website-report/SKILL.md)**
  Project, quality and follow-up reports for websites in plain language, from check results.

## Web

- **[launch-check](web/launch-check/SKILL.md)**
  Checks before go-live, on launch day and after launch, with a findings list and raw data.

## External skills we use

Third-party skills and tools these skills build on or are used alongside.

- **Impeccable**: design skill set with deterministic slop detector (`detect`, `critique`, `audit`). [impeccable.style](https://impeccable.style) · [GitHub](https://github.com/pbakaus/impeccable)
- **Hallmark**: anti-AI-slop design skill with `sloplint`. [GitHub](https://github.com/Nutlope/hallmark)
- **Taste Skill**: opinionated design system skill with copy and layout checks. [GitHub](https://github.com/Leonxlnx/taste-skill)
- **Apple Design Skill (dickwu)**: Apple-style design guidance. [GitHub](https://github.com/dickwu/apple-design-skill)
- **Apple Design (Emil Kowalski)**: Apple-style design and motion guidance, part of Emil Kowalski's skills. [GitHub](https://github.com/emilkowalski/skills/tree/main/skills/apple-design)
- **Prototype (Emil Kowalski)**: prototyping skill, part of Emil Kowalski's skills. [GitHub](https://github.com/emilkowalski/skills/tree/main/skills/prototype)
- **Web Interface Guidelines (Vercel)**: technical front-end checklist (accessibility, focus, forms, animation, i18n); complements the design skills. [GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) · [Rules](https://github.com/vercel-labs/web-interface-guidelines)
- **Writing Guidelines (Vercel)**: docs writing rules; four AI-tell patterns adopted into copy-rules. [GitHub](https://github.com/vercel-labs/writing-guidelines)
- **shadcn (official)**: reads `components.json` and the shadcn CLI so components and props are used correctly; used alongside app-ui-system. [Docs](https://ui.shadcn.com/docs/skills)

## Installation

Copy a skill's folder into your agent's skills directory, e.g. `~/.claude/skills/ui-principles/` for Claude Code.

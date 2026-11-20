# SFX AI Skills

Agent skills by SmileFX in the open SKILL.md format. Works with Claude, Codex, Gemini CLI, Cursor and other agents that read skills.

## Design

| Skill | Purpose |
| --- | --- |
| [ui-principles](design/ui-principles/SKILL.md) | Audits and refines websites and app screens against principles of good UI (focal point, spacing, typography, color, content, details, motion) |
| [ui-refinement](design/ui-refinement/SKILL.md) | Finds and fixes 15 detail-level UI/UX mistakes and suggests UX upgrades |
| [layout-refinement](design/layout-refinement/SKILL.md) | Audits and improves layouts against 7 layout techniques from graphic design |
| [ux-psychology](design/ux-psychology/SKILL.md) | Audits and improves screens and flows against 9 principles of how people perceive and decide, without dark patterns |
| [logo-design](design/logo-design/SKILL.md) | Guides logo work from brief to handover and reviews logos against 12 principles |

## Copy

| Skill | Purpose |
| --- | --- |
| [copy-rules](copy/copy-rules/SKILL.md) | Rules for German marketing and business copy: stance, sentence rules, banned AI patterns, value-driven wording, sentence checker script |
| [sales-page-copy](copy/sales-page-copy/SKILL.md) | Sales pages, landing pages and pitch presentations end to end: instruction checklist, reader chain, copy, review rounds, hand-off |
| [copy-review-panel](copy/copy-review-panel/SKILL.md) | Independent reviewer panel for copy: personas, sales psychology expert, client reviewer, behavior test, debate with referee |

## External skills we use

Third-party skills and tools these skills build on or are used alongside.

| Name | What for | Link |
| --- | --- | --- |
| Impeccable | Design skill set with deterministic slop detector (`detect`, `critique`, `audit`) | [impeccable.style](https://impeccable.style) · [GitHub](https://github.com/pbakaus/impeccable) |
| Hallmark | Anti-AI-slop design skill with `sloplint` | [GitHub](https://github.com/Nutlope/hallmark) |
| Taste Skill | Opinionated design system skill with copy and layout checks | [GitHub](https://github.com/Leonxlnx/taste-skill) |
| Apple Design Skill (dickwu) | Apple-style design guidance | [GitHub](https://github.com/dickwu/apple-design-skill) |
| Apple Design (Emil Kowalski) | Apple-style design and motion guidance, part of Emil Kowalski's skills | [GitHub](https://github.com/emilkowalski/skills/tree/main/skills/apple-design) |
| Prototype (Emil Kowalski) | Prototyping skill, part of Emil Kowalski's skills | [GitHub](https://github.com/emilkowalski/skills/tree/main/skills/prototype) |
| Web Interface Guidelines (Vercel) | Technical front-end checklist: accessibility, focus, forms, animation, i18n; complements the design skills | [GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) · [Rules](https://github.com/vercel-labs/web-interface-guidelines) |
| Writing Guidelines (Vercel) | Docs writing rules; four AI-tell patterns adopted into copy-rules | [GitHub](https://github.com/vercel-labs/writing-guidelines) |

## Installation

Copy a skill's folder into your agent's skills directory, e.g. `~/.claude/skills/ui-principles/` for Claude Code.

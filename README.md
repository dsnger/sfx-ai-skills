# SFX AI Skills

Agent skills by SmileFX in the open SKILL.md format. Works with Claude, Codex, Gemini CLI, Cursor and other agents that read skills.

## Design

| Skill | Purpose |
| --- | --- |
| [ui-principles](design/ui-principles/SKILL.md) | Audits and refines websites and app screens against principles of good UI (focal point, spacing, typography, color, content, details, motion) |
| [ui-refinement](design/ui-refinement/SKILL.md) | Finds and fixes 15 detail-level UI/UX mistakes and suggests UX upgrades |
| [layout-refinement](design/layout-refinement/SKILL.md) | Audits and improves layouts against 7 layout techniques from graphic design |

## External skills we use

Third-party skills and tools these skills build on or are used alongside.

| Name | What for | Link |
| --- | --- | --- |
| Impeccable | Design skill set with deterministic slop detector (`detect`, `critique`, `audit`) | [impeccable.style](https://impeccable.style) · [GitHub](https://github.com/pbakaus/impeccable) |
| Hallmark | Anti-AI-slop design skill with `sloplint` | [GitHub](https://github.com/Nutlope/hallmark) |
| Taste Skill | Opinionated design system skill with copy and layout checks | [GitHub](https://github.com/Leonxlnx/taste-skill) |
| Design Slop Cop | Scores websites for AI design patterns | [GitHub](https://github.com/AdrianKrebs/design-slop-cop) |

## Installation

Copy a skill's folder into your agent's skills directory, e.g. `~/.claude/skills/ui-principles/` for Claude Code.

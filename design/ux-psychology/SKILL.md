---
name: ux-psychology
description: Audits and improves websites, landing pages, app screens, sign-up and onboarding flows, forms, upgrade dialogs, paywalls and pricing against nine principles of how people perceive and decide (first impression, low effort, peaks and a good ending, smart defaults, head start, give before you ask, let them build, show what is at stake, anchor the cost), honestly and without dark patterns, with a score from 0 to 9. Use this skill whenever a site feels cheap or untrustworthy, a flow converts poorly, users drop off, a form, onboarding, sign-up, upgrade or checkout is designed or reviewed, or someone asks about UX psychology, conversion, "premium feel" or "why don't users finish this", even if no principle is named.
---

# UX Psychology

Screens fail less often because they look bad than because they ignore how people perceive and decide. People judge a whole site by its first view, trust what is easy to process, remember the best moment and the end, avoid effort, speed up near a goal, return favors, value what they made, weigh losses more than gains and judge every number against the last one. This skill applies that to a screen, honestly.

## Modes

- **audit**: check only, report with score.
- **fix**: improve following the principles, then audit again.
- No mode given: audit first, then ask whether to fix.

## Honesty comes first (overrides the principles)

These principles work because they match real behavior. Used to deceive, they turn into dark patterns, cost trust and in many markets break consumer or privacy law. Premium feel comes from respect for the visitor's time and intelligence, not from tricks. So:

1. **Everything shown is true.** Result counts are real, deadlines exist, losses are the user's actual loss. Progress counts only steps the user did or confirmed; a pre-filled default the user hasn't looked at is not progress. A missing fact becomes a placeholder, never an invention.
2. **Declining stays easy and neutral.** The way out is visible and worded plainly ("Nicht jetzt", "Ohne Upgrade weiter"). No shaming labels, no hidden close buttons.
3. **Defaults serve the user, never the business at the user's expense.** Never preselect consent, newsletters, paid extras, data sharing or longer contracts.
4. **No fake pressure.** No invented countdowns, scarcity or "only 2 left" without data behind it.
5. **Brand palette, signature elements and content stay** as in other design work. Microcopy that a principle is about (button labels, decline labels, a progress line, a price reference, a confirmation message) may change. German copy follows `copy-rules` if available.

## The 9 principles

### How it feels (perception)

| # | Principle | Why it works | Typical mistake | Fix |
| --- | --- | --- | --- | --- |
| 1 | **First impression** | The first view is judged in a moment and colors the judgment of everything after it (halo effect) | First screen crowded with badges, several buttons, sliders, weak or generic imagery, unclear message | Decide the one feeling and one message the first view must carry, give it room and the best material, move everything else below |
| 2 | **Low effort to understand** | What is easy to process feels better, calmer and more trustworthy (cognitive fluency); effort feels like risk | Competing elements, long navigation, several goals per section, dense text | One primary goal per section, clear order of importance, short predictable navigation, room around content. Remove before adding. For the visual execution use `ui-principles` and `layout-refinement` |
| 3 | **Peaks and a good ending** | People remember an experience by its best moments and by how it ended (peak-end rule) | Static controls without feedback, forms that end in a bare "Gesendet", flows that stop without a next step | Give every action quiet feedback (hover, focus, validation, saved state). Design the end of every flow on purpose: confirm what happened, what comes next, and give one useful next step |

### What people do (decisions)

| # | Principle | Why it works | Typical mistake | Fix |
| --- | --- | --- | --- | --- |
| 4 | **Smart defaults** | Every open choice is effort; many choices at once lead to no choice. A sensible default reads as a recommendation, and most people keep it | Empty forms, every field a decision, long option lists, a button that only says "Submit" | Pre-fill each field with the most common or most likely choice, cut options, ask later what can wait. The button names the result ("12 freie Termine anzeigen") |
| 5 | **Head start** | People speed up the closer they feel to a goal, and the starting line can be set | Progress at 0 %, a long list of empty steps, account creation treated as something before the journey | Count what the user has really done as the first step, show where they are and how little is left |
| 6 | **Give before you ask** | Receiving something real creates a wish to give back; asking first feels like a wall | Results locked behind sign-up, "enter your email to continue" before any value | Deliver a real, useful part first, then offer the account as a way to save or get more |
| 7 | **Let them build** | People value what they made or chose themselves; leaving then means abandoning it | Sign-up screen with nothing of the user's own on it | Let users create or configure something before the account step; the account step saves their work ("Weiter", "Speichern") |
| 8 | **Show what is at stake** | Losing weighs more than gaining; people protect what they have | Upgrade screens that only list features, nothing changes when ignored | Where acting really matters, name the user's concrete loss or limit in their own terms (their files, their data, their deadline). Keep the decline neutral |
| 9 | **Anchor the cost** | Every number is judged against the one seen just before | A price alone on its own screen, a cost without any reference | Show the cost next to the honest reference it belongs to: what it protects, today's cost, the per unit or per day amount, the larger purchase it is part of |

A principle that does not apply to the screen (no price, no sign-up, no flow) is **n/a** and does not count against the score.

## Audit: steps

1. Look at the screen or flow: screenshots or the HTML, the first view without scrolling, and the step before and after if they exist.
2. Name the one feeling the first view should create, the one action the screen wants, and the moment the user might leave.
3. Answer the nine check questions with Yes, No or n/a and concrete evidence (element, label, value).
4. Check the honesty rules. Any violation goes into the report even if it scores well.
5. Output the report.

### Check questions

1. Does the first view carry one clear message and feeling, with nothing competing?
2. Can a first-time visitor see the order of importance and the next step without effort?
3. Does every action get feedback, and does every flow end on purpose with a next step?
4. Are the likely choices already made for the user, and does the button name the result?
5. Does the user start with visible progress that counts only real steps?
6. Does the user get something real before being asked for anything?
7. Does the user own something on this screen before the account step?
8. Where acting matters, does the screen name the user's concrete loss, with a neutral way out?
9. Is every cost shown next to an honest reference?

### Report format (keep it short)

Score large at the top (counting only applicable principles), then one table, nothing else:

```
# 3 / 6

| # | Principle | Result | Evidence | Fix |
|---|---|---|---|---|
| 1 | First impression | No | Hero holds badge, slider and three buttons | One message, one button, slider below the fold |
| 4 | Smart defaults | No | Five empty fields, button "Absenden" | Pre-fill date and time with the next free slot, button "3 freie Termine anzeigen" |
| 9 | Anchor the cost | n/a | No price on this screen | |
...
Honesty: no issues
```

At most one closing sentence: the biggest lever.

## Fix: steps

Work in this order, keep layout and components, change only what a principle is about.

1. **First view:** one message, one feeling, one primary action, the best material; everything else moves down.
2. **Remove effort:** fewer competing elements and navigation items, defaults, fewer options, defer what can wait, result-naming buttons.
3. **Set the starting line:** count real completed steps, show remaining steps.
4. **Move value forward:** show the real part of the result before any gate.
5. **Give ownership:** let the user make choices of their own before the account step.
6. **Make stakes concrete** where it matters, with a neutral decline.
7. **Anchor costs** with an honest reference.
8. **Peaks and ending:** feedback on every control, a designed confirmation with what happens next.

Then check the honesty rules, audit again and report the before/after score. Facts the screen needs but you don't have (real numbers, the user's items) become clearly marked placeholders.

## Output

- Keep replies short, one point per reply.
- Always output code changes complete and copy-ready in one piece.
- Provide created files or pages as clickable links.

## Related

- Visual quality: `ui-principles`, `ui-refinement`, `layout-refinement`.
- Wording of buttons, prices, decline labels and confirmations: `copy-rules`.

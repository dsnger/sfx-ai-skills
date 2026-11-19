---
name: copy-review-panel
description: Runs a panel of independent reviewers on copy (sales pages, landing pages, offers, presentations), namely target-group personas, a sales psychology expert, a strict client reviewer, a second AI or senior copywriter, behavior tests and a debate with a referee, then merges the findings. Use this skill whenever copy should be tested before hand-off, the user asks "how would customers react", wants feedback rounds, a second opinion or a score for a text, even if they don't say "panel".
---

# Copy Review Panel

One author grading their own text misses what readers notice. This panel lets several independent reviewers read the same text, each with a different role, then merges what they find. Findings named independently by several reviewers count most.

## Setup

- Generate a plain text version (Markdown) of the page or presentation. Reviewers read only that, change no file, and answer within a word limit.
- Gather the inputs reviewers need: the instruction checklist, the project's text rules, the `copy-rules` skill, and the client's original messages (for tone and standard).
- Run reviewers in parallel as subagents, mixing different models where possible. Continue personas and the client reviewer in follow-up rounds (same agent, new message) so they compare improvements.
- **Without subagents** (or when they can't write files): run the roles one after another yourself. Write each role's answer completely before reading the next role, and never let a role see the others' results. Flag this in the report ("roles run sequentially by one model, reduced independence"), because agreements then count less.
- Save every reviewer's full answer in a separate file (`review-voices.md` or one file per reviewer). The report itself only holds the merged result.

## Reviewers

### Personas (one small, one medium, one large business)

> You are {name}, {age}, owner of {business with concrete details: locations, offer, current website, attitude towards agencies}. You arrive at the page after {occasion}. Read {path} from top to bottom. Answer in first person, at most 300 words: Where do you think "yes, exactly", where "so what" or "no" (quote the heading)? Where do you drop out? Which objections remain? Which sentence convinces, which disturbs? Probability 1 to 10 that you book the conversation, and what's missing for a 9.

### Sales psychology expert

> Check {path} against concept {path}, checklist {path}, text rules {path}. Does the reader chain carry stage by stage? Three missing levers (wanting, believing, risk). At most eight changes with quote and rule-compliant replacement. Grade 1 to 6.

### Client reviewer (the strictest)

> You review the way the client would. They are demanding and have already rejected versions as insufficient. Read checklist {path}, text rules {path} and their original messages {path} (tone and standard). Check {path}. Grade from their view. Every spot that would annoy them, worst first: quote, reason, finished replacement (things never as subject, no assumptions, no triads or punchlines, max 15 words, never their own words, never patronizing). Watch especially for language logic, references, unproven claims, the common thread. Would they buy the service themselves?

### Second AI or senior copywriter without prior knowledge

> Check {path} against {rules}. Deliberate decisions (do not flag): {list}. Only real errors with quote and replacement, breaks in the common thread, grade.

## Optional formats

### Behavior test with customer personas

Give only the role (person, business, situation, device, occasion), nothing else: no questions, no hints, no grading grid. Show the page as a sequence of screens (desktop 1280 in 900 px steps, phone 390 in 780 px steps) plus a neutral list of moving parts. The only task: "Visit the page as … and tell me how it feels." Mix models. Count findings that several personas name independently.

### Debate with a referee

Three experts (different roles and models) review independently, given only their role. Round 2: each reads the others, objects or concedes, and closes with their own top six. A referee (another model, high effort) knows the client's binding requirements, decides every point of contention and separates "implement now" from "ask the client".

## Handling findings

- Adopt a hint when it supports the rules, the checklist or proven facts.
- Reject it, with a reason in the report, when it contradicts client requirements (e.g. order of sections, questions as headings).
- Never invent missing facts; collect them and present them to the client at the end.
- After changes, run a new round with the same reviewers until the client reviewer finds nothing that would annoy the client and no persona drops out at a solvable spot.

## Report format (keep it short)

```
# Panel: Ø 7.5 / 10 booking probability · Expert 2 · Client reviewer 2-

| Finding | Named by | Action |
|---|---|---|
| "…" sounds patronizing | Client reviewer, 2 personas | Rewritten |
...

Rejected: … (reason)
Open for the client: …
Single voices: review-voices.md
```

Keep the report to one screen: score line, at most about ten merged findings, rejected hints, open points. No quotes from individual voices beyond the finding itself.

## Output

- Keep replies short, one point per reply.
- Provide created files as clickable links.

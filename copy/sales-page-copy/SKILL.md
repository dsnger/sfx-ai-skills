---
name: sales-page-copy
description: Writes or reworks German sales pages, landing pages, offer pages and presentation texts end to end, from collecting the client's instructions to a reader chain concept, copy, review rounds and hand-off. Use this skill whenever the user asks for copy, headlines, structure, a "roter Faden", argumentation or objection handling for a sales or landing page or a pitch presentation, or criticizes such a page as weak, salesy or AI-like, even if they only ask to fix one section.
---

# Sales Page Copy

Guiding idea: **reader chain**. Every stage of the page answers exactly the question the reader brings from the previous stage and triggers a thought the reader thinks themselves. Text is written only once the reader chain stands. Patching single spots is never the answer to criticism of the whole.

Required companions:
- `copy-rules` for every sentence (stance, language, banned patterns, sentence checker).
- `copy-review-panel` for the review rounds in step 5.
- [references/page-types.md](references/page-types.md) for proven page structures and pricing logic, if available.

## Steps

1. **Collect instructions.** Pull every requirement, correction and approval from the conversation, project files (text rules, briefings, PRODUCT.md) and earlier versions into a numbered checklist in the project (`docs/checklist-instructions-<page>.md`), with dates. For each instruction note its scope: which place or purpose it was given for (for example, workshop feedback on explaining AI features to specialists is not a rule for the service promise). Mark contradictions and clarify them with a question.
   *Done when:* every requirement has an item and every contradiction is resolved or asked.

2. **Clarify facts and proof.** List which commitments (prices, deadlines, ownership, services, references, numbers) are proven or approved. Anything missing becomes `[NEED]` or a question to the client, never invented. Market and study numbers only with source and year. Benefit promises and positioning are not commitments; a concrete unproven claim stays and gets a proof question. Product knowledge is no correction order: change facts in the text only when the client asked for it, otherwise ask.
   *Done when:* every commitment points to a source, an approval or a marked placeholder.

3. **Build the reader chain.** The page type decides the chain (see [references/page-types.md](references/page-types.md)). Write the concept as a table: stage, question on arrival, what the stage must achieve, thought afterwards. The default chain below fits offer pages; other page types follow their own chain.
   *Done when:* the headings alone tell the argument and every stage connects to the previous one.

4. **Write.** Two or three variants per unit, keep the best. Never adopt the client's wording. Then run the `copy-rules` sentence checker and resolve every hit.
   *Done when:* the checker is clean and every rule in `copy-rules` has been checked once.

5. **Review rounds.** Run the `copy-review-panel` (personas, sales psychology expert, client reviewer, brand and campaign reviewer, second AI or senior copywriter). Adopt hints that support the rules or the checklist; reject with reasons hints that contradict client requirements. Then a new round.
   *Done when:* the client reviewer names no spot that would annoy the client and no persona drops out at a solvable spot. Never hand in the first version.

6. **Hand-off.** Generate the source of truth (`texts-final.md`) from the built page, with open commitments as a "to be confirmed" list at the end. Tell the client briefly: what changed, the reviewers' scores, what only they can provide.
   *Done when:* page, text file and checklist show the same state.

## Reader chain (default for offer pages)

| Stage | Question on arrival | Must achieve |
| --- | --- | --- |
| Header | Am I in the right place? | Short H1 naming the result, subline with the precondition and the biggest relief. No price. One button. No mockup without reason. |
| Three pain questions | Does this concern me? | One heading per pain that names it openly ("Ärgert es Sie …", "Gehen Ihnen … verloren"), text as a real question or proven fact, a self-test. Ordered by weight. |
| Buffer | (consolidate agreement) | One large sentence that sums up the three pains in the reader's goal and allows a real answer ("Wie viele Stunden und Kunden verlieren Sie …?"). No empty yes-question, no reading instruction. |
| Summary | Is there a solution? | "Für diese drei Situationen …", three points mirroring the pains, first conversation button. |
| Fork | Do I have to redo everything? | Clarify the smaller alternative offer before the main offer, in the language of the goal. |
| Implementation | Does this really work? | One block per pain: problem as question, then solution, one illustration. |
| Trust | Can they do it? Can I trust them? | Industry knowledge, real proof (reference with link, screenshot), proof at hand-off (checklist). |
| Contract | Am I taking a risk? | Costs, term, rights, named contact person. |
| Process | Do I have time for this? | Steps as they really run (analysis, draft with approval, review, introduction), the reader's share, second button. |
| Prices | Is it worth it? | Transition to the benefit, one clear number per package, invite comparison with today's costs. Include everything the reader would otherwise pay extra. |
| Objections | And what if …? | Five or seven questions titled "Häufig gestellte Fragen", each starting with yes/no or the clear answer; one honest answer on guarantees of success. |
| Close | What's the next step? | Conversation with a named contact person (no phone as channel), free, without obligation. |

For presentations, the same chain applies per slide group: one statement per slide, a recognizable transition between slides.

## Entry and buttons

- **Message match.** Readers arrive with a promise in their head (ad, email, link, search result). That promise comes back in the H1 in the same sense. If it is missing on arrival, readers leave before the chain starts. Ask the client where the traffic comes from if it's unclear.
- **Buttons say what the reader gets.** Action verb plus what they receive, plus a qualifier if needed ("Kostenloses Erstgespräch vereinbaren", "Beispielseite ansehen"). Never generic labels like "Absenden", "Mehr erfahren", "Hier klicken", "Jetzt starten". Every button on the page leads to the same next step unless the chain needs a smaller one.

*Button formula adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), message match from [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT).*

## Working with the client

- **Every instruction immediately becomes a checklist item**, then implement or ask specifically. Decide yourself what can be derived from the project, research or context. Do tasks like "take this as inspiration" right away.
- **Never silently change approved text.** Ask first; if that's impossible, report it first in the next update with before/after.
- **Make every change visible** once a version the client has seen is revised: a change list or an overlay with old, new and reason for each spot.
- **On any criticism, check the whole first:** Is the section in the right place of the reader chain? Is it redundant with another section? Only then change locally. Never several isolated fixes in a row without reading the whole page.
- **Suggestions on approved texts as a table** (spot, problem, suggestion); the client chooses ("alle" is enough).
- **Make your own recommendation.** Propose, justify, and ask only about real decisions. Show finished options instead of links to styles.
- **Files always as clickable links**; requested content directly in the chat.
- **Short reports:** what changed, what was checked, what only the client can decide.
- **At the end of a project**, review the conversation and evolve the skills (rules, error catalog, page types, design).

## If the page is also designed

Design serves the reader chain: structure and text first, then form. On criticism of a section, first check whether it sits in the right place and carries material, only then adjust visuals. Never two identically built sections in a row; a heading with one sentence is not a section. For the visual work use the design skills (`ui-principles`, `ui-refinement`, `layout-refinement`).

## Practice notes

- A real reference (screenshot of a successful page from a similar industry) beats any design skill.
- Settle text and structure first, then build section by section; create a design system file (colors, type, spacing) first or the style drifts.
- Generate several layout variants per section and pick one instead of writing longer prompts.
- AI falls back to default patterns (three equal cards, same order): check and break them deliberately.
- Headlines and CTA wording need human finishing; keep a facts file and forbid invented numbers.
- Screenshot loop at several widths (desktop and phone) after every change.

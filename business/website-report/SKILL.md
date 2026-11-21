---
name: website-report
description: Writes closing and quality reports for websites in plain language for non-technical readers, in the name of any sender (own brand, agency or white label), namely a project report after build or relaunch, a quality report after go-live and a follow-up report against an earlier baseline. Turns check results and measurements (from `launch-check` or provided data) into a short report with a summary first, numbers with sources and thresholds, honest notes on what the measurements can say, causes before recommendations, recommendations derived from the data, and open points kept separate. Use this skill whenever a website report, "Abschlussbericht", "Projektbericht", "Qualitätsbericht", performance or SEO report for a client is requested, even if the user only hands over numbers and asks to "make something for the client".
---

# Website Report

Clients and agencies read the first page, look at the numbers and forward the PDF. So the report says the state in a few sentences, every number is traceable, every judgement follows from the data, and the next steps are concrete. It is written for people who are not technical.

## Report types

| Type | When | Core content |
| --- | --- | --- |
| **Project report** | Build or relaunch finished | What was done (grouped by area), measured results at hand-off, open points, recommendations |
| **Quality report** | Some weeks after go-live, once search data exists | Technical scores, Core Web Vitals, search visibility, indexing, security, recommendations from the data |
| **Follow-up report** | Months later | The same measurements against the earlier report: what changed and why |

Pick the type from the request; if unclear, ask once.

## Input

- Use the findings and raw data from `launch-check` if available, or the data the user provides (exports, screenshots, notes).
- If measurements are missing, run `launch-check` first or name exactly what is missing. **Never fill in a value that wasn't measured.** Missing facts become `[NEED: …]`.
- Project measures come from the user's notes or the project, never invented.

## Rules

- **Written for non-technical readers.** Each section opens with one sentence saying what the result means for the client ("Ihre Website lädt auf dem Handy schnell genug für Google"), then the evidence. Explain a technical term in a few words the first time or leave it out.
- **As short as possible.** A reader gets the state from the summary and the first sentence of each section. Checks without anything worth mentioning become one line ("Alle Sicherheitsprüfungen bestanden"). Raw values, all runs and detail tables go into an appendix.
- **Summary first:** the three or four most important results with their numbers, then the main open topic.
- **Every number with source and date.** Scales and thresholds sit next to the values ("Werte ab 90 gelten als sehr gut"; "Google-Schwelle gut: höchstens 2,5 s").
- **Honest about measurement.** Name what the numbers can and can't say: lab vs real-user data, variance between runs (report the range and which run is shown and why), short periods, early relaunch effects.
- **Judgements follow from data.** No unprovable comparisons ("faster than most", "top values"), no superlatives, also not when the client asks for them; offer a provable alternative instead.
- **Compare with the site's own best values** instead of outside comparisons (a weak page against the best page of the same site); that is provable and shows the potential.
- **Cause before recommendation.** Explain where a problem comes from, then what follows from it, including which future changes would make it worse. If a remaining gap to the top score isn't worth chasing, say why (effort against benefit).
- **Baseline:** state that the values serve as the baseline for the next report and when a repeat measurement becomes meaningful.
- **Recommendations from the data:** each points to the finding behind it (a page with many impressions and few clicks, a topic just below page one). Content, technical next steps and ongoing operation are separate groups.
- **Open points separate** from what is done, with who handles them if known.
- **Sender and recipient** as given; in white label work only the sender's name appears.
- **Wording follows `copy-rules`** (German texts: people act, short sentences, no hype, no patronizing, no em or en dashes) and, for recommendations, the reader logic of `sales-page-copy` if available.
- Tables for anything compared, charts for trends over time.

## Structure (leave out what doesn't apply)

1. Cover data: site, client, report date, measurement time and period, data sources, author and sender.
2. Summary.
3. Project report: what was done, grouped by area.
4. Speed and technical quality: scores and Core Web Vitals with thresholds, what the measurement can say, the cause of the main delay if there is one.
5. Real-user data.
6. Visibility in search: totals, trend, queries, pages, devices.
7. Indexing, security and configuration: short, problems first.
8. Recommendations from the data, then for ongoing operation, then open points.
9. Contact.
10. Appendix: raw values, all runs, detail tables, tool versions.

Follow-up report: add a column "previous report" to the compared tables and one sentence per change explaining it.

## Output

- Deliver as an editable document (a doc where the session offers one, otherwise Markdown), exportable as PDF; a branded PDF only if the user asks.
- Keep the chat reply short: what the report says, what is still missing, one point per reply.
- Provide created files as clickable links.

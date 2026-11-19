---
name: copy-rules
description: Rules for writing and editing German marketing and business copy (websites, landing pages, offers, presentations, emails) so it sounds human, respectful and valuable instead of salesy or AI-generated. Covers stance, sentence rules, banned AI patterns, value-driven wording and a sentence checker script. Use this skill whenever German copy is written, rewritten or reviewed, or when the user criticizes text as "KI-Slop", "bevormundend", "werblich", "platt" or "steif", even if they don't mention rules.
---

# Copy Rules

Rules for German copy that respects the reader, says something real and sounds like a person wrote it. They apply to every text type: website, landing page, offer, presentation, speaker notes, email.

Project-specific text rules (e.g. a `textregeln.md` in the project) take precedence. These rules always apply in addition.

## How to use

1. Before writing: read the project's own text rules and briefing, if any.
2. Write the text following the rules below. For each unit (heading, paragraph, button) draft two or three variants and keep the best.
3. If `scripts/check_sentences.py` is available (it ships with this skill in the sfx-ai-skills repo), run `python3 scripts/check_sentences.py <file>` (HTML or Markdown). Add project nouns that must never act, e.g. `--things "Dashboard|Portal"`. Resolve every hit or consciously keep it. Without the script, check sentence length, things as subject, "nicht … sondern", dashes and short punchlines by hand.
4. Check every rule below once more by hand. The script only catches mechanical patterns.

## Stance

| Rule | Why | Check question |
| --- | --- | --- |
| **Reader's perspective.** Every section names a problem from the reader's view first, then the solution | Readers decide in a second whether a section concerns them | Can the reader tell if this applies to them? |
| **Never patronize.** Never say what the reader needs or must do; let them draw the conclusion | Being told what you need creates resistance | Does a sentence contain "braucht", "muss", "sollte" aimed at the reader? |
| **No assumptions about their history.** Don't claim who built their website, what they do in the evening, which agency they had; ask real questions instead | Wrong assumptions break trust instantly | Could this be untrue for some readers? |
| **Name the reader's real goal.** More customers, more bookings, less work. Not a means like "found on Google" | Means are not motivating, results are | Is this the goal or only a tool? |
| **No constructed scenes.** No invented evenings, people or story examples. Invented names only in clearly labeled example graphics | Staged scenes feel fake | Did this actually happen? |
| **Honest about limits.** No ranking guarantees, nothing that can't be in a contract | Overpromising costs credibility later | Could this be written into a contract? |
| **No jabs at your own industry** ("typical agency trouble") if the sender is part of it. Pick up worries as a question | Jabs backfire on the sender | Would a colleague feel attacked? |

## Sentences and language

- **Sie form**, reading level grade 5 to 7, sentences of at most 15 words.
- **Only people act.** Things, systems, pages, prices and rules are never the subject, not even with "ist", "steht", "liegt", "gilt", "bestimmt", "kostet". At most "dient dazu", "vereinfacht". Check question: Who is doing something here?
  - Wrong: "Die Website zeigt die Termine." Right: "Ihre Kunden sehen die Termine auf jeder Seite."
  - Wrong: "Stehen Ihre Termine in PDFs?" Right: "Verwalten Sie Ihre Termine in Tabellen oder auf Papier?"
- **Transitive verbs need an object.** Not "Sie ändern sofort selbst", but "Änderungen erledigen Sie sofort selbst".
- **Language logic.** Does the question fit the answer? Does every "darum", "dafür", "dort", "diese" have a clear reference? No "darum" after a question.
- **Time logic.** No skewed time statements ("um Technik kümmern wir uns nach dem Start").
- **No tool or jargon names.** No Lighthouse, W3C, SEO, sitemap, structured data. Say what is done and what the reader gains ("Wir messen, wie schnell Ihre Website lädt").
- **Don't describe what is visible.** No sentence repeats what layout, cards, steps or images already show ("Wir bieten drei Pakete an" above three price cards). Every sentence adds information or a reason.
- **Three, five or seven.** Per semantic unit (list, card, accordion, argument block) never more than seven points, and only three, five or seven. Combine and shorten instead.
- **Positive and lively.** Moderate adjectives on the service ("persönliche Einführung", "einfach", "jederzeit"), not exaggerated, not silly, no assumed feelings. Not "kurzer Termin" or "Videotermin" but "persönliche Einführung im Video-Call". Never offer what can't be delivered.
- **Don't promise the obvious.** What every customer expects anyway (own page title, site goes live only when finished, bugs get fixed) is never a feature, guarantee or checkpoint. It raises the suspicion it might be different otherwise. Check question: Would a customer assume the opposite? If not, delete.
- **Improving never means lengthening.** A correction makes a sentence clearer or stronger, not longer. If a block now outgrows its counterpart (image, demo), the correction was wrong.
- **Contrast with stakes.** In "advantage / instead of" lines both sides need attractive, concrete words: "in Ihren eigenen Worten" vs. "verschachtelte Menüs und komplizierte Einstellungen". Sell simplicity, not brevity.
- **Neutral standard terms instead of groups of people.** "Häufig gestellte Fragen", not "Was Inhaber uns fragen".
- **Describe processes as they really run.** No "Sie wählen das Design" if there is one targeted draft. Step headings must never mislead.
- **Price headings with value, never as a cost question.** "Ihre Rundum-sorglos-Website zum festen Preis", not "Was zahlen Sie heute …?". Comparison questions at most small, below the prices.
- **Anticipation sentences must hold for every reader.** Not too specific, not abstract. Each names an experience of the owner or their customers: find quickly, feel welcome, appear likeable and competent, want to book, book effortlessly.
- **Never adopt the client's wording.** Their examples set the direction, not the words.
- **Numbers only with source and year**, linked in the text. Mark US data as such. Missing facts become `[NEED]` or a question to the client, never invented.

## Banned patterns (typical AI tells)

- Triads as a stylistic device (lists of real components are fine)
- Slogans and advertising phrases ("Gefunden, gewählt, gebucht", "Einfach geht's")
- Wordplay, parallelisms, chiasmus ("Zwei Ziele, eine Grundlage", "Was der KI hilft, hilft auch …")
- "nicht X, sondern Y"
- Staccato punchlines ("Bei uns nicht.", "Die KI liefert den Entwurf. Sie entscheiden.")
- Half sentences like "… oder eben nicht"
- Dashes (em or en) as a stylistic device
- Metaphors from the reader's own industry, including hidden ones
- Unexplained jargon
- Kickers or eyebrows above headings
- Empty yes-questions and salesy tone ("genickt?")
- Invented numbers, testimonials or promises

## Value-driven wording

Plain activity words get lifted the same way every time:

- **Outcome with a quality marker instead of an activity.** Not "Aufbau und Betrieb" but what the customer gets and how good it is: "durchdachtes Konzept", "technisch moderne Umsetzung", "zuverlässige Erreichbarkeit". Check question: How does the customer notice the service is good?
- **Modern terms instead of legacy ones.** "Pflege", "Wartung", "Technik-Service" sound dated. Name the service as all-round care and list its parts concretely.
- **Emphasize completeness.** One price covers everything; list parts the customer would otherwise expect to pay extra for.
- **Positive direction only.** "verlängern", never "kündigen". Never offer exit, take-away or fine print. Where a downside matters, name its consequences for the customer.
- **Terms from the customer's view.** Name what they pay for the way they understand it.
- **Headings in customer language.** Quality words belong in the service description, never on what the customer wants. Nobody orders "eine durchdachte Website"; they want bookings, no work, no worries.

Limit: quality words must be provable (no "perfekt", "beste").

## Error catalog

Check before every hand-off. Patterns, not project names.

| Error | Example | Right |
| --- | --- | --- |
| Thing as subject | "Die Website bucht über das Buchungssystem" | "Ihre Kunden buchen …" |
| Patronizing | "Was Ihr Betrieb braucht …" | Ask the problem, offer the solution |
| Question without pain | "Pflegen Sie Ihre Website nach Feierabend?" | Name the pain openly |
| Client wording adopted | Their example sentence as heading | Own wording in their direction |
| Invented backstory | "Ihre Website hat oft eine Agentur gebaut …" | Question or proven fact |
| Wrong reader goal | "Geht es Ihnen nur um Google?" | More customers and bookings |
| Constructed scene | A prospect books in the evening while the owner is off | Summary without a scene |
| Language logic | "Erkennen Sie Ihren Betrieb wieder?" | "Kennen Sie diese Situationen …?" |
| Promised non-existent service | "Ihren Google-Eintrag pflegen wir mit" | Only promise real services |
| Stiff or negative | "auf Anfragen optimiert" | Name the result positively |
| Activity instead of value | "Sie zahlen Aufbau und Betrieb" | Value with quality markers |
| Negative direction | "Danach kündigen Sie monatlich" | "Monat für Monat weiter" |
| Fine print | Grey footnote below prices | Clear, friendly paragraph |
| Describes what is visible | "Wir bieten drei Pakete an" above three cards | Delete or add what the image doesn't show |
| Quality word on the wish | "Sie zahlen eine durchdachte Website" | "Sie zahlen alles, was Ihre Website braucht" |
| Tool names | "mit Lighthouse und W3C-Validator" | "Wir messen, wie schnell Ihre Website lädt" |
| Assumed feeling | "Sie arbeiten gern an Ihrer Website" | Benefit as action: "Updates erledigen wir für Sie" |
| Technical details without benefit | "Admin-Zugänge geschützt" | Only the result: "Sicherheit geprüft" |
| Obvious promised | "Jede Seite bekommt einen eigenen Titel" | Delete |
| Misleading step heading | "Sie wählen das Design" (only one draft) | "Sie erhalten einen Entwurf" |
| Cost question as heading | "Was zahlen Sie heute …?" | Value heading, comparison small below |
| Verb without object | "Sie ändern sofort selbst" | "Änderungen erledigen Sie sofort selbst" |
| Phone as channel | "Oder rufen Sie … an" | Contact person without channel |

## Output

- Keep replies short, one point per reply.
- Always output corrected texts complete and copy-ready, never only the changed sentence.
- Provide created files as clickable links.

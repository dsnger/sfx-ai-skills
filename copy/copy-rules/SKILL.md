---
name: copy-rules
description: Rules for writing and editing German marketing and business copy (websites, landing pages, offers, presentations, emails) so it sounds human, respectful and valuable instead of salesy or AI-generated. Covers stance, sentence rules, banned AI patterns, value-driven wording and a sentence checker script. Use this skill whenever German copy is written, rewritten or reviewed, or when the user criticizes text as "KI-Slop", "bevormundend", "werblich", "platt" or "steif", even if they don't mention rules.
---

# Copy Rules

Rules for German copy that respects the reader, says something real and sounds like a person wrote it. They apply to every text type: website, landing page, offer, presentation, speaker notes, email.

Project-specific text rules (e.g. a `textregeln.md` in the project) take precedence. These rules always apply in addition.

## Text type first

Decide before anything else which kind of text this is, because the truth rules apply differently:

- **Persuasive texts** (landing pages, sales and product pages, offers, campaigns, pitch decks): their job is to make the reader want something. Effect beats rule compliance: when a rule and the selling wording conflict, the selling wording wins. Benefit promises and positioning ("Prozesse, die von selbst laufen", "in Sekunden erledigt") stay. Only commitments of a contractual kind (prices, deadlines, guarantees, scope of service, ownership) must be backed. A concrete claim nobody has proven yet stays in the text and gets a proof question to the client. Effect only counts for wording a native speaker would actually say: a selling form (triad, rhythm, alliteration) is never on its own a reason to keep a line. Check every verb against its subject and object the way people use them in daily speech (a business is not "gebucht", its services are). If one word fails, the line gets rewritten in the same spirit. Images should come from the reader's real situation (searching online is not walking past a shop window).
- **Factual texts** (journalism, reports, scientific or technical texts, quotes, documentation): every statement must be true and provable; numbers with source and year; nothing is promised or embellished.

When unsure, ask which kind it is. Everything below applies to both kinds unless it says otherwise.

## How to use

1. Before writing: read the project's own text rules and briefing, if any, and decide the text type.
2. Write the text following the rules below. For each unit (heading, paragraph, button) draft two or three variants and keep the best. When writing new copy or reworking a draft, also read `references/lift-techniques.md` for ways to lift plain lines.
3. If `scripts/check_sentences.py` is available (it ships with this skill in the sfx-ai-skills repo), run `python3 scripts/check_sentences.py <file>` (HTML or Markdown). Add project nouns that must never act, e.g. `--things "Dashboard|Portal"`. Resolve every hit or consciously keep it. Without the script, check sentence length, things as subject, "nicht … sondern", dashes and short punchlines by hand.
4. Check every rule below once more by hand. The script only catches mechanical patterns.

## Before and while writing

- **Diagnose first, in one line with evidence.** Which situation is this? Then change only as much as the situation allows.
  - *Blank or generic:* a one-line ask or interchangeable company speak. Build the argument from briefing and facts; freedom in the angle, never in the facts.
  - *Real voice present:* the draft has an angle or a recognizable voice, even if rough. Anything the client has already seen or approved counts as their voice automatically. Keep the argument, the emphasis and the client's vocabulary; fix only buried statements, vague lines, rule violations and structure. Don't add sections nobody asked for. The result is a change list (old → new → reason), not a new text.
  - *Point edit:* "fix this heading". Change only that, plus the minimum around it, and return the rest untouched.
- **Three questions per line.** Can the reader picture it? Is it concrete enough to be true or false (not vague)? Could a competitor write the exact same sentence, or does it add nothing others don't already say? Three passes: keep it. Two: sharpen the weak spot. One or none: rewrite from the facts or mark `[NEED: …]`. In persuasive texts a concrete but unproven claim passes the second question; it gets a proof question, not a rewrite.
- **Check whether more cases belong in.** When a line says what the reader gets, check whether it gets better by naming the other main situations the offer solves, not only the first that comes to mind (e.g. readers who are not found and readers who are found but not convinced). When there are many, look for a middle way instead of all or one: the two or three that matter most to the reader, or a wording that covers them together. Judge by what makes the line stronger.
- **Ration the strong moments.** Most lines are plain, concrete and calm. A page gets one or two memorable moments, usually the main heading and one section. When every line tries to stand out, none does, and the text reads as AI.
- **Leave-it-alone test.** Before handing over, check every change: clearly better or just different? In persuasive texts also: does the new wording sound more fascinating, more positive, like less work for the reader? If not, the old wording stays. Wording that stays must still be correct, idiomatic language; a line kept "because it sells" names the words that sell and confirms each of them fits its subject. Undo changes without a reason, especially when a real voice was present.
- **Never weaken an unproven claim silently.** The claim stays as it is and gets a question to the client in a list at the end ("Beleg für ‚in Sekunden'?"). In factual texts, an unproven statement is marked and asked about the same way, never kept as fact. Never invent facts, numbers or testimonials.

*Diagnosis, the three questions, ration and leave-it-alone test adapted from the `copywriting` skill in [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), which credits Profound's skills-marketing-library (MIT); the "adds nothing others say" question from [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT).*

## Stance

| Rule | Why | Check question |
| --- | --- | --- |
| **Reader's perspective.** Every section names a problem from the reader's view first, then the solution | Readers decide in a second whether a section concerns them | Can the reader tell if this applies to them? |
| **Never patronize.** Never say what the reader needs or must do; let them draw the conclusion | Being told what you need creates resistance | Does a sentence contain "braucht", "muss", "sollte" aimed at the reader? |
| **No assumptions about their history.** Don't claim who built their website, what they do in the evening, which agency they had; ask real questions instead | Wrong assumptions break trust instantly | Could this be untrue for some readers? |
| **Name the reader's real goal.** More customers, more bookings, less work. Not a means like "found on Google" | Means are not motivating, results are | Is this the goal or only a tool? |
| **No constructed scenes.** No invented evenings, people or story examples. Invented names only in clearly labeled example graphics | Staged scenes feel fake | Did this actually happen? |
| **Honest about commitments.** Prices, deadlines, guarantees and scope of service must hold; no ranking guarantees. This does not apply to benefit promises and positioning | Broken commitments cost credibility later | Is this a commitment the reader could hold us to, like a price, a deadline or a guarantee? |
| **Inform before offering.** Readers recognize their gap themselves before an offer comes; pains are named openly, never dramatized | Fear and pressure create resistance | Does the reader see the problem before the solution, without being scared? |
| **Competition only with evidence.** Argue with competitive pressure only if the market situation is proven; otherwise creating demand is often the stronger argument | Assumed pressure sounds like a sales trick | Is there proof that competitors really do this? |
| **No jabs at your own industry** ("typical agency trouble") if the sender is part of it. Pick up worries as a question | Jabs backfire on the sender | Would a colleague feel attacked? |

## Sentences and language

- **Sie form**, reading level grade 5 to 7, sentences of at most 15 words.
- **Only people act.** Things, systems, pages, prices and rules are never the subject, not even with "ist", "steht", "liegt", "gilt", "bestimmt", "kostet". At most "dient dazu", "vereinfacht". Check question: Who is doing something here? Exception: in promises about automation and AI, the thing acting is exactly the message ("Die KI kennt jeden Vertrag"), so it may be the subject.
  - Wrong: "Die Website zeigt die Termine." Right: "Ihre Kunden sehen die Termine auf jeder Seite."
  - Wrong: "Stehen Ihre Termine in PDFs?" Right: "Verwalten Sie Ihre Termine in Tabellen oder auf Papier?"
- **Transitive verbs need an object.** Not "Sie ändern sofort selbst", but "Änderungen erledigen Sie sofort selbst".
- **Language logic.** Does the question fit the answer? Does every "darum", "dafür", "dort", "diese" have a clear reference? No "darum" after a question.
- **Time logic.** No skewed time statements ("um Technik kümmern wir uns nach dem Start").
- **No tool or jargon names.** No Lighthouse, W3C, SEO, sitemap, structured data. Say what is done and what the reader gains ("Wir messen, wie schnell Ihre Website lädt").
- **Don't describe what is visible.** No sentence repeats what layout, cards, steps or images already show ("Wir bieten drei Pakete an" above three price cards). Every sentence adds information or a reason.
- **Three, five or seven.** For arguments, benefits and choices: per semantic unit (list, card, accordion, argument block) prefer three, five or seven points, and pick the strongest rather than all (see "Check whether more cases belong in"). Lists whose value lies in completeness (services, what is included, scope) may run longer; there, cut only what is padding.
- **Positive and lively.** Moderate adjectives on the service ("persönliche Einführung", "einfach", "jederzeit"), not silly, no assumed feelings. In persuasive texts intensifying words ("maximale Entlastung", "optimal", "wertvolle Impulse") are fine in moderation: a few strong spots, not on every line. Not "kurzer Termin" or "Videotermin" but "persönliche Einführung im Video-Call". Never offer what can't be delivered.
- **Don't promise the obvious.** What every customer expects anyway (own page title, site goes live only when finished, bugs get fixed) is never a feature, guarantee or checkpoint. It raises the suspicion it might be different otherwise. Check question: Would a customer assume the opposite? If not, delete.
- **Improving never means lengthening.** A correction makes a sentence clearer or stronger, not longer. If a block now outgrows its counterpart (image, demo), the correction was wrong.
- **Contrast with stakes.** In "advantage / instead of" lines both sides need attractive, concrete words: "in Ihren eigenen Worten" vs. "verschachtelte Menüs und komplizierte Einstellungen". Sell simplicity, not brevity.
- **Headings are concrete statements or real questions**, never buzzwords ("Sicherheit", "Mehrwert").
- **Neutral standard terms instead of groups of people.** "Häufig gestellte Fragen", not "Was Inhaber uns fragen".
- **Describe processes as they really run.** No "Sie wählen das Design" if there is one targeted draft. Step headings must never mislead.
- **Price headings with value, never as a cost question.** "Ihre Rundum-sorglos-Website zum festen Preis", not "Was zahlen Sie heute …?". Comparison questions at most small, below the prices.
- **Anticipation sentences must hold for every reader.** Not too specific, not abstract. Each names an experience of the owner or their customers: find quickly, feel welcome, appear likeable and competent, want to book, book effortlessly.
- **Never adopt the client's wording.** Their examples set the direction, not the words.
- **Numbers only with source and year**, linked in the text. Mark US data as such. Missing facts become `[NEED]` or a question to the client, never invented.

## Banned patterns (typical AI tells)

- Triads whose words don't fit (see "Text type first"). A triad of precise words can beat a flat heading ("Persönlich. Proaktiv. Praxisnah."); use one or two per page at most
- Slogans and advertising phrases ("Gefunden, gewählt, gebucht", "Einfach geht's")
- Wordplay, parallelisms, chiasmus ("Zwei Ziele, eine Grundlage", "Was der KI hilft, hilft auch …")
- "nicht X, sondern Y"
- Staccato punchlines as a constant pattern ("Bei uns nicht.", "Die KI liefert den Entwurf. Sie entscheiden."). One or two well-chosen ones per page can work; pairs usually work better than three
- Half sentences like "… oder eben nicht"
- Dashes (em or en) as the default connector. At most one per page, where it carries a real pause, e.g. after a list of examples ("A, B, C – das alles …"); everywhere else use a full stop, comma or colon
- Metaphors from the reader's own industry used carelessly, including hidden ones: a wrong term embarrasses the writer, and borrowed insider talk reads as pretending to belong. A deliberate, sparing comparison that places the offer in terms the reader knows well can be very strong, if every term is used correctly
- Unexplained jargon
- Kickers or eyebrows above headings
- Empty yes-questions and salesy tone ("genickt?")
- Invented numbers or testimonials, and promises of services that do not exist
- Summary transitions that recap the previous section before the next point ("Nachdem wir … gesehen haben", "Damit ist klar …")
- Data sheet tone: "bietet", "ermöglicht", "verfügt über", "ist konfigurierbar" instead of what a person does or gets
- Vague quantities and hedges ("oft", "viele", "deutlich", "in der Regel") where a concrete figure or claim is possible; without a provable figure, say what happens instead
- One connected thought chopped into a chain of staccato fragments ("Früher manuell. Jetzt automatisch. Das spart Zeit."). Keep at most a pair and continue in a full sentence: "Früher manuell, jetzt automatisch. Das spart Ihnen viel Zeit, die Sie für andere Dinge nutzen können."

*The last four adapted from [vercel-labs/writing-guidelines](https://github.com/vercel-labs/writing-guidelines) (MIT).*

## Value-driven wording

Plain activity words get lifted the same way every time:

- **Outcome with a quality marker instead of an activity.** Not "Aufbau und Betrieb" but what the customer gets and how good it is: "durchdachtes Konzept", "technisch moderne Umsetzung", "zuverlässige Erreichbarkeit". Check question: How does the customer notice the service is good?
- **Modern terms instead of legacy ones.** "Pflege", "Wartung", "Technik-Service" sound dated. Name the service as all-round care and list its parts concretely.
- **Emphasize completeness.** One price covers everything; list parts the customer would otherwise expect to pay extra for.
- **Positive direction only.** "verlängern", never "kündigen". Never offer exit, take-away or fine print. Where a downside matters, name its consequences for the customer.
- **Terms from the customer's view.** Name what they pay for the way they understand it.
- **Headings in customer language.** Quality words belong in the service description, never on what the customer wants. Nobody orders "eine durchdachte Website"; they want bookings, no work, no worries.

Limit: no unprovable comparisons with others ("perfekt", "die beste", "Nr. 1").

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
| Assumed organization | "Ihr Team spart Zeit" (maybe one person does it all) | "Sie" or a neutral wording |
| Kept for its form | "Wird Ihr Betrieb gefunden, gewählt und gebucht?" kept as a selling triad, though nobody "wählt" or "bucht" a business | Check each word: "Ihre Kunden suchen online. Landen sie bei Ihnen?" |
| Image from the wrong world | "wo Kunden an Ihrem Betrieb vorbeigehen" for online search | An image from the real situation: "ob Kunden Sie bei ihrer Suche finden" |
| Only half the offer | "warum Kunden Sie nicht finden" when the offer also fixes unconvincing pages | If it stays short: "ob Kunden Sie finden, was sie danach noch abhält und wie Sie das ändern" |
| Claim weakened without request | "in Sekunden erledigt" turned into "schnell erledigt" | Keep the claim, ask the client for proof |

## Output

- Keep replies short, one point per reply.
- When a text the client has already seen is revised, show every change visibly (old → new → reason, as a list or an overlay on the page), so wrong changes are caught at a glance.
- Always output corrected texts complete and copy-ready, never only the changed sentence.
- Provide created files as clickable links.

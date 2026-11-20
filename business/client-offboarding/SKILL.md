---
name: client-offboarding
description: Creates client offboarding documents for web projects in the name of any sender (own brand, agency or white label), namely a project handover when a website or app is finished, and an end-of-service document when a client leaves a provider. Covers what is handed over, who owns which licenses, accounts and renewals, the provider's own components and how they stay updated, access transfer and removal, backups and a friendly close. Use this skill whenever a project is wrapped up, a site is handed to a client, a client switches provider, or the user asks for handover, offboarding, "Übergabedokument", "Projektabschluss" or "Ende der Betreuung", even if they only ask what to send the client.
---

# Client Offboarding

Most providers have a clean start to a project and a messy end. Who owns the licenses, who renews the domain, whose access stays, what happens to backups: unclear endings cost money, licenses and goodwill. These documents end a project as clearly as it started, in plain language the client understands.

## Two document types

| Type | When | Goal |
| --- | --- | --- |
| **Project handover** | A project is finished and goes to the client | The client knows what they received, what they own and what needs renewing |
| **End of service** | A client leaves the provider or switches to another one | Control is transferred safely, the provider's own licenses and access are withdrawn, nothing breaks by surprise, and the relationship stays good |

## Before writing: collect

Everything below is optional. Include only what applies to the project; leave out items that don't exist instead of writing "n/a".

1. **Sender.** In whose name is the document sent (company, contact person, signature, tone)? Use only that name. In white label work, never mention who actually built or maintains the site behind the sender.
2. **Recipient.** Company and contact person.
3. **The inventory:** domain, hosting, DNS, email, website software and theme, plugins and extensions, the provider's own components, third-party services (analytics, forms, payments, maps, fonts, newsletter), backups, design and source files, documentation.
4. **For each item:** who is the account or license holder, whether it can be transferred, renewal date and cost, who pays today.
5. **Dates:** handover date, last day of service, when licenses and access end.
6. **Follow-up service**, only if the user wants it in the document: what it covers and its price.

Anything missing becomes a marked placeholder (`[NEED: …]`) or a question to the user. Never invent license states, dates, prices or account owners.

## Rules for every document

- **Plain language.** Written for someone who is not technical. Explain each technical term in a few words the first time it appears ("DNS, die Einstellung, die Ihre Domain mit dem Server verbindet"), or leave it out.
- **One table of what is handed over** with owner, status and the client's to-do per row. Readers scan, they don't read.
- **Licenses honestly.** Say per license whether it belongs to the client or to the provider. Licenses held by the provider (agency or developer licenses) usually can't be transferred: state what happens when they end and what the client would need instead. Never imply the client owns what they don't.
- **The provider's own components.** Themes, plugins or modules the provider develops and maintains themselves are named as such: who may use them, and how they stay updated (for example through a connected update source such as a code repository). Where no rule exists yet for the time after handover (whether updates continue, what happens if the connection ends), mark it as an open point for the user to decide. Never invent a rule.
- **No passwords or secrets in the document.** Access data goes through a secure channel (password manager share, separate encrypted message). The document only says which accesses exist and how they are handed over.
- **Security after transfer.** Recommend changing passwords and checking user accounts and two-factor settings once control has passed, and say which provider accounts will be removed and when.
- **Every recurring cost has an owner and a date.** Domain, hosting, licenses, services: who pays, when it renews, what happens if nobody does.
- **Follow-up service only when asked.** Maintenance or care offers are usually settled separately. Include them only if the user asks, then as an honest, equal choice without sales pressure.
- **A clear close.** Contact person, until when questions are answered, and one friendly sentence. Thanks without exaggeration.
- **Legal points as notes, not advice.** Data processing agreements, deletion of personal data, rights of use: name what applies and that it should be checked; don't phrase legal conclusions.
- Language and copy follow the sender's tone; German texts follow `copy-rules` if available.

## Project handover: structure

Leave out sections that don't apply.

1. Short opening: what was delivered, and the date.
2. What you receive (table: item, where it lives, owner, your to-do).
3. Licenses, own components and renewals (table: item, holder, renews on or update source, cost, what happens if it ends).
4. Access: which accesses exist, how they are handed over, what the client should do first.
5. Backups and files: where the latest backup is, what the client gets, how long the provider keeps copies.
6. Only if asked: follow-up service.
7. Next steps with dates, contact, close.

## End of service: structure

Leave out sections that don't apply.

1. Short opening: what ends and on which date, written calmly.
2. What stops when (hosting, updates, backups, monitoring, licenses, updates of own components).
3. Transfer checklist (table: item, from, to, by date, who does it).
4. Licenses, own components and access the provider withdraws, with dates and consequences, and what the client or new provider needs to replace.
5. Final backup and data: what is handed over, and when remaining copies and personal data are deleted.
6. Open items: last invoice, notice periods, anything still running.
7. Close: contact until the last day, one line that the door stays open, thanks.

## Output

- Deliver as a document the user can edit and send (a doc where the session offers one, otherwise Markdown), in the sender's name.
- Keep the chat reply short: what was created, which placeholders need facts, one point per reply.
- Provide created files as clickable links.

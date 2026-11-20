---
name: launch-check
description: Runs the technical and quality checks for a website before go-live, on launch day and some weeks after, and records the results as a findings list with status, evidence, severity and fix, plus raw data for later reports. Covers search engine visibility, performance with repeated runs, Core Web Vitals in lab and field, Search Console, indexing, security and configuration, consent and tracking, legal pages, forms, redirects and links, interface quality against the Web Interface Guidelines, and operations (backups, monitoring, updates). Use this skill whenever a site is about to launch, has just launched, a relaunch needs checking, someone asks "what should I check before or after go-live", or a report needs measurements, even if they only ask whether the site is "ready".
---

# Launch Check

Most launch problems are small and embarrassing: the search engine block from staging is still on, the contact form sends nowhere, the old URLs return 404. This skill checks a site systematically and records what it finds, so problems get fixed before anyone notices and the numbers can later go into a report (`website-report`).

## Phases

| Phase | When | Focus |
| --- | --- | --- |
| **Before go-live** | On staging, before the switch | Blockers: everything that must not go live |
| **Launch day** | Right after the switch | The live site behaves like staging, plus everything that only works live |
| **After launch** | Some weeks later, once search data exists | Measurements, field data, visibility, indexing |

Pick the phase from the request; run every check that applies to it and say which ones you skipped and why.

## How to check

- Use the tools available in the session (browser, command line, APIs, connectors). If a check can't be run here, mark it **not checked** and say what the user needs to provide (export, screenshot, access). **Never mark something as passed that wasn't checked, and never fill in a value that wasn't measured.**
- For every measurement record tool and version, date and time, device or emulation and URL. Keep raw results (exports, JSON, screenshots) in a folder next to the findings.
- Check as a visitor would: a fresh browser session without login, on desktop and phone.

## Checks

### Before go-live and launch day

| Area | Check |
| --- | --- |
| **Search engines** | Staging block removed on the live site (CMS setting, `noindex`, `robots.txt`), staging itself stays blocked; sitemap reachable; canonical tags point to the live domain |
| **Domain and HTTPS** | Valid certificate, HTTP and the non-canonical host (with or without www) redirect permanently to one address, no mixed content (HTTP resources on HTTPS pages) |
| **Content** | No sample content or placeholder text, no test pages, titles and descriptions set, favicon and preview image (Open Graph) present, custom 404 page |
| **Redirects and links** (relaunch) | Old URLs redirect permanently to the matching new ones, no broken internal links |
| **Forms** | Every form sends, arrives at the right address, shows a confirmation, has spam protection |
| **Legal and consent** | Imprint and privacy pages present and linked everywhere; consent banner with equal accept and reject; tracking and third-party content load only after consent |
| **Configuration** | Debug mode and error display off, versions not exposed, no exposed sensitive files or directory listings, user enumeration blocked, unused interfaces (e.g. XML-RPC) off, admin accounts personal and with strong passwords, security headers set |
| **Interface quality** | Findings against the Web Interface Guidelines: accessibility (labels, alt texts, keyboard use, contrast), focus states, forms, animation, typography, content handling, images. Use the `web-design-guidelines` skill if installed, otherwise its rule list ([vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines)) |
| **Operations** | Backups run and a restore is possible, uptime monitoring active, updates planned, caching on |
| **Analytics and Search Console** | Property verified, sitemap submitted, analytics receives data after consent |

### After launch

| Area | Check |
| --- | --- |
| **Performance (lab)** | PageSpeed or Lighthouse, mobile and desktop, four category scores, FCP, LCP, TBT, CLS, Speed Index, with Google's thresholds. **Run several times**: scores vary with cache and server load. Record every run, the range, and which run represents real visitors and why |
| **Cause of the main delay** | LCP breakdown (server response, load delay, load time, render delay) and the largest avoidable resources |
| **Core Web Vitals (field)** | Search Console field data per device (good, needs improvement, poor); field data lags about four weeks |
| **Search visibility** | Exact period, clicks, impressions, CTR, position, top queries and pages, devices, countries, daily trend; note relaunch effects in early data |
| **Indexing** | Indexed pages, sitemap status and last read, structured data, manual actions or security issues |
| **Repeat** the security and configuration checks with an external checker and name it |

## Findings list

One row per finding, sorted by severity:

| Status | Severity | Area | Finding | Evidence | Fix | Who |
| --- | --- | --- | --- | --- | --- | --- |
| failed | blocker | Search engines | Live site sends `noindex` | Header of / on 20.11. 10:12 | Turn off the search engine block in the CMS | [NEED] |

- **Status:** passed, failed, warning, not checked.
- **Severity:** blocker (must be fixed before or right after go-live), important (fix soon), minor.
- Passed checks are listed briefly at the end in one block, not as rows.
- End with one line: ready to go live yes or no, and the blockers left.

## Output

- Save the findings list as an editable document or Markdown next to the raw data.
- Keep the chat reply short: ready or not, the blockers, what was not checked.
- For a client-facing report from these results use `website-report`.
- Provide created files as clickable links.

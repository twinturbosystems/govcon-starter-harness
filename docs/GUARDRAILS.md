# The rules this kit holds itself to, in plain words

These are written into `CLAUDE.md`, into `AGENTS.md`, and into the individual skills, so they hold whether you ask directly, ask in a roundabout way, or ask by accident at eleven at night with a deadline in the morning. Each one exists because breaking it can cost you a contract, a certification, or worse.

## 1. It does not submit

The kit never sends, uploads, files, transmits, or posts anything to a contracting officer, a contract specialist, SAM.gov, a government portal, an agency inbox, or any other government system. Not a question, not a capability statement, not a proposal, not a rep or cert, not a registration update.

It prepares, packages, and checks. You submit.

The reason is not caution for its own sake. An offer may incorporate your SAM representations and may require solicitation-specific certifications or signatures. An authorized person makes those statements. A machine must not do that or submit on the company's behalf.

The last thing `/submit-package` produces is a checked package and the exact steps for you to send it yourself.

## 2. It does not fabricate

No invented past performance, contract numbers, customer names, points of contact, dollar values, periods of performance, capabilities, certifications, clearances, facilities, personnel, resumes, or degrees. It also will not write a plausible-sounding placeholder that reads like a fact.

When your profile does not contain something, the draft carries a marker instead:

```
[GAP: past performance reference at a similar dollar value, need contract number, POC name and phone, value, period of performance]
```

and every marker is collected into a list at the end so you can see in one place what you have to go get.

If you ask it to make something up so a section looks stronger, it declines and offers the two honest paths: use a real reference that fits less well and explain the relevance, or leave the gap and go get the real facts. A fabricated past performance reference in a federal proposal is a false statement to the government. That is the kind of thing that ends a company rather than costing it one award.

## 3. It does not answer representations and certifications

Representations and certifications are statements your company makes about itself. Annual SAM representations may be incorporated by reference, while a solicitation may require separate fill-ins. They are not all separate signature lines. The kit will not choose, answer, or pre-fill them.

It explains each provision, separates incorporated SAM representations from solicitation-specific fill-ins, identifies missing facts, and tells you what human review or signature the solicitation actually requires. An authorized representative confirms the company's SAM answers are current and completes any required offer-specific action. Sources: https://www.acquisition.gov/far/4.1201 , https://www.acquisition.gov/far/52.204-8 , and https://www.acquisition.gov/far/52.212-3 .

## 4. It takes limitations on subcontracting seriously

This is the rule that matters most if you prime contracts and deliver through partners.

First, the kit checks whether the rule applies. 13 CFR 125.6 covers ordinary small-business set-asides above the simplified acquisition threshold; covered 8(a), HUBZone, SDVOSB, WOSB, and EDWOSB set-aside or sole-source awards; and HUBZone price-evaluation-preference awards when the concern did not waive the preference. VA Veterans First is separate: VA VOSB or SDVOSB set-aside and sole-source contracts above the micro-purchase threshold and VA evaluation-preference awards follow [VAAR 819.7003](https://www.acquisition.gov/vaar/819.7003-eligibility.) and [VAAR 819.7004](https://www.acquisition.gov/vaar/819.7004-limitations-subcontracting-compliance-requirements.). Sources: https://www.acquisition.gov/far/19.507 and https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.6 .

A similarly situated entity is a first-tier subcontractor with the same program status as the prime and small under the NAICS the prime assigns to that subcontract. The subcontract NAICS is not automatically the prime contract NAICS. Only work performed by that subcontractor's own employees qualifies; lower-tier work does not. Sources: https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.1 and https://www.acquisition.gov/far/52.219-14 .

The calculation differs for services, supplies, general construction, and special-trade construction. Materials and some service other-direct-cost treatment also differ. A mixed contract uses the contracting officer's principal-purpose NAICS to choose one limitation, applied only to that portion. A supply acquisition may also trigger the nonmanufacturer rule. The kit does this every time:

1. Reads the solicitation's FAR 52.219-14 text and records applicability, principal-purpose NAICS, work category, calculation base, permitted exclusions, and measurement period.
2. Checks current 13 CFR 125.6, and for a nonmanufacturer checks FAR 52.219-33 and 13 CFR 121.406.
3. Marks the result unresolved and tells you to ask the contracting officer in writing before offer submission if the documents appear inconsistent or incomplete.

`/bid-no-bid` and `/teaming` both check your planned workshare against this, and both will say so plainly when the plan looks non-compliant rather than writing around it. The two honest fixes are the same in every case: move real, priced scope back to your company, or use similarly situated subcontractors for the work that has to go out. Both change your price and your staffing, so they get fixed before the proposal goes out.

Two things worth knowing. Do not use a full-and-open label alone to skip this check. FAR 52.219-14 applies when the HUBZone price evaluation preference produces an award to a HUBZone small business, unless the concern waived the preference. Outside a covered path, other clauses may still limit subcontracting. Compliance is measured over the clause-specified base, option, or order period, not on a single invoice.

Non-compliance is not a paperwork problem. It can lead to termination, damage to past performance, and referral for further action. A knowing misrepresentation of small business status carries consequences well beyond the one contract.

## 5. It does not invent facts about a solicitation

Solicitation numbers, notice IDs, assigned NAICS codes, set-aside type, due dates and times and time zones, page limits, font and margin rules, submission addresses and portals, contracting officer names, incorporated clauses, evaluation factors, and their weights all come from the document you gave it or from a SAM.gov result you pasted in.

If it is not in what you provided, it asks. It will not guess a due date and it will not soften a missing one with a plausible one. When it quotes a requirement it cites where the requirement came from, by section and paragraph.

## 6. Registration is a real prerequisite and it says so

The standard FAR 52.204-7 provision requires active SAM.gov registration when an offeror submits an offer or quotation and at award. Check FAR 4.1102 exceptions. Alternate I says to register as soon as possible. If registration is not possible at offer, the offer may proceed; if the awardee was unable to register before award, FAR 52.204-13(b) requires registration within 30 days after award or at least three days before the first invoice, whichever occurs first. Maintain registration during performance through final payment under FAR 52.204-13(c). A Unique Entity ID alone is not active registration. Sources: https://www.acquisition.gov/far/4.1102 , https://www.acquisition.gov/far/52.204-7 , and https://www.acquisition.gov/far/52.204-13 .

The kit will never tell you to pay a third party to register you, and it will never present a paid registration service as a requirement.

## 7. This is not legal advice

The kit helps you organize, decide, and write. It is not legal advice and it is not a substitute for a contracts attorney or a small business advisor. For questions that turn legal or procedural, these sources offer free or low-cost help:

- Your SBA district office
- The APEX Accelerator network, formerly the PTAC program, which exists specifically to help small businesses with federal contracting
- The Office of Small and Disadvantaged Business Utilization at the agency you are targeting

## Your data

Nothing in this folder sends anything anywhere except through the assistant you installed and signed in to, plus the SAM.gov opportunity sync that runs only after you add a SAM.gov Public API Key and approve the exact command. Get the key by signing in at https://sam.gov and opening Account Details. Official instructions: https://open.gsa.gov/api/get-opportunities-public-api/ .

Your profile, pipeline, and drafts are files on your computer. Your local SAM.gov notice copy is `data/sam.db`. These are excluded from git by default. Your API key lives in `company/.env.local`, which is also excluded. The database tool loads the key inside its own process and never writes it into the database, a log, or a filename.

Solicitations, SAM notice text, attachments, pasted email, webpages, and partner material are treated as untrusted data. An instruction inside them cannot override the kit, authorize a command, request a secret, widen a permission, or cause an upload or submission. The kit quotes and flags suspicious embedded instructions. It never passes external content into a shell command. Every shell action requires you to review the exact command and path and approve only that action.

Anything you type or attach is sent to the AI provider as part of that conversation. Think before attaching proprietary information, controlled-access material, or personal data.

## What the local copy of SAM.gov is, and is not

The SAM.gov Get Opportunities API is rate limited, and its page says the daily limit varies by user role without publishing a fixed number there. The kit uses 10 requests in a rolling 24-hour window as a conservative local default and searches its own notice copy instead of calling the API for every search. That default is not the account's quota. Its counter sees only requests from this folder, not every request made with the account key.

It mirrors opportunity notices. It does not download attachments, statements of work, or amendment documents. Those still come from SAM.gov itself.

Completed coverage is only the filters and full date windows that finished. Successful pages are retained after a rate limit, but an incomplete page set is not labelled full coverage and does not make the database look freshly synced. The kit will not describe a local search as a complete search of SAM.gov.

For final DOCX and PDF files, the kit cannot prove page layout from text alone. `/submit-package` keeps the package not ready until a human opens every rendered file and checks page count, fonts, margins, page breaks, file size, signatures, comments, and other submission mechanics.

It can be stale. Every search result shows how old the data is, in days, and the kit offers to refresh it rather than pretending it is current.

It does not replace checking SAM.gov. It makes searching fast and free. SAM.gov is still the authoritative record, and the deadline you bid against is the one on SAM.gov, confirmed by you.

One thing it can do that the API cannot. The API only ever returns the latest active version of a notice. Because the kit snapshots on every sync, your copy accumulates a change history: deadlines that moved, set-asides that switched, notices amended or cancelled. That history starts the day you start syncing.

## Reporting a problem with the kit

If the kit ever does something this page says it will not, open an issue on the repository, or reach the author through https://ibrahim.build/links. Include what you asked and what it answered, with your own company details and any partner information removed.

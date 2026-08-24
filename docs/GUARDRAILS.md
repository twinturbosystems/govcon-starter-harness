# The rules this kit holds itself to, in plain words

These are written into `CLAUDE.md`, into `AGENTS.md`, and into the individual skills, so they hold whether you ask directly, ask in a roundabout way, or ask by accident at eleven at night with a deadline in the morning. Each one exists because breaking it can cost you a contract, a certification, or worse.

## 1. It does not submit

The kit never sends, uploads, files, transmits, or posts anything to a contracting officer, a contract specialist, SAM.gov, a government portal, an agency inbox, or any other government system. Not a question, not a capability statement, not a proposal, not a rep or cert, not a registration update.

It prepares, packages, and checks. You submit.

The reason is not caution for its own sake. A federal proposal carries certifications about your company, its size, its socioeconomic status, and the truth of what is in the document. A person with authority to bind the company makes those statements and signs them. A machine must not be the one making them, and no deadline is worth blurring that.

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

Reps and certs, for example the annual representations at FAR 52.204-8 or the offeror representations at FAR 52.212-3, are statements your company makes about itself, signed by someone authorized to bind it. The kit will not answer them, pre-fill them, or recommend an answer as though it were fact.

What it will do is genuinely useful. It reads a rep or cert and tells you in plain English what it is actually asking. It lists which ones in a given solicitation need a decision from you. It flags the ones whose answers depend on facts it does not have. And it notes which ones are pulled from your SAM.gov record rather than typed into the proposal. Then it hands you the list.

## 4. It takes limitations on subcontracting seriously

This is the rule that matters most if you prime contracts and deliver through partners.

When a small business wins a set-aside contract, it cannot simply pass the work through to other companies. Federal rules at 13 CFR 125.6 cap how much of the amount paid under the contract may go to subcontractors that are not similarly situated entities. A similarly situated entity is a subcontractor that is itself small under the NAICS code assigned to that contract and holds the same set-aside status the prime won under, for example another SDVOSB on an SDVOSB set-aside. Work performed by a similarly situated entity does not count against the cap. Work performed by anyone else does.

The cap is a percentage of the amount paid, and the percentage is different for services, for supplies, for general construction, and for construction by special trade contractors. Because it depends on the contract type, and because the clause written into your specific solicitation is what actually binds you, this kit will not state a percentage as settled fact. It does this instead, every time:

1. Points you at the limitations on subcontracting clause in your solicitation, usually FAR 52.219-14, and asks you to read the percentage and the contract type as that solicitation states them.
2. Points you at 13 CFR 125.6, which is the controlling authority, to confirm it.
3. Tells you to ask the contracting officer in writing before bid if the two appear to disagree or the solicitation is silent.

`/bid-no-bid` and `/teaming` both check your planned workshare against this, and both will say so plainly when the plan looks non-compliant rather than writing around it. The two honest fixes are the same in every case: move real, priced scope back to your company, or use similarly situated subcontractors for the work that has to go out. Both change your price and your staffing, so they get fixed before the proposal goes out.

Two things worth knowing. A full and open contract with no set-aside does not carry this cap in the same way, though other clauses may still limit subcontracting, so the clause list still gets read. And compliance is measured over the period the clause specifies, not on a single invoice.

Non-compliance is not a paperwork problem. It can end in termination, it damages your past performance, and a knowing misrepresentation of small business status carries consequences well beyond the one contract.

## 5. It does not invent facts about a solicitation

Solicitation numbers, notice IDs, assigned NAICS codes, set-aside type, due dates and times and time zones, page limits, font and margin rules, submission addresses and portals, contracting officer names, incorporated clauses, evaluation factors, and their weights all come from the document you gave it or from a SAM.gov result you pasted in.

If it is not in what you provided, it asks. It will not guess a due date and it will not soften a missing one with a plausible one. When it quotes a requirement it cites where the requirement came from, by section and paragraph.

## 6. Registration is a real prerequisite and it says so

A company cannot be awarded a federal contract without an active registration in SAM.gov and a Unique Entity ID. Registration is free, and you do it yourself at https://sam.gov. `/setup-profile` establishes where you stand, and if you are not registered it says so plainly and puts that first, ahead of everything else in the kit, so you do not spend a week on a proposal you cannot legally be awarded.

The kit will never tell you to pay a third party to register you, and it will never present a paid registration service as a requirement.

## 7. This is not legal advice

The kit helps you organize, decide, and write. It is not legal advice and it is not a substitute for a contracts attorney or a small business advisor. For the questions that turn legal or procedural, three sources of help are free:

- Your SBA district office
- The APEX Accelerator network, formerly the PTAC program, which exists specifically to help small businesses with federal contracting
- The Office of Small and Disadvantaged Business Utilization at the agency you are targeting

## Your data

Nothing in this folder sends anything anywhere except through the assistant you installed and signed in to, plus one optional SAM.gov opportunity search that only runs if you set up a free api.data.gov key and approve the command.

Your profile, your pipeline, and your drafts are text files on your computer. They are excluded from git by default so that pushing your copy of this folder does not publish your bid pipeline or your partners' information. Your api.data.gov key lives in `company/.env.local`, which is also excluded, and the kit is instructed never to print it, repeat it, or write it into another file.

## Reporting a problem with the kit

If the kit ever does something this page says it will not, open an issue on the repository, or reach the author through https://ibrahim.build/links. Include what you asked and what it answered, with your own company details and any partner information removed.

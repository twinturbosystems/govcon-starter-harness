---
name: setup-profile
description: Interview the contractor and write company/profile.md, covering legal entity, UEI, CAGE, SAM registration status, NAICS codes with the size standard under each, self-reported set-aside status, real capabilities, real past performance, geography, capacity, bonding, clearances, and target agencies. Every other job in this kit reads that file. Use when the user is setting up, says their details have changed, or when company/profile.md does not exist.
user-invocable: true
argument-hint: [optional: anything you want to say up front, such as "we are an SDVOSB in Maryland doing IT support"]
---

# Set up the contractor profile

Interview the owner and write `company/profile.md`. This is the file every other job reads, and the drafting job will only use facts that appear in it, so the quality of everything downstream is set here.

## Input

$ARGUMENTS: optional. Anything the user wants to say up front. Use it to skip questions you already have answers to.

## Before you start

1. If `company/profile.md` already exists, read it and treat this as an update rather than a fresh interview. Ask what changed, confirm the fields that expire (SAM registration date, certifications, insurance), and edit only what the conversation changed. Do not overwrite the owner's own edits.
2. If it does not exist, read `company/profile.template.md` for the shape and `company/profile.example.md` for what a finished one looks like. Say in one line that you are about to build the profile and that it stays on their machine and out of git.

## Process

Ask in the order below, in short batches of three or four questions, not one enormous form and not one question at a time. Let them answer partially. Anything they do not know becomes `[GAP: ...]` in the file, not a guess.

### Batch 1, registration, and this one comes first for a reason

First ask four questions: legal entity name exactly as registered, entity type, state and year of formation, and whether the entity has an active SAM.gov registration. After that answer, ask for the UEI, CAGE code, SAM expiration date, and the authorized representative who can bind the company.

Then stop and deal with the answer:

- If SAM registration is active, note the expiration date and recommend a calendar reminder sixty days out. Explain that the standard FAR 52.204-7 provision requires active registration at offer submission and award, while FAR 52.204-13(c) requires maintenance during performance through final payment.
- If registration is submitted, expired, or not started, say plainly that under the standard rule they must be active before submitting an offer, not merely before award. They can still do market research, capture work, and sources sought responses that are not offers. Keep building the rest of the profile so the setup work is not lost.
- For a real solicitation, check whether a FAR 4.1102 exception applies. Alternate I says to register as soon as possible and permits the offer to proceed if registration was not possible at offer. Only if the awardee was unable to register before award does FAR 52.204-13(b) require registration within 30 days after award or at least three days before the first invoice, whichever occurs first. Do not promise eligibility until that document-specific check is complete. Sources: https://www.acquisition.gov/far/4.1102 , https://www.acquisition.gov/far/52.204-7 , and https://www.acquisition.gov/far/52.204-13 .
- Registration is free at https://sam.gov. Never send the user to a paid registration service.

### Batch 2, what they sell

Ask: what they actually deliver, in the customer's words. Which NAICS codes they market under, and which is primary. Whether they have looked up the SBA size standard for each of those codes and whether they are small under it.

Then, for the NAICS table, ask them to check each code against the SBA table of size standards and give you the figure and the date they checked. Do not supply a size standard from your own memory as fact. If they do not know the standard, write `[GAP: size standard for NAICS xxxxxx, look up in the SBA table of size standards]` and move on.

For each capability, ask the question that matters most in this business model: who actually does that work. Own staff, a named partner, or a partner they would have to go find. Record it that way. A capability delivered entirely by a partner they have never worked with is not the same asset as one their own people have delivered three times, and the bid decision later depends on knowing the difference.

### Batch 3, socioeconomic status

Ask which of these they claim today: small business, 8(a), SDVOSB, VOSB, WOSB, EDWOSB, HUBZone, and any state or agency program. For each, record the evidence source, application or certification status, approval date, expiration if the program uses one, and the date the owner checked it.

Record every answer as self-reported. This kit does not verify status and does not imply it has. Write that line into the profile section itself so it is visible later.

Apply the correct gate rather than one generic "certified or self-certified" choice:

- Small business is a size representation under the applicable NAICS, not a generic SBA certificate. Source: https://www.acquisition.gov/far/52.219-1 .
- For an 8(a) competitive offer, use FAR 52.219-18. A sole-source award also requires SBA acceptance and approval, small status under the assigned NAICS, and current participation at award. Sources: https://www.acquisition.gov/far/52.219-18 , https://www.acquisition.gov/far/19.804-3 , and https://www.acquisition.gov/far/19.808-1 .
- SDVOSB generally uses SBA certification. For a non-VA procurement, preserve the narrow transition for a concern that represented as SDVOSB in SAM and submitted a complete SBA certification application by December 31, 2023, until SBA approves or declines it. VA Veterans First awards instead require SBA VOSB or SDVOSB certification and the solicitation's VA-specific eligibility and certification-of-compliance requirements; the non-VA transition does not apply. Sources: https://www.acquisition.gov/far/52.219-27 , https://www.ecfr.gov/current/title-13/chapter-I/part-128/subpart-B/section-128.200 , https://www.ecfr.gov/current/title-13/chapter-I/part-128/subpart-C/section-128.300 , [VAAR 819.7003](https://www.acquisition.gov/vaar/819.7003-eligibility.) , and [VAAR 819.7004](https://www.acquisition.gov/vaar/819.7004-limitations-subcontracting-compliance-requirements.).
- HUBZone uses SBA certification and acquisition-specific timing. Source: https://www.acquisition.gov/far/19.1303 .
- A competitive WOSB or EDWOSB offer may use the complete-pending-application path only as the current rule permits, but certification is required before award. Sole-source requires certification before offer. Sources: https://www.acquisition.gov/far/52.219-30 and https://www.ecfr.gov/current/title-13/chapter-I/part-127/subpart-E/section-127.504 .
- VOSB alone is not a government-wide SDVOSB status. Treat it as VA-specific unless the solicitation states another authority. Source: https://www.sba.gov/veterans/ .
- If evidence is missing, mark the status unresolved. Do not infer it from a logo, marketing page, or old entry.

### Batch 4, past performance

This is the section that decides how much of a proposal can be written honestly, so spend the time here.

For each reference, ask: customer, whether they were prime or subcontractor, contract or order number, contract type, value, period of performance, NAICS assigned, what they actually did in a few sentences, an outcome with any number they can substantiate, the CPARS rating if it was rated, and a point of contact who is willing to take a call.

Rules while you record it:

- Never help them stretch a reference. If they were a subcontractor, the profile says subcontractor. If the work was commercial rather than federal, the profile says so.
- If a number cannot be substantiated, either drop it or record it with the source that would back it up.
- If they have no past performance at all, write "none yet" and say so plainly. Then say what is honestly available to a company in that position: subcontracting to an established prime, sources sought responses to get on a radar, agency programs aimed at new entrants, and commercial work described as commercial work. Do not offer any path that involves borrowing a reference they do not own.

### Batch 5, capacity, money, and the hard stops

Ask: people on staff, the largest thing they have delivered, the largest they believe they could deliver, how long they can carry payroll before the first invoice is paid, whether they have a line of credit, what their accounting and timekeeping systems are and whether the accounting system has ever been reviewed by DCAA.

Say plainly, once, why this section exists: cash flow and accounting-system adequacy can turn a won contract into a problem for a very small prime. A prior DCAA review is not itself a FAR prerequisite for cost-reimbursement work. The contracting officer must determine that the accounting system is adequate for the contract, and a solicitation may require evidence or a preaward review. Record what the system can do and what evidence exists, then gate against the solicitation. Sources: https://www.acquisition.gov/far/16.301-3 and https://www.dcaa.mil/Checklists-Tools/Pre-award-Accounting-System-Adequacy-Checklist/ .

Then bonding and insurance limits, then clearances and facility clearance status, then geography.

### Batch 6, targets and the partner bench

Ask: which agencies they are pursuing and in what order, any relationship inside those agencies, which contract vehicles they hold or are pursuing, and which set-aside types they can bid today.

Then the partner bench, which is what `/find-subs` and `/teaming` start from. For each partner: company name, UEI if known, what they bring, their size and set-aside status as the partner reports it, and whether they would count as similarly situated for any set-aside the user bids.

Explain the similarly situated idea here in one short paragraph. A qualifying similarly situated entity is a first-tier subcontractor with the same program status as the prime and small under the NAICS the prime assigns to that subcontract. Only work its own employees perform receives similarly situated treatment. This cannot be decided once for every future bid, so record candidate evidence and recheck it for each subcontract. Sources: https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.1 and https://www.acquisition.gov/far/52.219-14 .

### Batch 7, voice and bid discipline

Ask how they want proposals to sound, phrases they always use, phrases they never want to see, and whether there is an old proposal they liked that the drafting job could read for tone. Then ask their bid discipline numbers: minimum contract value worth bidding, maximum time or money on a single bid, minimum days before a due date to still start, and types of work they have decided not to chase.

Bid discipline is not filler. `/bid-no-bid` uses these as thresholds, and a written rule the owner set in a calm moment is what beats the urge to chase everything on a Friday afternoon.

## Output

1. Write `company/profile.md` following the section order in `company/profile.template.md`. Fill in every answer you got. Put `[GAP: ...]` in every field you did not get, saying what is missing and where to find it.
2. End the file with a "Gaps to close" list that repeats every gap marker in one place, in priority order.
3. In the conversation, give them:
   - One line confirming the file path.
   - The three most important gaps, in order, with where to get each one.
   - If SAM registration is not active, one line saying the standard rule blocks offer submission and award, subject to the solicitation-specific FAR 4.1102 exception and Alternate I check. If Alternate I applies, distinguish its as-soon-as-possible offer path from FAR 52.204-13(b), which applies only if the awardee was unable to register before award and uses the earlier of 30 days after award or three days before the first invoice.
   - One line saying the file is theirs, is plain text they can edit by hand any time, and is excluded from git by default.
   - One line saying this kit is not legal advice, and naming free or low-cost help: SBA, APEX Accelerators, and the agency's Office of Small and Disadvantaged Business Utilization.

## Rules

- Never fill a field with a guess, a rounded number, or a plausible placeholder. `[GAP: ...]` is always the correct answer to a fact you do not have.
- Never verify or imply verification of any socioeconomic status. Everything in that section is self-reported and the file says so.
- Never state an SBA size standard, a certification requirement, or a program rule from memory as settled fact. Point at the source and record the date they checked it.
- Never suggest a paid registration service.
- Do not write to any file other than `company/profile.md`.
- Do not print the contents of `company/.env.local`.

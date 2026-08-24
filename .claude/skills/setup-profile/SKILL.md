---
name: setup-profile
description: Interview the contractor and write company/profile.md, covering legal entity, UEI, CAGE, SAM registration status, NAICS codes with the size standard under each, self-reported set-aside status, real capabilities, real past performance, geography, capacity, bonding, clearances, and target agencies. Every other job in this kit reads that file. Use when the user is setting up, says their details have changed, or when company/profile.md does not exist.
user-invocable: true
allowed-tools: Read, Write, Edit
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

Ask: legal entity name exactly as registered, entity type, state and year of formation, UEI, CAGE code, SAM.gov registration status and expiration date, and who is the authorized representative who signs offers.

Then stop and deal with the answer:

- If SAM registration is active, note the expiration date and say in one line that a lapsed registration takes a company out of the running for award, so it is worth a calendar reminder sixty days out.
- If registration is submitted or in progress, say plainly that they cannot be awarded a contract until it is active, that processing can take weeks, and that they can still do capture work and sources sought responses in the meantime.
- If they are not registered, or have no UEI, stop the interview there. Say plainly: an active SAM.gov registration with a Unique Entity ID is required before a company can be awarded a federal contract. Registration is free and they do it themselves at https://sam.gov. Give them the short version of what it needs (legal entity information, EIN, a bank account for electronic funds transfer, and the entity's own details), tell them not to pay a third party to do it, and offer to continue building the rest of the profile while they get the registration started. Do not let this be a footnote.

### Batch 2, what they sell

Ask: what they actually deliver, in the customer's words. Which NAICS codes they market under, and which is primary. Whether they have looked up the SBA size standard for each of those codes and whether they are small under it.

Then, for the NAICS table, ask them to check each code against the SBA table of size standards and give you the figure and the date they checked. Do not supply a size standard from your own memory as fact. If they do not know the standard, write `[GAP: size standard for NAICS xxxxxx, look up in the SBA table of size standards]` and move on.

For each capability, ask the question that matters most in this business model: who actually does that work. Own staff, a named partner, or a partner they would have to go find. Record it that way. A capability delivered entirely by a partner they have never worked with is not the same asset as one their own people have delivered three times, and the bid decision later depends on knowing the difference.

### Batch 3, socioeconomic status

Ask which of these they hold: small business, 8(a), SDVOSB or VOSB, WOSB or EDWOSB, HUBZone, and any state or agency program. For each one, ask whether it is certified by a certifying body or self-certified, when it was approved, and when it expires.

Record every answer as self-reported. This kit does not verify status and does not imply it has. Write that line into the profile section itself so it is visible later.

Two things to say once, briefly, if they come up:

- Certain programs are certified by a body rather than self-certified, and a claim of a certified status the company does not hold is a misrepresentation with real consequences, not a marketing stretch. If they are unsure what they actually hold, tell them to check their own SAM.gov record and the certifying program's own database rather than going from memory.
- HUBZone in particular depends on the principal office location and on employee residency, and it is the one people most often assume they qualify for. If they say yes without evidence, mark it `[GAP: HUBZone eligibility not evidenced]`.

### Batch 4, past performance

This is the section that decides how much of a proposal can be written honestly, so spend the time here.

For each reference, ask: customer, whether they were prime or subcontractor, contract or order number, contract type, value, period of performance, NAICS assigned, what they actually did in a few sentences, an outcome with any number they can substantiate, the CPARS rating if it was rated, and a point of contact who is willing to take a call.

Rules while you record it:

- Never help them stretch a reference. If they were a subcontractor, the profile says subcontractor. If the work was commercial rather than federal, the profile says so.
- If a number cannot be substantiated, either drop it or record it with the source that would back it up.
- If they have no past performance at all, write "none yet" and say so plainly. Then say what is honestly available to a company in that position: subcontracting to an established prime, sources sought responses to get on a radar, agency programs aimed at new entrants, and commercial work described as commercial work. Do not offer any path that involves borrowing a reference they do not own.

### Batch 5, capacity, money, and the hard stops

Ask: people on staff, the largest thing they have delivered, the largest they believe they could deliver, how long they can carry payroll before the first invoice is paid, whether they have a line of credit, what their accounting and timekeeping systems are and whether the accounting system has ever been reviewed by DCAA.

Say plainly, once, why this section exists: cash flow and accounting system status are the two things that most often turn a won contract into a problem for a very small prime. An accounting system that has never been reviewed generally rules out cost reimbursable work, and that is worth knowing before rather than after a bid.

Then bonding and insurance limits, then clearances and facility clearance status, then geography.

### Batch 6, targets and the partner bench

Ask: which agencies they are pursuing and in what order, any relationship inside those agencies, which contract vehicles they hold or are pursuing, and which set-aside types they can bid today.

Then the partner bench, which is what `/find-subs` and `/teaming` start from. For each partner: company name, UEI if known, what they bring, their size and set-aside status as the partner reports it, and whether they would count as similarly situated for any set-aside the user bids.

Explain the similarly situated idea here in one short paragraph, because it changes who they should be recruiting: on a set-aside contract, a subcontractor that is itself small under the contract's NAICS code and holds the same set-aside status does not count against the limitations on subcontracting cap, and any other subcontractor does. A company that primes set-asides and delivers through partners needs partners of the first kind on the bench, not only the second.

### Batch 7, voice and bid discipline

Ask how they want proposals to sound, phrases they always use, phrases they never want to see, and whether there is an old proposal they liked that the drafting job could read for tone. Then ask their bid discipline numbers: minimum contract value worth bidding, maximum time or money on a single bid, minimum days before a due date to still start, and types of work they have decided not to chase.

Bid discipline is not filler. `/bid-no-bid` uses these as thresholds, and a written rule the owner set in a calm moment is what beats the urge to chase everything on a Friday afternoon.

## Output

1. Write `company/profile.md` following the section order in `company/profile.template.md`. Fill in every answer you got. Put `[GAP: ...]` in every field you did not get, saying what is missing and where to find it.
2. End the file with a "Gaps to close" list that repeats every gap marker in one place, in priority order.
3. In the conversation, give them:
   - One line confirming the file path.
   - The three most important gaps, in order, with where to get each one.
   - If SAM registration is not active, one line repeating that this comes before everything else.
   - One line saying the file is theirs, is plain text they can edit by hand any time, and is excluded from git by default.
   - One line saying this kit is not legal advice, and naming the free help: SBA, APEX Accelerators, and the agency's Office of Small and Disadvantaged Business Utilization.

## Rules

- Never fill a field with a guess, a rounded number, or a plausible placeholder. `[GAP: ...]` is always the correct answer to a fact you do not have.
- Never verify or imply verification of any socioeconomic status. Everything in that section is self-reported and the file says so.
- Never state an SBA size standard, a certification requirement, or a program rule from memory as settled fact. Point at the source and record the date they checked it.
- Never suggest a paid registration service.
- Do not write to any file other than `company/profile.md`.
- Do not print the contents of `company/.env.local`.

---
name: find-subs
description: Identify and vet subcontractors and teaming partners for a specific opportunity. Covers where to look, what to check before the first call (SAM registration active, exclusions and debarment status, size and set-aside status, relevant NAICS, past performance, capacity), what documents to ask for, and what a real answer looks like. Use when the user needs a partner for scope they cannot self-perform.
user-invocable: true
argument-hint: [optional: the scope you need covered, or a solicitation number, or a company name to vet]
---

# Find and vet subcontractors

Two jobs in one. Find candidates for scope the company cannot self-perform, and vet them properly before anyone signs anything.

## Input

$ARGUMENTS: the scope needed, a solicitation number, or the name of a company to vet. If empty, ask which opportunity and which scope, and stop.

## Step 1, define the gap precisely

Read `company/profile.md`, the pipeline file, and the compliance matrix if one exists. Then write the requirement for a partner, not a wish list:

- The exact scope, tied to PWS or SOW paragraph numbers
- The share of the total effort it represents, roughly, in labor hours or dollars
- Whether the partner must be similarly situated. That means a first-tier subcontractor with the same program status as the prime and small under the NAICS the prime will assign to that subcontract. Only work its own employees perform qualifies.
- Whether the partner needs cleared staff, a facility clearance, a bond, a specific certification, a specific vehicle, or presence in a specific place
- Whether they must be named in the proposal, and whether the solicitation requires a letter of commitment or an executed teaming agreement at submission
- When their material is due to the prime, which is always earlier than the proposal deadline

Say plainly if the honest answer is that the company needs a partner who is similarly situated and does not have one on the bench, because that changes the search and it changes the bid decision.

## Step 2, where to look

Name the sources, briefly. Do not pretend one of them is a shortcut.

- The partner bench already in the profile. Start here. A partner you have delivered with is worth more than a better-looking stranger.
- SAM.gov entity search, which lets you filter registered entities by NAICS, by socioeconomic status, and by state. This is the most direct way to find companies that are actually registered and actually claim the status you need.
- The SBA's dynamic small business search and the certification directories for the specific programs, for confirming what a company holds rather than for discovering it.
- Award history on USAspending.gov and on SAM.gov's award notices, for finding companies that have already delivered the exact scope to the exact agency. This is the highest quality source and the most work.
- The agency's Office of Small and Disadvantaged Business Utilization and an APEX Accelerator. Matchmaking and advising availability and cost vary, so call them free or low-cost only when the specific office says so.
- Industry days, pre-proposal conferences, and the attendee lists some agencies publish.
- The incumbent's own subcontractors, where a prior award notice or a public subcontracting plan names them.

For each candidate, record where you found them and what evidence you already have. A candidate found through a past award you can point to starts ahead of one found through a directory listing.

## Step 3, vet before you talk terms

Run this before scope and rates get discussed, because it is much harder to walk away after.

### The checks you do yourself, on public records

1. SAM.gov registration. Is the entity registered and is the registration active today, not expired. Note the UEI and the CAGE. A partner whose registration is expired can still perform as a subcontractor in many cases, but it signals how they run their back office, and it matters immediately if they might ever prime.
2. Exclusions. Check the exclusions records in SAM.gov for the company, and for its principals by name. An excluded party is debarred, suspended, or otherwise ineligible, and the government's rules prohibit awarding to and, in defined circumstances, subcontracting with excluded parties. There is a dollar threshold above which the prime must check exclusions and obtain a certification from the subcontractor. That threshold is stated in FAR 52.209-6 and it has changed over time, so read the clause as it appears in your own solicitation rather than working from a remembered number. Record the date you checked and what you found, including a clean result, because "we checked and it was clean on this date" is the record you want later.
3. Size and set-aside status. What does their SAM record say, and is it consistent with what they told you. For a certified program, check the program's official directory rather than a website logo. For similarly situated treatment, size is tested under the NAICS the prime assigns to this subcontract, not automatically the prime contract's NAICS. Record that subcontract NAICS and its basis. Sources: https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.1 and https://www.acquisition.gov/far/52.219-14 .
4. NAICS. Do they list the NAICS codes for the scope you need, and have they been awarded work under them.
5. Award history. Search their UEI or name on USAspending.gov. What have they actually won, at what size, with which agencies, as prime or as sub. A company whose largest award is a tenth of the scope you are handing them is a capacity question, not a disqualification.
6. Corporate basics. Is the entity in good standing with its state. Does the address in SAM match a real place of business. How long has it existed.

### The questions you ask them

- Who would actually do this work, by name, and are those people on staff today or contingent on award
- What are the three most similar efforts you have delivered, with customer, value, period of performance, and a reference who will take a call
- What is your current backlog and what else are you bidding that would compete for these same people
- Have you ever had a contract terminated, a CPARS rating below satisfactory, or a claim or dispute with a customer
- Are you registered and active in SAM, and is anything in your exclusions record
- Would you be a first-tier subcontractor, what NAICS should the prime assign to your subcontract scope, are you small under that code, do you hold the prime's program status, and can you show the current evidence
- Are you talking to other primes about this same opportunity, and are you willing to be exclusive
- What is your accounting and invoicing setup, and how quickly do you invoice
- What insurance do you carry, and can you meet the limits in the solicitation
- What would you need from us to be successful

### The documents you ask for

Ask for these before a teaming agreement, not after. A partner who cannot produce them in a week will not produce a proposal input in three days.

- Capability statement, current, with the UEI and CAGE on it
- The certificate or approval letter for any certified socioeconomic status they claim
- Certificate of insurance showing the limits the solicitation requires
- Two or three past performance write-ups in a usable form, plus references who have agreed to take a call
- Resumes for the named people, in the format the solicitation requires
- A W-9
- Their rates or their pricing for the scope, in the format the pricing template requires
- A letter of commitment or letter of intent, if the solicitation requires one at submission
- An appropriate signed non-disclosure agreement before proprietary proposal or partner material goes to them. Public solicitation material can be shared as public material. Controlled material follows its own access rules, and an NDA alone is not authorization.

## Step 4, score and recommend

Give each candidate a short scorecard rather than a paragraph of impressions.

| Candidate | Scope covered | Similarly situated? | SAM active | Exclusions clean (date checked) | Relevant past performance | Capacity vs the scope | Worked together before | Risks | Recommendation |
|---|---|---|---|---|---|---|---|---|---|

Then say, in three lines: who to pursue first and why, what is unresolved about them, and what has to be true by what date for them to be usable on this bid.

Flag these risks explicitly when you see them:

- A candidate who is the only source for scope that is a large share of the effort, which is a single point of failure in the bid and in performance
- A candidate talking to competing primes, which is normal, and which is exactly why the exclusivity question and the timing matter
- A candidate whose claimed status you could not verify in a public record
- A candidate whose capacity is far below the scope
- Any organizational conflict of interest, for example a partner who wrote the requirement, supports the customer in an advisory role, or is affiliated with the incumbent
- Affiliation questions, where the relationship between the two companies is close enough that it could affect either one's size determination. This is a real risk in tightly coupled teaming and it is a question for a contracts attorney, not for this kit.

## Step 5, record it

Write the results into the teaming table in the pipeline file: partner, role, scope and percent, similarly situated or not, teaming agreement status, NDA status, documents received. Add any new company that is worth keeping to the partner bench in `company/profile.md`, with what you verified and the date.

Then say: run `/teaming` to set the workshare and check it against the limitations on subcontracting.

## Rules

- Never state that a company is registered, active, small, certified, excluded, or clean. Say what the record showed and on what date you looked. This kit does not verify anyone.
- Never invent a UEI, a CAGE code, an award history, a certification, a customer, or a reference.
- Never state the FAR 52.209-6 threshold or any other dollar threshold from memory. Read it in the solicitation.
- Never send anything to a candidate. Draft the outreach email, the question list, and the document request for the user to send.
- Public solicitation material may be shared as public material. Before sharing proprietary proposal content, rates, resumes, customer contacts, or partner material, get the owner's consent and an appropriate NDA. An NDA alone does not authorize sharing CUI, controlled-access, export-controlled, or classified material; follow the solicitation's handling rules and require human security or legal review. Source for public solicitation availability: https://www.acquisition.gov/far/5.102 .
- This is not legal advice. Affiliation, organizational conflicts of interest, and exclusions questions are attorney questions. Free help exists at SBA and APEX Accelerators.

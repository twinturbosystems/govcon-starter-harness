---
name: bid-no-bid
description: Score one opportunity against company/profile.md on a stated rubric covering NAICS and capability fit, set-aside eligibility, incumbent presence, realistic win probability, time to deadline, cost to bid, and whether the work can actually be staffed or subcontracted, including a limitations on subcontracting check against the planned workshare. Ends with a clear go or no-go and the reasoning. Use when the user asks whether to bid something.
user-invocable: true
allowed-tools: Read, Write, Edit
argument-hint: [paste the opportunity, or give the pipeline file name, or the solicitation number]
---

# Bid or no-bid

Score one opportunity, then say go or no-go and why. The answer is a recommendation with its reasoning exposed, so the owner can disagree with a specific line rather than with a verdict.

## Input

$ARGUMENTS: a pasted notice or solicitation, a path to a file in `pipeline/`, or a solicitation number already tracked. If empty, ask which opportunity, and stop there.

## Step 1, gather what you actually have

1. Read `company/profile.md`. If it does not exist, say so and offer `/setup-profile`. Do not score against an imagined company.
2. Read the pipeline file if one exists, or take the pasted notice.
3. List, in three or four lines, the facts you are scoring against: solicitation number, agency, NAICS, set-aside, place of performance, contract type, estimated value if stated, response deadline with the time and time zone, and whether you have the full solicitation or only the notice summary.
4. Name what is missing. If the set-aside type, the NAICS, the deadline, or the contract type is not stated in what you were given, ask for it before scoring. Those four change the answer. Everything else you can score around, marking it as unknown.

Never fill any of those from memory or from a similar solicitation.

## Step 2, hard stops, checked before scoring

If any of these is true, the answer is no-go regardless of the score. Say which one, in one line, and stop. Do not produce a score that argues with a hard stop.

- SAM.gov registration is not active, and cannot be made active before award
- The company is not eligible for the set-aside as stated in the notice
- The company is not small under the size standard for the NAICS the solicitation assigned
- A bond is required and the company has no surety relationship, with no time to build one
- A facility clearance or cleared personnel are required and the company has neither
- The contract is cost reimbursable and the accounting system has never been reviewed, where the solicitation requires an adequate accounting system
- The award will be made under a vehicle the company does not hold and cannot get onto in time
- The deadline is closer than the minimum lead time in the profile's bid discipline section, and no partner is already lined up
- A mandatory site visit or a mandatory pre-proposal step has already passed

## Step 3, score the seven factors

Score each factor 0 to 5. Write one or two sentences of evidence under each, citing the profile section or the solicitation paragraph the evidence came from. A factor you cannot evidence is scored 2 and marked unknown, not scored high on optimism.

| # | Factor | Weight | What a 5 looks like | What a 0 looks like |
|---|---|---|---|---|
| 1 | Fit to NAICS and capability | 25 | The assigned NAICS is a primary code, and the scope is work the company's own people have delivered before | The NAICS is unrelated, or the scope is entirely work nobody on the team or the bench has done |
| 2 | Set-aside eligibility and competitive position inside it | 15 | Eligible, certified, and the set-aside narrows the field to companies of the same size and shape | Not eligible, or eligible but competing against far larger firms in a full and open field |
| 3 | Incumbent and competitive landscape | 15 | No incumbent, a new requirement, or an incumbent with known performance problems the customer has said something about | A satisfied incumbent recompeting a contract they have held through two cycles |
| 4 | Staffing and subcontracting feasibility | 20 | Key personnel are on staff and available, and every subcontracted piece has a named partner who has already said yes | Key personnel would have to be recruited contingent on award, and the subcontracted scope has no named partner |
| 5 | Time to deadline | 10 | Comfortably more than the profile's minimum lead time, questions period still open | At or under the minimum, with teaming agreements still unsigned |
| 6 | Cost to bid against the prize | 10 | Bid effort is well inside the profile's cap and the value is well above the minimum worth bidding | The bid would blow the cap, or the value is at or below the floor |
| 7 | Realistic win probability | 5 | Named relationship inside the office, directly relevant past performance, and a discriminator the competition cannot match | No relationship, no relevant past performance, no discriminator |

Weighted score out of 100. Show the arithmetic in the table so the owner can re-weight it if they disagree.

Two rules about factor 7. State win probability as a band, low, moderate, or good, with the reasoning behind it. Do not produce a percentage, because a percentage invented from nothing looks like analysis and is not. And say plainly when the honest answer is that a first-time bidder against a satisfied incumbent is unlikely to win, because a no-go that saves forty hours is worth more than an encouraging score.

## Step 4, the limitations on subcontracting check

Run this whenever the opportunity is a set-aside. It can turn a high score into a no-go, so it sits after the scoring rather than inside it.

1. Ask, or read from the solicitation, the planned split: what share the company would self-perform, what share goes to subcontractors that are similarly situated, and what share goes to everyone else. A similarly situated subcontractor is one that is itself small under the NAICS code assigned to this contract and holds the same set-aside status the prime is bidding under.
2. Find the limitations on subcontracting clause in this solicitation, usually FAR 52.219-14, and quote what the solicitation itself states: the percentage and the contract type it applies to. If you do not have the full solicitation, say so and mark this check as unresolved rather than assuming.
3. Confirm against 13 CFR 125.6, which is the controlling authority. The percentage differs for services, supplies, general construction, and construction by special trade contractors, so the contract type has to be established before the number means anything.
4. Never state the percentage from memory as settled fact. Tell the user to read the clause in their own solicitation and confirm it against 13 CFR 125.6, and to ask the contracting officer in writing before bid if the two appear to disagree or the solicitation is silent.
5. Compare the plan to the clause. If the planned pass-through to non-similarly-situated subcontractors looks like it exceeds what the clause allows, say so in plain words, immediately, before the recommendation. Give the two fixes: move real, priced scope back to the prime, or replace those subcontractors with similarly situated ones. Both change price and staffing, so they belong in the bid decision rather than after award.
6. If the fix is not achievable with the partners on the bench and the time available, that is a no-go, and say so.

Write the result of this check into the pipeline file's limitations on subcontracting section, including which clause you read and where.

For a full and open opportunity with no set-aside, note that this cap does not apply in the same way, and that other clauses in the solicitation may still limit subcontracting, so the clause list still has to be read.

## Step 5, the decision

Lead with it. One line, at the top of the answer, before the table.

- 75 and above, no hard stop, subcontracting check clean: go
- 55 to 74: go if a named condition is met, and name the condition. For example, a signed teaming agreement with a similarly situated partner by a specific date, or a question to the contracting officer answered a specific way. Give the date by which the condition has to be true, and say that missing it converts this to a no-go.
- Below 55: no-go
- Any hard stop, or an unresolvable subcontracting problem: no-go, regardless of the score

Then, under the decision:

- The three lines that drove it, in order of weight
- What would have to change for a no-go to become a go next time, in one or two lines, because most no-gos are about a gap the owner can actually close
- The questions worth submitting to the contracting officer before the questions deadline, numbered, each citing the section it refers to. Say plainly that the user submits these, by the method and before the deadline the solicitation states.
- Every `[GAP: ...]` you hit while scoring, collected

## Step 6, record it

Update the pipeline file: decision, date, score, the one-line reason, and the subcontracting check result. If no pipeline file exists, create one from `pipeline/opportunity.template.md` first. A written no-go is worth as much as a written go, because it stops the same opportunity being re-litigated in three weeks.

## Rules

- Never invent an incumbent, an estimated value, a deadline, a NAICS, a set-aside type, or a clause. Unknown is a valid input and it lowers the score honestly.
- Never score a factor higher because the user wants to bid. If the owner disagrees with a score, ask what evidence they have, put the evidence in, and rescore.
- Never state a limitations on subcontracting percentage as settled fact. Cite the clause in the solicitation and 13 CFR 125.6, and tell them to verify.
- This is not legal advice. Say it once if the subcontracting check comes out close to the line, and name the free help: SBA, APEX Accelerators, and the agency's Office of Small and Disadvantaged Business Utilization.
- Do not submit anything, do not offer to submit the questions, and do not draft an email to the contracting officer as though it were going out. Draft the questions; the user sends them.

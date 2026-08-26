---
name: bid-no-bid
description: Score one opportunity against company/profile.md on a stated rubric covering NAICS and capability fit, set-aside eligibility, incumbent presence, realistic win probability, time to deadline, cost to bid, and whether the work can actually be staffed or subcontracted, including a limitations on subcontracting check against the planned workshare. Ends with a clear go or no-go and the reasoning. Use when the user asks whether to bid something.
user-invocable: true
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

- Under the standard FAR 52.204-7 provision, SAM.gov registration is not active and cannot be active before offer submission or award. First check FAR 4.1102 exceptions. Under Alternate I, inability to register at offer does not itself block the offer, and the offeror must register as soon as possible. Only if the awardee was unable to register before award does FAR 52.204-13(b) set the deadline at 30 days after award or at least three days before the first invoice, whichever occurs first. Maintain registration during performance through final payment under FAR 52.204-13(c). Sources: https://www.acquisition.gov/far/4.1102 , https://www.acquisition.gov/far/52.204-7 , and https://www.acquisition.gov/far/52.204-13 .
- The company cannot satisfy the program-specific gate for the set-aside. Apply the 8(a), SDVOSB, WOSB or EDWOSB, HUBZone, or general-small-business gate in `CLAUDE.md`; do not accept a generic “self-certified” answer.
- The company is not small under the size standard for the NAICS the solicitation assigned
- A bond is required and the company has no surety relationship, with no time to build one
- A facility clearance or cleared personnel are required and the company has neither
- The solicitation requires an adequate accounting system and the company cannot evidence or establish adequacy in time. A prior DCAA review is relevant evidence, not a universal prerequisite. Sources: https://www.acquisition.gov/far/16.301-3 and https://www.dcaa.mil/Checklists-Tools/Pre-award-Accounting-System-Adequacy-Checklist/ .
- The award will be made under a vehicle the company does not hold and cannot get onto in time
- The deadline is closer than the minimum lead time in the profile's bid discipline section, and no partner is already lined up
- A mandatory site visit or a mandatory pre-proposal step has already passed

## Step 3, score the seven factors

Score each factor 0 to 5. Write one or two sentences of evidence under each, citing the profile section or the solicitation paragraph the evidence came from. A factor you cannot evidence is scored 2 and marked unknown, not scored high on optimism.

| # | Factor | Weight | What a 5 looks like | What a 0 looks like |
|---|---|---|---|---|
| 1 | Fit to NAICS and capability | 25 | The assigned NAICS is a primary code, and the scope is work the company's own people have delivered before | The NAICS is unrelated, or the scope is entirely work nobody on the team or the bench has done |
| 2 | Set-aside eligibility and competitive position inside it | 15 | Current evidence satisfies the named program gate, or the general small-business size representation where that is the gate, and the acquisition narrows the field as stated | The named program or size gate is not met, or evidence is missing and eligibility cannot be established |
| 3 | Incumbent and competitive landscape | 15 | No incumbent, a new requirement, or an incumbent with known performance problems the customer has said something about | A satisfied incumbent recompeting a contract they have held through two cycles |
| 4 | Staffing and subcontracting feasibility | 20 | Key personnel are on staff and available, and every subcontracted piece has a named partner who has already said yes | Key personnel would have to be recruited contingent on award, and the subcontracted scope has no named partner |
| 5 | Time to deadline | 10 | Comfortably more than the profile's minimum lead time, questions period still open | At or under the minimum, with teaming agreements still unsigned |
| 6 | Cost to bid against the prize | 10 | Bid effort is well inside the profile's cap and the value is well above the minimum worth bidding | The bid would blow the cap, or the value is at or below the floor |
| 7 | Realistic win probability | 5 | Named relationship inside the office, directly relevant past performance, and a discriminator the competition cannot match | No relationship, no relevant past performance, no discriminator |

Weighted score out of 100. Show the arithmetic in the table so the owner can re-weight it if they disagree.

Two rules about factor 7. State win probability as a band, low, moderate, or good, with the reasoning behind it. Do not produce a percentage, because a percentage invented from nothing looks like analysis and is not. And say plainly when the honest answer is that a first-time bidder against a satisfied incumbent is unlikely to win, because a no-go that saves forty hours is worth more than an encouraging score.

## Step 4, the limitations on subcontracting check

First decide whether the rule applies. 13 CFR 125.6 covers ordinary small-business set-asides above the simplified acquisition threshold; covered 8(a), HUBZone, SDVOSB, WOSB, and EDWOSB set-aside or sole-source awards; and HUBZone price-evaluation-preference awards when the concern did not waive the preference. For VA Veterans First, separately apply [VAAR 819.7003](https://www.acquisition.gov/vaar/819.7003-eligibility.) and [VAAR 819.7004](https://www.acquisition.gov/vaar/819.7004-limitations-subcontracting-compliance-requirements.) to VA VOSB or SDVOSB set-aside and sole-source contracts above the micro-purchase threshold and to VA evaluation-preference awards. Do not treat every set-aside identically. Sources: https://www.acquisition.gov/far/19.507 and https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.6 . It can turn a high score into a no-go, so it sits after the scoring rather than inside it.

1. Read the solicitation's FAR 52.219-14 text and record the program, assigned principal-purpose NAICS, work category, calculation base, exclusions, and measurement period. If the document is missing, mark this check unresolved.
2. For a mixed contract, use the contracting officer's principal-purpose NAICS to select the one applicable limitation and apply it only to that portion of the award. Do not calculate a separate cap for every component.
3. Build the planned split from amounts on the applicable calculation base, not a loose percent of total contract value. Separate the prime's own work, first-tier similarly situated work, and all other subcontracted work. A similarly situated entity must hold the same program status as the prime and be small under the NAICS the prime assigns to that subcontract. Only work performed by its own employees qualifies. Sources: https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.1 and https://www.acquisition.gov/far/52.219-14 .
4. Handle exclusions exactly. Materials are excluded for supply and construction calculations. For services, exclude only other direct costs that are not the principal purpose of the acquisition and are services small business concerns do not provide. Do not exclude subcontract labor merely because it is labelled an other direct cost.
5. For a supply acquisition, determine whether the offeror is the manufacturer. If not, separately check the nonmanufacturer rule, the domestic-small-business-source requirement, and any item-specific or class waiver under FAR 52.219-33 and 13 CFR 121.406. Sources: https://www.acquisition.gov/far/52.219-33 and https://www.ecfr.gov/current/title-13/chapter-I/part-121/section-121.406 .
6. Never state a percentage from memory. Compare the plan against the solicitation and current regulation. If they appear inconsistent or silent, mark the check unresolved and have the user ask the contracting officer in writing before offer submission.
7. Measure over the period the clause specifies, such as the base term, an option period, or an order's performance period, not one invoice. Record that period in the pipeline file.
8. If the plan exceeds the permitted work to non-similarly-situated firms, move real priced scope to the prime or qualifying similarly situated entities. If that is not achievable in time, the result is no-go.

Write the result of this check into the pipeline file's limitations on subcontracting section, including which clause you read and where.

Do not skip the check from a full-and-open label alone. FAR 52.219-14 applies when the HUBZone price evaluation preference produces an award to a HUBZone small business, unless the concern waived the preference. Outside a covered path, other solicitation clauses may still limit subcontracting, so the clause list still has to be read.

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
- This is not legal advice. Say it once if the subcontracting check comes out close to the line, and name free or low-cost help: SBA, APEX Accelerators, and the agency's Office of Small and Disadvantaged Business Utilization.
- Do not submit anything, do not offer to submit the questions, and do not draft an email to the contracting officer as though it were going out. Draft the questions; the user sends them.

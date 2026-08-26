---
name: teaming
description: Prepare the teaming approach for one opportunity. Sets the workshare split, checks it against the limitations on subcontracting for a set-aside, produces a teaming agreement checklist and the NDA points, and lists everything that must be settled before the proposal goes out. Use when the user is deciding who does what share, or is about to sign a teaming agreement.
user-invocable: true
argument-hint: [solicitation number, or the partners and the split you are considering]
---

# Teaming

Set the workshare, check it against the rule, and list what has to be signed before the proposal goes out.

## Input

$ARGUMENTS: a solicitation number, or a described split such as "we do program management, Talbot does the field work, roughly 70 percent to them". If empty, ask which opportunity and stop.

## Step 1, read the situation

Read `company/profile.md`, the pipeline file, and the compliance matrix if it exists. Establish and state, in five or six lines:

- Set-aside type, or full and open
- The NAICS code the solicitation assigned, and whether the prime is small under it
- Contract type, as the solicitation states it, because the subcontracting cap differs by contract type
- The scope broken into pieces, tied to PWS or SOW paragraph numbers
- Which pieces the prime self-performs today, which need a partner, and which partners are candidates
- What the solicitation requires at submission regarding partners: named or not, letters of commitment, executed teaming agreements, subcontractor past performance rules, and whether a small business subcontracting plan is required

If the solicitation is not in hand, say plainly that the workshare check cannot be completed without the clause, and do the rest of the work marked as provisional.

## Step 2, build the workshare table

One row per piece of scope. Record the dollar amount against the calculation base named in the clause, plus value and labor percentages for planning. Do not assume total contract value or headcount is the legal calculation base.

| Scope | PWS ref | Performed by | First-tier? | Subcontract NAICS | Program status and evidence | Similarly situated? | Amount on clause calculation base | Percent of value | Percent of labor | Basis |
|---|---|---|---|---|---|---|---|---|---|---|

A similarly situated entity is a first-tier subcontractor with the same program status as the prime and small under the NAICS the prime assigns to that subcontract. That subcontract NAICS may differ from the prime contract NAICS. Only work its own employees perform qualifies. Mark each partner yes, no, or unverified, and never mark one yes on the partner's say-so alone. Record the evidence and date. Sources: https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.1 and https://www.acquisition.gov/far/52.219-14 .

Then total three numbers: self-performed, similarly situated subcontractors, everyone else.

## Step 3, the limitations on subcontracting check

This is the step this whole skill exists for. First establish applicability. 13 CFR 125.6 covers ordinary small-business set-asides above the simplified acquisition threshold; covered 8(a), HUBZone, SDVOSB, WOSB, and EDWOSB set-aside or sole-source awards; and HUBZone price-evaluation-preference awards when the concern did not waive the preference. For VA Veterans First, separately apply [VAAR 819.7003](https://www.acquisition.gov/vaar/819.7003-eligibility.) and [VAAR 819.7004](https://www.acquisition.gov/vaar/819.7004-limitations-subcontracting-compliance-requirements.) to VA VOSB or SDVOSB set-aside and sole-source contracts above the micro-purchase threshold and to VA evaluation-preference awards. Sources: https://www.acquisition.gov/far/19.507 and https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.6 .

Explain it plainly to the user before you check it, in something close to these words.

When the rule applies, 13 CFR 125.6 and FAR 52.219-14 limit amounts paid to subcontractors that are not similarly situated. Qualifying first-tier similarly situated work may count, but lower-tier work does not. The calculation and exclusions differ for services, supplies, general construction, and special-trade construction.

Then do this, in order, and do not skip a step:

1. Find FAR 52.219-14 in this solicitation. Record the program, assigned principal-purpose NAICS, work category, percentage, calculation base, exclusions, and clause-specified measurement period.
2. Confirm it against 13 CFR 125.6. If the solicitation and current regulation appear inconsistent or silent, mark the check unresolved and have the user ask the contracting officer in writing before offer submission.
3. For a mixed contract, use the principal-purpose NAICS assigned by the contracting officer to choose one limitation and apply it only to that portion of the award. Do not apply separate limitations to each component.
4. Apply exclusions exactly. Materials are excluded for supply and construction calculations. For services, exclude only other direct costs that are not the principal purpose of the acquisition and are services small business concerns do not provide. Subcontract labor is not excluded merely because it is labelled an other direct cost.
5. If this is a supply acquisition, decide whether the offeror is the manufacturer. If not, separately check FAR 52.219-33 and 13 CFR 121.406, including the domestic-small-business-source requirement and any item-specific or class waiver. Sources: https://www.acquisition.gov/far/52.219-33 and https://www.ecfr.gov/current/title-13/chapter-I/part-121/section-121.406 .
6. Compare the planned amounts from step 2 against the clause calculation.

Never state the percentage from your own memory as settled fact, and never let the user proceed on a figure you supplied without sending them to those two sources.

Then say the result in one line, at the top of the answer, in plain words. One of:

- The plan looks compliant against the clause as written in this solicitation, with the arithmetic shown, and the user should still confirm the clause text themselves.
- The plan looks non-compliant. Say by roughly how much, and say it before anything else in the answer.
- The check cannot be completed. Say exactly what is missing: the clause, the contract type, or a partner's similarly situated status.

If the plan looks non-compliant, give the two fixes and price both:

1. Move real, priced scope back to the prime. Name which scope, say who would do it, and say what it changes in the staffing and the price. Scope moved back on paper without a person behind it is not a fix, it is a bigger problem later.
2. Replace non-similarly-situated subcontractors with similarly situated ones for some or all of that scope. Name what the search costs in time against the deadline, and say what happens if it is not found.

If neither fix is achievable with the partners available and the time left, say so plainly and send the user back to `/bid-no-bid`, because this is a no-go and it is better found now.

Two more things to say when they apply. Compliance is measured over the period the clause specifies, such as the base term, an option period, or an order's performance period, not on a single invoice. Record that period and track it during performance. Do not skip the check from a full-and-open label alone. FAR 52.219-14 applies when the HUBZone price evaluation preference produces an award to a HUBZone small business, unless the concern waived the preference. Outside a covered path, other clauses may still limit subcontracting.

Write the result into the limitations on subcontracting section of the pipeline file, including which clause you read, what it said, and the date.

## Step 4, the teaming agreement checklist

A teaming agreement is signed before award and governs how the two companies pursue the opportunity and what happens if they win. It is not the subcontract. Produce the checklist below for the user to work through with counsel, and say once that this is not legal advice.

Scope and workshare

- The exact scope each party performs, tied to PWS or SOW paragraph numbers, not a percentage alone
- The workshare expressed both as a percentage and as the named scope, and what happens if the government changes the scope
- Whether the workshare is a commitment or a good-faith target, which is the single most argued clause in these agreements
- Confirmation that the split as written keeps the prime compliant with the limitations on subcontracting clause

Exclusivity and conduct

- Whether the partner is exclusive to this prime for this opportunity, and for how long
- Whether either party may bid the same opportunity independently or with another team
- Who owns the customer relationship during capture, and who may contact the contracting officer, which should be the prime only
- Non-solicitation of each other's employees, and for how long

Proposal work

- What each party contributes, in what format, and by what date, which should be well before the proposal deadline
- Who owns the proposal material, and who may reuse it if the team does not win
- Who bears their own bid and proposal costs, which is usually each party for itself
- Consent to use the partner's name, past performance, and resumes in the proposal, and what happens to that consent if the team breaks up
- Approval rights over how the partner is described

If you win

- The obligation to negotiate a subcontract in good faith, and a deadline for it, usually counted from award
- The terms already agreed, so the subcontract negotiation is not a second negotiation from zero: rates or price basis, payment terms, invoicing timing, key personnel commitments
- Flow-down clauses the subcontract will carry
- What happens if the government directs a change to the team, or refuses to consent to the subcontractor

Ending it

- Term of the agreement and what ends it: no award, award to someone else, a stated date, cancellation of the solicitation
- Termination for cause and the notice period
- What survives termination: confidentiality, non-solicitation, and ownership of proposal material
- Dispute resolution and governing law

Housekeeping

- Independent contractor language, no partnership or joint venture created, unless a joint venture is actually the intent, which is a different structure with its own rules and its own attorney conversation
- No authority to bind the other party
- Assignment and change of control
- Notices, signatures, and who is authorized to sign for each party

## Step 5, information-sharing and NDA points

Classify the material before sharing it:

- A public solicitation and its public attachments can be shared without pretending an NDA makes them confidential. Cite the public source. FAR 5.102 addresses public availability: https://www.acquisition.gov/far/5.102 .
- Proprietary proposal material, rates, partner past performance, resumes, customer contacts, and nonpublic business information need owner consent and an appropriate NDA before sharing.
- Controlled Unclassified Information, controlled-access portal material, export-controlled data, and classified information follow the solicitation's access and handling rules. An NDA alone does not authorize access or transmission. Stop and require the user's security, legal, or contracting review.

When proprietary material will be exchanged, cover:

- What is confidential: restricted solicitation material, the proposal, pricing, rates, technical approach, customer contacts, and the fact of the teaming discussion itself
- Mutual, not one way, because both sides are handing over rates and past performance
- Duration, and a longer or indefinite term for anything that is a trade secret
- Permitted use limited to this opportunity, named by solicitation number
- Who inside each company may see it, and the obligation to bind those people
- Return or destruction on request, and what may be retained for legal record keeping
- No license granted to anything
- Government and legal disclosure carve-outs, with notice to the other party where allowed
- Whether the partner may disclose the existence of the team to anyone, including the customer

## Step 6, what must be settled before the proposal goes out

Produce a dated list, working backwards from the proposal deadline, with owners:

- NDA signed before proprietary material is exchanged, and documented authorization before any controlled material is shared
- Teaming agreement signed with every partner named in the proposal, or a letter of commitment if that is what the solicitation requires
- The workshare final, and the limitations on subcontracting check clean and written down
- Partner documents received: capability statement, insurance certificate, past performance write-ups, resumes, W-9, rates in the pricing format, certification evidence
- Partner exclusions check done and the date recorded
- Consent obtained to use the partner's name and past performance
- Pricing built with the partner's actual rates, not placeholders
- Every partner-owned section of the proposal delivered to the prime with time left to edit it
- If a small business subcontracting plan is required, who writes it and when

Anything on this list without a date and an owner is the thing that will be missing at midnight.

## Rules

- Never state a limitations on subcontracting percentage as settled fact. Cite the clause in this solicitation and 13 CFR 125.6 and tell the user to verify both.
- Never mark a partner similarly situated without saying what evidence that rests on and when it was checked.
- Never write a teaming agreement or an NDA as an executable document and present it as ready to sign. Produce the checklist and the points, and say that a contracts attorney reviews the agreement. This is not legal advice.
- Never invent a partner, a rate, a percentage, a scope commitment, or a signature date.
- Never send anything to a partner. Draft it; the user sends it.
- If the workshare plan is non-compliant, say so first, before anything else in the answer, and do not draft around it.

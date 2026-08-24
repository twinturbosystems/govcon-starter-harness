---
name: teaming
description: Prepare the teaming approach for one opportunity. Sets the workshare split, checks it against the limitations on subcontracting for a set-aside, produces a teaming agreement checklist and the NDA points, and lists everything that must be settled before the proposal goes out. Use when the user is deciding who does what share, or is about to sign a teaming agreement.
user-invocable: true
allowed-tools: Read, Write, Edit
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

One row per piece of scope. Percentages of the total contract value, and separately of the total labor where the two differ, because on a services contract the cap is usually measured against the amount paid rather than against headcount, and confusing the two is how plans go wrong quietly.

| Scope | PWS ref | Performed by | Similarly situated? | Percent of value | Percent of labor | Basis for the estimate |
|---|---|---|---|---|---|---|

A similarly situated entity is a subcontractor that is itself small under the NAICS code assigned to this contract and holds the same set-aside status the prime is bidding under, for example another SDVOSB on an SDVOSB set-aside. Mark each partner yes, no, or unverified, and never mark one yes on the partner's say-so alone; note what evidence it rests on and the date it was checked.

Then total three numbers: self-performed, similarly situated subcontractors, everyone else.

## Step 3, the limitations on subcontracting check

This is the step this whole skill exists for. Run it every time the contract is a set-aside.

Explain it plainly to the user before you check it, in something close to these words.

When a small business wins a set-aside contract, it cannot simply pass the work through to other companies and keep a margin. Federal rules at 13 CFR 125.6 cap how much of the amount paid under the contract may go to subcontractors that are not similarly situated entities. Work performed by a similarly situated subcontractor does not count against that cap. Work performed by anyone else does. The cap is a percentage, and the percentage is different for services, for supplies, for general construction, and for construction by special trade contractors.

Then do this, in order, and do not skip a step:

1. Find the limitations on subcontracting clause in this solicitation, usually FAR 52.219-14. Quote what the solicitation itself states: the percentage, and the contract type it applies to.
2. Confirm it against 13 CFR 125.6, which is the controlling authority. If the clause in the solicitation and the regulation appear to disagree, or the solicitation is silent on it, tell the user to ask the contracting officer in writing before bid rather than assuming either way.
3. Establish which contract type applies here, because the number is meaningless without it. If the solicitation mixes services and supplies, say so, and say that the treatment of a mixed contract is a question for the contracting officer.
4. Compare the planned split from step 2 against what the clause states.

Never state the percentage from your own memory as settled fact, and never let the user proceed on a figure you supplied without sending them to those two sources.

Then say the result in one line, at the top of the answer, in plain words. One of:

- The plan looks compliant against the clause as written in this solicitation, with the arithmetic shown, and the user should still confirm the clause text themselves.
- The plan looks non-compliant. Say by roughly how much, and say it before anything else in the answer.
- The check cannot be completed. Say exactly what is missing: the clause, the contract type, or a partner's similarly situated status.

If the plan looks non-compliant, give the two fixes and price both:

1. Move real, priced scope back to the prime. Name which scope, say who would do it, and say what it changes in the staffing and the price. Scope moved back on paper without a person behind it is not a fix, it is a bigger problem later.
2. Replace non-similarly-situated subcontractors with similarly situated ones for some or all of that scope. Name what the search costs in time against the deadline, and say what happens if it is not found.

If neither fix is achievable with the partners available and the time left, say so plainly and send the user back to `/bid-no-bid`, because this is a no-go and it is better found now.

Two more things to say when they apply. Compliance is measured over the period the clause specifies, not on a single invoice, so a plan that averages out has to be shown to average out, and the workshare has to be tracked during performance and not only proposed. And on a full and open contract with no set-aside this cap does not apply in the same way, though other clauses in the solicitation may still limit subcontracting, so the clause list still has to be read.

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

## Step 5, the NDA points

The NDA comes first, before any solicitation material or proposal content goes to a candidate. Cover:

- What is confidential: the solicitation content where restricted, the proposal, pricing, rates, technical approach, customer contacts, and the fact of the teaming discussion itself
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

- NDA signed with every partner whose material appears in the proposal
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

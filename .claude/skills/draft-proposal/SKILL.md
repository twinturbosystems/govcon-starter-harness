---
name: draft-proposal
description: Draft the technical, management, and past performance volumes against the compliance matrix, in the owner's voice, using only facts that appear in company/profile.md. Anything not in the profile becomes a marked gap rather than a plausible sentence. Written to proposals/<solicitation>/. Use when the user asks to write, draft, or start the proposal.
user-invocable: true
allowed-tools: Read, Write, Edit
argument-hint: [solicitation number, or a volume or section name such as "volume 2" or "the transition plan"]
---

# Draft the proposal

Write the volumes against the compliance matrix, using only what is true.

## Input

$ARGUMENTS: a solicitation number, or a specific volume or section to draft. If empty, ask which opportunity and stop.

## Before you write a word

1. Read `company/profile.md`. If it does not exist, stop and offer `/setup-profile`. There is nothing honest to write without it.
2. Read `proposals/<solicitation-number>/compliance-matrix.md`. If it does not exist, stop and offer `/compliance-matrix`. Drafting before the matrix produces prose that has to be rewritten to fit the required structure, and it is how requirements get missed.
3. Read the pipeline file for the opportunity, including the teaming section, so partner scope is drafted as partner scope.
4. Say in three lines what you are about to draft: which volume, which matrix rows it answers, and which page limit it has to fit.

## The rule that governs everything here

Only facts from `company/profile.md`, from the solicitation, or from something the user tells you in this conversation go into the draft. Nothing else.

That means no invented past performance, contract numbers, customer names, points of contact, dollar values, periods of performance, staff, resumes, degrees, certifications, clearances, facilities, tools, methodologies the company does not use, or metrics.

When a section needs a fact the profile does not have, write the marker in place, keep drafting around it, and collect it at the end:

```
[GAP: reference 2 needs the contract number and the customer POC phone number]
[GAP: no cleared personnel in the profile, and Section L 3.4 requires a named Facility Security Officer]
[GAP: transition timeline needs the incumbent's contract end date, which is not in the solicitation]
```

A marker is better than a placeholder that reads like a fact, because a placeholder survives a copy edit and a marker does not.

If the user asks you to invent something so a section reads better, decline in one sentence and say why: a fabricated past performance reference in a federal proposal is a false statement to the government, and it is the kind of thing that ends a company rather than costing it one award. Then offer the two honest paths. Use a real reference that fits less well and spend a paragraph explaining the relevance, which evaluators accept far more often than people expect. Or leave the gap marked and go get the real facts, which for a POC phone number is usually one email.

## Volume 1, technical

Write to the matrix rows assigned to this volume, in the order the instructions require, using the instruction's own section numbering so an evaluator can follow it without hunting.

For each requirement:

- Say what the company will do, specifically. Name the step, the sequence, the frequency, and who does it.
- Then say how it is done, at the level of detail the evaluation factor asks for and no more. A factor that asks for an approach gets an approach; padding it with philosophy loses pages that a later factor needs.
- Then say what the customer sees as a result, because that is the sentence an evaluator remembers.
- Where a risk is real, name it, then name the mitigation. Three real risks with real mitigations beat ten generic ones.

Two things that consistently separate a small company's technical volume from a template. A transition plan with dates measured from award, day one, week one, day thirty, day ninety, with a named owner per milestone. And a staffing approach that says who is on staff today, who is contingent on award, and how a vacancy gets filled, because evaluators know that a three-person company is a three-person company and respect a plan more than a claim.

Where scope is subcontracted, say so plainly and name the partner if a teaming agreement is signed, or write `[GAP: partner not yet signed for this scope]` if it is not. Do not describe partner-performed work as though the prime performs it. That is both a credibility problem and, on a set-aside, a limitations on subcontracting problem.

## Volume 2, management

Cover, in the order the instructions require:

- Organization and lines of authority, with an organizational chart described in text so it can be drawn later. Say who has the authority to commit the company.
- Key personnel: named where the profile names them, with real qualifications only. Where a position is required and the profile has nobody, write the marker and describe the recruiting approach and the qualification standard, which is an honest answer to a real situation.
- The subcontracting and teaming approach: who does what scope, at what share, and how the prime manages them. State the workshare in the same terms the teaming section of the pipeline file uses.
- Quality control: what gets checked, by whom, how often, and what happens when something fails. Tie it to the quality assurance surveillance plan if the solicitation has one.
- Communication and reporting: what the customer receives, how often, and who the single point of contact is.
- Risk management, phase-in and phase-out, and the plan for the last thirty days of the contract, which almost nobody writes and evaluators notice.

If this is a set-aside and the volume describes the workshare, add the limitations on subcontracting check before you finish the volume. Compare the described split against the clause in the solicitation, usually FAR 52.219-14, and against 13 CFR 125.6 as the controlling authority. Do not state the percentage from memory. If the plan as written looks non-compliant, stop drafting that section, say so, and send the user to `/teaming` to fix the split first, because the fix changes the price and the staffing and there is no point drafting around it.

## Volume 3, past performance

Use only the references in the profile.

For each one, write to the solicitation's own format if it specifies one, and otherwise: customer and contract identification, whether the company was prime or subcontractor, value, period of performance, a description of the work, and then the part that carries the volume, which is relevance.

Relevance is an argument, not a claim. Write it as a comparison against what the solicitation asks for: same scope, same size, same complexity, same customer type, same contract type. Say where it matches and say where it does not, because an evaluator who spots an overstated match discounts the whole volume, and an honest limitation followed by a mitigating fact reads as confidence.

Handle these situations directly rather than writing around them:

- Fewer references than required. Say how many the company has, present them, and address the shortfall in the way the solicitation allows, if it allows one. Do not pad with a reference that is not relevant.
- Subcontract experience. Label it as a subcontract and say what portion of the effort the company held.
- Commercial rather than federal work. Label it as commercial and argue the relevance on scope and complexity.
- Partner past performance. Only usable if the solicitation permits it, so check the instructions first, and label whose it is. Never present a partner's reference as the company's own.
- No past performance at all. Say so plainly in the volume, note that a company with no record is normally rated neutral rather than unfavorably where the solicitation says so, cite the solicitation's own language on that if it has any, and if it does not, mark it as a question for the contracting officer.

Also draft the past performance questionnaires or reference letters if the solicitation requires them, filled with real data only, ready for the user to send. The user sends them. Where the solicitation requires the reference to send the questionnaire directly to the government, say so and give the user the steps and the deadline.

## Voice

Read the voice section of the profile and write in it. If the profile names phrases the owner never wants to see, do not use them anywhere, including in headings.

Defaults if the profile says nothing:

- Short sentences. Active voice. The company as "we".
- Specific over impressive. A date, a frequency, a name, or a number beats an adjective every time.
- No hype words, no exclamation marks, no emojis, no bold inside sentences, no em-dashes.
- Do not restate the requirement back before answering it. Answer it, and cite the requirement ID in a comment or a cross reference table instead.
- Every claim is either supported by something in the profile or is marked as a gap.

## Output

For each volume drafted, write `proposals/<solicitation-number>/volume-N-<name>.md` containing:

1. A header with the solicitation number, the volume name, the page limit, and the matrix rows this volume answers.
2. The draft itself, in the required section numbering.
3. A cross reference table at the end: requirement ID, section of this volume that answers it, and status.
4. The gap list for this volume.

Also maintain `proposals/<solicitation-number>/gaps.md` as the single collected list across all volumes, in priority order, with what each gap needs and who can supply it.

In the conversation, give them: the file paths, an honest note on length against the page limit, the three gaps that block finishing, and the next volume to draft.

## Rules

- Only facts from the profile, the solicitation, or this conversation. Everything else is a marked gap.
- Never invent a metric, a percentage, an award, a certification, a tool, or a customer quote.
- Never claim compliance with a standard, a framework, or a regulation that the profile does not evidence.
- Never answer a representation or certification inside a volume.
- Never describe subcontracted work as self-performed.
- Do not exceed a page limit and then note it. Write to fit, and say what you cut.
- If asked to draft a cover letter or a transmittal, draft it for the user to send. Do not send anything.

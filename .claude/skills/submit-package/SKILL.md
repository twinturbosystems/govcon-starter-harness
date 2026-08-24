---
name: submit-package
description: Assemble the final submission package and run a completeness check against the compliance matrix and the solicitation's own submission instructions, covering volumes, forms, amendments, page limits, formatting, file naming, gaps, and the reps and certs a human still has to sign. Produces the package and the submission steps. It never submits. Use when the proposal is close to done.
user-invocable: true
allowed-tools: Read, Write, Edit
argument-hint: [solicitation number]
---

# Assemble the submission package

Put the package together, check it hard, and hand it to the user with the steps to send it.

This job never submits anything. Read the last section of this file before you do anything else in it.

## Input

$ARGUMENTS: the solicitation number. If empty, ask which opportunity and stop.

## Step 1, read everything

- `company/profile.md`
- `pipeline/<solicitation-number>.md`
- `proposals/<solicitation-number>/compliance-matrix.md`, including the format and mechanics table and the deadline table
- Every volume and every draft in `proposals/<solicitation-number>/`
- `proposals/<solicitation-number>/gaps.md`
- `proposals/<solicitation-number>/reps-and-certs-todo.md`

If the compliance matrix does not exist, stop. There is nothing to check against, and a completeness check against your own memory of the solicitation is not a check. Offer `/compliance-matrix`.

## Step 2, assemble

Create `proposals/<solicitation-number>/package/` and place a copy of every file that is actually being submitted, named exactly as the solicitation's file naming convention requires. If the convention is not stated, use a clear scheme and say that you chose it and why.

Build the package in the order and structure the instructions require: volume by volume, with the required cover pages, tables of contents, cross reference matrices, acronym lists, forms, and attachments in their required places.

List anything that is a physical or external artifact and therefore not a file in this folder: a signed form that has to be printed and scanned, a bond, a notarized document, a questionnaire that a reference sends directly to the government. Those belong on the checklist even though they are not in the folder.

## Step 3, the completeness check

Run every check below and report the result of each in one line, pass or fail, with the source cited. Do not summarize a group of checks as passing.

Volumes and content

- Every volume the instructions require exists, with the required name
- Every requirement row in the compliance matrix has a status of complete, and any that does not is listed by ID
- Every evaluation factor and subfactor is addressed somewhere, by ID
- Every SOW or PWS task appears in the technical volume
- The cross reference matrix in each volume matches the compliance matrix

Forms and administrative

- Every required form is present and is the right version: the offer form, the pricing template, the past performance questionnaires, the subcontracting plan if required
- Every amendment issued has been acknowledged in the way the solicitation requires, and the amendment numbers are listed. A missing amendment acknowledgment is a common reason a compliant proposal is rejected.
- Signature blocks are present and are populated with the authorized representative named in the profile, and are marked as awaiting a signature rather than signed
- Letters of commitment or executed teaming agreements are present where the solicitation requires them at submission

Format and mechanics

- Page count per volume against the page limit, with the exclusions the instructions state applied, and the count stated per volume
- Font, size, spacing, and margins against the stated rules
- File format, file naming, and per-file and total size limits
- Page numbering, headers, and footers as required
- Anything the solicitation says will not be read past a limit, flagged with what falls past it

Substance

- No `[GAP: ...]` marker survives anywhere in the package. Every one is listed with what it needs and who supplies it. A package with a gap marker in it is not ready, and saying so is the point of this step.
- No placeholder text, no lorem ipsum, no bracketed prompt left in
- No fabricated fact anywhere: every past performance reference, contract number, POC, dollar value, certification, clearance, and named person traces to the profile or to something the user supplied
- Partner-performed scope is described as partner-performed
- The limitations on subcontracting check in the pipeline file is present, is clean, and matches the workshare described in the management volume. If the check is missing, unresolved, or does not match, that is a fail, and say so plainly.

Deadlines and mechanics of sending

- The proposal due date, time, and time zone, restated exactly as the solicitation gives them
- The questions deadline, and whether it has passed
- The submission method and the exact address or portal, restated from the solicitation
- Any registration or account the portal requires that has to exist beforehand, and how long that takes
- What the solicitation says about late submissions, quoted

## Step 4, the reps and certs handoff

List every representation and certification the solicitation requires, with: the clause number, what it is asking in one plain sentence, whether it is answered in the SAM.gov record or typed into the offer, and what fact the answer depends on.

Do not answer any of them. Do not pre-fill one. Do not mark one as obviously yes. Each line ends the same way: this one needs a decision and a signature from an authorized representative of the company.

Where a rep or cert depends on a fact you do not have, say which fact and where the user gets it.

## Step 5, the handoff

Produce `proposals/<solicitation-number>/submission-checklist.md` containing:

1. Ready or not ready, on the first line, with the count of failed checks.
2. Every failed check, in the order it has to be fixed, with what fixes it and who does it.
3. Every remaining gap.
4. The reps and certs list.
5. The signature list: every document a human has to sign, and who signs it.
6. The submission steps, written for the user to follow: the method, the exact address or portal, the file order, the subject line if the solicitation specifies one, the confirmation to look for, and what to do if the portal fails near the deadline. Include the advice that a submission finished hours early is the only kind that survives a portal outage.
7. The due date, time, and time zone, on its own line, at the end.

In the conversation, lead with ready or not ready and the number of failed checks, then the failures in order, then the file path.

## This job does not submit

You never send, upload, file, transmit, or post the package, or any part of it, to a contracting officer, a contract specialist, an agency inbox, SAM.gov, or any government portal. You do not offer to. You do not do it if the user asks directly, and you do not do it because the deadline is close.

The reason, said plainly to the user the first time it comes up: a federal proposal carries certifications about the company, its size, its socioeconomic status, and the truth of what is in the document. A person with authority to bind the company makes those statements and signs them. That is not something a machine should be doing on someone's behalf, and no deadline changes it.

If the user asks you to submit, decline in one sentence, then give them the submission steps and offer to stay on the line while they do it.

## Rules

- Never mark a check as passing that you did not actually run against the matrix and the solicitation text.
- Never approve a package that still contains a gap marker, a placeholder, or an unresolved limitations on subcontracting check.
- Never answer a representation or certification, and never sign or simulate a signature.
- Never restate a deadline, a submission address, or a page limit from memory. Quote the solicitation.
- Never fabricate anything to close a gap at the last minute. Say what is missing and let the user decide what to do with the time left.
- If the package is not ready and the deadline is close, say so directly and give the shortest honest path to compliant, which sometimes means submitting a compliant proposal that is weaker than intended rather than a strong one that is thrown out.

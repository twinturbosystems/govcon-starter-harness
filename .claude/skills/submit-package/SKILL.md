---
name: submit-package
description: Assemble the final submission package and run a completeness check against the compliance matrix and the solicitation's own submission instructions, covering volumes, forms, amendments, page limits, formatting, file naming, gaps, incorporated annual representations, and any offer-specific human answers, certifications, or signatures. Produces the package and the submission steps. It never submits. Use when the proposal is close to done.
user-invocable: true
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

Create `proposals/<solicitation-number>/package/` and a package manifest. For text files, create the required package copies. For an existing binary document such as DOCX or PDF, do not claim to copy, convert, or repair it unless the user reviews and approves an exact local operation naming the source and destination. Never modify the only copy. Name files exactly as the solicitation requires. If no convention is stated, use a clear scheme and label it as the kit's choice rather than a government requirement.

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

Format and mechanics, human rendered-document gate

Do not mark a DOCX or PDF mechanically compliant from its text, filename, or source markup. The authorized human must open every final document in the viewer used for submission and record pass or fail for:

- Page count per volume against the page limit, applying only the exclusions the instructions state
- Font, size, spacing, margins, page numbering, headers, footers, tables, images, and page breaks
- File format, file naming, and per-file and total file-size limits
- Legibility at normal zoom, correct redactions, working links if required, and no tracked changes or comments
- Anything the solicitation says will not be read past a limit, including what falls past it

You may prepare the checklist and compare values the tools can actually read. You may not convert “not mechanically verified” into a pass. The package remains not ready until the user records that they opened and visually checked each rendered final file.

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
- The standard FAR 52.204-7 active-at-offer-and-award rule, any FAR 4.1102 exception, Alternate I's as-soon-as-possible offer path, FAR 52.204-13(b)'s post-award deadline only when the awardee was unable to register before award, and the FAR 52.204-13(c) maintenance duty. Sources: https://www.acquisition.gov/far/4.1102 , https://www.acquisition.gov/far/52.204-7 , and https://www.acquisition.gov/far/52.204-13 .
- What the solicitation says about late submissions, quoted

## Step 4, the reps and certs handoff

List every representation and certification the solicitation requires, with: the clause number, what it asks in one plain sentence, whether an annual SAM representation is incorporated by reference or a solicitation-specific fill-in is required, what fact the answer depends on, and what human review, certification, or signature the solicitation requires.

Do not answer any of them. Do not pre-fill one. Do not mark one as obviously yes. Annual SAM representations are not each separate signature lines. The authorized representative confirms that incorporated SAM representations are current and makes any solicitation-specific answers, signatures, or certifications actually required. Sources: https://www.acquisition.gov/far/4.1201 , https://www.acquisition.gov/far/52.204-8 , and https://www.acquisition.gov/far/52.212-3 .

Where a rep or cert depends on a fact you do not have, say which fact and where the user gets it.

## Step 5, the handoff

Produce `proposals/<solicitation-number>/submission-checklist.md` containing:

1. Ready or not ready, on the first line, with the count of failed checks and human gates still open.
2. Every failed check, in the order it has to be fixed, with what fixes it and who does it.
3. Every remaining gap.
4. The reps and certs list.
5. The human action list: every document that requires a signature or certification, who handles it, and the rendered-document verification for every final DOCX or PDF.
6. The submission steps, written for the user to follow: the method, the exact address or portal, the file order, the subject line if the solicitation specifies one, the confirmation to look for, and what to do if the portal fails near the deadline. Include the advice that a submission finished hours early is the only kind that survives a portal outage.
7. The due date, time, and time zone, on its own line, at the end.

In the conversation, lead with ready or not ready and the number of failed checks, then the failures in order, then the file path.

## This job does not submit

You never send, upload, file, transmit, or post the package, or any part of it, to a contracting officer, a contract specialist, an agency inbox, SAM.gov, or any government portal. You do not offer to. You do not do it if the user asks directly, and you do not do it because the deadline is close.

The reason, said plainly to the user the first time it comes up: an offer may incorporate representations and may require certifications or signatures by a person authorized to bind the company. The kit prepares the package and points to each human action. It does not make those statements or submit on the company's behalf.

If the user asks you to submit, decline in one sentence, then give them the submission steps and offer to stay on the line while they do it.

## Rules

- Never mark a check as passing that you did not actually run against the matrix and the solicitation text.
- Never approve a package that still contains a gap marker, a placeholder, or an unresolved limitations on subcontracting check.
- Never call a package ready until the user records the rendered-document gate as passed for every final DOCX or PDF.
- Never answer a representation or certification, and never sign or simulate a signature.
- Never restate a deadline, a submission address, or a page limit from memory. Quote the solicitation.
- Never fabricate anything to close a gap at the last minute. Say what is missing and let the user decide what to do with the time left.
- If the package is not ready and the deadline is close, say so directly and give the shortest honest path to compliant, which sometimes means submitting a compliant proposal that is weaker than intended rather than a strong one that is thrown out.

---
name: compliance-matrix
description: Build the compliance matrix for one solicitation from Sections L and M and the SOW or PWS, mapping every instruction and every evaluation factor to the volume, section, and page where it will be answered, plus format rules, submission mechanics, and a coverage check for requirements with no home. Written to proposals/<solicitation>/compliance-matrix.md. Use when the user pastes or attaches a solicitation, an RFP, an RFQ, or an RFI and wants the matrix.
user-invocable: true
argument-hint: [paste or attach the solicitation, or give the path to it, or the solicitation number already in pipeline/]
---

# Compliance matrix

The compliance matrix is the single most valuable artifact in a proposal. It is the thing that stops a good bid from being thrown out for a mechanical reason, it tells the writer exactly what to write, and it is what the evaluator effectively grades against. Build it thoroughly and build it first. Everything else in the proposal is written against it.

## Input

$ARGUMENTS: the solicitation, pasted or attached, or a path to it, or a solicitation number already tracked in `pipeline/`. If empty, ask for the document and stop. Do not build a matrix from a notice summary and call it a matrix; say plainly that the summary is not enough and ask for the solicitation and its attachments.

## Step 1, inventory the document set

Before extracting anything, list what you actually have and what is missing.

1. Name every file you were given, and what each one is: the solicitation body, the SOW or PWS or SOO, the attachments, the wage determination, the pricing worksheet, the past performance questionnaire form, the amendments.
2. Identify the format, because it changes where the instructions live:
   - Uniform contract format, Sections A through M. Instructions are in Section L, evaluation in Section M, the work in Section C, deliverables in Section F, special requirements in Section H, clauses in Section I, reps and certs in Section K.
   - A commercial item solicitation under FAR Part 12. Instructions come from FAR 52.212-1 and any addendum to it, evaluation from FAR 52.212-2 or a stated alternative, and reps and certs from FAR 52.212-3. There may be no Section L or M at all, and an addendum can move the real instructions somewhere unexpected.
   - A combined synopsis and solicitation, where all of it is compressed into one notice and the instructions can be a single paragraph.
   - A request for quotation under FAR Part 13, or a task order request against an existing vehicle, where the vehicle's own terms also apply.
3. Check for amendments. Every amendment can change requirements, dates, page limits, and attachments, and an amendment usually has to be acknowledged in the offer itself. If any amendment number in the series is missing, say so and ask for it before you build the matrix. Note the acknowledgment requirement as its own matrix row.
4. Say plainly what is missing. A matrix built on a partial document set will be missing requirements, and a missing requirement is exactly the failure mode this artifact exists to prevent.

## Step 2, extract the instructions

Go through the instructions section, or FAR 52.212-1 with its addendum, line by line. Do not summarize a paragraph into one row when it contains three obligations.

Capture every requirement, which means every sentence containing shall, must, will, is required to, offerors are to, the offeror shall provide, submit, include, describe, demonstrate, identify, address, or provide. Also capture:

- Volume structure: how many volumes, what each is called, what goes in each
- Page limits, per volume and per section, and what is excluded from the count, for example resumes, cover letters, tables, appendices
- Format rules: font family and size, line spacing, margins, paper size, header and footer content, page numbering, whether graphics text has a separate minimum size
- File requirements: file format, file naming convention, maximum file size, whether files must be separate or combined, whether a single PDF is required
- Required forms: SF 1449, SF 33, SF 30 for amendments, the pricing template, the past performance questionnaire, the subcontracting plan form
- Required content by name: cover letter, executive summary, table of contents, acronym list, cross reference matrix, letters of commitment, resumes and their format, organizational chart, transition plan, quality control plan, safety plan
- Past performance rules: how many references, how recent, what counts as relevant, whether subcontractor and affiliate performance is allowed, whether questionnaires go directly from the reference to the government
- Key personnel: which positions, minimum qualifications, whether letters of intent are required, whether resumes count against the page limit
- Pricing instructions, including which CLINs to price, whether option periods are priced, rounding, and where price goes
- Deadlines: proposal due date, time, and time zone; questions due date and method; site visit dates; oral presentation dates
- Submission mechanics: portal or email, the exact address, size limits, whether an email confirmation is required, what happens to a late submission
- Anything conditional: requirements that apply only to small businesses, only to large businesses, only if teaming, only if proposing a subcontracting plan
- SAM registration timing: the standard FAR 52.204-7 offer-and-award rule, any FAR 4.1102 exception, Alternate I's as-soon-as-possible offer path, FAR 52.204-13(b)'s post-award deadline only when the awardee was unable to register before award, and the FAR 52.204-13(c) maintenance duty
- Program eligibility provisions for the named small-business set-aside, including the required certification or pending-application state and whether it is tested at initial offer, award, or both
- FAR 52.219-14 applicability and calculation details, and for supplies any FAR 52.219-33 nonmanufacturer requirement or waiver

Give every requirement a stable identifier tied to its source, for example `L-3.2.1-b`, so a writer can find it in the document in seconds.

## Step 3, extract the evaluation factors

From the evaluation section, or FAR 52.212-2 with its addendum, capture:

- Every factor and subfactor, by name and number
- The relative importance the solicitation states: which factors are more important than which, whether the non-price factors combined are significantly more important, approximately equal, or less important than price, and any stated adjectival rating scale
- The basis of award as stated: lowest price technically acceptable, best value tradeoff, highest technically rated with a fair and reasonable price, or something else
- What each factor says it is looking for, quoted rather than paraphrased where the wording is specific
- Any stated go or no-go gate, for example acceptability thresholds a proposal must pass before anything else is evaluated
- Whether the government intends to award without discussions
- Any stated page or content that will not be evaluated

Give each one an identifier, for example `M-2.1`.

## Step 4, extract the work

From the SOW, PWS, SOO, or Section C, capture every task, subtask, deliverable, performance standard, and acceptance criterion. From Section F, capture delivery dates and periods of performance. From Section H, capture special contract requirements, which is where things like key personnel substitution rules, security requirements, and government furnished property usually sit.

For a performance work statement, capture the performance requirements summary or quality assurance surveillance plan if there is one, because those are the standards the work is actually measured against.

Give each one an identifier, for example `PWS-3.4`.

## Step 5, cross-map

This is the step that makes the matrix worth building.

1. Map every instruction to the evaluation factor it feeds. An instruction that no factor evaluates still has to be complied with; mark it "compliance only". A factor with no matching instruction is a warning sign, and it usually means the response has to be built somewhere the instructions did not name. Flag it and say so.
2. Map every SOW or PWS task to the volume section that will address it. A task that appears in no volume is the most common way a technically capable company loses on a technical factor.
3. Assign each row a home: volume, section number, and target page or page range. This is what turns the matrix into an outline.
4. Assign an owner for each row. In a company of one that is the owner for everything except the rows that belong to a teaming partner, and those need naming, because a partner-owned row with no name is a row that arrives late.
5. Set a due date per row, working backwards from the proposal due date, with the partner-owned rows due earliest.

## Step 6, the coverage check

Before you output anything, run these checks and report the result of each in one line:

- Every M factor and subfactor has at least one L instruction and at least one proposal section that answers it
- Every L instruction has a home in a volume and a section
- Every PWS or SOW task appears in at least one row
- Every required form and attachment appears as a row
- Every page limit has a section that it applies to
- Every deadline is captured with its time and time zone
- Every amendment has an acknowledgment row
- The volume structure in the matrix matches the volume structure the instructions require, in name and in count

Any check that fails becomes an open item at the top of the file, not a footnote.

## Step 7, reps and certs, flagged and not answered

Pull every representation and certification the solicitation requires, for example those at FAR 52.204-8 or FAR 52.212-3, and list them separately in `proposals/<solicitation>/reps-and-certs-todo.md`.

For each one: the clause number, title, what it asks in one plain sentence, whether an annual SAM representation is incorporated by reference or a solicitation-specific fill-in is required, what fact the answer depends on, and what human review, certification, or signature the solicitation actually requires.

Do not answer any of them. Do not suggest an answer or mark one as obviously yes. Annual SAM representations are not each separate signature lines. The authorized representative confirms that incorporated SAM representations are current and completes the answers, certifications, or signatures the solicitation requires. Sources: https://www.acquisition.gov/far/4.1201 , https://www.acquisition.gov/far/52.204-8 , and https://www.acquisition.gov/far/52.212-3 . Where an answer depends on a fact you do not have, say which fact.

## Output

Write `proposals/<solicitation-number>/compliance-matrix.md`, creating the folder if needed, containing:

1. A header: solicitation number, title, agency, NAICS, set-aside, contract type, proposal due date with time and time zone, questions due date, and the list of documents the matrix was built from, including amendment numbers.
2. Open items: everything the coverage check flagged, and every document you did not receive.
3. The matrix itself:

| ID | Source | Requirement | Type | Evaluated under | Volume | Section | Page | Owner | Due | Status |
|---|---|---|---|---|---|---|---|---|---|---|

Type is one of: instruction, evaluation, technical, administrative, format, form, pricing, deadline. Status starts at "not started" for every row.

4. A separate format and mechanics table: page limits per volume, font, spacing, margins, file naming, file format, maximum file size, submission method and address, and what the solicitation says about late submissions.
5. A separate deadline table, in date order, with times and time zones.
6. A proposal outline generated from the matrix: the volumes, their sections in order, and the requirement IDs each section answers. This is what `/draft-proposal` writes against.
7. The reps and certs list, or a pointer to `reps-and-certs-todo.md`.
8. Every `[GAP: ...]` collected in one list.

In the conversation, give them: the file path, the count of rows by type, the open items, the closest deadline, and the three rows most likely to be missed, which are usually a form nobody reads, a page limit exclusion, and a partner-owned document.

## Rules

- Quote the requirement or paraphrase it tightly, and always cite section and paragraph. A row without a source is not usable.
- Never invent a requirement, a page limit, a font rule, a deadline, a factor, or a weight. If the solicitation does not say, the cell says "not stated" and it becomes a question to the contracting officer.
- Never drop a requirement because it seems minor. The mechanical ones are what get proposals thrown out.
- Never answer a representation or certification.
- Where the solicitation is ambiguous, say so, put it in open items, and draft the question for the user to submit before the questions deadline.
- If the user gives you only a notice summary, say plainly that a real matrix needs the solicitation and its attachments, and offer to build a partial matrix marked as partial.

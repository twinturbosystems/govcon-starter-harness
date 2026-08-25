# Contractor profile

Fill this in once. Short answers are fine. Every job in this kit reads this file before it produces anything, and the drafting job will only use facts that appear here.

Two rules for filling it in. Write only what is true and what you could show a contracting officer if asked. Leave anything you do not have blank or marked `[GAP: ...]`, because a blank is honest and a guess is a false statement waiting to be signed.

Copy this file over `profile.md` when you are ready to start, or run `/setup-profile` and let the interview write it for you.

---

## Identity and registration

| Field | Value |
|---|---|
| Legal entity name (exactly as registered) | |
| Doing business as, if any | |
| Entity type (LLC, S-corp, C-corp, sole proprietor) | |
| State and year of formation | |
| Unique Entity ID (UEI), 12 characters | |
| CAGE code | |
| SAM.gov registration status (active, submitted, expired, not started) | |
| SAM registration expiration date | |
| Employer Identification Number on file with SAM (yes or no, do not write the number here) | |
| Authorized representative who signs offers (name and title) | |

If SAM registration is not active, nothing else in this file matters yet. Registration is free at https://sam.gov and you do it yourself. Do not pay a third party.

## NAICS codes

One row per code you actually market under. The size standard is the SBA figure for that specific code, either an employee count or average annual receipts, and it is what determines whether you count as small on a contract assigned that code. Look each one up in the SBA table of size standards and write the figure and the date you checked it.

| NAICS | What it covers | Size standard | Small under it? | Primary? |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Size standards checked on: [date]

## Socioeconomic status (self-reported)

Write only what you hold today, and how it is evidenced. This kit treats every line here as your own report of your status, not as verification of it. Certified programs are verified by the certifying body, not by you and not by this file.

| Program | Status | Certified or self-certified | Certifying body | Certificate or approval date | Expiration |
|---|---|---|---|---|---|
| Small business | | | | | |
| 8(a) Business Development | | | | | |
| SDVOSB or VOSB | | | | | |
| WOSB or EDWOSB | | | | | |
| HUBZone | | | | | |
| Other (state or agency programs) | | | | | |

Notes on anything in progress, including application dates:

## Capabilities

What you actually deliver, in the customer's words rather than yours. For each one, say who does the work: your own staff, a named partner, or a partner you would have to go find.

| Capability | Delivered by | Depth (how many past efforts) | Evidence |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

Things you are asked for often and do not do:

## Past performance

Only real contracts, subcontracts, or commercial work. If you have none yet, write "none yet" and say so; there are honest ways to compete without it, and inventing one is not among them.

### Reference 1

| Field | Value |
|---|---|
| Customer (agency, office, or company) | |
| Prime or subcontractor | |
| Contract or order number | |
| Contract type (FFP, T&M, cost reimbursable, other) | |
| Total value | |
| Period of performance (start and end) | |
| NAICS assigned | |
| What you actually did, three to five sentences | |
| Outcome, with any number you can substantiate | |
| CPARS rating, if rated | |
| Point of contact: name, title, phone, email | |
| Is the POC willing to take a call? | |
| Relevance to what you are chasing now | |

### Reference 2

Copy the table above.

### Reference 3

Copy the table above.

## Key personnel

Only people you can actually put on a contract, with their real credentials. A resume you cannot produce on request does not go here.

| Name | Role | Years relevant experience | Degrees and certifications | Clearance level and status | Available how soon | On staff or contingent hire |
|---|---|---|---|---|---|---|
| | | | | | | |

## Geography

- Where you are located:
- Where you can perform without adding cost:
- Where you can perform with travel or a local hire:
- Where you will not go:
- Do you have a HUBZone-qualifying principal office or employee residency situation? If HUBZone matters to you, write what you actually have:

## Capacity and money

| Field | Value |
|---|---|
| People on staff today | |
| Largest single contract you have delivered, by value | |
| Largest you believe you could deliver | |
| How long you can carry payroll before the first invoice is paid | |
| Line of credit or factoring in place | |
| Accounting system (name it; note whether it has ever been reviewed by DCAA) | |
| Timekeeping system | |

## Bonding and insurance

| Field | Value |
|---|---|
| Bonding capacity, single | |
| Bonding capacity, aggregate | |
| Surety name | |
| General liability limits | |
| Professional liability limits | |
| Workers compensation | |
| Cyber liability | |
| Any coverage you would have to add for a specific pursuit | |

## Clearances and facility security

| Field | Value |
|---|---|
| Facility Clearance (FCL) level, or none | |
| Cage code sponsored under, if applicable | |
| Cleared personnel, by level and count | |
| Ability to sponsor clearances | |
| Cybersecurity posture claimed in SAM, for example a SPRS score if you have one | |
| CMMC status, if relevant to your market | |

## Target agencies and vehicles

- Agencies you are pursuing, in order:
- Offices or program shops inside them where you have a relationship:
- Contract vehicles you hold (GSA MAS, agency IDIQ, BPA):
- Vehicles you are pursuing:
- Set-aside types you can bid today:
Optional, and only if you want `/sync` to filter at the SAM.gov API rather than pulling every set-aside under your NAICS codes and filtering locally. Write the API codes on a line of their own, exactly like this, and `/sync` will read them:

SAM set-aside codes: SBA, SDVOSBC

The codes SAM.gov documents are SBA and SBP for small business, 8A and 8AN, HZC and HZS for HUBZone, SDVOSBC and SDVOSBS, WOSB and WOSBSS, EDWOSB and EDWOSBSS, LAS, IEE, ISBEE, BICiv, VSA and VSS. Check the current list at https://open.gsa.gov/api/get-opportunities-public-api/ before you rely on one, because the kit has not verified them against a live call. Leaving this line out is the cheaper option: it costs fewer API calls and covers more, because every set-aside under your NAICS codes comes down and the filtering happens locally.


## Partner bench

Companies you have worked with, or would team with, and what each one brings. This is what `/find-subs` and `/teaming` start from.

| Company | UEI | What they bring | Size and set-aside status (as they report it) | Similarly situated for which set-asides? | Worked together before? |
|---|---|---|---|---|---|
| | | | | | |

## How you write

Two or three lines describing how you want your proposals to sound, plus anything you always say and anything you never say. If you have a past proposal you liked, note where it is so you can point the drafting job at it.

- Voice:
- Phrases you use:
- Phrases you never use:

## Bid discipline

- Minimum contract value worth bidding:
- Maximum you will spend on a single bid, in hours or dollars:
- Minimum days before a due date that you will still start a bid:
- Types of work you have decided not to chase:

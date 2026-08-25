---
name: find-opps
description: Search the local opportunity database in data/sam.db for notices that fit the contractor profile and shortlist them into pipeline/ files. Searches offline by default and never calls the SAM.gov API for a search, because that API is rate limited to as few as 10 requests per day. Offers /sync when the local data is stale, and keeps the manual path where the user searches sam.gov in a browser and pastes results in for people with no key at all. Use when the user asks to find work, check for new opportunities, or search SAM.
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
argument-hint: [optional: a NAICS code, a set-aside type, an agency, a state, a keyword, or a date range]
---

# Find opportunities

Turn the profile into a search, run it against the local database, and shortlist what actually fits into `pipeline/`.

## The one thing that changed, and why

This job used to call the SAM.gov API for every search. It does not any more. The API is rate limited to 10 requests per day for a non-federal user with no role on an entity registration, and 1,000 per day with a role. A handful of searches would use up a whole day. So the kit keeps a local copy of the notices, refreshed by one small `/sync` a day, and every search after that is free, instant, and offline.

Searching never calls the API. If the local data is stale, this job says so and offers `/sync`. It does not quietly go and spend a call.

## Input

$ARGUMENTS: optional filters. A NAICS code, a set-aside type, an agency, a state, a keyword, or a date range. If empty, build the search from the profile.

## Step 1, build the search from the profile

Read `company/profile.md` and pull out:

- Every NAICS code marketed under, primary first
- Set-aside types the company can bid today
- Geography where they can perform without adding cost, and where they can perform with travel
- Minimum contract value worth bidding, from the bid discipline section
- The hard stops: bonding, clearance, accounting system, vehicles held. These are filters, not preferences.

State the search you are about to run in three or four lines before you run it, so the user can correct it. For example: NAICS 541519 and 541512, total small business and SDVOSB set-asides plus full and open, Maryland, Virginia, and DC, deadline at least ten days out, active notices only.

## Step 2, pick the path

Three paths. Pick the first one that is actually available, and switch without ceremony if it is not.

### Path A, the local database, which is the normal path

Check whether it exists and how old it is:

```bash
python3 tools/samdb.py status
```

On Windows, `python3` often opens the Microsoft Store instead of running. Use `python` or `py -3` instead, and use the same one in every command. If none of the three answers with a version number, Python 3 is missing:

> Python 3 is not installed on this computer. Install it from https://www.python.org/downloads/ , then run `/find-opps` again. On Windows, tick "Add python.exe to PATH" on the first screen of the installer.

Then read what `status` said and act on it:

- No database yet: say so in one line and offer `/backfill` for history, or `/sync` for the last week. Then go to path C if the user wants results now.
- Synced today or yesterday: go ahead and search.
- Three or more days old: say how old it is, in days, and offer `/sync` in one line. If they say no, search anyway and put the age on the results.
- Never synced, or the coverage line does not include the NAICS codes in the profile: say plainly which codes are covered and which are not, then offer `/sync`. Do not present a search over two NAICS codes as though it covered four.

Now search. Everything below runs offline and costs nothing.

```bash
python3 tools/samdb.py search --from-profile --min-days 10
```

Useful filters, all optional and all combinable:

```bash
--naics 541519 --naics 541512      one or more NAICS codes
--from-profile                     take the NAICS codes from company/profile.md
--set-aside SBA --set-aside SDVOSBC  set-aside code or any part of its description
--state MD --state VA              place of performance
--agency "veterans affairs"        any part of the agency path
--keyword "help desk"              title, description, or solicitation number
--notice-type-filter solicitation  notice type text
--posted-since 2026-07-01          posted on or after
--deadline-before 2026-10-01       deadline on or before
--min-days 10                      only deadlines at least ten days out
--changed-since 2026-08-20         only notices that changed on or after that sync date
--include-inactive                 include cancelled and archived notices
--limit 50                         how many to return, default 25
--json                             machine-readable, for when you want to process it
```

Every result carries three things you must pass on rather than strip: how old the data is, what the database actually covers, and the change history for that notice.

### Path B, the pasted results, for people with no key at all

Use this when there is no api.data.gov key, when the network is not reachable, when the assistant has no shell, or when the user simply wants results now. It is not a lesser path. A lot of good capture work is done this way, and it stays in this kit on purpose.

Walk them through it:

1. Go to https://sam.gov and choose Search, then Contract Opportunities.
2. Set the filters that match the search you stated in step 1: NAICS code, notice type, set-aside, place of performance, and posted date.
3. Set the status filter to active notices only, unless they are researching an incumbent, in which case include awards.
4. Sort by response date so the ones closing soonest are at the top.
5. For each result that looks plausible, copy the notice into the chat: title, solicitation number, notice ID, agency and office, NAICS, set-aside, place of performance, response deadline with the time and time zone, contract type if stated, and the link. Or download the results as a file and attach it.

Then take what they paste and go to step 3. Do not fill in a field they did not paste. If the set-aside type or the response deadline is missing from a pasted result, ask for it, because both are load-bearing in the next step.

### Path C, both

The two paths mix well and nobody has to choose once. Search the local database for what it covers, and use the web search for the codes or the dates it does not. Say which results came from which, so the user knows what was covered by a local search and what was found by hand.

## Step 3, shortlist

Do not hand back everything the search returned. Sort it into three lists and explain each in one line.

Worth a look. Passes all of these:

- NAICS matches a code in the profile, or is close enough that the capability transfers, and the company is small under that code's size standard
- Set-aside type is one the company can bid today, or it is full and open
- Place of performance is somewhere the company said it can perform
- Estimated value, where stated, is above the minimum in the bid discipline section
- Response deadline leaves at least the minimum number of days the profile says they need
- None of the hard stops apply: no bond required when they have no surety, no clearance required when they have no cleared staff, no cost reimbursable work when the accounting system is not ready, no vehicle required that they do not hold

Watch. Fails one thing that could change, and worth tracking anyway. Say which thing. A recompete twelve months out, a vehicle they are applying for, a set-aside they are certifying for.

Not this one. Fails something structural. Say which, in one clause, and move on. This list is short and it is not a lecture.

For anything that is a sources sought or a request for information rather than a solicitation, say so explicitly and treat it differently: it is a chance to shape the requirement and to get on the radar, and it is usually cheap to answer. It is not a bid.

## Step 4, use the change history, because the API cannot give it to you

Every result from the local database carries what changed since the database first saw it. This exists only because the kit snapshots on every sync. The API itself only ever returns the latest active version of a notice, so a caller cannot see what moved. Use it:

- A deadline that already moved once will often move again. Say so when you see it.
- A set-aside that changed from SDVOSB to total small business, or the other way, changes who can bid and changes the workshare maths. Never bury it.
- A notice that has been cancelled, or made inactive, goes on the not this one list with that as the reason.
- A presolicitation that has become a solicitation means the clock is now real.

To see the history on its own, or across everything since a date:

```bash
python3 tools/samdb.py changes --since 2026-08-01
python3 tools/samdb.py changes --notice-id <notice id>
```

## Step 5, write the pipeline files

For each opportunity on the worth a look list, create `pipeline/<solicitation-number>.md` from `pipeline/opportunity.template.md`, replacing any character illegal in a filename with a dash. Fill in only what the notice or the pasted result actually said. Every field the source did not state gets "not stated", never a guess.

Then tell the user, in the conversation:

- One line per shortlisted opportunity: title, agency, set-aside, NAICS, deadline with the time zone, and the file path
- The single closest deadline, called out on its own line
- Any change history that matters, named against the opportunity it belongs to
- Which ones are missing the attachments or the full solicitation document, since the next step needs them
- How old the local data is, in days, and the line that the deadline must be confirmed on SAM.gov before bidding
- One line: run `/bid-no-bid` on the one you care about most

## What this job is honest about, every time

Say these plainly rather than leaving them implied. They are not disclaimers to bury at the end.

- This is a mirror of opportunity notices. It does not hold attachments, statements of work, or amendment documents. Those come from SAM.gov itself, and `/compliance-matrix` needs the real document.
- Coverage is exactly whatever was synced. If two NAICS codes were synced, the database knows two NAICS codes and nothing else. Never present a local search as a complete search of SAM.gov.
- The local copy can be stale. Show its age in days on every set of results.
- This does not replace checking SAM.gov. It makes searching fast and free. SAM.gov is still the authoritative record, and the deadline you bid against is the one on SAM.gov.

## Rules

- Never call the SAM.gov API from this job. Searching is local. If fresh data is needed, offer `/sync` and let the user decide.
- Never print, echo, repeat, or log the api.data.gov key, and never write it into a file under `pipeline/`, `proposals/`, or `data/`.
- Never invent a solicitation number, notice ID, deadline, agency, set-aside type, or contact. If the source did not state it, it is "not stated" and you ask.
- Never state a response deadline without the time and the time zone as the notice gives them, and never convert a time zone.
- Never contact anyone. This job reads a local file and reads what the user pastes. It does not email a contracting officer, register for anything, or submit a response.
- If a search returns nothing, say so plainly and suggest one specific loosening, for example a wider posted date range or a second NAICS code, or `/sync` if the data is old. Do not quietly broaden the search yourself.

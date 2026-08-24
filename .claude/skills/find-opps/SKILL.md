---
name: find-opps
description: Search SAM.gov for opportunities that fit the contractor profile and shortlist them into pipeline/ files. Runs either through the free SAM.gov Get Opportunities API with an api.data.gov key kept in company/.env.local, or, when there is no key or no network, by walking the user through the SAM.gov web search and taking pasted results. Use when the user asks to find work, check for new opportunities, or search SAM.
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
argument-hint: [optional: a NAICS code, a set-aside type, an agency, a state, a date range, or a keyword]
---

# Find opportunities

Turn the profile into a search, run it, and shortlist what actually fits into `pipeline/`.

## Input

$ARGUMENTS: optional filters. A NAICS code, a set-aside type, an agency, a state, a date range, or a keyword. If empty, build the search from the profile.

## Step 1, build the search from the profile

Read `company/profile.md` and pull out:

- Every NAICS code marketed under, primary first
- Set-aside types the company can bid today
- Geography where they can perform without adding cost, and where they can perform with travel
- Minimum contract value worth bidding, from the bid discipline section
- The hard stops: bonding, clearance, accounting system, vehicles held. These are filters, not preferences.

State the search you are about to run in three or four lines before you run it, so the user can correct it. For example: NAICS 541519 and 541512, total small business and SDVOSB set-asides plus full and open, Maryland, Virginia, and DC, posted in the last thirty days, active notices only.

## Step 2, pick the path

There are two paths and both are fine. Pick based on what is actually available, and switch without ceremony if the first one fails.

### Path A, the API

SAM.gov publishes a public Get Opportunities API. It needs a free key from api.data.gov, not from SAM directly.

If `company/.env.local` does not exist, tell the user this, in these words or close to them:

1. Go to https://api.data.gov/signup/ and sign up. It is free, it takes about a minute, and the key arrives by email.
2. In this folder, copy the example file: `cp company/.env.local.example company/.env.local`
3. Open `company/.env.local` in a text editor and paste the key after `SAM_API_KEY=`.
4. Save it. That file is gitignored, so it stays on your machine.
5. Come back and run `/find-opps` again.

Do not ask them to paste the key into the chat, and do not offer to write it into the file for them.

Once the key exists, run the search as a shell command that loads the key inside the command rather than reading it into the conversation. The shape of the request:

```bash
set -a; . ./company/.env.local; set +a
curl -s -G "https://api.sam.gov/opportunities/v2/search" \
  --data-urlencode "api_key=$SAM_API_KEY" \
  --data-urlencode "postedFrom=07/25/2026" \
  --data-urlencode "postedTo=08/24/2026" \
  --data-urlencode "ncode=541519" \
  --data-urlencode "ptype=o" \
  --data-urlencode "limit=100" \
  -o pipeline/.search-results.json
```

On Windows PowerShell, the same thing without a shell that understands `set -a`:

```powershell
$key = (Get-Content company\.env.local | Where-Object { $_ -like 'SAM_API_KEY=*' }) -replace '^SAM_API_KEY=',''
$q = @{ api_key = $key; postedFrom = '07/25/2026'; postedTo = '08/24/2026'; ncode = '541519'; ptype = 'o'; limit = '100' }
Invoke-RestMethod -Uri 'https://api.sam.gov/opportunities/v2/search' -Body $q -OutFile pipeline\.search-results.json
```

Notes on the request, and one honest caveat. The parameter names above are the ones the API has used: `postedFrom` and `postedTo` in MM/dd/yyyy form and usually limited to a range of a year or less, `ncode` for NAICS, `ptype` for notice type, `typeOfSetAside` for the set-aside filter, `state`, `title`, `limit` and `offset` for paging, and `rdlfrom` and `rdlto` for the response deadline. Do not treat that list as permanent. If a call returns an error about a parameter, or returns nothing when you expect results, open the current API documentation at https://open.gsa.gov/api/get-opportunities-public-api/ and use the parameter names it lists today. Say plainly what you changed and why.

Run the smallest useful query first: one NAICS code, one month, so an error costs one call rather than twenty. Then widen. Keys are rate limited, so do not loop through every NAICS code and every set-aside in one pass without telling the user how many calls that will be.

Write the raw response to `pipeline/.search-results.json`, which is already excluded from git, and read it from there rather than pulling the whole response into the conversation.

### Path B, the web search

Use this whenever there is no key, the network is not reachable, the assistant has no shell, or the API is returning errors and the user wants results now. It is not a lesser path; a lot of good capture work is done this way.

Walk them through it:

1. Go to https://sam.gov and choose Search, then Contract Opportunities.
2. Set the filters that match the search you stated in step 1: NAICS code, notice type, set-aside, place of performance, and posted date.
3. Set the status filter to active notices only, unless they are researching an incumbent, in which case include awards.
4. Sort by response date so the ones closing soonest are at the top.
5. For each result that looks plausible, copy the notice into the chat: title, solicitation number, notice ID, agency and office, NAICS, set-aside, place of performance, response deadline with the time and time zone, contract type if stated, and the link. Or download the results as a file and attach it.

Then take what they paste and go to step 3. Do not fill in a field they did not paste. If the set-aside type or the response deadline is missing from a pasted result, ask for it, because both are load-bearing in the next step.

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

## Step 4, write the pipeline files

For each opportunity on the worth a look list, create `pipeline/<solicitation-number>.md` from `pipeline/opportunity.template.md`, replacing any character illegal in a filename with a dash. Fill in only what the notice or the pasted result actually said. Every field the source did not state gets "not stated", never a guess.

Then tell the user, in the conversation:

- One line per shortlisted opportunity: title, agency, set-aside, NAICS, deadline with the time zone, and the file path
- The single closest deadline, called out on its own line
- Which ones are missing the attachments or the full solicitation document, since the next step needs them
- One line: run `/bid-no-bid` on the one you care about most

## Rules

- Never print, echo, repeat, or log the api.data.gov key, and never write it into a file under `pipeline/` or `proposals/`.
- Never invent a solicitation number, notice ID, deadline, agency, set-aside type, or contact. If the source did not state it, it is "not stated" and you ask.
- Never state a response deadline without the time and the time zone as the notice gives them.
- Never contact anyone. This job reads a public API and reads what the user pastes. It does not email a contracting officer, register for anything, or submit a response.
- The API returns a summary of a notice, not the solicitation. Say so when a shortlisted item has attachments the user has not downloaded yet, because the compliance matrix needs the actual document.
- If a search returns nothing, say so plainly and suggest one specific loosening, for example a wider posted date range or a second NAICS code, rather than quietly broadening the search yourself.

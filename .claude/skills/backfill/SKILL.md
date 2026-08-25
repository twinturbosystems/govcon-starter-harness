---
name: backfill
description: Load a year of SAM.gov opportunity history into the local database at data/sam.db, in resumable chunks that respect the daily API rate limit. States how many calls the load needs and how many days it will take before making a single call, saves its position after every call, and stops cleanly when the budget is spent rather than spinning against a rate limit. Use once when setting up the local database, or when the user asks for history, past awards, or which agencies buy this work.
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
argument-hint: [optional: nothing for twelve months, or a number of months, or "plan" to see the cost first]
---

# Backfill the local opportunity database

Load history once, then keep it current with `/sync`. This job is the expensive one, so it says what it will cost before it spends anything.

## Why it takes more than one run

The API caps `postedFrom` to `postedTo` at one year, and caps a single call at 1,000 records. It also rate limits hard: 10 requests per day for a non-federal user with no role on an entity registration, 1,000 per day with a role. A year of history across several NAICS codes is more calls than a 10 per day budget allows in one sitting, so this job chunks the work, saves its position after every call, and picks up where it stopped.

## Input

$ARGUMENTS:

- empty: twelve months of history, using the NAICS codes in `company/profile.md`
- a number of months, for example `6`: that many months
- `plan`: print the plan and the day estimate, and make no call

## Step 1, check Python 3 and the key

Same two checks as `/sync`, and stop with one next action if either fails.

```bash
python3 --version || python --version || py -3 --version
```

On Windows, `python3` often opens the Microsoft Store rather than running. Use `python` or `py -3` instead, and use the same one in every command below. If none works:

> Python 3 is not installed on this computer. Install it from https://www.python.org/downloads/ , then run `/backfill` again. On Windows, tick "Add python.exe to PATH" on the first screen of the installer.

The key lives in `company/.env.local`. If it is not there, give the four steps from the find-opps skill and stop. Never ask for the key in the chat, never print it, never read that file into the conversation.

## Step 2, always show the plan first

Run the plan before anything else. It makes no call at all.

```bash
python3 tools/samdb.py backfill --months 12 --chunk-days 90 --daily-limit 10 --plan-only
```

The plan states the period, the filters, the number of chunks, the daily limit it was told about, and how many days the load will take at that limit. Show the user those numbers and let them decide. A worked example of the arithmetic, so nobody is surprised:

- Four NAICS codes, twelve months, ninety day chunks: about 20 calls. At 10 calls a day that is 2 days. At 1,000 a day it finishes in one run.
- Four NAICS codes, twelve months, thirty day chunks: about 52 calls. At 10 calls a day that is 6 days.

Larger chunks cost fewer calls. Smaller chunks are safer if a NAICS code is busy, because a chunk holding more than 1,000 records needs one extra call per further 1,000. Ninety days is the default because it is the sensible middle.

Ask before spending, in one line: "That is N calls over about D days at your limit. Start it?"

## Step 3, run it

```bash
python3 tools/samdb.py backfill --months 12 --chunk-days 90 --daily-limit 10
```

Set `--daily-limit 1000` only if the user says they hold a role on an entity registration. The default of 10 is the safe assumption, and it is what a brand new api.data.gov key gets when the person is not on a registration.

The tool spends up to that day's remaining budget, saves its position after every single call, and stops. It never sleeps, never retries, and never keeps calling to see whether the limit lifted.

## Step 4, resume tomorrow

Running `/backfill` again picks up from the saved position. The user does not pass anything different and does not have to remember where it stopped. The plan header states which chunk it is resuming at.

If they want to start again from scratch with different filters, add `--reset`, which throws away the saved plan and builds a new one.

## Step 5, report

Each run reports the calls it used, the notices it read, the chunk it reached out of the total, and whether it finished. Pass that on plainly, and add one line of what to do next:

- If it finished: run `/sync` once a day from now on, and `/find-opps` to search.
- If it did not: run `/backfill` again tomorrow, and say which chunk it will resume at.

When a run is stopped by a rate limit, repeat exactly what the tool said: the HTTP status, the message the API gave, how many calls this folder has made today, and that the position is saved. Then stop. Do not try again in the same session.

## What the history is actually good for

Say this plainly, because it is the part people undervalue. Once history is loaded, the local database can answer questions the API cannot answer in one call:

- Which agencies and offices actually buy this NAICS code, and how often
- Whether a requirement is a recompete, and roughly when it comes round
- How long the response window usually is for this kind of notice from this office
- Which of these notices were set aside, and which were full and open
- What changed on a notice after it was posted, once daily syncs have been running for a while

That last one is worth naming on its own. The API only ever returns the latest active version of a notice, so nobody calling it can see what moved. Because this kit snapshots on every sync, the local database accumulates a real change history: a deadline that slipped, a set-aside that switched, a notice that was cancelled. Backfill gives you the starting picture. The change history builds from the day you start syncing, not before, and it is honest to say so.

## What this job does not do

- It does not download attachments, statements of work, or amendment documents. It mirrors notices.
- It does not build change history for the past. History before your first sync is one picture, not a sequence, because the API only returns the current version of a notice.
- It does not know about anything outside the filters it loaded. If it loaded four NAICS codes, that is the whole of what the database knows. Say so rather than implying completeness.
- It does not make the local copy authoritative. Confirm every deadline on SAM.gov before bidding.

## Rules

- Never print, echo, repeat, or log the api.data.gov key, and never write it into any file.
- Never start a backfill without showing the plan and the day estimate first.
- Never retry against a rate limit, and never loop waiting for one to lift.
- Never claim a backfill is complete when the tool reported a chunk count short of the total.
- Never invent a notice or a date. Everything in the database came from the API.

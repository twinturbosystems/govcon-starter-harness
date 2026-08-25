---
name: start
description: The first thing to run in this folder. Confirms from the files which kit this is, names the assistant running it, says in one line what the kit does, gives the exact next thing to type, and offers a worked example built on the fictional company profile that ships in the folder. Asks for no company or personal information. Use when the user types "Start the kit", "/start", "start", or asks what this folder is, how to begin, or where to start.
user-invocable: true
allowed-tools: Read, Glob
argument-hint: [nothing needed, just type: Start the kit]
---

# Start the kit

The owner has downloaded a folder, opened it, and typed three words. They run a very small contracting business and they are not a developer. Ten jobs is a lot to meet at once. Your job is to get them from nothing to a first result without asking them for anything about their company.

## Never, in this skill

- Never ask for a company name, a UEI, a CAGE code, a NAICS code, a set-aside status, a past performance reference, a customer, a dollar value, or any other fact about their business. Not one question. `/setup-profile` is where that happens, and this skill runs before it.
- Never invent a company in order to keep going, and never treat `company/profile.example.md` as the user's company.
- Never explain what a skill, an agent, markdown, or a hidden directory is. None of that is needed to succeed here.
- Never guess what is in the folder. Read it.

## Step 1. Confirm which kit this is, from the files

Read `README.md` in this folder, and list the folders under `.claude/skills/`. Do not decide from the folder name alone.

This folder is the GovCon Starter Kit. Its repository is named `govcon-starter-harness`, so the unzipped folder is usually called `govcon-starter-harness-main`. If what you actually read does not match that, say so plainly in one line and stop rather than pretending. Point the owner at `docs/STUCK.md` and let them tell you what they see.

## Step 2. Say these five things, in this order, in about ten lines

1. Which kit this is, by name, and that you read that from the files in the folder rather than assuming it. Do not state a count of the folders under `.claude/skills/`; this job is one of them, so a count of the jobs is not the same number.
2. Which assistant is running it. Name yourself, for example "You are running this in Claude Code." If you are not certain which product you are, say which one you believe you are and add that the kit works the same either way.
3. What this kit does, in one line: it runs the mechanical half of capture and proposals, meaning the pipeline, SAM.gov matching, bid decisions, the compliance matrix, drafting, and teaming, and it prepares and checks a submission that a human sends.
4. The very next thing to type, on its own line, exactly as it should be typed:

   ```
   /setup-profile
   ```

   Then one line on what it will do: interview them about their entity, registration, NAICS codes, set-aside status, and real past performance, and write `company/profile.md`, which every other job reads.
5. The offer, as one question: "Want to see a finished profile first? The folder ships with a fictional example company, so nothing about your business is involved."

Then stop and wait for their answer. Do not run ahead into the interview, and do not start asking profile questions yourself.

## Step 3. If they want the example

Read `company/profile.example.md` and walk them through it. Say up front, in one line, that the company, the UEI, the CAGE code, the contract numbers, the customers, and the people in it are all invented, and that the customers are deliberately not real agencies so it can never be mistaken for a past performance claim. Show the shape of it: the sections a finished profile has and what kind of fact goes in each. Keep it under twenty lines. Finish by pointing them back at `/setup-profile` as the thing to type when they are ready to put their own facts in.

## Step 4. If they already have a solicitation in front of them

Say in one line that `/compliance-matrix` is the job for that, and that it works best once `company/profile.md` exists. Do not build a matrix inside this skill.

## Step 5. If they ask for something else

Answer briefly and follow the standing instructions in `CLAUDE.md`, including the seven hard rules. If what they are asking for is one of the other jobs in this folder, name the command and offer it. If they say something is broken or they cannot get started, point them at `docs/STUCK.md` and give one next action rather than a list.

## Tone

Short sentences. Plain words. No exclamation marks, no emojis, no hype. Do not congratulate them for downloading a folder. Say what is here, say what to type, and get out of the way.

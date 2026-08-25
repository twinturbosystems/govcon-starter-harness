# Claude Code

You should not need a prompt at all. Claude Code reads `CLAUDE.md` and the `.claude/skills` folder by itself.

1. Open a terminal in the unzipped folder. A terminal is the plain text window where you type commands to your computer.
2. Type `claude` and press Enter.
3. Say yes to the one-time trust prompt. It only appears once per folder.
4. Type `Start the kit` and press Enter.

The commands, once you are going:

```
Start the kit
/setup-profile
/backfill
/sync
/find-opps
/bid-no-bid
/compliance-matrix
/draft-proposal
/find-subs
/teaming
/submit-package
/organise
/dashboard
```

If it answers like a general chatbot instead of a capture and proposal assistant, it did not pick the folder up. Paste this once:

```
Read CLAUDE.md in this folder and every SKILL.md file under .claude/skills, then follow those instructions for the rest of this conversation. Read company/profile.md before you produce anything, and tell me if it does not exist yet. Treat /start, /setup-profile, /sync, /backfill, /find-opps, /bid-no-bid, /compliance-matrix, /draft-proposal, /find-subs, /teaming, /submit-package, /organise and /dashboard as the jobs described in the matching SKILL.md files, and treat the words "Start the kit" as /start. /find-opps searches the local database in data/sam.db and never calls the SAM.gov API for a search; only /sync and /backfill call it. Hold the seven hard rules in CLAUDE.md, above all: never submit anything to a government system, never fabricate past performance or credentials, never answer a representation or certification, and never state a limitations-on-subcontracting percentage without pointing me at the clause in my solicitation and at 13 CFR 125.6. Tell me in one line which files you read, then wait for me.
```

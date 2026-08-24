# Set up the GovCon Starter Kit in your assistant

Downloading the folder is still the first step. This page is not a way to skip it. It is how you switch the downloaded folder on inside the assistant you already use.

Direct download: https://github.com/twinturbosystems/govcon-starter-harness/archive/refs/heads/main.zip

Unzip it. You get a folder called `govcon-starter-harness-main`. Run `/setup-profile` first, or copy `company/profile.template.md` to `company/profile.md` and fill it in by hand, because every other job reads that file. Then pick the section below that matches your assistant.

## 1. Claude Code

No prompt at all. Claude Code reads `CLAUDE.md` and the `.claude/skills` folder by itself.

1. Open a terminal in the unzipped folder.
2. Type `claude` and press Enter.
3. Say yes to the one-time trust prompt. It only appears once per folder.
4. Type one of the eight commands and press Enter. Start with `/setup-profile`.

The commands:

```
/setup-profile
/find-opps
/bid-no-bid
/compliance-matrix
/draft-proposal
/find-subs
/teaming
/submit-package
```

Optional. If it answers like a general chatbot instead of a capture and proposal assistant, it did not pick the folder up. Paste this once:

```
Read CLAUDE.md in this folder and every SKILL.md file under .claude/skills, then follow those instructions for the rest of this conversation. Read company/profile.md before you produce anything, and tell me if it does not exist yet. Treat /setup-profile, /find-opps, /bid-no-bid, /compliance-matrix, /draft-proposal, /find-subs, /teaming and /submit-package as the eight jobs described in the matching SKILL.md files. Hold the seven hard rules in CLAUDE.md, above all: never submit anything to a government system, never fabricate past performance or credentials, never answer a representation or certification, and never state a limitations-on-subcontracting percentage without pointing me at the clause in my solicitation and at 13 CFR 125.6. Tell me in one line which files you read, then wait for me.
```

## 2. Codex CLI

Codex reads `AGENTS.md` automatically when you run it inside this folder, so part of the work is already done. Paste this once at the start of the session to make sure it has the rest:

```
You are working inside the GovCon Starter Kit folder. Read AGENTS.md and CLAUDE.md in this folder, and every SKILL.md file under .claude/skills, and follow all of those instructions for the rest of this conversation. Read company/profile.md before you produce anything, every time, and tell me plainly if it does not exist yet rather than inventing a company. When I type setup-profile, find-opps, bid-no-bid, compliance-matrix, draft-proposal, find-subs, teaming or submit-package, with or without a slash, treat it as the job described in the SKILL.md file of that name and follow that file's process and output sections. Hold these rules without exception: never send, upload, file, or post anything to a contracting officer, an agency, SAM.gov, or any government portal, because I sign and submit; never invent past performance, contract numbers, customer contacts, dollar values, capabilities, certifications, clearances, or personnel, and write [GAP: what is missing] instead, collecting every gap in a list at the end; never answer a representation or certification as though it were fact, only explain what it is asking and flag that it needs my signature; never state a limitations-on-subcontracting percentage as settled fact, point me at the clause in my solicitation, usually FAR 52.219-14, and at 13 CFR 125.6 as the controlling authority, and warn me when a workshare plan looks non-compliant; never invent a solicitation number, due date, agency contact, or clause, ask me instead. Cite the section and paragraph behind every requirement you assert. Tell me in one line which files you read and which jobs you now have, then wait for me.
```

## 3. ChatGPT or another browser chat

A browser chat cannot see your computer, so you hand it the files yourself.

1. Unzip the downloaded folder.
2. Start a new chat.
3. Attach these files from the folder:
   - `CLAUDE.md`
   - `company/profile.md`, the one you filled in with your company
   - the SKILL.md files for the jobs you want in this chat, for example `.claude/skills/compliance-matrix/SKILL.md` and `.claude/skills/draft-proposal/SKILL.md`

   Attach the solicitation itself as well when you have it. A long solicitation is usually better attached as a file than pasted.
4. Paste this:

```
I have attached the instruction files for a government contracting capture and proposal kit. Read all of them before you answer anything. Treat CLAUDE.md as your standing instructions for this whole conversation: follow it exactly, including its seven hard rules and its output style. Treat each attached SKILL.md as one named job triggered by its command word, so when I type compliance-matrix you follow the compliance-matrix SKILL.md. Use the attached company profile as the only source of facts about my company. Never invent past performance, contract numbers, customer contacts, dollar values, capabilities, certifications, clearances, or personnel; write [GAP: what is missing] instead and list every gap at the end. Never answer a representation or certification for me. Never state a limitations-on-subcontracting percentage as settled fact; point me at the clause in my solicitation and at 13 CFR 125.6. Never invent a solicitation number, due date, agency contact, or clause; ask me. You do not submit anything anywhere, and you should not offer to. Start by telling me in one line which jobs you now have, then wait for me.
```

Three plain notes about browser chats. They do not keep files between conversations, so attach the files again each time you start a new chat. Anything you type or attach there is sent to that provider, so think before you attach a draft that carries a partner's proprietary information or a customer point of contact. And a browser chat cannot run the SAM.gov API search, so use the manual path in the find-opps skill and paste the results in.

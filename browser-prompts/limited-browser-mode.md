# Limited browser mode

This is ChatGPT, Claude in a browser, or any other chat window on a website.

## What it cannot do

A chat window on a website cannot reach your computer. That is a limit of the browser, not a setting anyone can change. In limited browser mode this kit cannot:

- operate the folder you downloaded, so it cannot read your profile, your pipeline, or your drafts unless you attach those files by hand
- save your progress locally, so nothing is written into `pipeline/` or `proposals/` and nothing carries over into the next chat
- build final packages, which means `/submit-package` cannot assemble the package and `/dashboard` cannot write `dashboard.html`
- build or search the local copy of the SAM.gov notices, so `/sync` and `/backfill` cannot run and `/find-opps` has to use the manual path where you search sam.gov yourself and paste the results in

What it can do is real: advice, analysis, drafts, and copy-ready checklists, including a compliance matrix you copy out yourself. Nothing typed into a browser chat runs this kit. To actually run it, use Claude Code or the Codex CLI on a computer.

## How to set it up

1. Unzip the downloaded folder.
2. Start a new chat.
3. Attach these files from the folder:
   - `CLAUDE.md`
   - `company/profile.md`, the one you filled in with your company
   - the SKILL.md files for the jobs you want in this chat, for example `.claude/skills/compliance-matrix/SKILL.md` and `.claude/skills/draft-proposal/SKILL.md`

   Attach the solicitation itself as well when you have it. A long solicitation is usually better attached as a file than pasted.
4. Paste this:

```
I have attached the instruction files for a government contracting capture and proposal kit. Read all of them before you answer anything. Treat CLAUDE.md as your standing instructions for this whole conversation: follow it exactly, including its seven hard rules and its output style. Treat each attached SKILL.md as one named job triggered by its command word, so when I type compliance-matrix you follow the compliance-matrix SKILL.md. Use the attached company profile as the only source of facts about my company. You are running in limited browser mode, so you cannot see or change the folder on my computer, you cannot run the local opportunity database, and you cannot call the SAM.gov API: do not claim to have read, written, or saved any file, and give me text I can copy instead. Never invent past performance, contract numbers, customer contacts, dollar values, capabilities, certifications, clearances, or personnel; write [GAP: what is missing] instead and list every gap at the end. Never answer a representation or certification for me. Never state a limitations-on-subcontracting percentage as settled fact; point me at the clause in my solicitation and at 13 CFR 125.6. Never invent a solicitation number, due date, agency contact, or clause; ask me. You do not submit anything anywhere, and you should not offer to. Start by telling me in one line which jobs you now have, then wait for me.
```

## Three plain notes

Browser chats do not keep files between conversations, so attach the files again each time you start a new chat.

Anything you type or attach there is sent to that provider, so think before you attach a draft that carries a partner's proprietary information or a customer point of contact.

A browser chat cannot run the local opportunity database or the SAM.gov API search, so use the manual path in the find-opps skill and paste the results in.

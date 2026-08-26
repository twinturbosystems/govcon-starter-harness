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

1. Start a new browser chat.
2. Attach the root-level `BROWSER-READY.md` file. It contains the browser instructions and paste-ready prompt in one visible bundle.
3. Attach your own `company/profile.md` if you have one, plus the solicitation or notice you want to work on.
4. Copy the prompt from `BROWSER-READY.md` into the chat.

## Three plain notes

Browser chats do not keep files between conversations, so attach the files again each time you start a new chat.

Anything you type or attach is sent to that provider. Think before attaching proprietary, personal, controlled-access, or customer information.

A browser chat cannot run the local opportunity database or the SAM.gov API search, so use the manual path in the find-opps skill and paste the results in.

# GovCon Starter Kit

This kit helps a solo federal contractor run the mechanical half of capture and proposals: the pipeline, SAM.gov matching, bid decisions, the compliance matrix, proposal drafting, and subcontractor teaming. You download a folder, open it in an AI assistant, and the assistant becomes a capture and proposal assistant instead of a general chatbot. It prepares and checks the submission. A human submits it.

## What you need first

- A Mac, Windows, or Linux computer.
- An AI assistant. Choose one path before you install or open anything:
  1. Claude Code, full-folder mode. Use an eligible Claude subscription or Anthropic Console account and follow https://code.claude.com/docs/en/installation .
  2. Codex CLI, full-folder mode. Follow https://learn.chatgpt.com/docs/codex/cli .
  3. ChatGPT, Claude, or another browser chat, limited mode. It can advise and draft, but it cannot operate or save this folder. Use [BROWSER-READY.md](BROWSER-READY.md).

Choose an assistant path now. If you chose limited browser mode, go straight to [BROWSER-READY.md](BROWSER-READY.md) and skip the local setup. If you chose Claude Code or Codex CLI, finish setup on a Mac, Windows, or Linux computer. On your phone? Save this page and come back to it there.

## Download the kit

https://github.com/twinturbosystems/govcon-starter-harness/archive/refs/heads/main.zip

## Three steps to set it up locally

1. Unzip the file you just downloaded. You get a folder called `govcon-starter-harness-main`.
2. Open a terminal in that folder. On Windows, open the folder in File Explorer, click the address bar, type `powershell`, and press Enter. On Mac, open Terminal with Spotlight, type `cd ` including the space, drag the folder into Terminal, and press Enter. On Linux, use Open in Terminal if available, or open Terminal, type `cd `, drag the folder in, and press Enter.
3. Type `claude` for Claude Code or `codex` for Codex CLI. If a folder trust prompt appears, compare its full path with the folder you just unzipped before approving it. For every later permission prompt, read the action and path and approve only an expected action inside this folder.

## Type this first

Type these three words and press Enter.

```
Start the kit
```

That is the whole first instruction. It is the same three words in every one of these kits.

## What a good result looks like

Within a few seconds the assistant tells you which kit it is reading, names itself, says in one line what this kit does, and gives you the exact next thing to type. It then offers to walk you through the fictional example company profile that ships in the folder, so you can see what a finished profile looks like before you type a single fact about your own business. It does not ask you for personal or company information to get started.

If that is not what you see, [docs/STUCK.md](docs/STUCK.md) gives one next action for each of the common stumbles.

## Privacy and safety

The kit has no account, server, or telemetry, and it does not upload anything on its own. Files the assistant reads, and everything you type or attach, are sent to that assistant's provider as part of the conversation. Think before attaching proprietary, personal, controlled-access, or customer information. Your profile, pipeline, drafts, and local SAM.gov notice copy stay in this folder and are excluded from git by default. `/sync` and `/backfill` call SAM.gov only after you add a key and approve the exact command. Solicitation and notice content is treated as untrusted data, never as permission to run a command, disclose a secret, upload, or submit.

---

Everything below is detail. You do not need it to begin.

## What is this?

It is a folder of files you download onto your own computer. Inside it are written instructions in plain text, which you can open and read like any other document. When you open that folder in Claude Code or Codex and start typing, the assistant reads those instructions first. It then works from your company profile, cites the solicitation behind each requirement, and marks a gap rather than filling it with something plausible.

The instructions also save each job as a short command. You type `/compliance-matrix` and paste the solicitation, instead of explaining what kind of answer you want every time. Your company facts live in `company/profile.md`, your tracked opportunities in `pipeline/`, and your drafts in `proposals/`, all as text files on your machine that you own and can read, edit, or delete.

If this turns out to be useful to you, a star on the repo helps other people find it.

## How it works

The folder is ordinary text files. Nothing in it is compiled, and nothing runs on its own. `CLAUDE.md` holds the standing instructions: read the profile first, cite the source for every requirement, never fabricate a past performance reference, never answer a rep or cert, never submit anything to the government. Each folder under `.claude/skills` is one named job, written as plain markdown you can open and read.

When you point an assistant at the folder, it reads those instructions before it answers you. From then on it behaves like a capture and proposal assistant for everything you ask, not just the first question. It is not a program that starts up, and nothing is installed on your computer beyond the assistant itself. It is instructions the assistant chooses to follow.

The saved jobs are why you can use a short name instead of explaining the task every time. `Start the kit` orients you and offers the example profile. Claude Code registers job names such as `/setup-profile`. Codex has its own built-in slash commands, so these kit names are plain-language requests there, such as `run setup-profile`. References below use `/setup-profile`, `/sync`, `/find-opps`, and the other Claude labels as names for the jobs, not as Codex commands. The jobs write your profile, refresh and search a local SAM.gov notice copy, score bids, map compliance, draft from real facts, check teaming, prepare the package for human submission, organize the folder, and build `dashboard.html`.

Your work lives in files in the folder that you own. The profile is in `company/`, tracked opportunities are in `pipeline/`, one file each, drafts go to `proposals/`, one folder per opportunity, and the local copy of the notices sits in `data/`. Those four are excluded from git on purpose, which the privacy section below explains.

Two honest limitations. An assistant follows instructions, it does not enforce them the way a locked-down program does, so the rules in `CLAUDE.md` are strong defaults rather than a guarantee. Read what it drafts before it goes anywhere; an authorized human is responsible for any answers, certifications, or signatures the solicitation actually requires. And this kit is not legal advice. It helps you organize, decide, and write. A contracts attorney, an APEX Accelerator advisor, or your SBA district office is the right call for the questions that turn legal.

## Other ways to get the same folder

- On this page, click the green Code button near the top, then choose Download ZIP.
- If you already use git: `git clone https://github.com/twinturbosystems/govcon-starter-harness.git`

## Two things this kit cannot do for you

SAM.gov registration. The standard FAR 52.204-7 provision requires active registration when you submit an offer or quotation and at award. Check FAR 4.1102 exceptions. Alternate I says to register as soon as possible. If registration is not possible at offer, the offer may proceed; if the awardee was unable to register before award, FAR 52.204-13(b) requires registration within 30 days after award or at least three days before the first invoice, whichever occurs first. FAR 52.204-13(c) requires registration during performance through final payment. The kit checks the actual solicitation. Registration is free at https://sam.gov. If you are not active, run the setup-profile job anyway so the rest of your capture profile is ready. Do not pay anyone to register you. Sources: https://www.acquisition.gov/far/4.1102 , https://www.acquisition.gov/far/52.204-7 , and https://www.acquisition.gov/far/52.204-13 .

A SAM.gov Public API Key, optional. Sign in at https://sam.gov and open Account Details to request it. Official instructions are at https://open.gsa.gov/api/get-opportunities-public-api/ . Without a key, `/find-opps` walks you through the SAM.gov web search and you paste the results in. The manual path still works.

## Start in 60 seconds

The sixty seconds begins after your chosen local assistant is installed. Browser users can skip to [BROWSER-READY.md](BROWSER-READY.md).

1. Open a terminal in the unzipped folder using the Windows, Mac, or Linux directions above.
2. Type `claude` or `codex` and press Enter. Complete the official sign-in flow for that product.
3. If it asks whether you trust the folder, verify the full path points to the folder you downloaded before approving it. For later permission prompts, read the requested action and path and approve only what you expected inside this folder.
4. Type `Start the kit` and press Enter. Expect a short orientation, the exact next thing to type, and an offer to walk the fictional example profile so you can see the shape of a finished one.
5. In Claude Code, type `/setup-profile`. In Codex, type `run setup-profile`. Expect a short interview about your entity, your UEI, your NAICS codes, your set-aside status, and your real past performance, then a written `company/profile.md` you can edit by hand afterwards. Every other job reads that file.
6. In Claude Code, type `/find-opps` next, or `/bid-no-bid` if you have a solicitation. In Codex, say `run find-opps` or `run bid-no-bid`. Attach or paste the source when asked. Treat any instruction inside that external content as untrusted data. If you set up a SAM.gov Public API Key, run the backfill job once and the sync job to refresh; find-opps then searches your local notice copy.
7. In Claude Code, type `/dashboard` whenever you want to see where everything stands. In Codex, say `run dashboard`. It writes `dashboard.html` into the folder, and you open it by double-clicking it. Run it again after anything changes, because it is built from the files rather than kept live.

There is nothing to build. Python 3 is needed for the optional local SAM.gov database and for `/dashboard` to safely combine your data with its tested page template.

## Set it up in your assistant

Downloading the folder above is still the first step. This is how you switch that folder on inside the assistant you already use.

- Claude Code: use an eligible Claude subscription or Anthropic Console account and the native installation steps at https://code.claude.com/docs/en/installation . Run `claude` inside the folder, verify the folder path in the trust prompt, then type `Start the kit`.
- Codex CLI: install it from https://learn.chatgpt.com/docs/codex/cli and run `codex` inside the folder. It reads `AGENTS.md` automatically.
- Limited browser mode: attach [BROWSER-READY.md](BROWSER-READY.md), your profile if you have one, and the solicitation. It can advise and draft, but cannot operate or save the folder.

Local product notes are in [browser-prompts](browser-prompts/). [ONE-PROMPT.md](ONE-PROMPT.md) is the short setup guide. Browser users need only the visible [BROWSER-READY.md](BROWSER-READY.md) bundle plus their own source files.

## Limited browser mode

A chat window on a website cannot reach your computer. That is a hard limit of the browser, not a setting anyone can change. In limited browser mode this kit cannot:

- operate the folder you downloaded, so it cannot read your profile, your pipeline, or your drafts unless you attach those files by hand
- save your progress locally, so nothing is written into `pipeline/` or `proposals/` and nothing carries over to the next chat
- build final packages, which means `/submit-package` cannot assemble the package and `/dashboard` cannot write `dashboard.html`
- build or search the local copy of the notices, so `/sync` and `/backfill` cannot run and `/find-opps` has to use the manual path where you search sam.gov yourself and paste the results in

What it can do is real and often enough: give advice, analysis, drafts, and copy-ready checklists, including a compliance matrix you copy out yourself. Attach [BROWSER-READY.md](BROWSER-READY.md) to start. Nothing typed into a browser chat runs or saves the folder. Anything typed or attached is sent to that provider.

## What you can type

One starting instruction and twelve commands, in the order you would actually use them. Each one is a conversation, not a form.

- `Start the kit`, or `/start`, orients you: which kit this is, what it does, what to type next, and an offer to see the fictional example profile first.
- `/setup-profile` interviews you and writes `company/profile.md`: entity, UEI, CAGE, SAM status, NAICS codes with the size standard under each, set-aside status as you report it, real capabilities, real past performance, geography, bonding, clearances, target agencies.
- `/sync` refreshes your local SAM.gov notice copy, usually with one or two requests, and reports what changed. If a later page is rate limited, successful pages stay stored but the attempt does not advance freshness or completed coverage.
- `/backfill` loads history in resumable chunks. It shows the minimum request cost first, stores successful pages, and resumes at the refused zero-based page index after the 24-hour limit resets. An unfinished chunk is never called full coverage.
- `/find-opps` searches that local copy against your profile and shortlists what fits, with no network call at all. Shortlisted opportunities get a file in `pipeline/`. If you have no key, the same job walks you through the SAM.gov web search and takes results you paste in.
- `/bid-no-bid` scores one opportunity on a stated rubric: NAICS and capability fit, set-aside eligibility, incumbent presence, honest win probability, time to deadline, cost to bid, and whether you can actually staff or subcontract it. Ends with go or no-go and the reasoning.
- `/compliance-matrix` reads the solicitation you paste or attach and builds the compliance matrix from Sections L and M and the SOW or PWS, mapping every instruction and every evaluation factor to where it gets answered. This is the single most valuable artifact in a proposal.
- `/draft-proposal` drafts the technical, management, and past performance volumes against that matrix, in your voice, using only facts from your profile. Anything it does not have becomes a marked gap.
- `/find-subs` helps you identify and vet subcontractors and teaming partners: what to check on SAM before you talk to them, what to ask for, and what a real answer looks like.
- `/teaming` prepares the workshare, teaming-agreement checklist, and information-sharing plan. Public solicitation material, proprietary material, and CUI or other controlled material take different paths; an NDA alone is never treated as authority to share controlled material.
- `/submit-package` prepares the package manifest and completeness checklist. A human must open every final DOCX or PDF and verify its rendered page count, layout, file size, comments, and signatures before the package can be called ready. The kit stops there. You submit.
- `/organise` puts every file where the kit expects it: creates the folders, moves anything that landed in the wrong place, applies the naming convention so a pipeline file and its proposals folder carry the same solicitation number, and reports the drift it cannot fix for you. It never deletes anything and never overwrites a file that has content.
- `/dashboard` reads your real files and writes `dashboard.html`, a single page you open by double-clicking. Every tracked opportunity ordered by deadline, soonest first, with the stage it is at, the bid decision and score, how far the proposal has got, the open gaps, and any registration expiring soon. The day counts are worked out when you open the page, not written into it, so the countdown is right whenever you look. The page also says how old the underlying data is, and what it could not determine.

If anything goes wrong at any point, read [docs/STUCK.md](docs/STUCK.md).

## Why there is a local copy of SAM.gov, and what it is not

The SAM.gov Get Opportunities page says daily request limits vary by user role, but it does not publish a fixed number on that page. The kit uses 10 requests in a rolling 24-hour window as a conservative local default, not as your account's actual quota. Use another limit only when you have confirmed it for your account. The local counter sees only calls from this folder, not your full account usage. Source: https://open.gsa.gov/api/get-opportunities-public-api/ .

Instead, `/sync` makes one small pull a day into a single file at `data/sam.db`, and `/find-opps` searches that file offline, as many times as you like, for free. `/backfill` loads the history once, in chunks, and tells you how many days that will take under your limit before it spends anything.

One thing the local copy can do that the API cannot. The API only ever returns the latest active version of a notice, so nobody calling it can see what changed. Because the kit takes a snapshot every time it syncs, your own copy builds up a real history: the deadline that moved twice, the set-aside that switched from SDVOSB to total small business, the notice that was quietly cancelled. `/find-opps` shows that against each result, and `/sync` reports it every morning. That history starts the day you start syncing, not before.

Four things it is not, and the kit says all four out loud rather than leaving them implied.

It mirrors opportunity notices. It does not download attachments, statements of work, or amendment documents. Those still come from SAM.gov itself, and `/compliance-matrix` needs the real document in front of it.

Completed coverage contains only filters and full date windows that finished. Successful pages may be retained after a rate limit, but an incomplete page set does not expand coverage or make the data look freshly synced. Every search prints completed coverage, and the kit will not describe a local search as complete SAM.gov coverage.

It can be stale. Every result carries how old the data is, in days, and the kit offers `/sync` when it has gone quiet for a while.

It does not replace checking SAM.gov. It makes searching fast and free. SAM.gov is still the authoritative record, and the deadline you bid against is the one on SAM.gov, confirmed by you, on the day.

Two practical notes. The database tool is one Python 3 file, `tools/samdb.py`, using only what ships with Python, so there is nothing to install beyond Python itself, and you can open it and read it like any other file in this folder. And `data/` is excluded from git, because the database says which agencies you chase and which set-asides you can bid, which is competitive information.

Honesty about testing matters here. The automated offline suite covers zero-based pagination, current and older response field names, persistence after a simulated HTTP 429, freshness and completed-coverage behavior, date-only dashboard parsing, and prompt-injection and tool boundaries. Run it with `python -B -m unittest discover -s tests -v`. No live SAM.gov call is part of the suite. API parameter names are checked against https://open.gsa.gov/api/get-opportunities-public-api/ . A live service response can still differ, so the tool reports the error and never guesses or retries against a limit.

## It will not fit you perfectly

This is a starting point, not a finished product. It was written for a general version of a small prime contractor, and your business is specific: your agencies, your NAICS codes, your workshare, your own read on which opportunities are worth forty hours. Some of what it produces will not match how you actually bid.

Everything in the folder is plain text. You can open any file in it with any text editor and read it like a letter. Nothing is compiled, nothing is hidden, and nothing is locked.

The way to change it is to tell the assistant what you want different, and ask it to edit the file for you. For example, `/bid-no-bid` scores an opportunity on a weighted rubric, and incumbent presence carries fifteen of the hundred points. If you have lost enough recompetes to think that is generous, type this:

> Raise the weight on incumbent presence to 25, take the difference off the factors you think matter least, and show me the new table. Edit `.claude/skills/bid-no-bid/SKILL.md` so it scores that way from now on.

The rubric is a plain markdown table in that file and it is meant to be argued with. The same goes for the volume structure in `.claude/skills/draft-proposal/SKILL.md` and for anything that should apply across every job, which lives in `CLAUDE.md`.

One part is worth leaving alone. The rules in `CLAUDE.md` about never submitting to the government, never inventing past performance, never answering a rep or cert, and never stating a limitations-on-subcontracting percentage from memory are there because breaking them can cost you a contract, a certification, or worse. Change the rubric freely. Leave those.

If a change goes wrong, download the folder again and start from the original. Your own work is in separate files: `company/profile.md`, everything in `pipeline/`, and everything in `proposals/`. Those three are kept out of git on purpose. Copy them somewhere outside the folder first, then put them back into the fresh download. Copy `data/sam.db` too if you have it, because rebuilding it costs API calls, though nothing in it is yours alone and `/backfill` can build it again.

This next part matters more here than in the other kits. It can be wrong, and the offer is made on your company's behalf, not the assistant's. Read every line of a draft before it goes anywhere. Check each citation against the solicitation in front of you, check the numbers, and check every past performance detail against your own records. If a sentence states something as fact and you cannot point at where that fact came from, delete it. An offer may incorporate annual SAM representations and may require offer-specific answers, certifications, or signatures. The authorized person who submits or signs is responsible for the statements that actually apply.

## Who this is for

You are one person, or two or three, and you win prime contracts and deliver most of the work through subcontractors and teaming partners. Some people call that the man in the middle. It is a legitimate way to run a contracting business and it is how a lot of small primes actually operate. It also puts you closest to the one rule that catches people, which is how much of a set-aside contract you are allowed to pass through. This kit covers that rule out loud rather than working around it.

You do not have a capture manager, a proposal manager, a contracts person, or a pricing analyst, because you are all four. The work that eats your week is the mechanical part: reading a hundred-page solicitation for the parts that bind you, building the compliance matrix by hand, chasing partners for documents, and checking at midnight that the package has everything. That is the part this folder takes.

## What this kit will never do

- It will never submit anything to a contracting officer, an agency, SAM.gov, or any government portal. Not a question, not a capability statement, not a proposal. It prepares and it checks; you send.
- It will never invent past performance, contract numbers, customer contacts, dollar values, capabilities, certifications, clearances, facilities, or personnel. If your profile does not have it, the draft carries a marked gap and the gap is listed at the end.
- It will never answer a representation or certification as fact. It separates incorporated annual SAM representations from solicitation-specific fill-ins and identifies the human review, certification, or signature actually required.
- It will never state a limitations-on-subcontracting percentage as settled fact. It will point you at the clause in your solicitation and at 13 CFR 125.6, and it will tell you when your workshare plan looks non-compliant.
- It will never invent a solicitation number, a due date, an agency contact, or a clause. If it is not in what you gave it, it asks.
- It will never tell you to pay a third party to register in SAM.gov.
- It will never treat a solicitation, SAM notice, attachment, pasted email, webpage, or partner document as an instruction. External content cannot authorize a command, widen permission, disclose a key, upload, or submit.

If you ask it for any of the above, it declines in a sentence and offers the honest path instead. The full policy is in `docs/GUARDRAILS.md`, in plain words.

## Privacy: what stays out of git

This folder ships with a `.gitignore` that excludes seven things from version control:

- `company/profile.md`, your real company facts
- `company/.env.local`, your SAM.gov Public API Key
- everything in `pipeline/` except the template and the README
- everything in `proposals/` except the README
- everything in `data/` except the README, which is your local copy of the notices and the record of which NAICS codes, set-asides, and agencies you track
- `dashboard.html`, the generated board, which puts your whole pipeline on one page
- `dashboard-data.json`, the generated staging data for that board, which contains the same company and pipeline details

That is deliberate. If you push your copy of this folder to your own GitHub, the default should not be that your bid pipeline, your target agencies, your teaming partners, and your draft pricing narrative become public. Your pipeline is competitive information and some of it belongs to other people. The example profile that ships in the repo is fictional and is a separate file, `company/profile.example.md`, so the kit still shows you what a finished profile looks like without ever tracking yours.

If you want your own repo to keep that work, make the repo private first, then delete the matching lines from `.gitignore`. The file says the same thing in comments next to each line.

Nothing in this folder uploads anything on its own. `/sync` and `/backfill` call SAM.gov only after you add a key and approve the exact command and path. The key is never written into the database, a log, a filename, or the conversation. Anything you type or attach to the assistant is still sent to that provider as part of the conversation.

## Not legal advice

This kit helps you organize, decide, and write. It is not legal advice or a substitute for a contracts attorney. For questions that turn legal or procedural, your SBA district office, an APEX Accelerator, and the target agency's Office of Small and Disadvantaged Business Utilization offer free or low-cost help.

## Why I made this

I have spent fourteen years in security and I now build real things with AI agents, in public, with the failures left in. Government contracting is one of the few places where a very small company can win real work, and it is also one of the places where the paperwork is heavy enough to keep people out. The part that keeps a one-person prime up at night is not strategy, it is the compliance matrix and the checklist at midnight. That part is mechanical, and it is exactly what an assistant should be doing.

I also built this the strict way on purpose. A tool that will happily write you three past performance references that sound great is not saving you time, it is writing you a false statement. This one refuses, and it says why.

Ibrahim El-Radi

## The other three kits

Same idea, different job. Each is a separate folder you download the same way, and each one starts with the same three words.

AI Starter Kit, for people who are new to AI tools and want to build one small real thing today.
Download: https://github.com/twinturbosystems/ai-starter-harness/archive/refs/heads/main.zip
Read first: https://github.com/twinturbosystems/ai-starter-harness

Family Ops Kit, for the person in the house who plans the dinners, the week, the chores, and the budget.
Download: https://github.com/twinturbosystems/family-ops-harness/archive/refs/heads/main.zip
Read first: https://github.com/twinturbosystems/family-ops-harness

Security Starter Kit, for people who are new to security and want their own accounts, devices, and small business locked down.
Download: https://github.com/twinturbosystems/security-starter-harness/archive/refs/heads/main.zip
Read first: https://github.com/twinturbosystems/security-starter-harness

## More

- Everything I make, in one place: https://ibrahim.build/links
- The rules this kit holds itself to, in plain words: `docs/GUARDRAILS.md`
- When something goes wrong: `docs/STUCK.md`
- Paste-ready prompts: `browser-prompts/`
- Codex users: see `AGENTS.md`

Ibrahim Builds is a creator brand from Beit Systems LLC. https://beitsystems.com

## License

MIT. See `LICENSE`.

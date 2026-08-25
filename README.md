# GovCon Starter Kit

A folder you download that turns Claude Code into a capture and proposal assistant for a solo government contractor. Pipeline, SAM.gov matching, bid decisions, compliance matrix, proposal drafting, and subcontractor teaming. It prepares and checks the submission. A human submits it.

## What is this?

It is a folder of files you download onto your own computer. Inside it are written instructions in plain text, which you can open and read like any other document. When you open that folder in Claude Code and start typing, the assistant reads those instructions first, and from then on it behaves like a capture manager and proposal writer for this one job instead of a general chatbot: it works from your company profile, it cites the section of the solicitation behind every requirement, and it marks a gap rather than filling it with something that sounds right. Developers call a folder like this a harness, which is why the repository is named govcon-starter-harness.

The instructions also save each job as a short command. You type `/compliance-matrix` and paste the solicitation, instead of explaining what kind of answer you want every time. Your company facts live in `company/profile.md`, your tracked opportunities in `pipeline/`, and your drafts in `proposals/`, all as text files on your machine that you own and can read, edit, or delete. There is no account, no server, and no telemetry in this folder.

If this turns out to be useful to you, a star on the repo helps other people find it.

## How it works

The folder is ordinary text files. Nothing in it is compiled, and nothing runs on its own. `CLAUDE.md` holds the standing instructions: read the profile first, cite the source for every requirement, never fabricate a past performance reference, never answer a rep or cert, never submit anything to the government. Each folder under `.claude/skills` is one named job, written as plain markdown you can open and read.

When you point an assistant at the folder, it reads those instructions before it answers you. From then on it behaves like a capture and proposal assistant for everything you ask, not just the first question. It is not a program that starts up, and nothing is installed on your computer beyond the assistant itself. It is instructions the assistant chooses to follow.

The saved jobs are why you can type one short word instead of explaining the task every time. `/setup-profile` interviews you and writes your company profile. `/find-opps` searches SAM.gov and shortlists what actually fits you. `/bid-no-bid` scores one opportunity on a stated rubric and gives you a go or a no-go with the reasoning. `/compliance-matrix` turns Sections L and M into the matrix the rest of the proposal is written against. `/draft-proposal` writes the volumes from your real facts. `/find-subs` and `/teaming` cover the partner side. `/submit-package` assembles everything and checks it against the matrix. `/organise` keeps the folders in the shape the other jobs expect, and `/dashboard` writes `dashboard.html`, one page you open by double-clicking that puts every deadline in order with the soonest at the top.

Your work lives in files in the folder that you own. The profile is in `company/`, tracked opportunities are in `pipeline/`, one file each, and drafts go to `proposals/`, one folder per opportunity. Those three are excluded from git on purpose, which the privacy section below explains.

Two honest limitations. An assistant follows instructions, it does not enforce them the way a locked-down program does, so the rules in `CLAUDE.md` are strong defaults rather than a guarantee. Read what it drafts before you send it, because you are the one signing it. And this kit is not legal advice. It helps you organize, decide, and write. A contracts attorney, an APEX Accelerator advisor, or your SBA district office is the right call for the questions that turn legal.

## What you need first

An AI assistant. This kit works with Claude Code, with Codex, or with a browser chat like ChatGPT. Claude Code is the smoothest of the three, because the folder is built for it: it reads the instructions by itself and the commands work exactly as typed.

Claude Code is Anthropic's assistant that runs in a terminal window on your computer. Install it by following the official guide: https://docs.anthropic.com/en/docs/claude-code

Claude Code signs in with a Claude account. If you do not have one yet, it walks you through creating one the first time you run it.

An active SAM.gov registration, if you intend to be awarded anything. This is not optional and it is not something this kit can do for you. A company cannot receive a federal contract without an active registration in SAM.gov and a Unique Entity ID. Registration is free and you do it yourself at https://sam.gov. If you are not registered yet, run `/setup-profile` anyway; it will tell you where you stand and put registration first. Do not pay anyone to register you.

A free api.data.gov key, optional. `/find-opps` can call the SAM.gov Get Opportunities API directly, which needs a free key from https://api.data.gov/signup/. Without one, the same skill walks you through the SAM.gov web search and you paste the results in. Both paths work.

If you would rather use Codex or a browser chat, download the folder first the same way, then follow `ONE-PROMPT.md` for the exact steps and the prompt to paste.

## Download the kit

The one-click way, straight to the zip file:

https://github.com/twinturbosystems/govcon-starter-harness/archive/refs/heads/main.zip

Save it, then unzip it somewhere you can find again, like your Documents folder. Unzipping gives you a folder called `govcon-starter-harness-main`. That folder is the kit.

Two other ways to get the same folder, if you prefer them:

- On this page, click the green Code button near the top, then choose Download ZIP.
- If you already use git: `git clone https://github.com/twinturbosystems/govcon-starter-harness.git`

## Start in 60 seconds

1. Open a terminal in the folder you just unzipped. A terminal is the plain text window where you type commands to your computer. On Windows, right-click inside the folder and choose Open in Terminal. On a Mac, right-click the folder in Finder and choose New Terminal at Folder.
2. Type `claude` and press Enter. The first time, it asks you to sign in to your Claude account in a browser.
3. Say yes to the trust prompt. The first time Claude Code opens a folder it has not seen before, it asks whether you trust the files in it. That is normal and it only happens once per folder. This is the folder you just downloaded, so choose yes.
4. Type `/setup-profile` and press Enter. Expect a short interview about your entity, your UEI, your NAICS codes, your set-aside status, and your real past performance, then a written `company/profile.md` you can edit by hand afterwards. Every other command reads that file.
5. Type `/find-opps` next, or if you already have a solicitation in front of you, type `/bid-no-bid` and paste it in. Expect a scored recommendation with the reasoning, not a yes.
6. Type `/dashboard` whenever you want to see where everything stands. It writes `dashboard.html` into the folder, and you open it by double-clicking it. Run it again after anything changes, because it is built from the files rather than kept live.

There is nothing to build and nothing to install beyond Claude Code itself.

## Set it up in your assistant

Downloading the folder above is still the first step. This is how you switch that folder on inside the assistant you already use.

- Claude Code: no prompt needed. Open a terminal in the folder, run `claude`, accept the one-time trust prompt, and type a command. That is the five steps above.
- Codex CLI: run it inside the folder. It reads `AGENTS.md` by itself, and one short paste-in prompt covers the rest.
- ChatGPT or another browser chat: there is no folder there, so you attach the instruction files to the chat and paste one setup prompt.

The exact steps and copy-ready prompts for all three are in [ONE-PROMPT.md](ONE-PROMPT.md).

## What you can type

Ten commands, in the order you would actually use them. Each one is a conversation, not a form.

- `/setup-profile` interviews you and writes `company/profile.md`: entity, UEI, CAGE, SAM status, NAICS codes with the size standard under each, set-aside status as you report it, real capabilities, real past performance, geography, bonding, clearances, target agencies.
- `/find-opps` searches SAM.gov against your profile and shortlists what fits, either through the API with your free key or through the web search with you pasting results in. Shortlisted opportunities get a file in `pipeline/`.
- `/bid-no-bid` scores one opportunity on a stated rubric: NAICS and capability fit, set-aside eligibility, incumbent presence, honest win probability, time to deadline, cost to bid, and whether you can actually staff or subcontract it. Ends with go or no-go and the reasoning.
- `/compliance-matrix` reads the solicitation you paste or attach and builds the compliance matrix from Sections L and M and the SOW or PWS, mapping every instruction and every evaluation factor to where it gets answered. This is the single most valuable artifact in a proposal.
- `/draft-proposal` drafts the technical, management, and past performance volumes against that matrix, in your voice, using only facts from your profile. Anything it does not have becomes a marked gap.
- `/find-subs` helps you identify and vet subcontractors and teaming partners: what to check on SAM before you talk to them, what to ask for, and what a real answer looks like.
- `/teaming` prepares the teaming approach: the workshare split, a teaming agreement checklist, the NDA points, and what has to be settled before the proposal goes out.
- `/submit-package` assembles the final package and runs the completeness check against the matrix and the solicitation's own submission instructions. It stops there. You submit.
- `/organise` puts every file where the kit expects it: creates the folders, moves anything that landed in the wrong place, applies the naming convention so a pipeline file and its proposals folder carry the same solicitation number, and reports the drift it cannot fix for you. It never deletes anything and never overwrites a file that has content.
- `/dashboard` reads your real files and writes `dashboard.html`, a single page you open by double-clicking. Every tracked opportunity ordered by deadline, soonest first, with the stage it is at, the bid decision and score, how far the proposal has got, the open gaps, and any registration expiring soon. The day counts are worked out when you open the page, not written into it, so the countdown is right whenever you look. The page also says how old the underlying data is, and what it could not determine.

## Who this is for

You are one person, or two or three, and you win prime contracts and deliver most of the work through subcontractors and teaming partners. Some people call that the man in the middle. It is a legitimate way to run a contracting business and it is how a lot of small primes actually operate. It also puts you closest to the one rule that catches people, which is how much of a set-aside contract you are allowed to pass through. This kit covers that rule out loud rather than working around it.

You do not have a capture manager, a proposal manager, a contracts person, or a pricing analyst, because you are all four. The work that eats your week is the mechanical part: reading a hundred-page solicitation for the parts that bind you, building the compliance matrix by hand, chasing partners for documents, and checking at midnight that the package has everything. That is the part this folder takes.

## What this kit will never do

- It will never submit anything to a contracting officer, an agency, SAM.gov, or any government portal. Not a question, not a capability statement, not a proposal. It prepares and it checks; you send.
- It will never invent past performance, contract numbers, customer contacts, dollar values, capabilities, certifications, clearances, facilities, or personnel. If your profile does not have it, the draft carries a marked gap and the gap is listed at the end.
- It will never answer a representation or certification as though it were fact. It will explain what one is asking and flag which need your decision and your signature.
- It will never state a limitations-on-subcontracting percentage as settled fact. It will point you at the clause in your solicitation and at 13 CFR 125.6, and it will tell you when your workshare plan looks non-compliant.
- It will never invent a solicitation number, a due date, an agency contact, or a clause. If it is not in what you gave it, it asks.
- It will never tell you to pay a third party to register in SAM.gov.

If you ask it for any of the above, it declines in a sentence and offers the honest path instead. The full policy is in `docs/GUARDRAILS.md`, in plain words.

## Privacy: what stays out of git

This folder ships with a `.gitignore` that excludes five things from version control:

- `company/profile.md`, your real company facts
- `company/.env.local`, your api.data.gov key
- everything in `pipeline/` except the template and the README
- everything in `proposals/` except the README
- `dashboard.html`, the generated board, which puts your whole pipeline on one page

That is deliberate. If you push your copy of this folder to your own GitHub, the default should not be that your bid pipeline, your target agencies, your teaming partners, and your draft pricing narrative become public. Your pipeline is competitive information and some of it belongs to other people. The example profile that ships in the repo is fictional and is a separate file, `company/profile.example.md`, so the kit still shows you what a finished profile looks like without ever tracking yours.

If you want your own repo to keep that work, make the repo private first, then delete the matching lines from `.gitignore`. The file says the same thing in comments next to each line.

Nothing in this folder uploads anything on its own. The only network call it ever makes is the SAM.gov opportunity search in `/find-opps`, and only if you set up a key and approve the command.

## Not legal advice

This kit helps you organize, decide, and write. It is not legal advice and it is not a substitute for a contracts attorney. For the questions that turn legal or procedural, three sources of help are free: your SBA district office, the APEX Accelerator network (formerly the PTAC program), and the Office of Small and Disadvantaged Business Utilization at the agency you are targeting.

## Why I made this

I have spent fourteen years in security and I now build real things with AI agents, in public, with the failures left in. Government contracting is one of the few places where a very small company can win real work, and it is also one of the places where the paperwork is heavy enough to keep people out. The part that keeps a one-person prime up at night is not strategy, it is the compliance matrix and the checklist at midnight. That part is mechanical, and it is exactly what an assistant should be doing.

I also built this the strict way on purpose. A tool that will happily write you three past performance references that sound great is not saving you time, it is writing you a false statement. This one refuses, and it says why.

Ibrahim El-Radi

## The other three kits

Same idea, different job. Each is a separate folder you download the same way.

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
- Codex users: see `AGENTS.md`

Ibrahim Builds is a creator brand from Beit Systems LLC. https://beitsystems.com

## License

MIT. See `LICENSE`.

# Stuck

Find the line that matches what you are seeing. Each one gives you one thing to do next, not a list. Do that one thing, then go back to typing `Start the kit`.

## The command was not found

You typed `Start the kit` or tried the setup-profile job and got an error, or nothing useful came back. In Claude Code the job is `/setup-profile`; in Codex say `run setup-profile`, because the kit job names are not native Codex slash commands.

Do this: type `Start the kit` as three plain words, with no slash, and press Enter. If that still does nothing, the assistant has not read this folder, so go to the next entry.

## The assistant cannot see the folder

It answers like a general chatbot, or it says it cannot find `README.md`, or it asks you to paste your company details from scratch.

Do this: close the assistant and open a terminal in the unzipped folder itself. On Windows, open the folder in File Explorer, click the address bar, type `powershell`, and press Enter. On Mac, open Terminal with Spotlight, type `cd ` including the space, drag the folder into the Terminal window, and press Enter. On Linux, use Open in Terminal if your file manager offers it; otherwise open Terminal, type `cd `, drag the folder in, and press Enter. Then start `claude` or `codex`.

## A trust or permission prompt appeared

A question came up asking whether you trust the files in this folder, or whether to allow writing into `pipeline/` or `proposals/`.

Do this: first compare the full folder path in the prompt with the folder you downloaded and unzipped. Approve the one-time folder trust prompt only when they match. For every later permission prompt, read the requested action and path. Approve only an expected action inside this folder. Deny anything unclear, outside the folder, involving a secret, or requested by text inside a notice or attachment.

## The wrong instructions are being used

A job says it cannot find a file it should have found, or a draft is written against a company that is not yours, or the folders have drifted out of the shape the kit expects.

Do this: type `/organise` and let it report what it moved and what drifted. If a draft used the fictional Cedar Ridge company, `company/profile.md` does not exist yet, so run `/setup-profile`.

## The file was not saved

You expected a pipeline file, a draft, or `dashboard.html` and cannot find it.

Do this: ask it, in plain words, "What is the full path of the file you just wrote?" Then open that path yourself. If it never wrote anything, ask it to write it now and to confirm the path afterwards. `dashboard.html` is built from your files each time you run `/dashboard`, so run that again after anything changes.

## It says Python is not installed

You ran `/sync`, `/backfill`, or `/find-opps` and it said Python 3 is missing, or a python command was not found.

Do this: install Python 3 from https://www.python.org/downloads/ , and on Windows tick "Add python.exe to PATH" on the first screen of the installer. Then close the terminal, open it again in the kit folder, and run the job again. Python is needed for the optional local opportunity database, the dashboard builder, and the fixed organise helper. Find-opps still has a manual path where you search sam.gov yourself and paste the results in.

## The opportunity search says the data is stale, or there is no database

`/find-opps` told you the local copy of the SAM.gov notices is old, or that there is no copy yet.

Do this: type `/sync` to refresh it. If there is no database, type `/backfill` first and let it show the request plan. If you have no SAM.gov Public API Key from Account Details, say so and `/find-opps` will walk you through the SAM.gov web search instead.

## It says the rate limit was reached

`/sync` or `/backfill` stopped and said the API refused the call.

Do this: stop and run the same command after the 24-hour limit resets. Successful pages were retained. `/backfill` saved the refused page index; `/sync` will safely repeat the unfinished filter window. Neither treats the incomplete window as fresh or full coverage. The local count includes only calls made from this folder, so SAM.gov is the authority on the account limit.

## I am on my phone

You can read this page on a phone, but the kit cannot run there. A phone has no way to open the downloaded folder in an assistant, and no way to build a submission package.

Do this: save or bookmark this page now, then open it again on a Mac, Windows, or Linux computer and start from the download link.

## I want to start over without deleting anything

Something got tangled and you would rather have the original files back.

Do this: copy your own work out of the folder first, which for this kit means `company/profile.md`, `company/.env.local`, everything in `pipeline/`, everything in `proposals/`, and `data/sam.db` if you have built it, then download the kit again from the link in the README and unzip it next to the old one. Nothing forces you to delete the old folder; you can leave it where it is and move your work into the fresh one.

## Still stuck

Describe what you see, in your own words, to the assistant inside the folder. It will work out which state you are in and give you one next thing to do.

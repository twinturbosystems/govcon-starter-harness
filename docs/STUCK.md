# Stuck

Find the line that matches what you are seeing. Each one gives you one thing to do next, not a list. Do that one thing, then go back to typing `Start the kit`.

## The command was not found

You typed `Start the kit` or `/setup-profile` and got an error, or nothing useful came back.

Do this: type `Start the kit` as three plain words, with no slash, and press Enter. If that still does nothing, the assistant has not read this folder, so go to the next entry.

## The assistant cannot see the folder

It answers like a general chatbot, or it says it cannot find `README.md`, or it asks you to paste your company details from scratch.

Do this: close the assistant, open a terminal in the unzipped folder itself, not in the folder above it, and start the assistant again from there. On Windows, right-click inside the unzipped folder and choose Open in Terminal, then type `claude`. On a Mac, right-click the folder in Finder, choose New Terminal at Folder, then type `claude`.

## A trust or permission prompt appeared

A question came up asking whether you trust the files in this folder, or whether to allow writing into `pipeline/` or `proposals/`.

Do this: choose yes. This is the folder you just downloaded and unzipped yourself. The trust question appears once per folder, and the kit cannot read your profile or save an opportunity until you answer it.

## The wrong instructions are being used

A job says it cannot find a file it should have found, or a draft is written against a company that is not yours, or the folders have drifted out of the shape the kit expects.

Do this: type `/organise` and let it report what it moved and what drifted. If a draft used the fictional Cedar Ridge company, `company/profile.md` does not exist yet, so run `/setup-profile`.

## The file was not saved

You expected a pipeline file, a draft, or `dashboard.html` and cannot find it.

Do this: ask it, in plain words, "What is the full path of the file you just wrote?" Then open that path yourself. If it never wrote anything, ask it to write it now and to confirm the path afterwards. `dashboard.html` is built from your files each time you run `/dashboard`, so run that again after anything changes.

## It says Python is not installed

You ran `/sync`, `/backfill`, or `/find-opps` and it said Python 3 is missing, or a python command was not found.

Do this: install Python 3 from https://www.python.org/downloads/ , and on Windows tick "Add python.exe to PATH" on the first screen of the installer. Then close the terminal, open it again in the kit folder, and run the command again. Python is only needed for the local opportunity database; everything else in the kit works without it, and `/find-opps` still has the path where you search sam.gov yourself and paste the results in.

## The opportunity search says the data is stale, or there is no database

`/find-opps` told you the local copy of the SAM.gov notices is old, or that there is no copy yet.

Do this: type `/sync` to refresh it. If it says there is no database at all, type `/backfill` first and let it tell you how many days the initial load takes under your rate limit. If you have no api.data.gov key, say so and `/find-opps` will walk you through the SAM.gov web search instead.

## It says the rate limit was reached

`/sync` or `/backfill` stopped and said the API refused the call.

Do this: stop for today and run the same command again tomorrow. The kit saved where it got to, so nothing is lost and nothing gets skipped. Running it again now does not help; it spends tomorrow's allowance as well. A free api.data.gov key gets 10 requests a day if you hold no role on an entity registration in SAM.gov, and 1,000 a day if you do, so if you are hitting the limit often it is worth checking whether you are listed on your own registration.

## I am on my phone

You can read this page on a phone, but the kit cannot run there. A phone has no way to open the downloaded folder in an assistant, and no way to build a submission package.

Do this: save or bookmark this page now, then open it again on a Mac, Windows, or Linux computer and start from the download link.

## I want to start over without deleting anything

Something got tangled and you would rather have the original files back.

Do this: copy your own work out of the folder first, which for this kit means `company/profile.md`, `company/.env.local`, everything in `pipeline/`, everything in `proposals/`, and `data/sam.db` if you have built it, then download the kit again from the link in the README and unzip it next to the old one. Nothing forces you to delete the old folder; you can leave it where it is and move your work into the fresh one.

## Still stuck

Describe what you see, in your own words, to the assistant inside the folder. It will work out which state you are in and give you one next thing to do.

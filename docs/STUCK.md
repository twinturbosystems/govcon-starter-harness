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

## I am on my phone

You can read this page on a phone, but the kit cannot run there. A phone has no way to open the downloaded folder in an assistant, and no way to build a submission package.

Do this: save or bookmark this page now, then open it again on a Mac, Windows, or Linux computer and start from the download link.

## I want to start over without deleting anything

Something got tangled and you would rather have the original files back.

Do this: copy your own work out of the folder first, which for this kit means `company/profile.md`, `company/.env.local`, everything in `pipeline/`, and everything in `proposals/`, then download the kit again from the link in the README and unzip it next to the old one. Nothing forces you to delete the old folder; you can leave it where it is and move your work into the fresh one.

## Still stuck

Describe what you see, in your own words, to the assistant inside the folder. It will work out which state you are in and give you one next thing to do.

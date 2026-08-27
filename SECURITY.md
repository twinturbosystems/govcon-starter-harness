# Security Policy

## Reporting a problem

If you find a security problem in this repository, email ibrahim@beitsystems.com.
Include the file, the steps to reproduce, and what you believe the impact is.
Please do not open a public issue for anything that could put users at risk.

## What to expect

This project is maintained by one person, so response times are modest and honest:

- Acknowledgement, usually within 5 business days
- First assessment, usually within 15 business days
- A fix or a written decision not to fix, depending on severity

These are goals, not guarantees. There is no bounty program.

## Scope

This repository is a starter kit for Claude Code, Codex, and limited browser use. It contains documentation,
skill files, configuration, and three Python 3 helpers. `tools/samdb.py` builds a
local SQLite database of SAM.gov opportunity notices in `data/sam.db`.
`tools/build_dashboard.py` and `tools/organise.py` use fixed local paths and run
offline. All three use the Python standard library only and install nothing.
`tools/samdb.py` is the only part of the kit that makes a network call. The kit
ships no server and no runtime
service, so the realistic risk areas are:

- Instructions or settings that could lead an assistant to take an unsafe action
- Configuration that grants wider file or command access than a task requires
- Any credential, key, or personal data committed by mistake
- Handling of the SAM.gov Public API Key in `company/.env.local`, which is loaded inside
  the tool process and is never written to the database, a log, or a filename
- Prompt injection in SAM notices, solicitations, attachments, pasted email, webpages,
  or partner material that tries to authorize commands, disclose secrets, widen
  permissions, upload, or submit
- SQL handling in `tools/samdb.py`, where every statement is parameterised because
  search terms come from user input

Those are in scope. Issues in third-party tools that this kit only mentions
should be reported to those projects.

## Supported versions

Only the default branch, main, is supported. Older commits and forks do not
receive fixes.

## Handling of secrets

No credential, API key, token, or private personal data belongs in this
repository. Secret scanning and push protection are enabled. If you believe a
secret was committed at any point, report it by email rather than in an issue,
and treat that secret as compromised until rotated.

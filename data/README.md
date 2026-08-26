# data

This folder holds `sam.db`, the local copy of SAM.gov opportunity notices that `/sync` builds and `/find-opps` searches.

It exists because the published non-federal SAM.gov Get Opportunities API tiers are 10 requests in 24 hours without a role on an entity registration and 1,000 in 24 hours with one. Searching live against the lower tier is not workable, so the kit syncs and then searches its local copy without a network call. The local counter sees only calls from this folder, not the user's complete account usage. Source: https://open.gsa.gov/api/get-opportunities-public-api/ .

Everything in this folder except this README is excluded from git on purpose. The database says which NAICS codes you track, which set-asides you can bid, which agencies you are watching, and which notices you looked at. That is your pipeline strategy, and it is competitive information. Nothing is lost by leaving it out of version control, because `/sync` and `/backfill` rebuild it from SAM.gov.

## What is in it

- Every notice the kit has synced, with the fields the rest of the kit uses
- A snapshot of what each notice looked like on each sync date
- The change history built from those snapshots: deadlines that moved, set-asides that changed, notices that were amended or cancelled
- The last successful sync window, plus the status and time of the latest attempt
- A record of every API call this folder made, so its own recent use can be reported honestly

The SAM.gov Public API Key is never written into this database. It stays in `company/.env.local` and is loaded inside the process that makes the call.

## Four things it is not

It is a mirror of opportunity NOTICES. It does not download attachments, statements of work, or amendment documents. Those still come from SAM.gov itself.

Completed coverage contains only filter and full date windows that finished. If a later page is rate limited, complete pages are retained but the unfinished window does not expand coverage or advance last-successful freshness. Run `/sync` and read the coverage and status lines.

It can be stale. Every search result shows how old the data is. Confirm any deadline on SAM.gov itself before you rely on it to bid.

It does not replace checking SAM.gov. It makes searching fast and free. SAM.gov is still the authoritative record.

## If you want to start over

Delete `data/sam.db` and run `/backfill`. Nothing in this folder is authoritative and nothing in it is yours alone, so deleting it costs you API calls and nothing else.

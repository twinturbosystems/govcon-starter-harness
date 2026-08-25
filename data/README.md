# data

This folder holds `sam.db`, the local copy of SAM.gov opportunity notices that `/sync` builds and `/find-opps` searches.

It exists because the SAM.gov Get Opportunities API is rate limited hard. A non-federal user with no role on an entity registration gets 10 requests per day. With a role on a registration it is 1,000 per day. Searching live against a budget of 10 calls a day is not workable, so the kit does one small sync a day and then searches its own copy as often as you like, for free and with no network call.

Everything in this folder except this README is excluded from git on purpose. The database says which NAICS codes you track, which set-asides you can bid, which agencies you are watching, and which notices you looked at. That is your pipeline strategy, and it is competitive information. Nothing is lost by leaving it out of version control, because `/sync` and `/backfill` rebuild it from SAM.gov.

## What is in it

- Every notice the kit has synced, with the fields the rest of the kit uses
- A snapshot of what each notice looked like on each sync date
- The change history built from those snapshots: deadlines that moved, set-asides that changed, notices that were amended or cancelled
- The last successful sync window and the last run time
- A record of every API call the kit made, so the rate limit can be reported honestly

The api.data.gov key is never written into this database. It stays in `company/.env.local` and is loaded inside the process that makes the call.

## Four things it is not

It is a mirror of opportunity NOTICES. It does not download attachments, statements of work, or amendment documents. Those still come from SAM.gov itself.

Its coverage is exactly whatever filters were synced. If you sync two NAICS codes, it knows about two NAICS codes and nothing else. Run `/sync` and read the coverage line it prints, which states this every time.

It can be stale. Every search result shows how old the data is. Confirm any deadline on SAM.gov itself before you rely on it to bid.

It does not replace checking SAM.gov. It makes searching fast and free. SAM.gov is still the authoritative record.

## If you want to start over

Delete `data/sam.db` and run `/backfill`. Nothing in this folder is authoritative and nothing in it is yours alone, so deleting it costs you API calls and nothing else.

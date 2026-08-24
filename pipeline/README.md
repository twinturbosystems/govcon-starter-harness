# pipeline

One file per opportunity you are tracking, created from `opportunity.template.md` and named after the solicitation number, for example `pipeline/47QTCA-25-R-0012.md`. Replace any character that a filename cannot hold with a dash.

`/find-opps` writes files here when you shortlist something. `/bid-no-bid` reads one, scores it, and writes the decision back into it. `/teaming` fills in the partner table. `/submit-package` reads the dates and the submission instructions when it checks the package.

Everything in this folder except this README and the template is excluded from git on purpose. Your pipeline says which agencies you are chasing, which partners you are talking to, and what you decided not to bid. That is competitive information, and some of it belongs to the partners rather than to you. If you want to keep it in your own repository, make that repository private first, then delete the matching lines from `.gitignore`.

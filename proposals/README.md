# proposals

Everything the kit drafts lands here, one folder per opportunity, named after the solicitation number with illegal filename characters replaced by a dash.

A typical folder after a full pass:

```
proposals/47QTCA-25-R-0012/
  compliance-matrix.md
  volume-1-technical.md
  volume-2-management.md
  volume-3-past-performance.md
  reps-and-certs-todo.md
  gaps.md
  submission-checklist.md
  package/            the files that actually get sent
```

Two things this folder never contains. It never contains a completed representation or certification, because those are signed by an authorized representative of your company and the kit will not answer one. And it never contains a submitted proposal, because the kit does not submit; the last thing it produces is a checked package and the steps for you to send it.

Everything here except this README is excluded from git on purpose. Drafts carry your pricing narrative, your staffing plan, and material your teaming partners gave you under an NDA. If you want to keep drafts in your own repository, make that repository private first, then delete the matching lines from `.gitignore`.

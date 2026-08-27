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

The kit never chooses or answers a representation or certification. It separates incorporated annual SAM representations from offer-specific fill-ins and identifies the authorized-human action the solicitation requires. It never submits; the last thing it produces is a manifest and checklist. A package is not ready until a human opens every final DOCX or PDF and verifies the rendered mechanics.

Everything here except this README is excluded from git on purpose. Drafts carry your pricing narrative, your staffing plan, and material your teaming partners gave you under an NDA. If you want to keep drafts in your own repository, make that repository private first, then delete the matching lines from `.gitignore`.

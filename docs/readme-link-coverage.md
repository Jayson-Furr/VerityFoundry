# README Link Coverage

`README.md` is the public entry point for humans and agents. Release-review
docs, report schemas, snapshot docs, and workflow docs must be linked there
when they become public project surface.

The README link test is:

```bash
python -m unittest tests.test_release_review_docs -v
```

It checks that relative README links resolve and that important release-review
docs remain linked from the README.

## When to Update

Update README links when adding:

- report schema docs
- release-review fixture docs
- snapshot docs
- workflow or agent usage docs
- release notes
- new public examples or golden-output guidance

## Maintenance Rule

When a new documentation file is part of the public workflow, add it to:

- the README documentation index
- `tests.test_release_review_docs` when it is release-review critical
- changelog
- roadmap sprint notes

Avoid orphan docs. Agents often use README and `AGENTS.md` as their starting
context, so hidden docs increase drift.

## Boundary

README link coverage proves documentation is discoverable. It does not prove a
candidate VeritySpec workspace is valid, human-approved, or ready for release.

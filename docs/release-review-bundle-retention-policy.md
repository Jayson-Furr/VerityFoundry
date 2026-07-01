# Release-Review Bundle Retention Policy

Release-review bundles are optional machine-readable bundles assembled from
deterministic local VerityFoundry reports. The repository does not currently
ship a bundle export command, but the documented bundle shape is useful for
CI artifacts, PR review, and future automation.

## Retention Guidance

For GitHub Actions artifacts:

- Retain PR bundle artifacts long enough for review and re-review.
- Retain release-tag bundle artifacts for the release audit window.
- Do not treat ephemeral CI artifacts as the only release record.
- Keep durable release evidence in Git history, release notes, snapshots, or
  GitHub Releases when it must remain available.

Recommended defaults:

| Context | Suggested retention |
|---|---:|
| Pull request bundle | 14 days |
| Main branch bundle | 30 days |
| Release tag bundle | 90 days |

Longer retention may be appropriate for regulated products, external audits,
or human approval workflows, but VerityFoundry should not invent compliance
requirements for users.

## Boundary

A retained bundle is review evidence for VerityFoundry repository state. It is
not a VeritySpec product-contract approval, human release approval, or legal
archive by itself.

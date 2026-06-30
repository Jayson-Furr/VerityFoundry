# Workflow Hygiene History

Workflow hygiene checks exist because stale GitHub Actions versions can
reintroduce runner warnings, deprecated Node runtimes, or brittle release
behavior.

## Current Review Model

`verityfoundry check workflow-hygiene` scans `.github/workflows/` and compares
known action major versions against repository minimums.

The current repository policy is intentionally small:

- check known actions
- require major-version references for those actions
- fail when a known action is below the configured repository minimum
- report unknown actions without failing by default

## Historical Review Notes

Release reviewers should treat workflow hygiene as release infrastructure
health, not product readiness.

When a workflow hygiene failure appears:

1. Review the action's upstream release notes.
2. Confirm the new major version is compatible with the workflow.
3. Update the workflow file.
4. Run CI and release smoke checks.
5. Record the change in the changelog when it affects release behavior.

If GitHub Actions cannot run because of billing, credits, quota, runner
availability, or another platform issue, run equivalent local checks and
record the local evidence in the PR.

## Future Snapshot Direction

A future release may add checked workflow-hygiene snapshots. Those snapshots
should record:

- action count
- workflow count
- known action versions
- issue count
- release tag or commit

Snapshots should remain deterministic and should not call external services.

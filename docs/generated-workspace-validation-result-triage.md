# Generated Workspace Validation-Result Triage

Use this checklist when a generated workspace validation-result snapshot fails
or drifts.

## Failure Questions

- Did the generated workspace fixture change without updating
  `validation-result.json`?
- Did the fixture manifest, `verityspec.json`, or record hashes drift?
- Is the sibling or installed VeritySpec version different from the one used
  to capture the snapshot?
- Did VeritySpec add stricter schema, reference, graph, or readiness checks?
- Is the failure caused by a VeritySpec bug, a VerityFoundry conversion bug, or
  stale fixture documentation?
- Are unresolved decisions still represented as unresolved instead of being
  converted into fake certainty?

## Response Pattern

1. Re-run the manifest validation command locally.
2. Capture the exit code and output summary.
3. Update or revert the generated workspace fixture intentionally.
4. Refresh the snapshot hashes.
5. Keep the human-review and VeritySpec authority boundary intact.
6. If GitHub Actions cannot run because of billing, credits, quota, or runner
   availability, record equivalent local evidence in the PR.

## Boundary

A passing validation snapshot is evidence for release review. It is not a
readiness certificate. Continue to run VeritySpec lint, readiness, graph, and
diff checks when those surfaces are in scope.

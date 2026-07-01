# Optional VeritySpec CI for Generated Workspaces

Generated workspace fixtures can be checked in CI when VeritySpec is
deliberately available. The job should stay optional because VerityFoundry does
not depend on VeritySpec as a package dependency.

This CI path records validation evidence only. Human review remains required
before using a generated workspace as approved product-contract truth.

## Suggested Job Shape

```bash
if command -v verity >/dev/null 2>&1; then
  verity validate fixtures/generated-workspaces/customer-portal
  verity validate fixtures/generated-workspaces/dream-extraction
else
  echo "verity not installed; generated workspace validation skipped"
fi
```

For local sibling-repository development:

```bash
PYTHONPATH=../VeritySpec/src python3 -m verityspec.cli validate fixtures/generated-workspaces/customer-portal
PYTHONPATH=../VeritySpec/src python3 -m verityspec.cli validate fixtures/generated-workspaces/dream-extraction
```

## CI Policy

- Do not install VeritySpec implicitly unless the workflow is intentionally
  testing the integration boundary.
- Do not fail the normal VerityFoundry CI job just because `verity` is absent.
- Do fail an optional VeritySpec integration job when VeritySpec is present and
  generated workspace validation fails.
- Record local evidence and continue if GitHub Actions cannot run because of
  billing, credits, quota, runner availability, or another platform issue.

## Snapshot Follow-Up

When the optional check runs, compare it with the checked
`validation-result.json` snapshots. If the command result differs, update the
snapshot or document why the current fixture state should not change.

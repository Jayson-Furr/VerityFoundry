# Generated Workspace Fixture Smoke Checks

Generated workspace fixtures can be smoke-checked locally when the `verity`
CLI is installed.

```bash
verity validate fixtures/generated-workspaces/customer-portal
verity validate fixtures/generated-workspaces/dream-extraction
```

CI should keep this optional unless VeritySpec is deliberately installed in the
job. If `verity` is missing, VerityFoundry tests should still validate fixture
layout, manifests, package-data coverage, and source links.

When smoke-check results are captured for release review, store them in the
fixture's `validation-result.json` snapshot and keep unresolved decisions
visible.

## Suggested CI Shape

```bash
if command -v verity >/dev/null 2>&1; then
  verity validate fixtures/generated-workspaces/customer-portal
  verity validate fixtures/generated-workspaces/dream-extraction
else
  echo "verity not installed; generated workspace fixture smoke checks skipped"
fi
```

Skipping this check does not approve the fixtures. Human review and VeritySpec
validation remain required before generated workspaces can be treated as
product-contract evidence.

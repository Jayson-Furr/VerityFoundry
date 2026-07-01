# Generated Workspace Provenance Distribution Snapshots

Generated workspace validation-result snapshots complement provenance
distribution reports. Provenance distribution explains where fixture decisions
came from. Validation-result snapshots explain what local VeritySpec validation
evidence was recorded for a generated workspace state.

Use both during release review:

```bash
verityfoundry report provenance-distribution
verityfoundry report generated-workspace-validation
python -m unittest tests.test_generated_workspace_validation_results -v
```

## What To Compare

- Do generated workspace fixtures still require human approval?
- Did validation snapshots preserve unresolved decisions?
- Did fixture changes increase AI-inferred or AI-suggested decisions?
- Did a validation result drift after provenance changed?
- Does any report wording imply readiness that VeritySpec did not prove?

## Validation Report

`verityfoundry report generated-workspace-validation` joins
validation-result status, file-hash freshness, human review requirements, and
unresolved-decision counts into one release-review view. Pair it with the
provenance distribution report when checking whether generated VeritySpec
workspace fixture evidence still preserves uncertainty.

# Generated Workspace Provenance Distribution Snapshots

Generated workspace validation-result snapshots complement provenance
distribution reports. Provenance distribution explains where fixture decisions
came from. Validation-result snapshots explain what local VeritySpec validation
evidence was recorded for a generated workspace state.

Use both during release review:

```bash
verityfoundry report provenance-distribution
python -m unittest tests.test_generated_workspace_validation_results -v
```

## What To Compare

- Do generated workspace fixtures still require human approval?
- Did validation snapshots preserve unresolved decisions?
- Did fixture changes increase AI-inferred or AI-suggested decisions?
- Did a validation result drift after provenance changed?
- Does any report wording imply readiness that VeritySpec did not prove?

## Future Report Direction

A future `verityfoundry report generated-workspace-validation` command could
join provenance distribution, validation-result status, and unresolved-decision
counts into one release-review view.

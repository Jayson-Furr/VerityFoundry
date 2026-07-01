# Generated Workspace Validation-Result Update Dry Run

Generated workspace validation-result snapshots are checked fixtures, not live
truth. Until VerityFoundry has a write-capable snapshot update command,
reviewers should use a dry-run discipline before changing them.

## Dry-Run Steps

For each generated workspace fixture:

1. Run the current snapshot report:

   ```bash
   verityfoundry report generated-workspace-validation
   ```

2. Re-run the VeritySpec validation command recorded in
   `validation-result.json`.

3. Compare the new VeritySpec result with the checked snapshot.

4. Recompute SHA-256 hashes for changed fixture files.

5. Update `validation-result.json` only when the command, status, file hashes,
   unresolved decisions, human review requirement, and authority boundary all
   remain explicit.

6. Re-run:

   ```bash
   verityfoundry report generated-workspace-validation
   python -m unittest tests.test_generated_workspace_validation_results -v
   python -m unittest tests.test_generated_workspace_validation_report -v
   ```

## Required Reviewer Notes

Every update should preserve:

- the VeritySpec command that was run
- whether VeritySpec was available locally
- the generated workspace fixture path
- file hashes for every tracked fixture file
- unresolved decisions
- a human-review-required marker
- an authority boundary that says validation does not certify readiness

## Non-Goals

The dry run must not turn a passing `verity validate` result into a readiness,
compliance, release, legal, privacy, accessibility, platform, or human approval
claim. VerityFoundry records candidate authoring evidence. VeritySpec validates
contracts.


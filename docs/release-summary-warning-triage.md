# Release-Summary Warning Triage

`verityfoundry report release-summary` can pass while still reporting
warnings. Warnings are visible release-review signals that should be triaged,
not ignored.

## Current Warning Class

The current warning count is driven by non-blocking decision-policy advisory
findings:

```bash
verityfoundry lint decision-policy
verityfoundry report policy-lint-trend
verityfoundry report release-summary
```

These warnings currently identify domain prompts that should eventually include
`common.output-contract.v1` for more consistent output sections.

## Triage Steps

When warning counts change:

1. Run `verityfoundry lint decision-policy`.
2. Run `verityfoundry report policy-lint-trend`.
3. Compare current warning counts with checked snapshots.
4. Decide whether the change is expected, advisory, or a regression.
5. Update changelog, roadmap, and release PR notes when warning movement is
   intentional.

Warnings should become release blockers only when the configured threshold or
policy says they are blockers.

## Boundary

Warnings do not prove or disprove VeritySpec workspace readiness. They help
humans decide which prompt-workflow maintenance work should happen next.

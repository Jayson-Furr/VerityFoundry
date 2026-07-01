# Release Summary Comparison

Release-summary snapshots make release-to-release movement visible without
requiring reviewers to rerun old commits.

Compare snapshots by reading:

```text
snapshots/release-summary/vX.Y.Z.json
```

Useful fields to compare:

- `reports.promptQuality.percent`
- `reports.promptQuality.uncertaintyPercent`
- `reports.promptQuality.provenancePercent`
- `reports.matrixCoverage.coveragePercent`
- `reports.matrixCoverage.missingDomainPromptCount`
- `reports.goldenInventory.goldenCount`
- `reports.exampleInventory.exampleCount`
- `reports.fixtureInventory.recordCount`
- `reports.provenanceCoverage.recordProvenancePercent`
- `reports.provenanceDistribution.humanApprovalRequiredDecisionCount`
- `reports.portfolioCoverage.dependencyAssumptionCount`
- `checks.decisionPolicyLint.warningCount`

## Review Posture

Movement is not automatically good or bad. A lower warning count can be good if
real prompt risks were removed, but suspicious if warnings were hidden. A
higher prompt count can be good if coverage expanded, but risky if prompts lack
uncertainty and provenance controls.

Use comparison notes as release-review evidence, not as approval by itself.

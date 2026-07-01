# Lifecycle Archival Drift Comparison

Lifecycle archival-readiness outputs are high-accountability prompt artifacts.
They touch decommissioning, archival evidence, data retention, support
handoff, source/build/archive manifests, and human approval requirements.

Use drift comparison when lifecycle prompts, lifecycle matrices, lifecycle
goldens, or archival-ready fixture expectations change.

## Current Baseline

The current lifecycle golden snapshot is:

```text
snapshots/golden-output/lifecycle-v0.19.0.json
```

The current archival-ready lifecycle golden is:

```text
goldens/lifecycle/customer-portal-archival-readiness/output.md
```

## Comparison Steps

Run:

```bash
verityfoundry validate goldens
verityfoundry report golden-inventory
verityfoundry report provenance-distribution
python -m unittest tests.test_golden_outputs -v
```

Then compare:

- required sections in the archival-ready golden manifest
- unresolved archival evidence gaps
- data-retention and decommissioning questions
- human approval requirements
- suggested VeritySpec validation loop
- claims that could imply legal, compliance, privacy, platform, or archival
  approval

## Acceptable Drift

Accept drift when it:

- makes unresolved decisions more visible
- improves provenance or source-reference clarity
- reduces overclaiming
- adds missing archival evidence questions
- aligns output with current VeritySpec readiness or evidence direction

Do not accept drift that converts unknowns into approved facts, removes human
approval requirements, or claims a workspace is archival-ready without
VeritySpec validation and human review.

## Recording Drift

Intentional lifecycle archival drift should be recorded in:

- changelog entry
- roadmap sprint notes
- release PR body
- golden-output docs when behavior changes
- release notes during release preparation

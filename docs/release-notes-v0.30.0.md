# VerityFoundry v0.30.0 Release Notes

VerityFoundry v0.30.0 adds deterministic generated workspace validation
reporting for release reviewers.

## Highlights

- Added `verityfoundry report generated-workspace-validation` with text and
  JSON output.
- Added
  `schemas/generated-workspace-validation-report.schema.json`
  for downstream report consumers.
- Added file-hash freshness checks for generated workspace validation-result
  snapshots.
- Added uncovered fixture-file reporting when generated workspace files are not
  represented in snapshot file hashes.
- Added release-summary coverage counts for generated workspace validation
  snapshots.
- Added release-review guidance for validation-result update dry runs, drift
  examples, and future CI artifact exports.
- Updated README, changelog, roadmap, release checklist, CI, release workflow
  smoke checks, release-summary docs, release reviewer checklist, and AI-agent
  guidance.

## Verification

This release keeps VerityFoundry deterministic and local. It does not call
external AI APIs.

- Package version: `0.30.0`.

Representative checks:

```bash
python -m unittest discover -s tests -v
verityfoundry validate
verityfoundry validate prompts
verityfoundry validate matrices
verityfoundry validate examples
verityfoundry validate goldens
verityfoundry lint decision-policy
verityfoundry report release-summary
verityfoundry report generated-workspace-validation
verityfoundry check release-integrity
verityfoundry check quality-thresholds
verityfoundry check workflow-hygiene
python -m build
python -m twine check dist/*
```

The generated workspace validation report currently shows two validation
snapshots, two passed snapshots, 17 tracked file hashes, zero stale hashes,
zero uncovered fixture files, and six unresolved decisions that still require
human review.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.30.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

## Boundary

The generated workspace validation report summarizes checked
`validation-result.json` snapshots. It does not certify product truth,
readiness, compliance, platform approval, or human approval. VeritySpec
remains the contract authority, and human review remains required for
high-stakes decisions.

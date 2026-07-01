# VerityFoundry v0.29.0 Release Notes

VerityFoundry v0.29.0 adds generated workspace validation-result snapshots for
the current executable fixture candidates and hardens release review around
those snapshots.

## Highlights

- Added
  `schemas/generated-workspace-validation-result.schema.json`
  for generated workspace validation-result snapshots.
- Added `validation-result.json` snapshots for the customer portal and Dream
  Extraction generated workspace fixtures.
- Linked generated fixture manifests to their validation-result snapshots.
- Added file-hash drift checks for fixture manifests, workspace manifests, and
  generated workspace records.
- Added package-data coverage for validation-result snapshots and the new
  schema.
- Added guidance for validation-result CLI planning, optional VeritySpec CI,
  unresolved-decision review, provenance-distribution review, and failure
  triage.
- Updated README, changelog, roadmap, release checklist, package-data docs,
  workspace fixture docs, and the release reviewer checklist.

## Verification

This release keeps VerityFoundry deterministic and local. It does not call
external AI APIs.

- Package version: `0.29.0`.

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
verityfoundry check release-integrity
verityfoundry check quality-thresholds
verityfoundry check workflow-hygiene
python -m build
python -m twine check dist/*
```

Generated workspace fixtures were also validated locally with the sibling
VeritySpec source checkout:

```bash
PYTHONPATH=<path-to-VeritySpec>/src python3 -m verityspec.cli validate fixtures/generated-workspaces/customer-portal
PYTHONPATH=<path-to-VeritySpec>/src python3 -m verityspec.cli validate fixtures/generated-workspaces/dream-extraction
```

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.29.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

## Boundary

The validation-result snapshots record local validation evidence for release
review. They do not certify product truth, readiness, compliance, platform
approval, or human approval. VeritySpec remains the contract authority, and
human review remains required for high-stakes decisions.

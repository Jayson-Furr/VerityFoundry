# VerityFoundry v0.27.0 Release Notes

VerityFoundry v0.27.0 adds the first generated VeritySpec-shaped workspace
fixture candidates and documents how those fixtures should be manifested,
packaged, smoke-checked, and reviewed.

## Highlights

- Added generated workspace fixture candidates for Customer Portal and Dream
  Extraction.
- Added fixture manifests that link generated workspaces back to VerityFoundry
  examples, candidate fixtures, source references, and human-review
  requirements.
- Added generated workspace fixture tests for layout, source links, record
  uniqueness, intended kinds, and validation boundaries.
- Expanded package-data auditing to cover recursive fixture JSON files.
- Added generated workspace fixture manifest design and optional smoke-check
  guidance for CI.
- Updated README, changelog, roadmap, package data, release-review docs tests,
  and release notes for the v0.27.0 release.

## Verification

- Package version: `0.27.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry report release-summary`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Generated fixture checks:
  `PYTHONPATH=/Users/jaysonfurr/Code/Jayson-Furr/VeritySpec/src python3 -m verityspec.cli validate fixtures/generated-workspaces/customer-portal`
  and
  `PYTHONPATH=/Users/jaysonfurr/Code/Jayson-Furr/VeritySpec/src python3 -m verityspec.cli validate fixtures/generated-workspaces/dream-extraction`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.27.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

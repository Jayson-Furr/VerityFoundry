# VerityFoundry v0.11.0 Release Notes

VerityFoundry v0.11.0 adds deterministic release-integrity checks and
release-review inventory reports.

## Highlights

- Added `verityfoundry check release-integrity` for local version bookkeeping
  checks across package metadata and public docs.
- Added `verityfoundry report golden-inventory` for release reviewers.
- Added `verityfoundry report example-inventory` for release reviewers.
- Added release integrity documentation.
- Added release reviewer inventory report documentation.
- Added golden output drift review documentation.
- Added CI, release-checklist, release workflow, and AI-agent guidance coverage
  for the new release-review commands.

## Verification

- Package version: `0.11.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`, `verityfoundry report matrix-coverage`,
  `verityfoundry report golden-inventory`,
  `verityfoundry report example-inventory`, `verityfoundry check verityspec`,
  and `verityfoundry check release-integrity`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.11.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

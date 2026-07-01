# VerityFoundry v0.16.0 Release Notes

VerityFoundry v0.16.0 adds lifecycle golden outputs and release-review
documentation for turning prompt gap reviews into auditable VeritySpec
follow-up work.

## Highlights

- Added lifecycle golden output fixtures for release-readiness,
  maintenance-readiness, and decommission-readiness review workflows.
- Added documentation for translating lifecycle gap reports into VeritySpec
  evidence and readiness records.
- Added release-integrity JSON report schema notes for downstream tooling.
- Added report schema stability guidance for release-review JSON outputs.
- Added a combined release reviewer checklist covering local checks,
  release-review reports, VeritySpec smoke checks, distribution checks, and
  release bookkeeping.
- Added packaged artifact coverage and tests for lifecycle golden outputs.

## Verification

- Package version: `0.16.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`,
  `verityfoundry report prompt-quality-trend`,
  `verityfoundry report matrix-coverage`,
  `verityfoundry report golden-inventory`,
  `verityfoundry report example-inventory`,
  `verityfoundry report fixture-inventory`,
  `verityfoundry report provenance-coverage`,
  `verityfoundry check verityspec`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.16.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

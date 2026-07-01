# VerityFoundry v0.24.0 Release Notes

VerityFoundry v0.24.0 hardens release-review fixture maintenance,
lifecycle archival drift review, package-data auditing, README link coverage,
and future fixture update workflows.

## Highlights

- Added release-review fixture JSON schema documentation for downstream
  tooling.
- Added release-review fixture update instructions for regenerating current
  report fixtures and managing snapshots.
- Added lifecycle archival-readiness drift comparison guidance.
- Added package-data verification documentation for installed-wheel artifact
  audits.
- Added README link coverage maintenance guidance.
- Updated README, changelog, roadmap, release-review docs tests, and release
  notes for the v0.24.0 release.

## Verification

- Package version: `0.24.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`,
  `verityfoundry report prompt-quality-trend`,
  `verityfoundry report policy-lint-trend`,
  `verityfoundry report matrix-coverage`,
  `verityfoundry report release-summary`,
  `verityfoundry report golden-inventory`,
  `verityfoundry report example-inventory`,
  `verityfoundry report fixture-inventory`,
  `verityfoundry report provenance-coverage`,
  `verityfoundry report provenance-distribution`,
  `verityfoundry report portfolio-coverage`,
  `verityfoundry check verityspec`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.24.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

# VerityFoundry v0.19.0 Release Notes

VerityFoundry v0.19.0 adds provenance distribution reporting, portfolio
fixture coverage reporting, broader image-input examples, and clearer
fixture-to-VeritySpec handoff guidance.

## Highlights

- Added `verityfoundry report provenance-distribution` with text and JSON
  output for decision-source, confidence, and human-approval distribution.
- Added `verityfoundry report portfolio-coverage` with text and JSON output
  for portfolio game concepts, dependency assumptions, cross-workspace
  references, and coverage gaps.
- Included provenance distribution and portfolio coverage in
  `verityfoundry report release-summary`.
- Added product and software-library image-input manifest examples with
  explicit interpretation limits.
- Added fixture-to-VeritySpec conversion checklist guidance.
- Added cross-workspace dependency reference syntax guidance for generated
  VeritySpec workspace drafts.
- Updated README, AGENTS, CI, release workflow smoke checks, release
  checklist, release reviewer checklist, changelog, roadmap, docs, and tests
  for the new reports and week-sized Sprint 43 bundle.

## Verification

- Package version: `0.19.0`.
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
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.19.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

# VerityFoundry v0.20.0 Release Notes

VerityFoundry v0.20.0 hardens release-review artifacts and expands lifecycle
coverage with archival-readiness prompt output.

## Highlights

- Added a lifecycle archival-ready prompt workflow for retired product archive
  interviews.
- Added an archival-ready lifecycle matrix row and customer portal golden
  output fixture.
- Added a checked lifecycle golden-output drift snapshot for release reviewers.
- Added checked release-review JSON fixtures for golden inventory, matrix
  coverage, portfolio coverage, and provenance distribution reports.
- Added README documentation-link tests so public documentation links stay
  executable from a source checkout.
- Expanded package-data coverage tests for prompts, matrices, config,
  snapshots, and release-review fixtures.
- Updated README, AGENTS, release-review docs, changelog, and roadmap for
  week-sized sprint discipline.

## Verification

- Package version: `0.20.0`.
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
pip install "verityfoundry @ git+https://github.com/Jason-Furr/verity-foundry.git@v0.20.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

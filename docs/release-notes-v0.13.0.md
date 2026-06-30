# VerityFoundry v0.13.0 Release Notes

VerityFoundry v0.13.0 hardens agent handoff and v0.x stabilization practices.

## Highlights

- Added a dedicated `github-copilot` render profile for GitHub Copilot
  handoff.
- Added policy-lint severity counts with blocking `error` findings and
  non-blocking `warning` advisories.
- Added warning-only advisory checks for domain prompts missing the common
  output contract.
- Added tests proving high-risk prompts render safety and provenance sections
  under every non-default agent profile.
- Added a v0.x stabilization checklist covering CLI output compatibility,
  manifest compatibility, report schema compatibility, and release discipline.
- Updated README, render-profile documentation, Copilot documentation,
  decision-policy lint documentation, changelog, roadmap, and AI-agent
  guidance.

## Verification

- Package version: `0.13.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`,
  `verityfoundry report prompt-quality-trend`,
  `verityfoundry report matrix-coverage`,
  `verityfoundry report golden-inventory`,
  `verityfoundry report example-inventory`, `verityfoundry check verityspec`,
  `verityfoundry check release-integrity`,
  `verityfoundry check quality-thresholds`, and
  `verityfoundry check workflow-hygiene`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.13.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

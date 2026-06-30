# VerityFoundry v0.6.0 Release Notes

VerityFoundry v0.6.0 expands example coverage and adds deterministic matrix
coverage reporting for prompt-library maintainers.

## Highlights

- Added a software-library example for a shared authentication package.
- Added a product example for a customer portal.
- Added `verityfoundry report matrix-coverage` with text and JSON output.
- Added matrix coverage checks to CI, release workflow wheel smoke tests, and
  local verification guidance.
- Documented the grouped sprint model for about one week of related work per
  sprint.
- Added dedicated matrix coverage documentation.

## Verification

- Package version: `0.6.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry report prompt-quality`,
  `verityfoundry report matrix-coverage`, and
  `verityfoundry check verityspec`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.6.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

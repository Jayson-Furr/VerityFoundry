# VerityFoundry v0.10.0 Release Notes

VerityFoundry v0.10.0 adds lifecycle readiness prompt workflows for release
gap review, shipped-product maintenance interviews, and decommissioning
interviews.

## Highlights

- Added `lifecycle.workspace.interview-medium.production-ready.release-gap-review.v1`
  for release-readiness gap review.
- Added `lifecycle.shipped-product.interview-high.maintenance-ready.v1` for
  shipped-product maintenance interviews.
- Added `lifecycle.retiring-product.interview-all.decommission-ready.v1` for
  decommissioning interviews.
- Added the `lifecycle` prompt matrix.
- Added matrix coverage for the new lifecycle domain.
- Added lifecycle readiness workflow documentation covering authority
  boundaries, release gaps, maintenance risks, decommissioning risks, and the
  VeritySpec validation loop.
- Updated packaged wheel data so installed CLI inspection includes the new
  lifecycle prompt files.

## Verification

- Package version: `0.10.0`.
- Local tests: `python -m unittest discover -s tests -v`.
- CLI checks: `verityfoundry validate`, `verityfoundry validate prompts`,
  `verityfoundry validate matrices`, `verityfoundry validate examples`,
  `verityfoundry validate goldens`, `verityfoundry lint decision-policy`,
  `verityfoundry report prompt-quality`, `verityfoundry report matrix-coverage`,
  and `verityfoundry check verityspec`.
- Distribution checks: `python -m build` and `python -m twine check dist/*`.
- Wheel smoke test: installed the built wheel into a clean virtual environment
  and ran CLI validation from `/tmp`, outside the source checkout.

## Install

```bash
pip install "verityfoundry @ git+https://github.com/Jayson-Furr/VerityFoundry.git@v0.10.0"
```

PyPI publishing remains intentionally disabled until package publishing is
explicitly configured.

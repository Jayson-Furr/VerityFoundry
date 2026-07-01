# Package-Data Verification

VerityFoundry ships prompt-library artifacts as package data so the installed
CLI can inspect prompts, matrices, examples, goldens, schemas, snapshots,
fixtures, and config files outside a source checkout.

## What Must Be Packaged

Package-data coverage should include:

- `config/*.json`
- `schemas/*.json`
- `prompts/**/*.md`
- `matrices/*.md`
- `examples/**/*.json`
- `examples/**/*.md`
- `goldens/**/*.json`
- `goldens/**/*.md`
- `fixtures/release-review/current/*.json`
- `fixtures/generated-workspaces/*/validation-result.json`
- `snapshots/**/*.json`
- `snapshots/render-profiles/*.md`

The primary package-data test is:

```bash
python -m unittest tests.test_packaged_fixture_files -v
```

## Installed-Wheel Audit

Run an installed-wheel audit before release:

```bash
rm -rf dist build
python -m build
python -m twine check dist/*

rm -rf /tmp/verityfoundry-wheel
python3 -m venv /tmp/verityfoundry-wheel
/tmp/verityfoundry-wheel/bin/python -m pip install --upgrade pip
/tmp/verityfoundry-wheel/bin/pip install dist/*.whl
(
  cd /tmp
  /tmp/verityfoundry-wheel/bin/verityfoundry --version
  /tmp/verityfoundry-wheel/bin/verityfoundry validate
  /tmp/verityfoundry-wheel/bin/verityfoundry validate goldens
  /tmp/verityfoundry-wheel/bin/verityfoundry report release-summary
  /tmp/verityfoundry-wheel/bin/verityfoundry report portfolio-coverage
  /tmp/verityfoundry-wheel/bin/verityfoundry check quality-thresholds
)
```

Source-checkout-only checks such as release integrity and workflow hygiene may
skip from `/tmp` because the installed wheel does not include repository
bookkeeping files or `.github/workflows/`.

## Update Rule

When adding a new artifact directory, update:

- `pyproject.toml` data files
- package-data tests
- installed-wheel release checklist
- README current scope, when user-visible
- changelog and roadmap

Do not rely on a source checkout path when testing installed CLI behavior.

## Boundary

Package-data verification proves VerityFoundry artifacts are present in an
installed wheel. It does not prove that generated VeritySpec workspaces are
valid, complete, human-approved, or release-ready.

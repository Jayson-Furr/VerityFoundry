# Release Checklist

## Prepare

- Confirm `main` is clean and CI is passing.
- Update `pyproject.toml` and `src/verityfoundry/__init__.py`.
- Update `README.md`, `CHANGELOG.md`, `ROADMAP.md`, and release notes.
- Confirm prompt, matrix, example, and golden output manifests validate.

## Verify

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools build twine
pip install -e .
python -m unittest discover -s tests -v
verityfoundry --version
verityfoundry list prompts
verityfoundry list matrices
verityfoundry list profiles
verityfoundry validate
verityfoundry validate prompts
verityfoundry validate matrices
verityfoundry validate examples
verityfoundry validate goldens
verityfoundry lint decision-policy
verityfoundry report prompt-quality
verityfoundry report prompt-quality-trend
verityfoundry report policy-lint-trend
verityfoundry report matrix-coverage
verityfoundry report release-summary
verityfoundry report golden-inventory
verityfoundry report example-inventory
verityfoundry report fixture-inventory
verityfoundry report provenance-coverage
verityfoundry report provenance-distribution
verityfoundry report portfolio-coverage
verityfoundry check verityspec
verityfoundry check release-integrity
verityfoundry check quality-thresholds
verityfoundry check workflow-hygiene
git diff --check
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
  /tmp/verityfoundry-wheel/bin/verityfoundry list prompts
  /tmp/verityfoundry-wheel/bin/verityfoundry list matrices
  /tmp/verityfoundry-wheel/bin/verityfoundry list profiles
  /tmp/verityfoundry-wheel/bin/verityfoundry validate
  /tmp/verityfoundry-wheel/bin/verityfoundry validate goldens
  /tmp/verityfoundry-wheel/bin/verityfoundry lint decision-policy
  /tmp/verityfoundry-wheel/bin/verityfoundry report prompt-quality
  /tmp/verityfoundry-wheel/bin/verityfoundry report prompt-quality-trend
  /tmp/verityfoundry-wheel/bin/verityfoundry report policy-lint-trend
  /tmp/verityfoundry-wheel/bin/verityfoundry report matrix-coverage
  /tmp/verityfoundry-wheel/bin/verityfoundry report release-summary
  /tmp/verityfoundry-wheel/bin/verityfoundry report golden-inventory
  /tmp/verityfoundry-wheel/bin/verityfoundry report example-inventory
  /tmp/verityfoundry-wheel/bin/verityfoundry report fixture-inventory
  /tmp/verityfoundry-wheel/bin/verityfoundry report provenance-coverage
  /tmp/verityfoundry-wheel/bin/verityfoundry report provenance-distribution
  /tmp/verityfoundry-wheel/bin/verityfoundry report portfolio-coverage
  /tmp/verityfoundry-wheel/bin/verityfoundry check verityspec
  /tmp/verityfoundry-wheel/bin/verityfoundry check quality-thresholds
)
```

## Tag

```bash
VERSION=v0.21.0
git tag -a "$VERSION" -m "VerityFoundry $VERSION"
git push origin "$VERSION"
```

Do not publish packages unless explicitly authorized.

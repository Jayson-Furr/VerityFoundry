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
verityfoundry report matrix-coverage
verityfoundry check verityspec
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
  /tmp/verityfoundry-wheel/bin/verityfoundry report matrix-coverage
  /tmp/verityfoundry-wheel/bin/verityfoundry check verityspec
)
```

## Tag

```bash
VERSION=v0.9.0
git tag -a "$VERSION" -m "VerityFoundry $VERSION"
git push origin "$VERSION"
```

Do not publish packages unless explicitly authorized.

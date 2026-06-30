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
verityfoundry validate
verityfoundry validate prompts
verityfoundry validate matrices
verityfoundry validate examples
verityfoundry validate goldens
verityfoundry report prompt-quality
git diff --check
rm -rf dist build
python -m build
python -m twine check dist/*
```

## Tag

```bash
VERSION=v0.3.0
git tag -a "$VERSION" -m "VerityFoundry $VERSION"
git push origin "$VERSION"
```

Do not publish packages unless explicitly authorized.

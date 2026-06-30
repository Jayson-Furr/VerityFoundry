# CI

CI is lightweight and deterministic. It does not call external AI APIs.

The GitHub Actions workflow runs:

```bash
python -m unittest discover -s tests -v
verityfoundry --version
verityfoundry list prompts
verityfoundry list matrices
verityfoundry validate
verityfoundry validate prompts
verityfoundry validate examples
git diff --check
```

If GitHub Actions is unavailable because of billing, credits, quota, runner
availability, or another platform issue, run equivalent local checks and record
that fallback evidence in the PR.

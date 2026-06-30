# Quality Thresholds

`verityfoundry check quality-thresholds` checks release-review baselines for
prompt quality, matrix coverage, and policy-lint counts.

Run:

```bash
verityfoundry check quality-thresholds
verityfoundry check quality-thresholds --format json
```

The default threshold config is:

```text
config/release-quality-thresholds.json
```

The current thresholds are conservative. They prevent accidental regression
below the existing prompt-quality and matrix-coverage baseline while still
allowing future sprints to improve the baseline deliberately.

Policy-lint errors are blocking. Policy-lint advisory warning thresholds are
reported as warnings so reviewers can see drift without blocking unrelated
release work.

When thresholds change, update the changelog and roadmap sprint notes so
release reviewers understand why the release gate moved.

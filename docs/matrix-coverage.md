# Matrix Coverage

The matrix coverage report shows how domain prompt workflows are represented
in prompt matrices.

Run it with:

```bash
verityfoundry report matrix-coverage
verityfoundry report matrix-coverage --format json
```

The report includes:

- total matrix count
- total matrix row count
- domain prompt coverage percentage
- per-domain coverage summaries
- domain prompts not referenced by any matrix row
- matrix rows that reference unknown prompt IDs

The report is deterministic and does not call external AI APIs. It is an
inspection aid for maintainers, not a readiness certification.

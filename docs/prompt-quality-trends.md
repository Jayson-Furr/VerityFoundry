# Prompt Quality Trends

`verityfoundry report prompt-quality-trend` compares the current prompt quality
report with checked-in snapshots.

Run:

```bash
verityfoundry report prompt-quality-trend
verityfoundry report prompt-quality-trend --format json
```

Snapshots live in:

```text
snapshots/prompt-quality/
```

The first snapshot is `v0.11.0`, captured after the v0.11.0 release. Future
snapshots should be added when a release intentionally changes the prompt
library, quality checks, or quality baseline.

The trend report is a release-review aid. It does not certify readiness and it
does not replace human review of prompt behavior.

Decision-policy lint trends are tracked separately in
[Policy lint trends](policy-lint-trends.md).

# Quality Threshold Ratcheting

Release quality thresholds are conservative baselines for prompt quality and
matrix coverage. They should improve intentionally over time.

## Current Config

Thresholds live in:

```text
config/release-quality-thresholds.json
```

Check them with:

```bash
verityfoundry check quality-thresholds
verityfoundry check quality-thresholds --format json
```

## Ratcheting Rules

Raise thresholds only when:

- the current repository passes the higher threshold
- the improvement is intentional, not accidental
- the changelog explains the threshold change
- tests cover failure behavior for over-strict configs
- release reviewers understand the new baseline

Do not raise a threshold in the same change that hides or removes weak prompt
evidence unless the prompt quality report still explains the tradeoff.

## Practical Sequence

1. Run `verityfoundry report prompt-quality`.
2. Run `verityfoundry report matrix-coverage`.
3. Decide which threshold can move without creating churn.
4. Update `config/release-quality-thresholds.json`.
5. Run `verityfoundry check quality-thresholds`.
6. Update docs and changelog.

Thresholds should push the project forward without making routine contribution
work noisy or arbitrary.

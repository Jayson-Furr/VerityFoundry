# Quality-Threshold Warning Trends

`verityfoundry check quality-thresholds` treats blocking threshold failures and
non-blocking warning trends differently.

Current non-blocking warning trend coverage comes from policy-lint warnings:

```bash
verityfoundry lint decision-policy
verityfoundry report policy-lint-trend
verityfoundry check quality-thresholds
```

## Review Guidance

Warnings should be visible in release review even when they do not block a
release. A stable warning count can be acceptable when the warnings are known
and tracked. A rising warning count should usually produce a remediation issue.

Do not treat a passing quality-threshold check as proof that generated
VeritySpec workspaces are ready. VeritySpec validation and readiness remain
separate authority.

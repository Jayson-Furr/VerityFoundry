# Policy-Lint Advisory Remediation

Policy-lint warnings are non-blocking release-review signals. They should be
triaged deliberately instead of ignored or hidden.

## Current Advisory

The current advisory class is:

```text
policy.advisory-missing-output-contract
```

This means a domain prompt can be strengthened by including the shared output
contract guidance.

## Remediation Pattern

For each warning:

1. Confirm the prompt is a domain prompt that should produce candidate
   VeritySpec authoring output.
2. Add the appropriate output-contract include when it improves the prompt.
3. Keep safety, uncertainty, provenance, and human-approval requirements
   visible.
4. Run `verityfoundry lint decision-policy`.
5. Run `verityfoundry report policy-lint-trend`.

Do not lower warning counts by weakening the linter or hiding prompts from
review. A reduced warning count should represent better prompt behavior.

# Prompt Quality Rubric

Use this rubric when reviewing prompt workflows.

| Area | Pass condition |
|---|---|
| Purpose | The prompt has a clear domain, input set, readiness target, and output contract. |
| VeritySpec boundary | The prompt states that VeritySpec validates the resulting workspace. |
| Uncertainty | Assumptions, defaults, suggestions, unresolved decisions, and approvals are separated. |
| Provenance | Outputs ask for source references and decision provenance. |
| Safety | High-stakes commitments are not fabricated. |
| Actionability | Outputs are useful for workspace drafting, interview follow-up, or readiness gap review. |
| Testability | The prompt has a manifest and appears in a matrix or example when appropriate. |

Prompt changes should improve at least one rubric area without weakening
uncertainty preservation.

Run the deterministic local report with:

```bash
verityfoundry report prompt-quality
verityfoundry report prompt-quality --format json
```

The report scores visible evidence in rendered prompt text. It is an inspection
aid, not a certification gate.

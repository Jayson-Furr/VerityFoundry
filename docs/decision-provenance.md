# Decision Provenance

Candidate outputs should distinguish where each decision came from.

Useful categories:

- `human-provided`
- `gdd-source`
- `concept-art-interpretation`
- `identity-image-interpretation`
- `ai-inferred`
- `ai-defaulted`
- `ai-suggested`
- `human-interview-answer`
- `prior-verityspec-record`
- `external-documented-source`

Suggested shape:

```json
{
  "sourceRefs": ["source.gdd.main"],
  "fabricationMode": "interview-medium-stakes",
  "decisionSource": "ai-inferred",
  "confidence": "medium",
  "humanApprovalRequired": true
}
```

Do not hide unsupported decisions inside generated records.

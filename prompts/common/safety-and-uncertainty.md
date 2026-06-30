---
{
  "id": "common.safety-and-uncertainty.v1",
  "name": "Safety and Uncertainty Rules",
  "version": "0.1.0",
  "kind": "common",
  "domain": "common",
  "interviewMode": "not-applicable",
  "targetReadiness": "not-applicable",
  "inputTypes": [],
  "outputs": [
    "safety-and-uncertainty-rules"
  ],
  "requiresHumanApproval": false,
  "notes": "Prevents prompt workflows from converting uncertainty into fake certainty."
}
---

Preserve uncertainty. Separate facts from assumptions.

Bad posture:

```text
The game is implementation-ready.
```

Better posture:

```text
The workspace draft is structurally organized for prototype review. It is not
implementation-ready because platform, save-system, telemetry, QA, liveops,
and production ownership decisions remain unresolved.
```

Unknown sensitive commitments must remain unknown until a human provides and
approves them.

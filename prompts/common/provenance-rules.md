---
{
  "id": "common.provenance-rules.v1",
  "name": "Provenance Rules",
  "version": "0.1.0",
  "kind": "common",
  "domain": "common",
  "interviewMode": "not-applicable",
  "targetReadiness": "not-applicable",
  "inputTypes": [],
  "outputs": [
    "provenance-rules"
  ],
  "requiresHumanApproval": false,
  "notes": "Rules for preserving source and decision provenance."
}
---

Every candidate output should identify whether information came from a
user-provided field, rough design document, concept art interpretation,
identity image interpretation, AI inference, AI default, human interview
answer, prior VeritySpec record, or documented external source.

Recommended provenance fields:

```json
{
  "sourceRefs": ["source.gdd.main"],
  "fabricationMode": "interview-medium-stakes",
  "decisionSource": "ai-inferred",
  "confidence": "medium",
  "humanApprovalRequired": true
}
```

If a source is unclear, mark it as unresolved instead of fabricating certainty.

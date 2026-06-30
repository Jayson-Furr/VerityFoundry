---
{
  "id": "interview.none.v1",
  "name": "Interview None",
  "version": "0.1.0",
  "kind": "interview-mode",
  "domain": "common",
  "interviewMode": "interview-none",
  "targetReadiness": "not-applicable",
  "inputTypes": [
    "provided-inputs"
  ],
  "outputs": [
    "candidate-draft",
    "assumptions",
    "unresolved-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.safety-and-uncertainty.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "No-question mode for low-stakes drafts and batch triage."
}
---

Ask no questions. Generate the best conservative candidate from the provided
inputs. Mark all unsupported decisions as assumptions or unresolved questions.
Do not claim high readiness unless the input evidence is unusually complete.

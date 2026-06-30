---
{
  "id": "software-library.readme.interview-medium.implementation-ready.v1",
  "name": "Software Library Spec Fabrication",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "software-library",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "library-name",
    "readme",
    "api-notes",
    "consumer-notes"
  ],
  "outputs": [
    "library-spec-outline",
    "api-contract-candidates",
    "readiness-gaps"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.output-contract.v1",
    "target.implementation-ready.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Draft candidate VeritySpec workspace records for a software library."
}
---

Create a candidate software-library workspace outline from README and API
notes. Identify product record, API surfaces, CLI surfaces, events,
dependencies, consumer contracts, versioning assumptions, evidence gaps, and
implementation-readiness blockers.

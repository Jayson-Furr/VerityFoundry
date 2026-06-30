---
{
  "id": "product.brief.interview-low.design-complete.v1",
  "name": "Product Brief to Design-Complete Candidate",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "product",
  "interviewMode": "interview-low-stakes",
  "targetReadiness": "design-complete",
  "inputTypes": [
    "product-name",
    "brief",
    "goals",
    "users"
  ],
  "outputs": [
    "product-spec-outline",
    "assumptions",
    "unresolved-questions",
    "readiness-gaps"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.output-contract.v1",
    "target.design-complete.v1",
    "interview.low-stakes.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Draft a product-focused VeritySpec workspace from a brief."
}
---

Create a candidate product workspace outline from a product brief. Identify
product identity, users, goals, interfaces, capabilities, telemetry questions,
risks, assumptions, unresolved decisions, and next interview questions.

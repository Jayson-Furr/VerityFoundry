"""Deterministic decision-policy linting."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

from .manifests import load_prompt_manifests


HIGH_RISK_INTERVIEW_MODES = {"interview-high-stakes", "interview-all"}
HIGH_RISK_TARGETS = {
    "production-ready",
    "operations-ready",
    "liveops-ready",
    "maintenance-ready",
    "decommission-ready",
    "archival-ready",
}
REQUIRED_HIGH_RISK_INCLUDE_REFS = {
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
}


@dataclass(frozen=True)
class PolicyLintIssue:
    """A deterministic decision-policy lint issue."""

    code: str
    message: str
    path: str
    promptId: str
    severity: str = "error"

    def format(self) -> str:
        return f"{self.severity}: {self.code}: {self.path}: {self.promptId}: {self.message}"

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


def lint_decision_policy(root: str | Path) -> list[PolicyLintIssue]:
    """Lint prompt workflows for high-stakes invention-risk controls."""

    root_path = Path(root)
    issues: list[PolicyLintIssue] = []
    for prompt in load_prompt_manifests(root_path):
        manifest = prompt.manifest
        prompt_id = str(manifest.get("id", prompt.path.stem))
        if manifest.get("kind") != "domain-prompt":
            continue

        include_refs = set(manifest.get("includeRefs", []))
        if not manifest.get("decisionPolicyRef"):
            issues.append(
                _issue(
                    "policy.missing-decision-policy",
                    "domain prompts must reference a decision policy",
                    root_path,
                    prompt.path,
                    prompt_id,
                )
            )

        if not manifest.get("requiresHumanApproval"):
            issues.append(
                _issue(
                    "policy.missing-human-approval",
                    "domain prompts must require human approval",
                    root_path,
                    prompt.path,
                    prompt_id,
                )
            )

        if _is_high_risk(manifest):
            for include_ref in sorted(REQUIRED_HIGH_RISK_INCLUDE_REFS - include_refs):
                issues.append(
                    _issue(
                        "policy.high-risk-missing-include",
                        f"high-risk prompts must include {include_ref}",
                        root_path,
                        prompt.path,
                        prompt_id,
                    )
                )

            expected_interview_ref = _expected_interview_ref(str(manifest.get("interviewMode", "")))
            if expected_interview_ref and expected_interview_ref not in include_refs:
                issues.append(
                    _issue(
                        "policy.high-risk-missing-interview-mode",
                        f"high-risk prompts must include {expected_interview_ref}",
                        root_path,
                        prompt.path,
                        prompt_id,
                    )
                )

    return sorted(issues, key=lambda issue: (issue.path, issue.code, issue.message))


def format_policy_lint_issues(issues: list[PolicyLintIssue]) -> str:
    """Format decision-policy lint output for humans."""

    if not issues:
        return "Decision policy lint passed.\n"

    lines = ["Decision policy lint failed.", ""]
    for issue in issues:
        lines.append(f"- {issue.format()}")
    return "\n".join(lines) + "\n"


def _is_high_risk(manifest: dict[str, object]) -> bool:
    interview_mode = str(manifest.get("interviewMode", ""))
    target = str(manifest.get("targetReadiness", ""))
    return interview_mode in HIGH_RISK_INTERVIEW_MODES or target in HIGH_RISK_TARGETS


def _expected_interview_ref(interview_mode: str) -> str | None:
    if interview_mode == "interview-high-stakes":
        return "interview.high-stakes.v1"
    if interview_mode == "interview-all":
        return "interview.all.v1"
    return None


def _issue(code: str, message: str, root: Path, path: Path, prompt_id: str) -> PolicyLintIssue:
    return PolicyLintIssue(
        code=code,
        message=message,
        path=str(path.relative_to(root)),
        promptId=prompt_id,
    )

"""Quality threshold checks for release review."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .manifests import read_json
from .matrix_coverage import generate_matrix_coverage_report
from .policy_lint import (
    SEVERITY_ERROR,
    SEVERITY_WARNING,
    count_policy_lint_severities,
    lint_decision_policy,
)
from .quality import generate_prompt_quality_report


@dataclass(frozen=True)
class ThresholdIssue:
    """A threshold failure."""

    code: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "message": self.message,
        }


def check_quality_thresholds(root: str | Path, config_path: str | Path | None = None) -> dict[str, Any]:
    """Check prompt quality and matrix coverage against configured thresholds."""

    root_path = Path(root)
    config_file = Path(config_path) if config_path else root_path / "config" / "release-quality-thresholds.json"
    config = read_json(config_file)
    prompt_report = generate_prompt_quality_report(root_path)
    matrix_report = generate_matrix_coverage_report(root_path)
    policy_counts = count_policy_lint_severities(lint_decision_policy(root_path))
    issues: list[ThresholdIssue] = []
    warnings: list[ThresholdIssue] = []

    prompt_thresholds = config.get("promptQuality", {})
    _check_min(
        issues,
        "threshold.prompt-quality-overall",
        "prompt quality overall percent",
        float(prompt_report["percent"]),
        float(prompt_thresholds.get("minOverallPercent", 0.0)),
    )
    _check_min(
        issues,
        "threshold.prompt-quality-uncertainty",
        "prompt quality uncertainty percent",
        float(prompt_report["uncertaintyPreservation"]["percent"]),
        float(prompt_thresholds.get("minUncertaintyPercent", 0.0)),
    )
    _check_min(
        issues,
        "threshold.prompt-quality-provenance",
        "prompt quality provenance percent",
        float(prompt_report["provenanceCompleteness"]["percent"]),
        float(prompt_thresholds.get("minProvenancePercent", 0.0)),
    )

    matrix_thresholds = config.get("matrixCoverage", {})
    _check_min(
        issues,
        "threshold.matrix-coverage",
        "matrix coverage percent",
        float(matrix_report["coveragePercent"]),
        float(matrix_thresholds.get("minCoveragePercent", 0.0)),
    )
    _check_max(
        issues,
        "threshold.matrix-missing-prompts",
        "missing matrix-covered domain prompts",
        int(matrix_report["missingDomainPromptCount"]),
        int(matrix_thresholds.get("maxMissingDomainPrompts", 999999)),
    )
    _check_max(
        issues,
        "threshold.matrix-unknown-refs",
        "unknown matrix prompt references",
        len(matrix_report["unknownPromptRefs"]),
        int(matrix_thresholds.get("maxUnknownPromptRefs", 999999)),
    )

    policy_thresholds = config.get("policyLint", {})
    _check_max(
        issues,
        "threshold.policy-lint-errors",
        "policy-lint errors",
        int(policy_counts[SEVERITY_ERROR]),
        int(policy_thresholds.get("maxErrors", 0)),
    )
    _check_max(
        warnings,
        "threshold.policy-lint-warnings",
        "policy-lint warnings",
        int(policy_counts[SEVERITY_WARNING]),
        int(policy_thresholds.get("maxWarnings", 999999)),
    )

    return {
        "status": "failed" if issues else "passed",
        "configPath": str(config_file),
        "issueCount": len(issues),
        "issues": [issue.to_dict() for issue in issues],
        "warningCount": len(warnings),
        "warnings": [warning.to_dict() for warning in warnings],
        "promptQuality": {
            "percent": prompt_report["percent"],
            "uncertaintyPercent": prompt_report["uncertaintyPreservation"]["percent"],
            "provenancePercent": prompt_report["provenanceCompleteness"]["percent"],
        },
        "matrixCoverage": {
            "coveragePercent": matrix_report["coveragePercent"],
            "missingDomainPromptCount": matrix_report["missingDomainPromptCount"],
            "unknownPromptRefCount": len(matrix_report["unknownPromptRefs"]),
        },
        "policyLint": {
            "errorCount": policy_counts[SEVERITY_ERROR],
            "warningCount": policy_counts[SEVERITY_WARNING],
        },
        "thresholds": config,
    }


def format_quality_threshold_report(report: dict[str, Any]) -> str:
    """Format quality threshold results for humans."""

    lines = [
        "Quality Threshold Check",
        "",
        f"Config: {report['configPath']}",
        (
            "Prompt quality: "
            f"{report['promptQuality']['percent']}% overall, "
            f"{report['promptQuality']['uncertaintyPercent']}% uncertainty, "
            f"{report['promptQuality']['provenancePercent']}% provenance"
        ),
        (
            "Matrix coverage: "
            f"{report['matrixCoverage']['coveragePercent']}% coverage, "
            f"{report['matrixCoverage']['missingDomainPromptCount']} missing, "
            f"{report['matrixCoverage']['unknownPromptRefCount']} unknown refs"
        ),
        (
            "Policy lint: "
            f"{report['policyLint']['errorCount']} errors, "
            f"{report['policyLint']['warningCount']} warnings"
        ),
    ]

    if report["warningCount"]:
        lines.extend(["", "Warnings:"])
        for warning in report["warnings"]:
            lines.append(f"- {warning['code']}: {warning['message']}")

    if report["issueCount"]:
        lines.extend(["", "Issues:"])
        for issue in report["issues"]:
            lines.append(f"- {issue['code']}: {issue['message']}")
    elif report["warningCount"]:
        lines.extend(["", "Quality threshold check passed with warnings."])
    else:
        lines.extend(["", "Quality threshold check passed."])

    return "\n".join(lines) + "\n"


def _check_min(
    issues: list[ThresholdIssue], code: str, label: str, actual: float, expected_min: float
) -> None:
    if actual < expected_min:
        issues.append(
            ThresholdIssue(
                code,
                f"{label} is {actual}, below minimum {expected_min}",
            )
        )


def _check_max(
    issues: list[ThresholdIssue], code: str, label: str, actual: int, expected_max: int
) -> None:
    if actual > expected_max:
        issues.append(
            ThresholdIssue(
                code,
                f"{label} is {actual}, above maximum {expected_max}",
            )
        )

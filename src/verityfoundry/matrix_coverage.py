"""Deterministic matrix coverage reporting."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .manifests import load_matrix_manifests, load_prompt_manifests


def generate_matrix_coverage_report(root: str | Path) -> dict[str, Any]:
    """Report how well prompt matrices cover domain prompt workflows."""

    root_path = Path(root)
    prompts = load_prompt_manifests(root_path)
    matrices = load_matrix_manifests(root_path)

    domain_prompts = [
        prompt
        for prompt in prompts
        if prompt.manifest.get("kind") == "domain-prompt"
        and isinstance(prompt.manifest.get("id"), str)
    ]
    prompt_by_id = {str(prompt.manifest["id"]): prompt for prompt in domain_prompts}

    matrix_rows: list[dict[str, Any]] = []
    referenced_prompt_ids: set[str] = set()
    unknown_prompt_refs: list[dict[str, Any]] = []
    for matrix in matrices:
        matrix_id = str(matrix.manifest.get("id", matrix.path.stem))
        for index, row in enumerate(matrix.manifest.get("rows", []), start=1):
            prompt_id = row.get("promptId")
            row_item = {
                "matrixId": matrix_id,
                "row": index,
                "domain": row.get("domain"),
                "interviewMode": row.get("interviewMode"),
                "targetReadiness": row.get("target"),
                "promptId": prompt_id,
            }
            matrix_rows.append(row_item)
            if isinstance(prompt_id, str):
                if prompt_id in prompt_by_id:
                    referenced_prompt_ids.add(prompt_id)
                else:
                    unknown_prompt_refs.append(row_item)

    prompt_items: list[dict[str, Any]] = []
    for prompt_id, prompt in sorted(prompt_by_id.items()):
        manifest = prompt.manifest
        prompt_items.append(
            {
                "id": prompt_id,
                "name": manifest.get("name", prompt_id),
                "domain": manifest.get("domain", "unknown"),
                "interviewMode": manifest.get("interviewMode", "unknown"),
                "targetReadiness": manifest.get("targetReadiness", "unknown"),
                "path": str(prompt.path.relative_to(root_path)),
                "covered": prompt_id in referenced_prompt_ids,
            }
        )

    missing_prompts = [item for item in prompt_items if not item["covered"]]
    domain_items = _domain_items(prompt_items, matrix_rows)
    prompt_count = len(prompt_items)
    covered_count = prompt_count - len(missing_prompts)

    return {
        "matrixCount": len(matrices),
        "matrixRowCount": len(matrix_rows),
        "domainPromptCount": prompt_count,
        "coveredDomainPromptCount": covered_count,
        "missingDomainPromptCount": len(missing_prompts),
        "coveragePercent": round((covered_count / prompt_count) * 100, 1) if prompt_count else 100.0,
        "domainCount": len(domain_items),
        "domains": domain_items,
        "missingDomainPrompts": missing_prompts,
        "unknownPromptRefs": unknown_prompt_refs,
        "domainPrompts": prompt_items,
    }


def format_matrix_coverage_report(report: dict[str, Any]) -> str:
    """Format a matrix coverage report for humans."""

    lines = [
        "Matrix Coverage Report",
        "",
        f"Matrices: {report['matrixCount']}",
        f"Matrix rows: {report['matrixRowCount']}",
        (
            "Domain prompt coverage: "
            f"{report['coveredDomainPromptCount']}/{report['domainPromptCount']} "
            f"({report['coveragePercent']}%)"
        ),
        "",
        "Domains:",
    ]

    for domain in report["domains"]:
        lines.append(
            f"- {domain['domain']}: {domain['coveredDomainPromptCount']}/"
            f"{domain['domainPromptCount']} covered, {domain['matrixRowCount']} matrix rows"
        )

    missing = report["missingDomainPrompts"]
    if missing:
        lines.extend(["", "Missing domain prompts:"])
        for prompt in missing:
            lines.append(
                f"- {prompt['id']} "
                f"({prompt['domain']} / {prompt['interviewMode']} / {prompt['targetReadiness']})"
            )
    else:
        lines.extend(["", "Missing domain prompts: none"])

    unknown = report["unknownPromptRefs"]
    if unknown:
        lines.extend(["", "Unknown matrix prompt references:"])
        for row in unknown:
            lines.append(f"- {row['matrixId']} row {row['row']}: {row['promptId']}")

    return "\n".join(lines) + "\n"


def _domain_items(prompt_items: list[dict[str, Any]], matrix_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    prompt_counts: dict[str, int] = defaultdict(int)
    covered_counts: dict[str, int] = defaultdict(int)
    row_counts: dict[str, int] = defaultdict(int)

    for prompt in prompt_items:
        domain = str(prompt["domain"])
        prompt_counts[domain] += 1
        if prompt["covered"]:
            covered_counts[domain] += 1

    for row in matrix_rows:
        prompt_id = row.get("promptId")
        domain = row.get("domain")
        if isinstance(domain, str):
            row_counts[_normalize_domain(domain)] += 1
        elif isinstance(prompt_id, str):
            row_counts["unknown"] += 1

    domains = sorted(set(prompt_counts) | set(row_counts))
    return [
        {
            "domain": domain,
            "domainPromptCount": prompt_counts[domain],
            "coveredDomainPromptCount": covered_counts[domain],
            "missingDomainPromptCount": prompt_counts[domain] - covered_counts[domain],
            "matrixRowCount": row_counts[domain],
        }
        for domain in domains
    ]


def _normalize_domain(value: str) -> str:
    return value.strip().lower().replace(" ", "-")

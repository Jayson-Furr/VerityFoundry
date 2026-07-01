"""Release-review inventory reports for examples and golden outputs."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from .manifests import load_example_manifests, load_golden_manifests, read_json


FIXTURE_KIND_PACKS = {
    "api.interface": "verity.pack.api",
    "core.product": "verity.core",
    "foundry.readiness-gap": "verityfoundry.authoring-output",
    "game.asset.image": "future verity.pack.game-assets",
    "game.gdd-source": "future verity.pack.game-core",
    "game.feature": "future verity.pack.game-core",
    "game.loop": "future verity.pack.game-core",
    "game.mode": "future verity.pack.game-core",
    "game.visual-identity": "future verity.pack.game-assets",
    "portfolio.collection": "future verity.pack.portfolio",
    "portfolio.coverage-gap": "future verity.pack.portfolio",
    "portfolio.game-concept": "future verity.pack.portfolio",
    "portfolio.triage-group": "future verity.pack.portfolio",
    "product.audience": "future verity.pack.product",
    "product.feature": "future verity.pack.product",
    "product.integration-assumption": "future verity.pack.product",
    "product.permission-decision": "future verity.pack.product",
    "security.decision": "verity.pack.security",
    "software.consumer": "future verity.pack.software",
    "software.package": "future verity.pack.software",
    "telemetry.intent": "verity.pack.observability",
    "unity.capability": "future verity.pack.unity",
    "unity.consumer-contract": "future verity.pack.unity",
    "unity.exported-record-assumption": "future verity.pack.unity",
    "unity.package": "future verity.pack.unity",
    "unity.package-dependency": "future verity.pack.unity",
    "workspace.cross-reference": "future VeritySpec workspace dependency support",
    "workspace.dependency": "future VeritySpec workspace dependency support",
    "workspace.dependency-risk": "future VeritySpec workspace dependency support",
}

PORTFOLIO_DEPENDENCY_KINDS = {
    "unity.exported-record-assumption",
    "unity.package-dependency",
    "workspace.cross-reference",
    "workspace.dependency",
    "workspace.dependency-risk",
}

PORTFOLIO_COVERAGE_GAP_KINDS = {
    "foundry.readiness-gap",
    "portfolio.coverage-gap",
}


def generate_example_inventory_report(root: str | Path) -> dict[str, Any]:
    """Summarize example manifests for release reviewers."""

    root_path = Path(root)
    examples = []
    for path, manifest in load_example_manifests(root_path):
        examples.append(
            {
                "id": manifest.get("id"),
                "name": manifest.get("name"),
                "domain": manifest.get("domain"),
                "interviewMode": manifest.get("interviewMode"),
                "targetReadiness": manifest.get("targetReadiness"),
                "inputCount": len(manifest.get("inputs", [])),
                "expectedOutputCount": len(manifest.get("expectedOutputs", [])),
                "workspaceFixtureCount": len(manifest.get("workspaceFixtures", [])),
                "expectedRecordCategoryCount": len(manifest.get("expectedRecordCategories", [])),
                "provenanceExampleCount": len(manifest.get("provenanceExamples", [])),
                "promptRefCount": len(manifest.get("promptRefs", [])),
                "path": str(path.relative_to(root_path)),
            }
        )

    examples.sort(key=lambda item: str(item["id"]))
    domains = _domain_summary(examples)
    return {
        "exampleCount": len(examples),
        "domainCount": len(domains),
        "domains": domains,
        "examples": examples,
    }


def format_example_inventory_report(report: dict[str, Any]) -> str:
    """Format an example inventory report for humans."""

    lines = [
        "Example Inventory Report",
        "",
        f"Examples: {report['exampleCount']}",
        f"Domains: {report['domainCount']}",
        "",
        "Domains:",
    ]
    for domain in report["domains"]:
        lines.append(f"- {domain['domain']}: {domain['count']} examples")

    lines.extend(["", "Examples:"])
    for example in report["examples"]:
        lines.append(
            f"- {example['id']} ({example['domain']} / {example['targetReadiness']}): "
            f"{example['inputCount']} inputs, {example['expectedOutputCount']} expected outputs, "
            f"{example['workspaceFixtureCount']} workspace fixtures, "
            f"{example['provenanceExampleCount']} provenance examples"
        )

    return "\n".join(lines) + "\n"


def generate_fixture_inventory_report(root: str | Path) -> dict[str, Any]:
    """Summarize candidate workspace fixtures and record kinds."""

    root_path = Path(root)
    fixtures = []
    kind_counts: Counter[str] = Counter()
    pack_counts: Counter[str] = Counter()
    record_count = 0

    for manifest_path, manifest in load_example_manifests(root_path):
        base = manifest_path.parent
        for relative in manifest.get("workspaceFixtures", []):
            fixture_path = base / relative
            exists = fixture_path.exists()
            records: list[dict[str, Any]] = []
            if exists:
                data = read_json(fixture_path)
                raw_records = data.get("records", [])
                if isinstance(raw_records, list):
                    records = [record for record in raw_records if isinstance(record, dict)]

            fixture_kinds = Counter(
                str(record.get("kind"))
                for record in records
                if isinstance(record.get("kind"), str)
            )
            for kind, count in fixture_kinds.items():
                kind_counts[kind] += count
                pack_counts[_pack_for_kind(kind)] += count
            record_count += len(records)
            fixtures.append(
                {
                    "exampleId": manifest.get("id"),
                    "domain": manifest.get("domain"),
                    "path": str(fixture_path.relative_to(root_path)),
                    "exists": exists,
                    "recordCount": len(records),
                    "kindCount": len(fixture_kinds),
                    "kinds": [
                        {
                            "kind": kind,
                            "count": count,
                            "recommendedPack": _pack_for_kind(kind),
                        }
                        for kind, count in sorted(fixture_kinds.items())
                    ],
                }
            )

    fixtures.sort(key=lambda item: str(item["path"]))
    kinds = [
        {
            "kind": kind,
            "count": count,
            "recommendedPack": _pack_for_kind(kind),
        }
        for kind, count in sorted(kind_counts.items())
    ]
    return {
        "fixtureCount": len(fixtures),
        "recordCount": record_count,
        "kindCount": len(kinds),
        "packCount": len(pack_counts),
        "packs": [
            {"pack": pack, "recordCount": count}
            for pack, count in sorted(pack_counts.items())
        ],
        "kinds": kinds,
        "fixtures": fixtures,
    }


def format_fixture_inventory_report(report: dict[str, Any]) -> str:
    """Format a fixture inventory report for humans."""

    lines = [
        "Fixture Inventory Report",
        "",
        f"Workspace fixtures: {report['fixtureCount']}",
        f"Fixture records: {report['recordCount']}",
        f"Record kinds: {report['kindCount']}",
        "",
        "Recommended packs:",
    ]
    for pack in report["packs"]:
        lines.append(f"- {pack['pack']}: {_count(pack['recordCount'], 'record')}")

    lines.extend(["", "Record kinds:"])
    for kind in report["kinds"]:
        lines.append(
            f"- {kind['kind']}: {_count(kind['count'], 'record')}, {kind['recommendedPack']}"
        )

    lines.extend(["", "Fixtures:"])
    for fixture in report["fixtures"]:
        status = "present" if fixture["exists"] else "missing"
        lines.append(
            f"- {fixture['path']} ({fixture['exampleId']}): "
            f"{_count(fixture['recordCount'], 'record')}, "
            f"{_count(fixture['kindCount'], 'kind')}, {status}"
        )

    return "\n".join(lines) + "\n"


def generate_provenance_coverage_report(root: str | Path) -> dict[str, Any]:
    """Summarize provenance coverage in candidate workspace fixtures."""

    root_path = Path(root)
    examples = []
    total_records = 0
    total_records_with_provenance = 0
    total_decision_records = 0

    for manifest_path, manifest in load_example_manifests(root_path):
        base = manifest_path.parent
        record_ids: set[str] = set()
        records_with_provenance: set[str] = set()
        approval_required = 0

        for relative in manifest.get("workspaceFixtures", []):
            fixture_path = base / relative
            if not fixture_path.exists():
                continue
            data = read_json(fixture_path)
            raw_records = data.get("records", [])
            if not isinstance(raw_records, list):
                continue
            for record in raw_records:
                if not isinstance(record, dict) or not isinstance(record.get("id"), str):
                    continue
                record_id = str(record["id"])
                record_ids.add(record_id)
                provenance = record.get("provenance")
                if isinstance(provenance, dict):
                    records_with_provenance.add(record_id)
                    if provenance.get("humanApprovalRequired") is True:
                        approval_required += 1

        decision_refs: set[str] = set()
        for relative in manifest.get("provenanceExamples", []):
            provenance_path = base / relative
            if not provenance_path.exists():
                continue
            data = read_json(provenance_path)
            decisions = data.get("decisions", [])
            if not isinstance(decisions, list):
                continue
            for decision in decisions:
                if isinstance(decision, dict) and isinstance(decision.get("recordRef"), str):
                    decision_refs.add(str(decision["recordRef"]))

        record_count = len(record_ids)
        provenance_count = len(records_with_provenance)
        decision_covered_count = len(record_ids & decision_refs)
        total_records += record_count
        total_records_with_provenance += provenance_count
        total_decision_records += decision_covered_count
        examples.append(
            {
                "exampleId": manifest.get("id"),
                "domain": manifest.get("domain"),
                "recordCount": record_count,
                "recordsWithProvenance": provenance_count,
                "recordProvenancePercent": _percent(provenance_count, record_count),
                "recordsWithDecisionExamples": decision_covered_count,
                "decisionExamplePercent": _percent(decision_covered_count, record_count),
                "humanApprovalRequiredRecords": approval_required,
                "provenanceExampleCount": len(manifest.get("provenanceExamples", [])),
                "missingProvenanceRecordRefs": sorted(record_ids - records_with_provenance),
                "missingDecisionExampleRecordRefs": sorted(record_ids - decision_refs),
            }
        )

    examples.sort(key=lambda item: str(item["exampleId"]))
    return {
        "exampleCount": len(examples),
        "recordCount": total_records,
        "recordsWithProvenance": total_records_with_provenance,
        "recordProvenancePercent": _percent(total_records_with_provenance, total_records),
        "recordsWithDecisionExamples": total_decision_records,
        "decisionExamplePercent": _percent(total_decision_records, total_records),
        "examples": examples,
    }


def format_provenance_coverage_report(report: dict[str, Any]) -> str:
    """Format provenance coverage for humans."""

    lines = [
        "Provenance Coverage Report",
        "",
        f"Examples: {report['exampleCount']}",
        (
            "Record provenance: "
            f"{report['recordsWithProvenance']}/{report['recordCount']} "
            f"({report['recordProvenancePercent']}%)"
        ),
        (
            "Decision examples: "
            f"{report['recordsWithDecisionExamples']}/{report['recordCount']} "
            f"({report['decisionExamplePercent']}%)"
        ),
        "",
        "Examples:",
    ]
    for example in report["examples"]:
        lines.append(
            f"- {example['exampleId']}: "
            f"{example['recordsWithProvenance']}/{example['recordCount']} records with provenance "
            f"({example['recordProvenancePercent']}%), "
            f"{example['recordsWithDecisionExamples']}/{example['recordCount']} with decision examples "
            f"({example['decisionExamplePercent']}%)"
        )

    return "\n".join(lines) + "\n"


def generate_provenance_distribution_report(root: str | Path) -> dict[str, Any]:
    """Summarize decision-source distribution across provenance examples."""

    root_path = Path(root)
    examples = []
    decision_source_counts: Counter[str] = Counter()
    record_source_counts: Counter[str] = Counter()
    decision_confidence_counts: Counter[str] = Counter()
    record_confidence_counts: Counter[str] = Counter()
    total_decisions = 0
    total_record_provenance = 0
    total_human_approval_decisions = 0
    total_human_approval_records = 0

    for manifest_path, manifest in load_example_manifests(root_path):
        base = manifest_path.parent
        example_decision_sources: Counter[str] = Counter()
        example_record_sources: Counter[str] = Counter()
        example_decision_confidence: Counter[str] = Counter()
        example_record_confidence: Counter[str] = Counter()
        example_decisions = 0
        example_record_provenance = 0
        example_human_approval_decisions = 0
        example_human_approval_records = 0

        for relative in manifest.get("provenanceExamples", []):
            provenance_path = base / relative
            if not provenance_path.exists():
                continue
            data = read_json(provenance_path)
            decisions = data.get("decisions", [])
            if not isinstance(decisions, list):
                continue
            for decision in decisions:
                if not isinstance(decision, dict):
                    continue
                example_decisions += 1
                source = _string_or_unknown(decision.get("decisionSource"))
                confidence = _string_or_unknown(decision.get("confidence"))
                example_decision_sources[source] += 1
                example_decision_confidence[confidence] += 1
                decision_source_counts[source] += 1
                decision_confidence_counts[confidence] += 1
                if decision.get("humanApprovalRequired") is True:
                    example_human_approval_decisions += 1

        for record in _fixture_records(manifest_path, manifest):
            provenance = record.get("provenance")
            if not isinstance(provenance, dict):
                continue
            example_record_provenance += 1
            source = _string_or_unknown(provenance.get("decisionSource"))
            confidence = _string_or_unknown(provenance.get("confidence"))
            example_record_sources[source] += 1
            example_record_confidence[confidence] += 1
            record_source_counts[source] += 1
            record_confidence_counts[confidence] += 1
            if provenance.get("humanApprovalRequired") is True:
                example_human_approval_records += 1

        total_decisions += example_decisions
        total_record_provenance += example_record_provenance
        total_human_approval_decisions += example_human_approval_decisions
        total_human_approval_records += example_human_approval_records
        examples.append(
            {
                "exampleId": manifest.get("id"),
                "domain": manifest.get("domain"),
                "decisionExampleCount": example_decisions,
                "recordProvenanceCount": example_record_provenance,
                "decisionSourceCounts": _counter_summary(
                    example_decision_sources,
                    "decisionSource",
                ),
                "recordProvenanceSourceCounts": _counter_summary(
                    example_record_sources,
                    "decisionSource",
                ),
                "decisionConfidenceCounts": _counter_summary(
                    example_decision_confidence,
                    "confidence",
                ),
                "recordConfidenceCounts": _counter_summary(
                    example_record_confidence,
                    "confidence",
                ),
                "humanApprovalRequiredDecisions": example_human_approval_decisions,
                "humanApprovalRequiredRecords": example_human_approval_records,
            }
        )

    examples.sort(key=lambda item: str(item["exampleId"]))
    return {
        "exampleCount": len(examples),
        "decisionExampleCount": total_decisions,
        "recordProvenanceCount": total_record_provenance,
        "humanApprovalRequiredDecisionCount": total_human_approval_decisions,
        "humanApprovalRequiredRecordCount": total_human_approval_records,
        "decisionSourceCounts": _counter_summary(decision_source_counts, "decisionSource"),
        "recordProvenanceSourceCounts": _counter_summary(
            record_source_counts,
            "decisionSource",
        ),
        "decisionConfidenceCounts": _counter_summary(
            decision_confidence_counts,
            "confidence",
        ),
        "recordConfidenceCounts": _counter_summary(record_confidence_counts, "confidence"),
        "examples": examples,
    }


def format_provenance_distribution_report(report: dict[str, Any]) -> str:
    """Format provenance decision-source distribution for humans."""

    lines = [
        "Provenance Distribution Report",
        "",
        f"Examples: {report['exampleCount']}",
        f"Decision examples: {report['decisionExampleCount']}",
        f"Fixture records with provenance: {report['recordProvenanceCount']}",
        (
            "Human approval required: "
            f"{report['humanApprovalRequiredDecisionCount']} decisions, "
            f"{report['humanApprovalRequiredRecordCount']} records"
        ),
        "",
        "Decision examples by source:",
    ]
    lines.extend(_format_counter_lines(report["decisionSourceCounts"], "decisionSource"))

    lines.extend(["", "Fixture provenance by source:"])
    lines.extend(_format_counter_lines(report["recordProvenanceSourceCounts"], "decisionSource"))

    lines.extend(["", "Examples:"])
    for example in report["examples"]:
        source_summary = _inline_counts(example["decisionSourceCounts"], "decisionSource")
        lines.append(
            f"- {example['exampleId']}: "
            f"{_count(example['decisionExampleCount'], 'decision')}, "
            f"{_count(example['recordProvenanceCount'], 'provenance record')}; "
            f"sources: {source_summary}"
        )

    return "\n".join(lines) + "\n"


def generate_portfolio_fixture_coverage_report(root: str | Path) -> dict[str, Any]:
    """Summarize portfolio fixture coverage by game concept and dependency assumption."""

    root_path = Path(root)
    examples = []
    total_game_concepts = 0
    total_dependency_assumptions = 0
    total_cross_workspace_references = 0
    total_coverage_gaps = 0

    for manifest_path, manifest in load_example_manifests(root_path):
        if manifest.get("domain") != "portfolio":
            continue

        records = _fixture_records(manifest_path, manifest)
        game_concepts = [
            _portfolio_record_summary(record)
            for record in records
            if record.get("kind") == "portfolio.game-concept"
        ]
        dependency_assumptions = [
            _dependency_assumption_summary(record)
            for record in records
            if record.get("kind") in PORTFOLIO_DEPENDENCY_KINDS
        ]
        coverage_gaps = [
            _portfolio_record_summary(record)
            for record in records
            if record.get("kind") in PORTFOLIO_COVERAGE_GAP_KINDS
        ]

        game_groups = _portfolio_game_groups(game_concepts, dependency_assumptions)
        cross_reference_count = sum(
            1
            for item in dependency_assumptions
            if item["kind"] == "workspace.cross-reference"
        )
        portfolio_level_dependency_count = sum(
            1 for item in dependency_assumptions if item["relatedGameConcept"] is None
        )

        total_game_concepts += len(game_concepts)
        total_dependency_assumptions += len(dependency_assumptions)
        total_cross_workspace_references += cross_reference_count
        total_coverage_gaps += len(coverage_gaps)
        examples.append(
            {
                "exampleId": manifest.get("id"),
                "path": str(manifest_path.relative_to(root_path)),
                "gameConceptCount": len(game_concepts),
                "dependencyAssumptionCount": len(dependency_assumptions),
                "crossWorkspaceReferenceCount": cross_reference_count,
                "portfolioLevelDependencyAssumptionCount": portfolio_level_dependency_count,
                "coverageGapCount": len(coverage_gaps),
                "gameConcepts": game_concepts,
                "dependencyAssumptions": dependency_assumptions,
                "gameConceptGroups": game_groups,
                "coverageGaps": coverage_gaps,
            }
        )

    examples.sort(key=lambda item: str(item["exampleId"]))
    return {
        "portfolioExampleCount": len(examples),
        "gameConceptCount": total_game_concepts,
        "dependencyAssumptionCount": total_dependency_assumptions,
        "crossWorkspaceReferenceCount": total_cross_workspace_references,
        "coverageGapCount": total_coverage_gaps,
        "examples": examples,
    }


def format_portfolio_fixture_coverage_report(report: dict[str, Any]) -> str:
    """Format portfolio fixture coverage for humans."""

    lines = [
        "Portfolio Fixture Coverage Report",
        "",
        f"Portfolio examples: {report['portfolioExampleCount']}",
        f"Game concepts: {report['gameConceptCount']}",
        f"Dependency assumptions: {report['dependencyAssumptionCount']}",
        f"Cross-workspace references: {report['crossWorkspaceReferenceCount']}",
        f"Coverage gaps: {report['coverageGapCount']}",
        "",
        "Examples:",
    ]
    for example in report["examples"]:
        lines.append(
            f"- {example['exampleId']}: "
            f"{_count(example['gameConceptCount'], 'game concept')}, "
            f"{_count(example['dependencyAssumptionCount'], 'dependency assumption')}, "
            f"{_count(example['crossWorkspaceReferenceCount'], 'cross-workspace reference')}, "
            f"{_count(example['coverageGapCount'], 'coverage gap')}"
        )
        for group in example["gameConceptGroups"]:
            lines.append(
                f"  - {group['gameConcept']}: "
                f"{_count(group['dependencyAssumptionCount'], 'dependency assumption')}, "
                f"{_count(group['crossWorkspaceReferenceCount'], 'cross-workspace reference')}"
            )
        if example["portfolioLevelDependencyAssumptionCount"]:
            lines.append(
                "  - portfolio-level: "
                f"{_count(example['portfolioLevelDependencyAssumptionCount'], 'dependency assumption')}"
            )

    return "\n".join(lines) + "\n"


def generate_golden_inventory_report(root: str | Path) -> dict[str, Any]:
    """Summarize golden output manifests for release reviewers."""

    root_path = Path(root)
    goldens = []
    for path, manifest in load_golden_manifests(root_path):
        output_path = path.parent / str(manifest.get("outputPath", ""))
        goldens.append(
            {
                "id": manifest.get("id"),
                "name": manifest.get("name"),
                "domain": manifest.get("domain"),
                "promptRef": manifest.get("promptRef"),
                "exampleRef": manifest.get("exampleRef"),
                "interviewMode": manifest.get("interviewMode"),
                "targetReadiness": manifest.get("targetReadiness"),
                "requiredSectionCount": len(manifest.get("requiredSections", [])),
                "outputPath": str(output_path.relative_to(root_path)),
                "outputExists": output_path.exists(),
                "path": str(path.relative_to(root_path)),
            }
        )

    goldens.sort(key=lambda item: str(item["id"]))
    domains = _domain_summary(goldens)
    return {
        "goldenCount": len(goldens),
        "domainCount": len(domains),
        "domains": domains,
        "goldens": goldens,
    }


def format_golden_inventory_report(report: dict[str, Any]) -> str:
    """Format a golden output inventory report for humans."""

    lines = [
        "Golden Output Inventory Report",
        "",
        f"Golden outputs: {report['goldenCount']}",
        f"Domains: {report['domainCount']}",
        "",
        "Domains:",
    ]
    for domain in report["domains"]:
        lines.append(f"- {domain['domain']}: {domain['count']} golden outputs")

    lines.extend(["", "Golden outputs:"])
    for golden in report["goldens"]:
        output_status = "present" if golden["outputExists"] else "missing"
        lines.append(
            f"- {golden['id']} ({golden['domain']} / {golden['targetReadiness']}): "
            f"{golden['requiredSectionCount']} required sections, output {output_status}, "
            f"prompt {golden['promptRef']}"
        )

    return "\n".join(lines) + "\n"


def _domain_summary(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = Counter(str(item.get("domain", "unknown")) for item in items)
    return [
        {
            "domain": domain,
            "count": count,
        }
        for domain, count in sorted(counts.items())
    ]


def _fixture_records(
    manifest_path: Path,
    manifest: dict[str, Any],
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    base = manifest_path.parent
    for relative in manifest.get("workspaceFixtures", []):
        fixture_path = base / relative
        if not fixture_path.exists():
            continue
        data = read_json(fixture_path)
        raw_records = data.get("records", [])
        if isinstance(raw_records, list):
            records.extend(record for record in raw_records if isinstance(record, dict))
    return records


def _counter_summary(counter: Counter[str], name: str) -> list[dict[str, Any]]:
    return [
        {
            name: key,
            "count": count,
        }
        for key, count in sorted(counter.items())
    ]


def _format_counter_lines(items: list[dict[str, Any]], key: str) -> list[str]:
    if not items:
        return ["- none: 0"]
    return [f"- {item[key]}: {item['count']}" for item in items]


def _inline_counts(items: list[dict[str, Any]], key: str) -> str:
    if not items:
        return "none"
    return ", ".join(f"{item[key]}={item['count']}" for item in items)


def _portfolio_record_summary(record: dict[str, Any]) -> dict[str, Any]:
    provenance = record.get("provenance")
    return {
        "id": record.get("id"),
        "kind": record.get("kind"),
        "name": record.get("name"),
        "status": record.get("status"),
        "decisionSource": _provenance_value(provenance, "decisionSource"),
        "confidence": _provenance_value(provenance, "confidence"),
    }


def _dependency_assumption_summary(record: dict[str, Any]) -> dict[str, Any]:
    summary = _portfolio_record_summary(record)
    summary.update(
        {
            "consumerWorkspace": record.get("consumerWorkspace"),
            "providerWorkspace": record.get("providerWorkspace"),
            "alias": record.get("alias"),
            "versionConstraint": record.get("versionConstraint"),
            "sourceRecord": record.get("sourceRecord"),
            "target": record.get("target"),
            "relatedGameConcept": _dependency_game_key(record),
        }
    )
    return summary


def _portfolio_game_groups(
    game_concepts: list[dict[str, Any]],
    dependency_assumptions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    keys: dict[str, str] = {}
    for concept in game_concepts:
        concept_id = concept.get("id")
        if not isinstance(concept_id, str):
            continue
        key = _game_concept_key(concept_id)
        keys[key] = str(concept.get("name") or key)

    for assumption in dependency_assumptions:
        key = assumption.get("relatedGameConcept")
        if isinstance(key, str) and key not in keys:
            keys[key] = key

    groups = []
    for key, name in sorted(keys.items()):
        dependencies = [
            item for item in dependency_assumptions if item.get("relatedGameConcept") == key
        ]
        groups.append(
            {
                "gameConcept": key,
                "name": name,
                "dependencyAssumptionCount": len(dependencies),
                "crossWorkspaceReferenceCount": sum(
                    1 for item in dependencies if item["kind"] == "workspace.cross-reference"
                ),
            }
        )
    return groups


def _game_concept_key(record_id: str) -> str:
    prefix = "portfolio.game."
    if record_id.startswith(prefix):
        return record_id[len(prefix) :]
    return record_id.rsplit(".", 1)[-1]


def _dependency_game_key(record: dict[str, Any]) -> str | None:
    consumer = record.get("consumerWorkspace")
    if isinstance(consumer, str) and consumer.startswith("studio.game."):
        return consumer.removeprefix("studio.game.")

    record_id = record.get("id")
    if not isinstance(record_id, str):
        return None
    for prefix in ("dependency.", "xref."):
        if record_id.startswith(prefix):
            rest = record_id[len(prefix) :]
            return rest.split(".", 1)[0]
    return None


def _provenance_value(provenance: Any, field: str) -> str:
    if not isinstance(provenance, dict):
        return "unknown"
    return _string_or_unknown(provenance.get(field))


def _string_or_unknown(value: Any) -> str:
    if isinstance(value, str) and value:
        return value
    return "unknown"


def _pack_for_kind(kind: str) -> str:
    return FIXTURE_KIND_PACKS.get(kind, "future custom or extension pack")


def _percent(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return 0.0
    return round((numerator / denominator) * 100, 1)


def _count(value: int, noun: str) -> str:
    suffix = "" if value == 1 else "s"
    return f"{value} {noun}{suffix}"

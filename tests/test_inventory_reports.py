from pathlib import Path
import unittest

from verityfoundry.inventory import (
    format_example_inventory_report,
    format_fixture_inventory_report,
    format_generated_workspace_validation_report,
    format_golden_inventory_report,
    format_portfolio_fixture_coverage_report,
    format_provenance_coverage_report,
    format_provenance_distribution_report,
    generate_example_inventory_report,
    generate_fixture_inventory_report,
    generate_generated_workspace_validation_report,
    generate_golden_inventory_report,
    generate_portfolio_fixture_coverage_report,
    generate_provenance_coverage_report,
    generate_provenance_distribution_report,
)


ROOT = Path(__file__).resolve().parents[1]


class InventoryReportTests(unittest.TestCase):
    def test_golden_inventory_counts_and_formats(self) -> None:
        report = generate_golden_inventory_report(ROOT)

        self.assertEqual(report["goldenCount"], 6)
        self.assertGreaterEqual(report["domainCount"], 2)
        self.assertTrue(all(item["outputExists"] for item in report["goldens"]))

        text = format_golden_inventory_report(report)
        self.assertIn("Golden Output Inventory Report", text)
        self.assertIn("golden.unity-game.dream-extraction.implementation-ready", text)
        self.assertIn("golden.lifecycle.customer-portal.release-readiness-gap-review", text)
        self.assertIn("golden.lifecycle.customer-portal.archival-readiness", text)

    def test_example_inventory_counts_and_formats(self) -> None:
        report = generate_example_inventory_report(ROOT)

        self.assertEqual(report["exampleCount"], 6)
        self.assertGreaterEqual(report["domainCount"], 4)
        self.assertTrue(all(item["workspaceFixtureCount"] >= 1 for item in report["examples"]))
        self.assertTrue(all(item["provenanceExampleCount"] >= 1 for item in report["examples"]))

        text = format_example_inventory_report(report)
        self.assertIn("Example Inventory Report", text)
        self.assertIn("example.portfolio.game-portfolio-triage", text)
        self.assertIn("example.unity-game.dream-extraction", text)

    def test_fixture_inventory_counts_and_formats(self) -> None:
        report = generate_fixture_inventory_report(ROOT)

        self.assertEqual(report["fixtureCount"], 6)
        self.assertGreaterEqual(report["recordCount"], 1)
        self.assertGreaterEqual(report["kindCount"], 1)
        self.assertTrue(all(item["exists"] for item in report["fixtures"]))
        self.assertIn("future verity.pack.unity", {item["pack"] for item in report["packs"]})

        text = format_fixture_inventory_report(report)
        self.assertIn("Fixture Inventory Report", text)
        self.assertIn("game.asset.image", text)
        self.assertIn("portfolio.game-concept", text)
        self.assertIn("workspace.dependency", text)
        self.assertIn("future verity.pack.game-assets", text)

    def test_provenance_coverage_counts_and_formats(self) -> None:
        report = generate_provenance_coverage_report(ROOT)

        self.assertEqual(report["exampleCount"], 6)
        self.assertEqual(report["recordProvenancePercent"], 100.0)
        self.assertGreater(report["decisionExamplePercent"], 0)
        self.assertLess(report["decisionExamplePercent"], 100.0)
        self.assertTrue(
            all(not item["missingProvenanceRecordRefs"] for item in report["examples"])
        )

        text = format_provenance_coverage_report(report)
        self.assertIn("Provenance Coverage Report", text)
        self.assertIn("Decision examples:", text)

    def test_provenance_distribution_counts_and_formats(self) -> None:
        report = generate_provenance_distribution_report(ROOT)

        self.assertEqual(report["exampleCount"], 6)
        self.assertGreaterEqual(report["decisionExampleCount"], 18)
        self.assertEqual(
            report["humanApprovalRequiredDecisionCount"],
            report["decisionExampleCount"],
        )
        decision_sources = {
            item["decisionSource"]: item["count"]
            for item in report["decisionSourceCounts"]
        }
        self.assertIn("user-provided", decision_sources)
        self.assertIn("ai-suggested", decision_sources)
        self.assertIn("unresolved", decision_sources)

        text = format_provenance_distribution_report(report)
        self.assertIn("Provenance Distribution Report", text)
        self.assertIn("Decision examples by source:", text)
        self.assertIn("Fixture provenance by source:", text)

    def test_portfolio_fixture_coverage_counts_and_formats(self) -> None:
        report = generate_portfolio_fixture_coverage_report(ROOT)

        self.assertEqual(report["portfolioExampleCount"], 2)
        self.assertEqual(report["gameConceptCount"], 3)
        self.assertGreaterEqual(report["dependencyAssumptionCount"], 7)
        self.assertEqual(report["crossWorkspaceReferenceCount"], 2)

        examples = {item["exampleId"]: item for item in report["examples"]}
        dependency_map = examples["example.portfolio.shared-unity-dependency-map"]
        group_keys = {item["gameConcept"] for item in dependency_map["gameConceptGroups"]}
        self.assertIn("dream_extraction", group_keys)
        self.assertIn("space_runners", group_keys)

        text = format_portfolio_fixture_coverage_report(report)
        self.assertIn("Portfolio Fixture Coverage Report", text)
        self.assertIn("Game concepts:", text)
        self.assertIn("Dependency assumptions:", text)

    def test_generated_workspace_validation_counts_and_formats(self) -> None:
        report = generate_generated_workspace_validation_report(ROOT)

        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["generatedWorkspaceCount"], 2)
        self.assertEqual(report["snapshotCount"], 2)
        self.assertEqual(report["staleFileHashCount"], 0)
        self.assertEqual(report["uncoveredFileCount"], 0)

        text = format_generated_workspace_validation_report(report)
        self.assertIn("Generated Workspace Validation Report", text)
        self.assertIn("Validation snapshots:", text)
        self.assertIn("VeritySpec remains the contract authority", text)


if __name__ == "__main__":
    unittest.main()

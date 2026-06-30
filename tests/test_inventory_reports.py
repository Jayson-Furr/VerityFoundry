from pathlib import Path
import unittest

from verityfoundry.inventory import (
    format_example_inventory_report,
    format_fixture_inventory_report,
    format_golden_inventory_report,
    format_provenance_coverage_report,
    generate_example_inventory_report,
    generate_fixture_inventory_report,
    generate_golden_inventory_report,
    generate_provenance_coverage_report,
)


ROOT = Path(__file__).resolve().parents[1]


class InventoryReportTests(unittest.TestCase):
    def test_golden_inventory_counts_and_formats(self) -> None:
        report = generate_golden_inventory_report(ROOT)

        self.assertEqual(report["goldenCount"], 2)
        self.assertGreaterEqual(report["domainCount"], 1)
        self.assertTrue(all(item["outputExists"] for item in report["goldens"]))

        text = format_golden_inventory_report(report)
        self.assertIn("Golden Output Inventory Report", text)
        self.assertIn("golden.unity-game.dream-extraction.implementation-ready", text)

    def test_example_inventory_counts_and_formats(self) -> None:
        report = generate_example_inventory_report(ROOT)

        self.assertEqual(report["exampleCount"], 4)
        self.assertGreaterEqual(report["domainCount"], 4)
        self.assertTrue(all(item["workspaceFixtureCount"] >= 1 for item in report["examples"]))
        self.assertTrue(all(item["provenanceExampleCount"] >= 1 for item in report["examples"]))

        text = format_example_inventory_report(report)
        self.assertIn("Example Inventory Report", text)
        self.assertIn("example.unity-game.dream-extraction", text)

    def test_fixture_inventory_counts_and_formats(self) -> None:
        report = generate_fixture_inventory_report(ROOT)

        self.assertEqual(report["fixtureCount"], 4)
        self.assertGreaterEqual(report["recordCount"], 1)
        self.assertGreaterEqual(report["kindCount"], 1)
        self.assertTrue(all(item["exists"] for item in report["fixtures"]))
        self.assertIn("future verity.pack.unity", {item["pack"] for item in report["packs"]})

        text = format_fixture_inventory_report(report)
        self.assertIn("Fixture Inventory Report", text)
        self.assertIn("game.asset.image", text)
        self.assertIn("future verity.pack.game-assets", text)

    def test_provenance_coverage_counts_and_formats(self) -> None:
        report = generate_provenance_coverage_report(ROOT)

        self.assertEqual(report["exampleCount"], 4)
        self.assertEqual(report["recordProvenancePercent"], 100.0)
        self.assertGreater(report["decisionExamplePercent"], 0)
        self.assertLess(report["decisionExamplePercent"], 100.0)
        self.assertTrue(
            all(not item["missingProvenanceRecordRefs"] for item in report["examples"])
        )

        text = format_provenance_coverage_report(report)
        self.assertIn("Provenance Coverage Report", text)
        self.assertIn("Decision examples:", text)


if __name__ == "__main__":
    unittest.main()

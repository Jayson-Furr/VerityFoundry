from pathlib import Path
import unittest

from verityfoundry.inventory import (
    format_example_inventory_report,
    format_golden_inventory_report,
    generate_example_inventory_report,
    generate_golden_inventory_report,
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


if __name__ == "__main__":
    unittest.main()

from pathlib import Path
import unittest

from verityfoundry.inventory import (
    generate_golden_inventory_report,
    generate_portfolio_fixture_coverage_report,
    generate_provenance_distribution_report,
)
from verityfoundry.manifests import read_json
from verityfoundry.matrix_coverage import generate_matrix_coverage_report


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "fixtures" / "release-review" / "current"


class ReleaseReviewFixtureTests(unittest.TestCase):
    def test_release_review_fixtures_match_current_reports(self) -> None:
        expected = {
            "golden-inventory.json": generate_golden_inventory_report(ROOT),
            "matrix-coverage.json": generate_matrix_coverage_report(ROOT),
            "portfolio-coverage.json": generate_portfolio_fixture_coverage_report(ROOT),
            "provenance-distribution.json": generate_provenance_distribution_report(ROOT),
        }

        for filename, report in expected.items():
            with self.subTest(filename=filename):
                self.assertEqual(read_json(FIXTURE_ROOT / filename), report)

    def test_release_review_fixtures_cover_expected_reports(self) -> None:
        self.assertEqual(
            {path.name for path in FIXTURE_ROOT.glob("*.json")},
            {
                "golden-inventory.json",
                "matrix-coverage.json",
                "portfolio-coverage.json",
                "provenance-distribution.json",
            },
        )


if __name__ == "__main__":
    unittest.main()

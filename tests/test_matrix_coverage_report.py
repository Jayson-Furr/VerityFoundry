from pathlib import Path
import unittest

from verityfoundry.matrix_coverage import (
    format_matrix_coverage_report,
    generate_matrix_coverage_report,
)


ROOT = Path(__file__).resolve().parents[1]


class MatrixCoverageReportTests(unittest.TestCase):
    def test_matrix_coverage_report_counts_domain_prompts(self) -> None:
        report = generate_matrix_coverage_report(ROOT)

        self.assertGreater(report["matrixCount"], 0)
        self.assertGreater(report["matrixRowCount"], 0)
        self.assertGreater(report["domainPromptCount"], 0)
        self.assertGreater(report["coveredDomainPromptCount"], 0)
        self.assertGreater(report["missingDomainPromptCount"], 0)
        self.assertGreater(report["coveragePercent"], 0)

    def test_matrix_coverage_report_includes_expected_domains(self) -> None:
        report = generate_matrix_coverage_report(ROOT)
        domains = {domain["domain"] for domain in report["domains"]}

        self.assertIn("product", domains)
        self.assertIn("software-library", domains)
        self.assertIn("unity-game", domains)
        self.assertIn("unity-shared-library", domains)

    def test_matrix_coverage_report_formats_text(self) -> None:
        report = generate_matrix_coverage_report(ROOT)
        text = format_matrix_coverage_report(report)

        self.assertIn("Matrix Coverage Report", text)
        self.assertIn("Domain prompt coverage:", text)
        self.assertIn("Missing domain prompts:", text)


if __name__ == "__main__":
    unittest.main()

from pathlib import Path
import unittest

from verityfoundry.release_integrity import (
    check_release_integrity,
    format_release_integrity_report,
)


ROOT = Path(__file__).resolve().parents[1]


class ReleaseIntegrityTests(unittest.TestCase):
    def test_release_integrity_passes_for_current_release(self) -> None:
        report = check_release_integrity(ROOT)

        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["expectedVersion"], "0.11.0")
        self.assertEqual(report["expectedTag"], "v0.11.0")
        self.assertEqual(report["issueCount"], 0)

        text = format_release_integrity_report(report)
        self.assertIn("Release Integrity Check", text)
        self.assertIn("Release integrity check passed.", text)

    def test_release_integrity_fails_for_wrong_expected_version(self) -> None:
        report = check_release_integrity(ROOT, expected_version="0.0.0")

        self.assertEqual(report["status"], "failed")
        self.assertGreater(report["issueCount"], 0)
        codes = {issue["code"] for issue in report["issues"]}
        self.assertIn("release.pyproject-version", codes)
        self.assertIn("release.readme-badge", codes)


if __name__ == "__main__":
    unittest.main()

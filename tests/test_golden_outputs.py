from pathlib import Path
import unittest

from verityfoundry.manifests import load_golden_manifests, read_json
from verityfoundry.validation import validate_goldens


ROOT = Path(__file__).resolve().parents[1]


class GoldenOutputTests(unittest.TestCase):
    def test_golden_outputs_validate(self) -> None:
        self.assertEqual(validate_goldens(ROOT), [])

    def test_unity_game_implementation_ready_golden_exists(self) -> None:
        manifests = {manifest["id"]: (path, manifest) for path, manifest in load_golden_manifests(ROOT)}
        path, manifest = manifests["golden.unity-game.dream-extraction.implementation-ready"]
        self.assertEqual(
            manifest["promptRef"],
            "unity-game.gdd-art.interview-medium.implementation-ready.v1",
        )
        output = (path.parent / manifest["outputPath"]).read_text(encoding="utf-8")
        self.assertIn("## Candidate Workspace Outline", output)
        self.assertIn("## Unresolved Decisions", output)
        self.assertIn("## Human Approval Requirements", output)
        self.assertIn("## Suggested VeritySpec Validation Loop", output)
        self.assertIn("not implementation-ready", output)

    def test_unity_shared_library_implementation_ready_golden_exists(self) -> None:
        manifests = {manifest["id"]: (path, manifest) for path, manifest in load_golden_manifests(ROOT)}
        path, manifest = manifests[
            "golden.unity-shared-library.shared-unity-runtime.implementation-ready"
        ]
        self.assertEqual(
            manifest["promptRef"],
            "unity-library.description.interview-medium.implementation-ready.v1",
        )
        output = (path.parent / manifest["outputPath"]).read_text(encoding="utf-8")
        self.assertIn("## Candidate Workspace Outline", output)
        self.assertIn("## Unresolved Decisions", output)
        self.assertIn("## Human Approval Requirements", output)
        self.assertIn("## Suggested VeritySpec Validation Loop", output)
        self.assertIn("Public/exported records versus internal/private records", output)
        self.assertIn("not implementation-ready", output)

    def test_lifecycle_golden_outputs_exist(self) -> None:
        manifests = {manifest["id"]: (path, manifest) for path, manifest in load_golden_manifests(ROOT)}
        expected = {
            "golden.lifecycle.customer-portal.release-readiness-gap-review": (
                "lifecycle.workspace.interview-medium.production-ready.release-gap-review.v1",
                "not release-ready",
                "## Blocking Gaps",
            ),
            "golden.lifecycle.shared-auth-library.maintenance-readiness": (
                "lifecycle.shipped-product.interview-high.maintenance-ready.v1",
                "not maintenance-ready",
                "## Support Handoff Gaps",
            ),
            "golden.lifecycle.shared-unity-runtime.decommission-readiness": (
                "lifecycle.retiring-product.interview-all.decommission-ready.v1",
                "not decommission-ready",
                "## Archive Follow-Up Items",
            ),
            "golden.lifecycle.customer-portal.archival-readiness": (
                "lifecycle.archived-product.interview-all.archival-ready.v1",
                "not archival-ready",
                "## Archive Manifest Gaps",
            ),
        }

        for golden_id, (prompt_ref, readiness_phrase, required_heading) in expected.items():
            with self.subTest(golden_id=golden_id):
                path, manifest = manifests[golden_id]
                self.assertEqual(manifest["domain"], "lifecycle")
                self.assertEqual(manifest["promptRef"], prompt_ref)
                output = (path.parent / manifest["outputPath"]).read_text(encoding="utf-8")
                self.assertIn(readiness_phrase, output)
                self.assertIn(required_heading, output)
                self.assertIn("## Human Approval Requirements", output)
                self.assertIn("## Suggested VeritySpec Validation Loop", output)

    def test_lifecycle_golden_drift_snapshot_exists(self) -> None:
        snapshot = read_json(ROOT / "snapshots" / "golden-output" / "lifecycle-v0.19.0.json")

        self.assertEqual(snapshot["label"], "v0.19.0-lifecycle")
        self.assertEqual(snapshot["goldenCount"], 3)
        self.assertEqual(
            {item["id"] for item in snapshot["goldens"]},
            {
                "golden.lifecycle.customer-portal.release-readiness-gap-review",
                "golden.lifecycle.shared-auth-library.maintenance-readiness",
                "golden.lifecycle.shared-unity-runtime.decommission-readiness",
            },
        )


if __name__ == "__main__":
    unittest.main()

from pathlib import Path
import unittest

from verityfoundry.manifests import load_matrix_manifests
from verityfoundry.matrix import render_matrix
from verityfoundry.validation import validate_matrices


ROOT = Path(__file__).resolve().parents[1]


class MatrixManifestTests(unittest.TestCase):
    def test_matrix_manifests_validate(self) -> None:
        self.assertEqual(validate_matrices(ROOT), [])

    def test_expected_matrices_exist(self) -> None:
        ids = {item.manifest["id"] for item in load_matrix_manifests(ROOT)}
        self.assertEqual(
            ids,
            {"unity-game", "unity-shared-library", "software-library", "product"},
        )

    def test_render_unity_game_matrix(self) -> None:
        rendered = render_matrix(ROOT, "unity-game")
        self.assertIn("Unity Game Prompt Matrix", rendered)
        self.assertIn("implementation-ready", rendered)


if __name__ == "__main__":
    unittest.main()

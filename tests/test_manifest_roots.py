import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from verityfoundry.manifests import find_project_root


def make_artifact_root(path: Path) -> None:
    for name in ("prompts", "matrices", "schemas", "examples", "goldens"):
        (path / name).mkdir(parents=True, exist_ok=True)


class ManifestRootTests(unittest.TestCase):
    def test_default_root_can_fallback_to_installed_artifacts(self) -> None:
        original_cwd = Path.cwd()
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            asset_root = temp_root / "share" / "verityfoundry"
            outside_checkout = temp_root / "outside"
            make_artifact_root(asset_root)
            outside_checkout.mkdir()

            try:
                os.chdir(outside_checkout)
                with patch.dict(os.environ, {"VERITYFOUNDRY_ASSET_ROOT": str(asset_root)}):
                    self.assertEqual(find_project_root(), asset_root.resolve())
            finally:
                os.chdir(original_cwd)

    def test_explicit_root_does_not_fallback_to_installed_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            asset_root = temp_root / "share" / "verityfoundry"
            explicit_root = temp_root / "explicit"
            make_artifact_root(asset_root)
            explicit_root.mkdir()

            with patch.dict(os.environ, {"VERITYFOUNDRY_ASSET_ROOT": str(asset_root)}):
                self.assertEqual(find_project_root(explicit_root), explicit_root.resolve())

    def test_explicit_artifact_root_does_not_need_pyproject(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            asset_root = Path(tmp) / "share" / "verityfoundry"
            make_artifact_root(asset_root)

            self.assertEqual(find_project_root(asset_root), asset_root.resolve())


if __name__ == "__main__":
    unittest.main()

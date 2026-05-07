import pytest

from src.kb_builder.config import load_config
from src.kb_builder.paths import ensure_project_paths, resolve_repo_path


def test_resolve_repo_path_rejects_parent_segments():
    with pytest.raises(ValueError):
        resolve_repo_path("../reference", "test.path")


def test_load_config_rejects_parent_segments():
    with pytest.raises(ValueError):
        load_config("../config.yml")


def test_resolve_repo_path_rejects_absolute_paths_outside_repo():
    with pytest.raises(ValueError):
        resolve_repo_path("/tmp/focuslocust-outside", "test.path")


def test_ensure_project_paths_creates_stage_one_directories(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    paths = ensure_project_paths(
        {
            "vault_path": "vault",
            "cache": {"dir": ".cache"},
            "logging": {"log_dir": ".logs"},
        }
    )

    assert paths.vault_path == tmp_path / "vault"
    assert (tmp_path / "vault/kb/mitre/attack/techniques").is_dir()
    assert (tmp_path / "vault/kb/mitre/attack/software").is_dir()
    assert (tmp_path / "vault/kb/mitre/attack/indexes").is_dir()
    assert (tmp_path / "vault/kb/indexes").is_dir()
    assert not (tmp_path / "vault/kb/tools").exists()
    assert not (tmp_path / "vault/kb/detections").exists()
    assert not (tmp_path / "vault/kb/tests").exists()
    assert not (tmp_path / "vault/kb/payloads").exists()
    assert not (tmp_path / "vault/ws").exists()

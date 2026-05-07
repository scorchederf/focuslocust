from src.kb_builder.safe_write import (
    clean_generated_markdown,
    is_generated_file,
    safe_write_text,
)


def test_generated_file_can_be_overwritten(tmp_path):
    path = tmp_path / "note.md"
    path.write_text("---\nparsed_by: focuslocust\n---\nold", encoding="utf-8")

    result = safe_write_text(
        path,
        "---\nparsed_by: focuslocust\n---\nnew",
        marker="focuslocust",
    )

    assert result is True
    assert "new" in path.read_text(encoding="utf-8")


def test_manual_file_cannot_be_overwritten(tmp_path):
    path = tmp_path / "note.md"
    path.write_text("manual note", encoding="utf-8")

    result = safe_write_text(
        path,
        "---\nparsed_by: focuslocust\n---\nnew",
        marker="focuslocust",
    )

    assert result is False
    assert path.read_text(encoding="utf-8") == "manual note"


def test_generated_detection(tmp_path):
    generated = tmp_path / "generated.md"
    manual = tmp_path / "manual.md"

    generated.write_text("---\nparsed_by: focuslocust\n---", encoding="utf-8")
    manual.write_text("manual", encoding="utf-8")

    assert is_generated_file(generated, "focuslocust") is True
    assert is_generated_file(manual, "focuslocust") is False


def test_clean_generated_markdown(tmp_path):
    generated = tmp_path / "generated.md"
    manual = tmp_path / "manual.md"

    generated.write_text("---\nparsed_by: focuslocust\n---", encoding="utf-8")
    manual.write_text("manual", encoding="utf-8")

    count = clean_generated_markdown([tmp_path], marker="focuslocust")

    assert count == 1
    assert not generated.exists()
    assert manual.exists()

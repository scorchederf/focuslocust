---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# poetry

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `poetry` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/poetry` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for poetry covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/poetry.md)
- Source verification: [source record](../../sources/gtfobins/poetry.md)

## Aliases

- `poetry`

## Source Verification

[source record](../../sources/gtfobins/poetry.md)

## Evidence Excerpt

```text
_body: ''
_name: poetry
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/poetry
functions:
inherit:
- code: 'echo ''...'' >/path/to/temp-file
poetry run python /path/to/temp-file'
comment: 'This allows to run Python code (`...`).
```

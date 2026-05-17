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

## Generated Concept Page

- [poetry](../../tools/linux/poetry.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | poetry |
| name | poetry |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/poetry/ |

## Preserved Source Material

```yaml
_body: ''
_name: poetry
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/poetry
functions:
  inherit:
  - code: 'echo ''...'' >/path/to/temp-file

      poetry run python /path/to/temp-file'
    comment: 'This allows to run Python code (`...`).


      A valid `pyproject.toml` file must be present in the current working directory, you can create one with `poetry init
      -n`.'
    contexts:
      sudo: null
      unprivileged: null
    from: python
```

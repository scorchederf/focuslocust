---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mypy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mypy` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mypy` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mypy](../../tools/linux/mypy.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mypy |
| name | mypy |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mypy/ |

## Preserved Source Material

```yaml
_body: ''
_name: mypy
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mypy
functions:
  file-read:
  - binary: false
    code: mypy /path/to/input-file
    comment: Partial content is leaked as error messages.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - binary: false
    code: mypy /path/to/input-file --junit-xml /path/to/output-file
    comment: Partial content is leaked as error messages inside some XML tags.
    contexts:
      sudo: null
      unprivileged: null
```

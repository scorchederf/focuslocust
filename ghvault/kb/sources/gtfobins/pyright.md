---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pyright

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pyright` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pyright` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pyright](../../tools/linux/pyright.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pyright |
| name | pyright |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pyright/ |

## Preserved Source Material

```yaml
_body: ''
_name: pyright
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pyright
functions:
  file-read:
  - binary: false
    code: pyright /path/to/input-file
    comment: Content is leaked as error messages.
    contexts:
      sudo: null
      unprivileged: null
  - binary: false
    code: pyright --outputjson /path/to/input-file
    comment: Content is leaked as error messages in JSON format.
    contexts:
      sudo: null
      unprivileged: null
  - code: pyright -w /path/to/input-dir/
    comment: Recursively walks directories, parsing all Python files and leaking some contents through diagnostics.
    contexts:
      sudo: null
      unprivileged: null
```

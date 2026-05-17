---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pipx

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pipx` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pipx` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pipx](../../tools/linux/pipx.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pipx |
| name | pipx |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pipx/ |

## Preserved Source Material

```yaml
_body: ''
_name: pipx
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pipx
functions:
  inherit:
  - code: 'echo ''...'' >/path/to/file.py

      pipx run /path/to/file.py'
    comment: This allows to run Python code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: python
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gimp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gimp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gimp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [gimp](../../tools/linux/gimp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | gimp |
| name | gimp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/gimp/ |

## Preserved Source Material

```yaml
_body: ''
_name: gimp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gimp
functions:
  inherit:
  - code: gimp -idf --batch-interpreter=python-fu-eval -b '...'
    comment: This allows to run Python code (`...`). It hangs afterwards and can be terminated by pressing `Ctrl-C`.
    contexts:
      sudo: null
      unprivileged: null
    from: python
```

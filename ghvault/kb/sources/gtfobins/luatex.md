---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# luatex

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `luatex` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/luatex` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [luatex](../../tools/linux/luatex.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | luatex |
| name | luatex |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/luatex/ |

## Preserved Source Material

```yaml
_body: ''
_name: luatex
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/luatex
functions:
  inherit:
  - code: luatex -shell-escape '\directlua{...}\end'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
```

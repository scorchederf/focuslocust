---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lualatex

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lualatex` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lualatex` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [lualatex](../../tools/linux/lualatex.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | lualatex |
| name | lualatex |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/lualatex/ |

## Preserved Source Material

```yaml
_body: ''
_name: lualatex
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lualatex
functions:
  inherit:
  - code: lualatex -shell-escape '\directlua{...}\end'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
```

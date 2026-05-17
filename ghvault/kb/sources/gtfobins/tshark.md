---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tshark

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tshark` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tshark` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tshark](../../tools/linux/tshark.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tshark |
| name | tshark |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tshark/ |

## Preserved Source Material

```yaml
_body: ''
_name: tshark
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tshark
functions:
  inherit:
  - code: 'echo ''...'' >/path/to/temp-file

      tshark -Xlua_script:/path/to/temp-file'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: lua
```

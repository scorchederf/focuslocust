---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sqlmap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sqlmap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlmap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sqlmap](../../tools/linux/sqlmap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sqlmap |
| name | sqlmap |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sqlmap/ |

## Preserved Source Material

```yaml
_body: ''
_name: sqlmap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlmap
functions:
  inherit:
  - code: sqlmap -u 127.0.0.1 --eval='...'
    comment: This allows to run Python code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: python
```

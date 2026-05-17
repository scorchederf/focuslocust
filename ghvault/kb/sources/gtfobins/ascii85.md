---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ascii85

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ascii85` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ascii85` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ascii85](../../tools/linux/ascii85.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ascii85 |
| name | ascii85 |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ascii85/ |

## Preserved Source Material

```yaml
_body: ''
_name: ascii85
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ascii85
functions:
  file-read:
  - code: ascii85 /path/to/input-file | ascii85 --decode
    contexts:
      sudo: null
      unprivileged: null
```

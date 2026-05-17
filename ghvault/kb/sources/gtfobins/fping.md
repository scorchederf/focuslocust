---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fping

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fping` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fping` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [fping](../../tools/linux/fping.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fping |
| name | fping |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/fping/ |

## Preserved Source Material

```yaml
_body: ''
_name: fping
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fping
functions:
  file-read:
  - binary: false
    code: fping -f /path/to/input-file
    comment: Each line is treated as an hostname and it's leaked as an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

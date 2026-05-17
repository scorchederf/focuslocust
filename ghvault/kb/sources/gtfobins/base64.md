---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# base64

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `base64` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base64` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [base64](../../tools/linux/base64.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | base64 |
| name | base64 |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/base64/ |

## Preserved Source Material

```yaml
_body: ''
_name: base64
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base64
functions:
  file-read:
  - code: base64 /path/to/input-file | base64 --decode
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

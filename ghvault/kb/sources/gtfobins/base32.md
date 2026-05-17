---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# base32

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `base32` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base32` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [base32](../../tools/linux/base32.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | base32 |
| name | base32 |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/base32/ |

## Preserved Source Material

```yaml
_body: ''
_name: base32
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base32
functions:
  file-read:
  - code: base32 /path/to/input-file | base32 --decode
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

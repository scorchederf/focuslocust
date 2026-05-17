---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# arj

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `arj` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arj` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [arj](../../tools/linux/arj.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | arj |
| name | arj |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/arj/ |

## Preserved Source Material

```yaml
_body: ''
_name: arj
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arj
functions:
  file-read:
  - binary: false
    code: 'arj a /path/to/output-file /path/to/input-file

      arj p /path/to/output-file'
    comment: The `.arj` suffix will be added to `output-file`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: 'echo DATA >output-file

      arj a x output-file

      arj e x /path/to/output-dir/'
    comment: The `.arj` suffix will be added to `x`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# date

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `date` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/date` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [date](../../tools/linux/date.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | date |
| name | date |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/date/ |

## Preserved Source Material

```yaml
_body: ''
_name: date
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/date
functions:
  file-read:
  - binary: false
    code: date -f /path/to/input-file
    comment: Each line is corrupted by a prefix string and wrapped inside quotes.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: GNU
```

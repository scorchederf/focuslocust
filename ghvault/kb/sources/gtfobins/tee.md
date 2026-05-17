---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tee

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tee` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tee` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tee](../../tools/linux/tee.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tee |
| name | tee |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tee/ |

## Preserved Source Material

```yaml
_body: ''
_name: tee
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tee
functions:
  file-write:
  - code: echo DATA | tee /path/to/output-file
    comment: Use `-a` to append data to exising files.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sort

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sort` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sort` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sort](../../tools/linux/sort.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sort |
| name | sort |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sort/ |

## Preserved Source Material

```yaml
_body: ''
_name: sort
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sort
functions:
  file-read:
  - binary: false
    code: sort -m /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - binary: false
    code: echo DATA | sort -m -o /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

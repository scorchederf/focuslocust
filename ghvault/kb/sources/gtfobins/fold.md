---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fold

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fold` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fold` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [fold](../../tools/linux/fold.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fold |
| name | fold |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/fold/ |

## Preserved Source Material

```yaml
_body: ''
_name: fold
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fold
functions:
  file-read:
  - binary: false
    code: fold -w999 /path/to/input-file
    comment: This corrupts the output by wrapping very long lines at the given width (`999`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

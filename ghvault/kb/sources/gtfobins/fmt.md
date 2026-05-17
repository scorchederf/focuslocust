---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fmt

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fmt` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fmt` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [fmt](../../tools/linux/fmt.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fmt |
| name | fmt |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/fmt/ |

## Preserved Source Material

```yaml
_body: ''
_name: fmt
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fmt
functions:
  file-read:
  - binary: false
    code: fmt -pNON_EXISTING_PREFIX /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: GNU
  - binary: false
    code: fmt -999 /path/to/input-file
    comment: This corrupts the output by wrapping very long lines at the given width (`999`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

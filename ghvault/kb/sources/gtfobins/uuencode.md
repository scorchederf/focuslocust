---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# uuencode

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `uuencode` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/uuencode` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [uuencode](../../tools/linux/uuencode.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | uuencode |
| name | uuencode |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/uuencode/ |

## Preserved Source Material

```yaml
_body: ''
_name: uuencode
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/uuencode
functions:
  file-read:
  - binary: false
    code: uuencode /path/to/input-file /dev/stdout | uudecode
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

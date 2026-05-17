---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xxd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xxd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xxd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [xxd](../../tools/linux/xxd.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xxd |
| name | xxd |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/xxd/ |

## Preserved Source Material

```yaml
_body: ''
_name: xxd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xxd
functions:
  file-read:
  - code: xxd /path/to/input-file | xxd -r
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: echo DATA | xxd | xxd -r - /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

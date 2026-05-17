---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dmesg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dmesg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmesg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dmesg](../../tools/linux/dmesg.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dmesg |
| name | dmesg |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dmesg/ |

## Preserved Source Material

```yaml
_body: ''
_name: dmesg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmesg
functions:
  file-read:
  - binary: false
    code: dmesg -rF /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  inherit:
  - code: dmesg -H
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: less
```

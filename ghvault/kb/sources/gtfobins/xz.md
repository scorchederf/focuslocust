---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xz

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xz` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xz` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [xz](../../tools/linux/xz.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xz |
| name | xz |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/xz/ |

## Preserved Source Material

```yaml
_body: ''
_name: xz
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xz
functions:
  file-read:
  - code: xz -c /path/to/input-file | xz -d
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# readelf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `readelf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/readelf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [readelf](../../tools/linux/readelf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | readelf |
| name | readelf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/readelf/ |

## Preserved Source Material

```yaml
_body: ''
_name: readelf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/readelf
functions:
  file-read:
  - binary: false
    code: readelf -a @/path/to/input-file
    comment: Each line is corrupted by a prefix string and wrapped inside single quotes. Also consider that lines are actually
      parsed as `readelf` options thus some file contents may lead to unexpected results.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xmodmap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xmodmap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xmodmap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [xmodmap](../../tools/linux/xmodmap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xmodmap |
| name | xmodmap |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/xmodmap/ |

## Preserved Source Material

```yaml
_body: ''
_name: xmodmap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xmodmap
comment: This requires a running X server.
functions:
  file-read:
  - binary: false
    code: xmodmap -v /path/to/input-file
    comment: The read file content is corrupted by error prints.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

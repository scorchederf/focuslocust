---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# genisoimage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `genisoimage` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/genisoimage` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [genisoimage](../../tools/linux/genisoimage.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | genisoimage |
| name | genisoimage |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/genisoimage/ |

## Preserved Source Material

```yaml
_body: ''
_name: genisoimage
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/genisoimage
functions:
  file-read:
  - code: genisoimage -q -o - /path/to/input-file
    comment: The output is placed inside the ISO9660 file system binary format, it can be mounted or extracted with tools
      like `7z`.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: genisoimage -sort /path/to/input-file
    comment: The file is parsed, and some of its content is disclosed by the error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

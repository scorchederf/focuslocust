---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xpad

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xpad` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xpad` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [xpad](../../tools/linux/xpad.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xpad |
| name | xpad |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/xpad/ |

## Preserved Source Material

```yaml
_body: ''
_name: xpad
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xpad
comment: This requires a running X server.
functions:
  file-read:
  - code: xpad -f /path/to/input-file
    comment: The file is displayed in a graphical window.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

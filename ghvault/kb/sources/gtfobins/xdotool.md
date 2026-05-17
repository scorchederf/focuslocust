---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xdotool

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xdotool` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xdotool` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [xdotool](../../tools/linux/xdotool.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xdotool |
| name | xdotool |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/xdotool/ |

## Preserved Source Material

```yaml
_body: ''
_name: xdotool
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xdotool
comment: This requires a running X server.
functions:
  shell:
  - code: xdotool exec --sync /bin/sh
    contexts:
      sudo: null
      suid:
        code: xdotool exec --sync /bin/sh -p
        shell: false
      unprivileged: null
```

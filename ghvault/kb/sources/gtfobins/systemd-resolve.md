---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# systemd-resolve

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `systemd-resolve` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/systemd-resolve` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [systemd-resolve](../../tools/linux/systemd-resolve.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | systemd-resolve |
| name | systemd-resolve |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/systemd-resolve/ |

## Preserved Source Material

```yaml
_body: ''
_name: systemd-resolve
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/systemd-resolve
functions:
  inherit:
  - code: systemd-resolve --status
    contexts:
      sudo: null
    from: less
```

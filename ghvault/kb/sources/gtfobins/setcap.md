---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# setcap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `setcap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setcap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [setcap](../../tools/linux/setcap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | setcap |
| name | setcap |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/setcap/ |

## Preserved Source Material

```yaml
_body: ''
_name: setcap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setcap
functions:
  privilege-escalation:
  - code: setcap cap_setuid+ep /path/to/command
    comment: This can be used to assign capabilities to executable files.
    contexts:
      sudo: null
      suid: null
```

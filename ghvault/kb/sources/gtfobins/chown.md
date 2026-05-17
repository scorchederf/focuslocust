---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# chown

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `chown` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chown` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [chown](../../tools/linux/chown.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | chown |
| name | chown |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/chown/ |

## Preserved Source Material

```yaml
_body: ''
_name: chown
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chown
functions:
  privilege-escalation:
  - code: chown $(id -un):$(id -gn) /path/to/input-file
    comment: This can be run with elevated privileges to change ownership and then read, write, or execute a file.
    contexts:
      sudo: null
      suid: null
```

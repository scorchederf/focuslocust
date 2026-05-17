---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# setfacl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `setfacl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setfacl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [setfacl](../../tools/linux/setfacl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | setfacl |
| name | setfacl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/setfacl/ |

## Preserved Source Material

```yaml
_body: ''
_name: setfacl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setfacl
functions:
  privilege-escalation:
  - code: setfacl -m u:$(id -un):rwx /path/to/input-file
    comment: This can be run with elevated privileges to change ownership and then read, write, or execute a file.
    contexts:
      sudo: null
      suid: null
```

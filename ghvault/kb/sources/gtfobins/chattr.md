---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# chattr

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `chattr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chattr` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [chattr](../../tools/linux/chattr.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | chattr |
| name | chattr |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/chattr/ |

## Preserved Source Material

```yaml
_body: ''
_name: chattr
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chattr
functions:
  privilege-escalation:
  - code: chattr +i /path/to/input-file
    comment: Make the target file immutable.
    contexts:
      sudo: null
      suid: null
```

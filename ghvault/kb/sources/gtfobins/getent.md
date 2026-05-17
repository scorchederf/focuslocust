---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# getent

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `getent` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/getent` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [getent](../../tools/linux/getent.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | getent |
| name | getent |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/getent/ |

## Preserved Source Material

```yaml
_body: ''
_name: getent
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/getent
functions:
  privilege-escalation:
  - code: getent shadow
    comment: This allows to dump password hashes from the `/etc/shadow` file.
    contexts:
      sudo: null
      suid: null
```

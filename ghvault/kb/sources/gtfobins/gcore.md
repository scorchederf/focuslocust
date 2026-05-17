---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gcore

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gcore` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcore` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [gcore](../../tools/linux/gcore.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | gcore |
| name | gcore |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/gcore/ |

## Preserved Source Material

```yaml
_body: ''
_name: gcore
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcore
functions:
  file-read:
  - code: gcore $PID
    comment: It can be used to generate core dumps of running processes (`$PID`). Such files often contains sensitive information
      such as open files content, cryptographic keys, passwords, etc. This command produces a binary file named `core.$PID`,
      that is then often filtered with `strings` to narrow down relevant information.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

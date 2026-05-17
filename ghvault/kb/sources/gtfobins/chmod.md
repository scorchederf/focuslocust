---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# chmod

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `chmod` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chmod` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [chmod](../../tools/linux/chmod.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | chmod |
| name | chmod |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/chmod/ |

## Preserved Source Material

```yaml
_body: ''
_name: chmod
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chmod
functions:
  privilege-escalation:
  - code: chmod 6777 /path/to/input-file
    comment: This can be run with elevated privileges to change permissions (`6` denotes the SUID bits) and then read, write,
      or execute a file.
    contexts:
      sudo: null
      suid: null
```

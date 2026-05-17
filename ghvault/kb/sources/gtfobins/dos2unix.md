---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dos2unix

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dos2unix` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dos2unix` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dos2unix](../../tools/linux/dos2unix.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dos2unix |
| name | dos2unix |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dos2unix/ |

## Preserved Source Material

```yaml
_body: ''
_name: dos2unix
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dos2unix
functions:
  file-read:
  - code: dos2unix -f -O /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: dos2unix -f -n /path/to/input-file /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

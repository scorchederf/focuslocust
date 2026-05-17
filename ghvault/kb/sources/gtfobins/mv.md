---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mv

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mv` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mv` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mv](../../tools/linux/mv.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mv |
| name | mv |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mv/ |

## Preserved Source Material

```yaml
_body: ''
_name: mv
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mv
functions:
  file-write:
  - code: 'echo DATA >/path/to/temp-file

      mv /path/to/temp-file /path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  privilege-escalation:
  - code: mv /path/to/input-file /path/to/output-file
    comment: This can be used to move and then read or write files from a restricted file systems or with elevated privileges.
    contexts:
      sudo: null
      suid: null
```

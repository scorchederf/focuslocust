---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# comm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `comm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/comm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [comm](../../tools/linux/comm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | comm |
| name | comm |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/comm/ |

## Preserved Source Material

```yaml
_body: ''
_name: comm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/comm
functions:
  file-read:
  - binary: false
    code: comm /path/to/input-file /dev/null
    comment: A newline is appended to the file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

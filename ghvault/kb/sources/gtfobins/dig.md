---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dig

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dig` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dig` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dig](../../tools/linux/dig.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dig |
| name | dig |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dig/ |

## Preserved Source Material

```yaml
_body: ''
_name: dig
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dig
functions:
  file-read:
  - code: dig -f /path/to/input-file
    comment: Each input line is treated as a lookup query for the `dig` command and the output is corrupted with the result
      or errors of the operation.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

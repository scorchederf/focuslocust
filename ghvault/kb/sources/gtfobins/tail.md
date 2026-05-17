---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tail

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tail` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tail` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tail](../../tools/linux/tail.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tail |
| name | tail |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tail/ |

## Preserved Source Material

```yaml
_body: ''
_name: tail
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tail
functions:
  file-read:
  - code: tail -c+0 /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

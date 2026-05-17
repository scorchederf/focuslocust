---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# expand

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `expand` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/expand` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [expand](../../tools/linux/expand.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | expand |
| name | expand |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/expand/ |

## Preserved Source Material

```yaml
_body: ''
_name: expand
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/expand
functions:
  file-read:
  - binary: false
    code: expand /path/to/input-file
    comment: The read file content is corrupted by replacing tabs with spaces.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

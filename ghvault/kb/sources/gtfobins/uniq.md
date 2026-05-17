---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# uniq

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `uniq` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/uniq` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [uniq](../../tools/linux/uniq.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | uniq |
| name | uniq |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/uniq/ |

## Preserved Source Material

```yaml
_body: ''
_name: uniq
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/uniq
functions:
  file-read:
  - binary: false
    code: uniq /path/to/input-file
    comment: The read file content is corrupted by squashing multiple adjacent lines.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

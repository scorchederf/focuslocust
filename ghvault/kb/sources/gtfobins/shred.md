---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# shred

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `shred` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/shred` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [shred](../../tools/linux/shred.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | shred |
| name | shred |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/shred/ |

## Preserved Source Material

```yaml
_body: ''
_name: shred
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/shred
functions:
  file-write:
  - code: shred -u /path/to/output-file
    comment: This actually deletes the chosen file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

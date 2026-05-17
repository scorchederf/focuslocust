---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# shuf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `shuf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/shuf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [shuf](../../tools/linux/shuf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | shuf |
| name | shuf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/shuf/ |

## Preserved Source Material

```yaml
_body: ''
_name: shuf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/shuf
functions:
  file-read:
  - code: shuf -z /path/to/input-file
    comment: The read file content is corrupted by randomizing the order of NUL terminated strings.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: shuf -e DATA -o /path/to/output-file
    comment: The written file content is corrupted by adding a newline.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

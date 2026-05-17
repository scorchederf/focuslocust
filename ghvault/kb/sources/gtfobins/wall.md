---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wall

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wall` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wall` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [wall](../../tools/linux/wall.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wall |
| name | wall |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/wall/ |

## Preserved Source Material

```yaml
_body: ''
_name: wall
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wall
functions:
  file-read:
  - binary: false
    code: wall --nobanner /path/to/input-file
    comment: The textual file is dumped on the current TTY (neither to `stdout` nor to `stderr`).
    contexts:
      sudo: null
```

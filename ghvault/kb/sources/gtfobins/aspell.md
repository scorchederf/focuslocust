---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# aspell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `aspell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aspell` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [aspell](../../tools/linux/aspell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | aspell |
| name | aspell |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/aspell/ |

## Preserved Source Material

```yaml
_body: ''
_name: aspell
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aspell
functions:
  file-read:
  - binary: false
    code: aspell -c /path/to/input-file
    comment: The textual file is displayed in an interactive TUI showing only the parts that contain mispelled words.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - binary: false
    code: aspell --conf /path/to/input-file
    comment: The first word is likely displayed as error messaged, and converted to lowercase.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

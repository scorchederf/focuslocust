---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mtr

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mtr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mtr` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mtr](../../tools/linux/mtr.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mtr |
| name | mtr |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mtr/ |

## Preserved Source Material

```yaml
_body: ''
_name: mtr
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mtr
functions:
  file-read:
  - binary: false
    code: mtr --raw -F /path/to/input-file
    comment: The file is actually parsed, thus the content is corrupted by error prints.
    contexts:
      sudo: null
      unprivileged: null
```

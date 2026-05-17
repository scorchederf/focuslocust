---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# grep

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `grep` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/grep` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [grep](../../tools/linux/grep.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | grep |
| name | grep |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/grep/ |

## Preserved Source Material

```yaml
_body: ''
_name: grep
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/grep
functions:
  file-read:
  - binary: false
    code: grep '' /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

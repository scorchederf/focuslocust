---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# strings

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `strings` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strings` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [strings](../../tools/linux/strings.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | strings |
| name | strings |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/strings/ |

## Preserved Source Material

```yaml
_body: ''
_name: strings
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strings
functions:
  file-read:
  - binary: false
    code: strings /path/to/input-file
    comment: This only returns ASCII strings.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

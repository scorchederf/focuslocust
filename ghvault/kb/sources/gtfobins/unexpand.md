---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# unexpand

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `unexpand` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unexpand` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [unexpand](../../tools/linux/unexpand.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | unexpand |
| name | unexpand |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/unexpand/ |

## Preserved Source Material

```yaml
_body: ''
_name: unexpand
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unexpand
functions:
  file-read:
  - binary: false
    code: unexpand -t999 /path/to/input-file
    comment: Convert sequences of (e.g., `999`) spaces to tab.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [bc](../../tools/linux/bc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bc |
| name | bc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/bc/ |

## Preserved Source Material

```yaml
_body: ''
_name: bc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bc
functions:
  file-read:
  - code: 'bc -s /path/to/input-file

      quit'
    comment: The file content is actually parsed and appears as error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

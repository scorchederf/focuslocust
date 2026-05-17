---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nm](../../tools/linux/nm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nm |
| name | nm |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nm/ |

## Preserved Source Material

```yaml
_body: ''
_name: nm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nm
functions:
  file-read:
  - binary: false
    code: nm /path/to/input-file
    comment: The file content is treated as command line options and disclosed through error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

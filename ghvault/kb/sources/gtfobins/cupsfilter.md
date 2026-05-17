---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cupsfilter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cupsfilter` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cupsfilter` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cupsfilter](../../tools/linux/cupsfilter.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cupsfilter |
| name | cupsfilter |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cupsfilter/ |

## Preserved Source Material

```yaml
_body: ''
_name: cupsfilter
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cupsfilter
functions:
  file-read:
  - code: cupsfilter -i application/octet-stream -m application/octet-stream /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# qpdf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `qpdf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/qpdf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [qpdf](../../tools/linux/qpdf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | qpdf |
| name | qpdf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/qpdf/ |

## Preserved Source Material

```yaml
_body: ''
_name: qpdf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/qpdf
functions:
  file-read:
  - code: 'qpdf --empty --add-attachment /path/to/input-file --key=x -- /path/to/output-file

      qpdf --show-attachment=x /path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

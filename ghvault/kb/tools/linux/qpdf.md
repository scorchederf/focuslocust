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

## Summary

GTFOBins entry for qpdf covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/qpdf.md)
- Source verification: [source record](../../sources/gtfobins/qpdf.md)

## Aliases

- `qpdf`

## Source Verification

[source record](../../sources/gtfobins/qpdf.md)

## Evidence Excerpt

```text
_body: ''
_name: qpdf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/qpdf
functions:
file-read:
- code: 'qpdf --empty --add-attachment /path/to/input-file --key=x -- /path/to/output-file
qpdf --show-attachment=x /path/to/output-file'
contexts:
```

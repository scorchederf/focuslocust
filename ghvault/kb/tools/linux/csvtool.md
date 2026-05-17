---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# csvtool

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `csvtool` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csvtool` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for csvtool covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/csvtool.md)
- Source verification: [source record](../../sources/gtfobins/csvtool.md)

## Aliases

- `csvtool`

## Source Verification

[source record](../../sources/gtfobins/csvtool.md)

## Evidence Excerpt

```text
_body: ''
_name: csvtool
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csvtool
functions:
file-read:
- binary: false
code: csvtool trim t /path/to/input-file
comment: The file is actually parsed and manipulated as CSV.
```

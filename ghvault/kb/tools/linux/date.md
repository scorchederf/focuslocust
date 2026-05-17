---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# date

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `date` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/date` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for date covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/date.md)
- Source verification: [source record](../../sources/gtfobins/date.md)

## Aliases

- `date`

## Source Verification

[source record](../../sources/gtfobins/date.md)

## Evidence Excerpt

```text
_body: ''
_name: date
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/date
functions:
file-read:
- binary: false
code: date -f /path/to/input-file
comment: Each line is corrupted by a prefix string and wrapped inside quotes.
```

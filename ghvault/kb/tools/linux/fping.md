---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fping

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fping` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fping` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for fping covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/fping.md)
- Source verification: [source record](../../sources/gtfobins/fping.md)

## Aliases

- `fping`

## Source Verification

[source record](../../sources/gtfobins/fping.md)

## Evidence Excerpt

```text
_body: ''
_name: fping
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fping
functions:
file-read:
- binary: false
code: fping -f /path/to/input-file
comment: Each line is treated as an hostname and it's leaked as an error message.
```

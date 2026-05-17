---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tee

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tee` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tee` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tee covering file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tee.md)
- Source verification: [source record](../../sources/gtfobins/tee.md)

## Aliases

- `tee`

## Source Verification

[source record](../../sources/gtfobins/tee.md)

## Evidence Excerpt

```text
_body: ''
_name: tee
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tee
functions:
file-write:
- code: echo DATA | tee /path/to/output-file
comment: Use `-a` to append data to exising files.
contexts:
```

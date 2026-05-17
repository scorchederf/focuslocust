---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# shred

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `shred` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/shred` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for shred covering file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/shred.md)
- Source verification: [source record](../../sources/gtfobins/shred.md)

## Aliases

- `shred`

## Source Verification

[source record](../../sources/gtfobins/shred.md)

## Evidence Excerpt

```text
_body: ''
_name: shred
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/shred
functions:
file-write:
- code: shred -u /path/to/output-file
comment: This actually deletes the chosen file.
contexts:
```

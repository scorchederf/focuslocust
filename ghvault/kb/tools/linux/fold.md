---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fold

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fold` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fold` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for fold covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/fold.md)
- Source verification: [source record](../../sources/gtfobins/fold.md)

## Aliases

- `fold`

## Source Verification

[source record](../../sources/gtfobins/fold.md)

## Evidence Excerpt

```text
_body: ''
_name: fold
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fold
functions:
file-read:
- binary: false
code: fold -w999 /path/to/input-file
comment: This corrupts the output by wrapping very long lines at the given width (`999`).
```

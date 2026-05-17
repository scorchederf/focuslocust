---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# genisoimage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `genisoimage` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/genisoimage` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for genisoimage covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/genisoimage.md)
- Source verification: [source record](../../sources/gtfobins/genisoimage.md)

## Aliases

- `genisoimage`

## Source Verification

[source record](../../sources/gtfobins/genisoimage.md)

## Evidence Excerpt

```text
_body: ''
_name: genisoimage
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/genisoimage
functions:
file-read:
- code: genisoimage -q -o - /path/to/input-file
comment: The output is placed inside the ISO9660 file system binary format, it can be mounted or extracted with tools
like `7z`.
```

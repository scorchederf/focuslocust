---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# readelf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `readelf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/readelf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for readelf covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/readelf.md)
- Source verification: [source record](../../sources/gtfobins/readelf.md)

## Aliases

- `readelf`

## Source Verification

[source record](../../sources/gtfobins/readelf.md)

## Evidence Excerpt

```text
_body: ''
_name: readelf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/readelf
functions:
file-read:
- binary: false
code: readelf -a @/path/to/input-file
comment: Each line is corrupted by a prefix string and wrapped inside single quotes. Also consider that lines are actually
```

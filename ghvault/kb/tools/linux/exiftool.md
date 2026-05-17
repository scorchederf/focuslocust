---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# exiftool

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `exiftool` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for exiftool covering file-read, file-write, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/exiftool.md)
- Source verification: [source record](../../sources/gtfobins/exiftool.md)

## Aliases

- `exiftool`

## Source Verification

[source record](../../sources/gtfobins/exiftool.md)

## Evidence Excerpt

```text
_body: ''
_name: exiftool
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool
functions:
file-read:
- code: 'exiftool -filename=/path/to/output-file /path/to/input-file
cat /path/to/output-file'
comment: If the permissions allow it, files are moved (instead of copied) to the destination.
```

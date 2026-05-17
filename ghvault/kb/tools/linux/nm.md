---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for nm covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nm.md)
- Source verification: [source record](../../sources/gtfobins/nm.md)

## Aliases

- `nm`

## Source Verification

[source record](../../sources/gtfobins/nm.md)

## Evidence Excerpt

```text
_body: ''
_name: nm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nm
functions:
file-read:
- binary: false
code: nm /path/to/input-file
comment: The file content is treated as command line options and disclosed through error messages.
```

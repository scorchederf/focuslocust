---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# comm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `comm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/comm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for comm covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/comm.md)
- Source verification: [source record](../../sources/gtfobins/comm.md)

## Aliases

- `comm`

## Source Verification

[source record](../../sources/gtfobins/comm.md)

## Evidence Excerpt

```text
_body: ''
_name: comm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/comm
functions:
file-read:
- binary: false
code: comm /path/to/input-file /dev/null
comment: A newline is appended to the file.
```

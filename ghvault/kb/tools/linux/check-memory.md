---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_memory

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-memory` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_memory` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for check_memory covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/check-memory.md)
- Source verification: [source record](../../sources/gtfobins/check-memory.md)

## Aliases

- `check-memory`
- `check_memory`

## Source Verification

[source record](../../sources/gtfobins/check-memory.md)

## Evidence Excerpt

```text
_body: ''
_name: check_memory
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_memory
comment: This is the `check_memory` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
file-read:
- code: check_memory --extra-opts=@/path/to/input-file
comment: The read file content is limited to the first line.
```

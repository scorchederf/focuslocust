---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# file

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `file` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/file` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for file covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/file.md)
- Source verification: [source record](../../sources/gtfobins/file.md)

## Aliases

- `file`

## Source Verification

[source record](../../sources/gtfobins/file.md)

## Evidence Excerpt

```text
_body: ''
_name: file
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/file
functions:
file-read:
- binary: false
code: file -f /path/to/input-file
comment: Each input line is treated as a filename for the `file` command and the output is corrupted by a suffix `:` followed
```

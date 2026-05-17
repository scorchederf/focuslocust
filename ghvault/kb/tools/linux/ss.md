---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ss

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ss` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ss` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ss covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ss.md)
- Source verification: [source record](../../sources/gtfobins/ss.md)

## Aliases

- `ss`

## Source Verification

[source record](../../sources/gtfobins/ss.md)

## Evidence Excerpt

```text
_body: ''
_name: ss
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ss
functions:
file-read:
- binary: false
code: ss -a -F /path/to/input-file
comment: The file content is actually parsed so only a part of the first line is returned as a part of an error message.
```

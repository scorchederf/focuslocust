---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# uuencode

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `uuencode` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/uuencode` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for uuencode covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/uuencode.md)
- Source verification: [source record](../../sources/gtfobins/uuencode.md)

## Aliases

- `uuencode`

## Source Verification

[source record](../../sources/gtfobins/uuencode.md)

## Evidence Excerpt

```text
_body: ''
_name: uuencode
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/uuencode
functions:
file-read:
- binary: false
code: uuencode /path/to/input-file /dev/stdout | uudecode
contexts:
```

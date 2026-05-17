---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# hexdump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `hexdump` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hexdump` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for hexdump covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/hexdump.md)
- Source verification: [source record](../../sources/gtfobins/hexdump.md)

## Aliases

- `hexdump`

## Source Verification

[source record](../../sources/gtfobins/hexdump.md)

## Evidence Excerpt

```text
_body: ''
_name: hexdump
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hexdump
functions:
file-read:
- code: hd /path/to/input-file
comment: The output is actually an hex dump.
contexts:
```

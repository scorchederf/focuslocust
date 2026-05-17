---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for wc covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/wc.md)
- Source verification: [source record](../../sources/gtfobins/wc.md)

## Aliases

- `wc`

## Source Verification

[source record](../../sources/gtfobins/wc.md)

## Evidence Excerpt

```text
_body: ''
_name: wc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wc
functions:
file-read:
- binary: false
code: wc --files0-from /path/to/input-file
comment: The file content is parsed as a sequence of `\x00` separated paths. On error the file content appears in a message.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bbot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bbot` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bbot` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for bbot covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/bbot.md)
- Source verification: [source record](../../sources/gtfobins/bbot.md)

## Aliases

- `bbot`

## Source Verification

[source record](../../sources/gtfobins/bbot.md)

## Evidence Excerpt

```text
_body: ''
_name: bbot
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bbot
functions:
file-read:
- binary: false
code: bbot -d -cy /path/to/input-file
comment: The file is displayed in the debug log.
```

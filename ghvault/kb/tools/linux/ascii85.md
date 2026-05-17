---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ascii85

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ascii85` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ascii85` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ascii85 covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ascii85.md)
- Source verification: [source record](../../sources/gtfobins/ascii85.md)

## Aliases

- `ascii85`

## Source Verification

[source record](../../sources/gtfobins/ascii85.md)

## Evidence Excerpt

```text
_body: ''
_name: ascii85
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ascii85
functions:
file-read:
- code: ascii85 /path/to/input-file | ascii85 --decode
contexts:
sudo: null
```

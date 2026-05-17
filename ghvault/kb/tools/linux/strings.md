---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# strings

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `strings` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strings` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for strings covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/strings.md)
- Source verification: [source record](../../sources/gtfobins/strings.md)

## Aliases

- `strings`

## Source Verification

[source record](../../sources/gtfobins/strings.md)

## Evidence Excerpt

```text
_body: ''
_name: strings
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strings
functions:
file-read:
- binary: false
code: strings /path/to/input-file
comment: This only returns ASCII strings.
```

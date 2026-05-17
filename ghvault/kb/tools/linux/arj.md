---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# arj

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `arj` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arj` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for arj covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/arj.md)
- Source verification: [source record](../../sources/gtfobins/arj.md)

## Aliases

- `arj`

## Source Verification

[source record](../../sources/gtfobins/arj.md)

## Evidence Excerpt

```text
_body: ''
_name: arj
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arj
functions:
file-read:
- binary: false
code: 'arj a /path/to/output-file /path/to/input-file
arj p /path/to/output-file'
```

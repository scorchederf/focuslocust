---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ar

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ar` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ar` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ar covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ar.md)
- Source verification: [source record](../../sources/gtfobins/ar.md)

## Aliases

- `ar`

## Source Verification

[source record](../../sources/gtfobins/ar.md)

## Evidence Excerpt

```text
_body: ''
_name: ar
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ar
functions:
file-read:
- code: 'ar r /path/to/output-file /path/to/input-file
ar p /path/to/output-file'
contexts:
```

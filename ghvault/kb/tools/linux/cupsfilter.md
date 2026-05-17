---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cupsfilter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cupsfilter` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cupsfilter` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for cupsfilter covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/cupsfilter.md)
- Source verification: [source record](../../sources/gtfobins/cupsfilter.md)

## Aliases

- `cupsfilter`

## Source Verification

[source record](../../sources/gtfobins/cupsfilter.md)

## Evidence Excerpt

```text
_body: ''
_name: cupsfilter
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cupsfilter
functions:
file-read:
- code: cupsfilter -i application/octet-stream -m application/octet-stream /path/to/input-file
contexts:
sudo: null
```

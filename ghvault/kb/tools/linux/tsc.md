---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tsc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tsc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tsc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tsc covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tsc.md)
- Source verification: [source record](../../sources/gtfobins/tsc.md)

## Aliases

- `tsc`

## Source Verification

[source record](../../sources/gtfobins/tsc.md)

## Evidence Excerpt

```text
_body: ''
_name: tsc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tsc
functions:
file-read:
- binary: false
code: tsc /path/to/input-file.ts
comment: Content is leaked as error messages. The file extension must be one of the supported ones, e.g., `.ts`, `.tsx`,
```

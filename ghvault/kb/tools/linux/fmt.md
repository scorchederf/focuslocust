---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fmt

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fmt` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fmt` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for fmt covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/fmt.md)
- Source verification: [source record](../../sources/gtfobins/fmt.md)

## Aliases

- `fmt`

## Source Verification

[source record](../../sources/gtfobins/fmt.md)

## Evidence Excerpt

```text
_body: ''
_name: fmt
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fmt
functions:
file-read:
- binary: false
code: fmt -pNON_EXISTING_PREFIX /path/to/input-file
contexts:
```

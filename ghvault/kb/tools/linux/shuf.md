---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# shuf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `shuf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/shuf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for shuf covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/shuf.md)
- Source verification: [source record](../../sources/gtfobins/shuf.md)

## Aliases

- `shuf`

## Source Verification

[source record](../../sources/gtfobins/shuf.md)

## Evidence Excerpt

```text
_body: ''
_name: shuf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/shuf
functions:
file-read:
- code: shuf -z /path/to/input-file
comment: The read file content is corrupted by randomizing the order of NUL terminated strings.
contexts:
```

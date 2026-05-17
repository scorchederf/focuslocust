---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pandoc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pandoc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pandoc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for pandoc covering file-read, file-write, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/pandoc.md)
- Source verification: [source record](../../sources/gtfobins/pandoc.md)

## Aliases

- `pandoc`

## Source Verification

[source record](../../sources/gtfobins/pandoc.md)

## Evidence Excerpt

```text
_body: ''
_name: pandoc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pandoc
functions:
file-read:
- binary: false
code: pandoc -t plain /path/to/input-file
contexts:
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# uniq

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `uniq` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/uniq` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for uniq covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/uniq.md)
- Source verification: [source record](../../sources/gtfobins/uniq.md)

## Aliases

- `uniq`

## Source Verification

[source record](../../sources/gtfobins/uniq.md)

## Evidence Excerpt

```text
_body: ''
_name: uniq
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/uniq
functions:
file-read:
- binary: false
code: uniq /path/to/input-file
comment: The read file content is corrupted by squashing multiple adjacent lines.
```

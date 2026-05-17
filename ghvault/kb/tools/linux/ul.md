---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ul

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ul` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ul` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ul covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ul.md)
- Source verification: [source record](../../sources/gtfobins/ul.md)

## Aliases

- `ul`

## Source Verification

[source record](../../sources/gtfobins/ul.md)

## Evidence Excerpt

```text
_body: ''
_name: ul
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ul
functions:
file-read:
- binary: false
code: ul /path/to/input-file
comment: The read file content is corrupted by replacing occurrences of `$'\b_'` to terminal sequences and by converting
```

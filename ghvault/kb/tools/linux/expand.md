---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# expand

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `expand` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/expand` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for expand covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/expand.md)
- Source verification: [source record](../../sources/gtfobins/expand.md)

## Aliases

- `expand`

## Source Verification

[source record](../../sources/gtfobins/expand.md)

## Evidence Excerpt

```text
_body: ''
_name: expand
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/expand
functions:
file-read:
- binary: false
code: expand /path/to/input-file
comment: The read file content is corrupted by replacing tabs with spaces.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for nl covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nl.md)
- Source verification: [source record](../../sources/gtfobins/nl.md)

## Aliases

- `nl`

## Source Verification

[source record](../../sources/gtfobins/nl.md)

## Evidence Excerpt

```text
_body: ''
_name: nl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nl
functions:
file-read:
- binary: false
code: nl -bn -w1 -s '' /path/to/input-file
comment: The read file content is corrupted by a leading space added to each line.
```

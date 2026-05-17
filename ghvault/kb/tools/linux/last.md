---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# last

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `last` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/last` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for last covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/last.md)
- Source verification: [source record](../../sources/gtfobins/last.md)

## Aliases

- `last`

## Source Verification

[source record](../../sources/gtfobins/last.md)

## Evidence Excerpt

```text
_body: ''
_name: last
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/last
functions:
file-read:
- code: last -a -f /path/to/input-file
comment: The output might be corrupted or incomplete if the file does not follow the expected database format.
contexts:
```

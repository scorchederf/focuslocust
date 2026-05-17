---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# grep

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `grep` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/grep` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for grep covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/grep.md)
- Source verification: [source record](../../sources/gtfobins/grep.md)

## Aliases

- `grep`

## Source Verification

[source record](../../sources/gtfobins/grep.md)

## Evidence Excerpt

```text
_body: ''
_name: grep
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/grep
functions:
file-read:
- binary: false
code: grep '' /path/to/input-file
contexts:
```

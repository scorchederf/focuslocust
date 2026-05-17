---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# unexpand

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `unexpand` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unexpand` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for unexpand covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/unexpand.md)
- Source verification: [source record](../../sources/gtfobins/unexpand.md)

## Aliases

- `unexpand`

## Source Verification

[source record](../../sources/gtfobins/unexpand.md)

## Evidence Excerpt

```text
_body: ''
_name: unexpand
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unexpand
functions:
file-read:
- binary: false
code: unexpand -t999 /path/to/input-file
comment: Convert sequences of (e.g., `999`) spaces to tab.
```

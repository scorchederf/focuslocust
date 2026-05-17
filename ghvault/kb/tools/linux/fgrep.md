---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fgrep

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fgrep` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fgrep` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for fgrep covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/fgrep.md)
- Source verification: [source record](../../sources/gtfobins/fgrep.md)

## Aliases

- `fgrep`

## Source Verification

[source record](../../sources/gtfobins/fgrep.md)

## Evidence Excerpt

```text
_body: ''
_name: fgrep
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fgrep
functions:
file-read:
- code: grep '' /path/to/input-file
contexts:
sudo: null
```

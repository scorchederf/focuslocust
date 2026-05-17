---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# egrep

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `egrep` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/egrep` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for egrep covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/egrep.md)
- Source verification: [source record](../../sources/gtfobins/egrep.md)

## Aliases

- `egrep`

## Source Verification

[source record](../../sources/gtfobins/egrep.md)

## Evidence Excerpt

```text
_body: ''
_name: egrep
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/egrep
functions:
file-read:
- code: grep '' /path/to/input-file
contexts:
sudo: null
```

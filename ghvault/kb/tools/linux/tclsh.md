---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tclsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tclsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tclsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tclsh covering library-load, reverse-shell, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tclsh.md)
- Source verification: [source record](../../sources/gtfobins/tclsh.md)

## Aliases

- `tclsh`

## Source Verification

[source record](../../sources/gtfobins/tclsh.md)

## Evidence Excerpt

```text
_body: ''
_name: tclsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tclsh
functions:
library-load:
- code: 'tclsh
load /path/to/lib.so x'
contexts:
```

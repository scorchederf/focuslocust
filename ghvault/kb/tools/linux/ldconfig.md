---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ldconfig

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ldconfig` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ldconfig` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ldconfig covering library-load.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ldconfig.md)
- Source verification: [source record](../../sources/gtfobins/ldconfig.md)

## Aliases

- `ldconfig`

## Source Verification

[source record](../../sources/gtfobins/ldconfig.md)

## Evidence Excerpt

```text
_body: ''
_name: ldconfig
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ldconfig
functions:
library-load:
- code: 'echo /path/to/temp-dir/ >/path/to/temp-file
ldconfig -f /path/to/temp-file
ping'
```

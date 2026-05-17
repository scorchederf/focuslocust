---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# urlget

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `urlget` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/urlget` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for urlget covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/urlget.md)
- Source verification: [source record](../../sources/gtfobins/urlget.md)

## Aliases

- `urlget`

## Source Verification

[source record](../../sources/gtfobins/urlget.md)

## Evidence Excerpt

```text
_body: ''
_name: urlget
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/urlget
functions:
file-read:
- code: urlget - /path/to/input-file
comment: This is part of `gettext` and usually not in `PATH`, e.g., on Arch it can be found at `/usr/lib/gettext/urlget`.
contexts:
```

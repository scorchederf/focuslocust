---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xmodmap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xmodmap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xmodmap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for xmodmap covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/xmodmap.md)
- Source verification: [source record](../../sources/gtfobins/xmodmap.md)

## Aliases

- `xmodmap`

## Source Verification

[source record](../../sources/gtfobins/xmodmap.md)

## Evidence Excerpt

```text
_body: ''
_name: xmodmap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xmodmap
comment: This requires a running X server.
functions:
file-read:
- binary: false
code: xmodmap -v /path/to/input-file
```

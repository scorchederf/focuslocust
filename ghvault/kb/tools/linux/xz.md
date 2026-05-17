---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xz

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xz` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xz` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for xz covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/xz.md)
- Source verification: [source record](../../sources/gtfobins/xz.md)

## Aliases

- `xz`

## Source Verification

[source record](../../sources/gtfobins/xz.md)

## Evidence Excerpt

```text
_body: ''
_name: xz
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xz
functions:
file-read:
- code: xz -c /path/to/input-file | xz -d
contexts:
sudo: null
```

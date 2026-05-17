---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zcat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zcat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zcat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for zcat covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/zcat.md)
- Source verification: [source record](../../sources/gtfobins/zcat.md)

## Aliases

- `zcat`

## Source Verification

[source record](../../sources/gtfobins/zcat.md)

## Evidence Excerpt

```text
_body: ''
_name: zcat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zcat
functions:
file-read:
- code: zcat -f /path/to/input-file
contexts:
sudo: null
```

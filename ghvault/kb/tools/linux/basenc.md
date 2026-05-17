---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# basenc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `basenc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/basenc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for basenc covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/basenc.md)
- Source verification: [source record](../../sources/gtfobins/basenc.md)

## Aliases

- `basenc`

## Source Verification

[source record](../../sources/gtfobins/basenc.md)

## Evidence Excerpt

```text
_body: ''
_name: basenc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/basenc
functions:
file-read:
- code: basenc --base64 /path/to/input-file | basenc -d --base64
contexts:
sudo: null
```

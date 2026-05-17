---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# base64

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `base64` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base64` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for base64 covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/base64.md)
- Source verification: [source record](../../sources/gtfobins/base64.md)

## Aliases

- `base64`

## Source Verification

[source record](../../sources/gtfobins/base64.md)

## Evidence Excerpt

```text
_body: ''
_name: base64
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base64
functions:
file-read:
- code: base64 /path/to/input-file | base64 --decode
contexts:
sudo: null
```

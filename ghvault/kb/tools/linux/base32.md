---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# base32

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `base32` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base32` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for base32 covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/base32.md)
- Source verification: [source record](../../sources/gtfobins/base32.md)

## Aliases

- `base32`

## Source Verification

[source record](../../sources/gtfobins/base32.md)

## Evidence Excerpt

```text
_body: ''
_name: base32
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base32
functions:
file-read:
- code: base32 /path/to/input-file | base32 --decode
contexts:
sudo: null
```

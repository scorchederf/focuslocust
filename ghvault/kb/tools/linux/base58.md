---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# base58

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `base58` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base58` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for base58 covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/base58.md)
- Source verification: [source record](../../sources/gtfobins/base58.md)

## Aliases

- `base58`

## Source Verification

[source record](../../sources/gtfobins/base58.md)

## Evidence Excerpt

```text
_body: ''
_name: base58
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/base58
functions:
file-read:
- code: base58 /path/to/input-file | base58 --decode
contexts:
sudo: null
```

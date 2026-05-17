---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pax

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pax` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pax` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for pax covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/pax.md)
- Source verification: [source record](../../sources/gtfobins/pax.md)

## Aliases

- `pax`

## Source Verification

[source record](../../sources/gtfobins/pax.md)

## Evidence Excerpt

```text
_body: ''
_name: pax
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pax
functions:
file-read:
- code: pax -w /path/to/input-file | tar -xO
contexts:
sudo: null
```

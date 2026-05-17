---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xxd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xxd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xxd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for xxd covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/xxd.md)
- Source verification: [source record](../../sources/gtfobins/xxd.md)

## Aliases

- `xxd`

## Source Verification

[source record](../../sources/gtfobins/xxd.md)

## Evidence Excerpt

```text
_body: ''
_name: xxd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xxd
functions:
file-read:
- code: xxd /path/to/input-file | xxd -r
contexts:
sudo: null
```

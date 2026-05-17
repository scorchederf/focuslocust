---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dmesg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dmesg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmesg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dmesg covering file-read, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dmesg.md)
- Source verification: [source record](../../sources/gtfobins/dmesg.md)

## Aliases

- `dmesg`

## Source Verification

[source record](../../sources/gtfobins/dmesg.md)

## Evidence Excerpt

```text
_body: ''
_name: dmesg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmesg
functions:
file-read:
- binary: false
code: dmesg -rF /path/to/input-file
contexts:
```

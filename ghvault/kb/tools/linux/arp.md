---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# arp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `arp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for arp covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/arp.md)
- Source verification: [source record](../../sources/gtfobins/arp.md)

## Aliases

- `arp`

## Source Verification

[source record](../../sources/gtfobins/arp.md)

## Evidence Excerpt

```text
_body: ''
_name: arp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arp
functions:
file-read:
- binary: false
code: arp -v -f /path/to/input-file
comment: Lines are likely leaked as error messages.
```

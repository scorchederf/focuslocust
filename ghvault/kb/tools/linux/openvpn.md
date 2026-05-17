---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# openvpn

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `openvpn` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openvpn` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for openvpn covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/openvpn.md)
- Source verification: [source record](../../sources/gtfobins/openvpn.md)

## Aliases

- `openvpn`

## Source Verification

[source record](../../sources/gtfobins/openvpn.md)

## Evidence Excerpt

```text
_body: ''
_name: openvpn
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openvpn
functions:
file-read:
- code: openvpn --config /path/to/input-file
comment: The file is actually parsed and the first partial wrong line is returned in an error message.
contexts:
```

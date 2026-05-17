---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nft

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nft` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nft` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for nft covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nft.md)
- Source verification: [source record](../../sources/gtfobins/nft.md)

## Aliases

- `nft`

## Source Verification

[source record](../../sources/gtfobins/nft.md)

## Evidence Excerpt

```text
_body: ''
_name: nft
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nft
functions:
file-read:
- code: nft -f /path/to/input-file
comment: The content is actually parsed and corrupted by the command.
contexts:
```

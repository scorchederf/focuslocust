---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tailscale

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tailscale` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tailscale` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tailscale covering upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tailscale.md)
- Source verification: [source record](../../sources/gtfobins/tailscale.md)

## Aliases

- `tailscale`

## Source Verification

[source record](../../sources/gtfobins/tailscale.md)

## Evidence Excerpt

```text
_body: ''
_name: tailscale
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tailscale
functions:
upload:
- code: tailscale serve --http=12345 /path/to/input-file
comment: The URL is reachable by any host of the same Tailnet.
contexts:
```

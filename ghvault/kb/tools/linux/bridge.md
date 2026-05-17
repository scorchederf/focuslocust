---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bridge

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bridge` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bridge` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for bridge covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/bridge.md)
- Source verification: [source record](../../sources/gtfobins/bridge.md)

## Aliases

- `bridge`

## Source Verification

[source record](../../sources/gtfobins/bridge.md)

## Evidence Excerpt

```text
_body: ''
_name: bridge
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bridge
functions:
file-read:
- code: bridge -b /path/to/input-file
comment: Outputs the first line of the file (until the first whitespace) inside an error message to stdandard error.
contexts:
```

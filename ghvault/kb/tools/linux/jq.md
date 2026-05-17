---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# jq

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `jq` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jq` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for jq covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/jq.md)
- Source verification: [source record](../../sources/gtfobins/jq.md)

## Aliases

- `jq`

## Source Verification

[source record](../../sources/gtfobins/jq.md)

## Evidence Excerpt

```text
_body: ''
_name: jq
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jq
functions:
file-read:
- binary: false
code: jq -Rr . /path/to/input-file
contexts:
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tail

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tail` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tail` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tail covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tail.md)
- Source verification: [source record](../../sources/gtfobins/tail.md)

## Aliases

- `tail`

## Source Verification

[source record](../../sources/gtfobins/tail.md)

## Evidence Excerpt

```text
_body: ''
_name: tail
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tail
functions:
file-read:
- code: tail -c+0 /path/to/input-file
contexts:
sudo: null
```

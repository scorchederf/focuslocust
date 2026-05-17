---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# csplit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `csplit` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csplit` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for csplit covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/csplit.md)
- Source verification: [source record](../../sources/gtfobins/csplit.md)

## Aliases

- `csplit`

## Source Verification

[source record](../../sources/gtfobins/csplit.md)

## Evidence Excerpt

```text
_body: ''
_name: csplit
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csplit
functions:
file-read:
- code: 'csplit /path/to/input-file 1
cat xx01'
contexts:
```

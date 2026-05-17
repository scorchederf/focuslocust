---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for bc covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/bc.md)
- Source verification: [source record](../../sources/gtfobins/bc.md)

## Aliases

- `bc`

## Source Verification

[source record](../../sources/gtfobins/bc.md)

## Evidence Excerpt

```text
_body: ''
_name: bc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bc
functions:
file-read:
- code: 'bc -s /path/to/input-file
quit'
comment: The file content is actually parsed and appears as error messages.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gtester

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gtester` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gtester` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for gtester covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/gtester.md)
- Source verification: [source record](../../sources/gtfobins/gtester.md)

## Aliases

- `gtester`

## Source Verification

[source record](../../sources/gtfobins/gtester.md)

## Evidence Excerpt

```text
_body: ''
_name: gtester
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gtester
functions:
file-write:
- code: gtester DATA -o /path/to/output-file
comment: Data to be written appears in an XML attribute in the output file (`<testbinary path="DATA">`).
contexts:
```

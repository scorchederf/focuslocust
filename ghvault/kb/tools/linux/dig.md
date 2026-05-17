---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dig

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dig` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dig` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dig covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dig.md)
- Source verification: [source record](../../sources/gtfobins/dig.md)

## Aliases

- `dig`

## Source Verification

[source record](../../sources/gtfobins/dig.md)

## Evidence Excerpt

```text
_body: ''
_name: dig
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dig
functions:
file-read:
- code: dig -f /path/to/input-file
comment: Each input line is treated as a lookup query for the `dig` command and the output is corrupted with the result
or errors of the operation.
```

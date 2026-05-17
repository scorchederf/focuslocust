---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cmp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cmp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for cmp covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/cmp.md)
- Source verification: [source record](../../sources/gtfobins/cmp.md)

## Aliases

- `cmp`

## Source Verification

[source record](../../sources/gtfobins/cmp.md)

## Evidence Excerpt

```text
_body: ''
_name: cmp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmp
functions:
file-read:
- binary: false
code: cmp /path/to/input-file /dev/zero -b -l
comment: Dump the bytes of the input file that are different from the NUL byte in a tabular format.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# od

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `od` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/od` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for od covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/od.md)
- Source verification: [source record](../../sources/gtfobins/od.md)

## Aliases

- `od`

## Source Verification

[source record](../../sources/gtfobins/od.md)

## Evidence Excerpt

```text
_body: ''
_name: od
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/od
functions:
file-read:
- code: od -An -c -w999 /path/to/input-file
comment: Three spaces are added before each character in the read file (wrapped at the specified value, i.e., `999`),
and non-printable chars are printed as backslash escape sequences.
```

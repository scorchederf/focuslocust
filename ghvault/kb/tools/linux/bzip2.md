---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bzip2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bzip2` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bzip2` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for bzip2 covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/bzip2.md)
- Source verification: [source record](../../sources/gtfobins/bzip2.md)

## Aliases

- `bzip2`

## Source Verification

[source record](../../sources/gtfobins/bzip2.md)

## Evidence Excerpt

```text
_body: ''
_name: bzip2
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bzip2
comment: There are also a number of other utilities that rely on `bzip2` under the hood, e.g., `bzless`, `bzcat`, `bunzip2`,
etc. Besides having similar features, they also allow privileged reads if `bzip2` itself is SUID.
functions:
file-read:
- code: bzip2 -c /path/to/input-file | bzip2 -d
```

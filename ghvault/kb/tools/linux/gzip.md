---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gzip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gzip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gzip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for gzip covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/gzip.md)
- Source verification: [source record](../../sources/gtfobins/gzip.md)

## Aliases

- `gzip`

## Source Verification

[source record](../../sources/gtfobins/gzip.md)

## Evidence Excerpt

```text
_body: ''
_name: gzip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gzip
comment: There are also a number of other utilities that rely on `gzip` under the hood, e.g., `zless`, `zcat`, `gunzip`, etc.
Besides having similar features, they also allow privileged reads if `gzip` itself is SUID.
functions:
file-read:
- code: gzip -c /path/to/input-file | gzip -d
```

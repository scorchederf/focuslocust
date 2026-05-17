---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# clamscan

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `clamscan` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clamscan` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for clamscan covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/clamscan.md)
- Source verification: [source record](../../sources/gtfobins/clamscan.md)

## Aliases

- `clamscan`

## Source Verification

[source record](../../sources/gtfobins/clamscan.md)

## Evidence Excerpt

```text
_body: ''
_name: clamscan
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clamscan
functions:
file-read:
- binary: false
code: 'touch x.yara
clamscan --no-summary -d x.yara -f /path/to/input-file 2>&1 | sed -nE ''s/^(.*): No such file or directory$/\1/p'''
```

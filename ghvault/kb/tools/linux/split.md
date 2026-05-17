---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# split

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `split` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/split` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for split covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/split.md)
- Source verification: [source record](../../sources/gtfobins/split.md)

## Aliases

- `split`

## Source Verification

[source record](../../sources/gtfobins/split.md)

## Evidence Excerpt

```text
_body: ''
_name: split
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/split
functions:
file-read:
- code: 'split -b 999 --additional-suffix suffix /path/to/input-file prefix
cat prefixaasuffix'
comment: This copies the input file in the current working directory in a file named `prefixaasuffix`, just make sure
```

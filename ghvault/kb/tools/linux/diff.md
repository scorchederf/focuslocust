---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# diff

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `diff` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/diff` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for diff covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/diff.md)
- Source verification: [source record](../../sources/gtfobins/diff.md)

## Aliases

- `diff`

## Source Verification

[source record](../../sources/gtfobins/diff.md)

## Evidence Excerpt

```text
_body: ''
_name: diff
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/diff
functions:
file-read:
- binary: false
code: diff --line-format=%L /dev/null /path/to/input-file
contexts:
```

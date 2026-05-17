---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mtr

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mtr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mtr` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for mtr covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/mtr.md)
- Source verification: [source record](../../sources/gtfobins/mtr.md)

## Aliases

- `mtr`

## Source Verification

[source record](../../sources/gtfobins/mtr.md)

## Evidence Excerpt

```text
_body: ''
_name: mtr
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mtr
functions:
file-read:
- binary: false
code: mtr --raw -F /path/to/input-file
comment: The file is actually parsed, thus the content is corrupted by error prints.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ed

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ed` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ed` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ed covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ed.md)
- Source verification: [source record](../../sources/gtfobins/ed.md)

## Aliases

- `ed`

## Source Verification

[source record](../../sources/gtfobins/ed.md)

## Evidence Excerpt

```text
_body: ''
_name: ed
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ed
functions:
file-read:
- binary: false
code: 'ed /path/to/input-file
,p
```

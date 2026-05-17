---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pyright

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pyright` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pyright` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for pyright covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/pyright.md)
- Source verification: [source record](../../sources/gtfobins/pyright.md)

## Aliases

- `pyright`

## Source Verification

[source record](../../sources/gtfobins/pyright.md)

## Evidence Excerpt

```text
_body: ''
_name: pyright
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pyright
functions:
file-read:
- binary: false
code: pyright /path/to/input-file
comment: Content is leaked as error messages.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mypy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mypy` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mypy` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for mypy covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/mypy.md)
- Source verification: [source record](../../sources/gtfobins/mypy.md)

## Aliases

- `mypy`

## Source Verification

[source record](../../sources/gtfobins/mypy.md)

## Evidence Excerpt

```text
_body: ''
_name: mypy
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mypy
functions:
file-read:
- binary: false
code: mypy /path/to/input-file
comment: Partial content is leaked as error messages.
```

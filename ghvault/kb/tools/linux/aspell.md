---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# aspell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `aspell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aspell` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for aspell covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/aspell.md)
- Source verification: [source record](../../sources/gtfobins/aspell.md)

## Aliases

- `aspell`

## Source Verification

[source record](../../sources/gtfobins/aspell.md)

## Evidence Excerpt

```text
_body: ''
_name: aspell
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aspell
functions:
file-read:
- binary: false
code: aspell -c /path/to/input-file
comment: The textual file is displayed in an interactive TUI showing only the parts that contain mispelled words.
```

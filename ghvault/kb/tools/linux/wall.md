---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wall

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wall` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wall` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for wall covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/wall.md)
- Source verification: [source record](../../sources/gtfobins/wall.md)

## Aliases

- `wall`

## Source Verification

[source record](../../sources/gtfobins/wall.md)

## Evidence Excerpt

```text
_body: ''
_name: wall
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wall
functions:
file-read:
- binary: false
code: wall --nobanner /path/to/input-file
comment: The textual file is dumped on the current TTY (neither to `stdout` nor to `stderr`).
```

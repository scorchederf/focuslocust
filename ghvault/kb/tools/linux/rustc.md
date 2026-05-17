---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rustc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rustc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rustc covering file-read, file-write, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rustc.md)
- Source verification: [source record](../../sources/gtfobins/rustc.md)

## Aliases

- `rustc`

## Source Verification

[source record](../../sources/gtfobins/rustc.md)

## Evidence Excerpt

```text
_body: ''
_name: rustc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustc
functions:
file-read:
- binary: false
code: rustc /path/to/input-file
comment: The compiler leaks some file lines in the compiler error.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# strace

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `strace` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strace` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for strace covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/strace.md)
- Source verification: [source record](../../sources/gtfobins/strace.md)

## Aliases

- `strace`

## Source Verification

[source record](../../sources/gtfobins/strace.md)

## Evidence Excerpt

```text
_body: ''
_name: strace
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strace
functions:
file-write:
- code: strace -s 999 -o /path/to/output-file strace - DATA
comment: The data to be written appears amid the syscall log, quoted and with special characters escaped in octal notation.
The string representation will be truncated, pick a value big enough instead of `999`. More generally, any binary that
```

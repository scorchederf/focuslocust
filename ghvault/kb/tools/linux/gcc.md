---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gcc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gcc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for gcc covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/gcc.md)
- Source verification: [source record](../../sources/gtfobins/gcc.md)

## Aliases

- `gcc`

## Source Verification

[source record](../../sources/gtfobins/gcc.md)

## Evidence Excerpt

```text
_body: ''
_name: gcc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcc
functions:
file-read:
- binary: false
code: gcc -x c -E /path/to/input-file
contexts:
```

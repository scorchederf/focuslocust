---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nasm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nasm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nasm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for nasm covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nasm.md)
- Source verification: [source record](../../sources/gtfobins/nasm.md)

## Aliases

- `nasm`

## Source Verification

[source record](../../sources/gtfobins/nasm.md)

## Evidence Excerpt

```text
_body: ''
_name: nasm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nasm
functions:
file-read:
- code: nasm -@ /path/to/input-file
comment: The file content is treated as command line options and disclosed throught error messages.
contexts:
```

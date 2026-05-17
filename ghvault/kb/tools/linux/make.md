---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# make

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `make` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/make` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for make covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/make.md)
- Source verification: [source record](../../sources/gtfobins/make.md)

## Aliases

- `make`

## Source Verification

[source record](../../sources/gtfobins/make.md)

## Evidence Excerpt

```text
_body: ''
_name: make
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/make
functions:
file-read:
- binary: false
code: make -s --eval='$(file >/dev/stdout,$(file </path/to/input-file))' .
contexts:
```

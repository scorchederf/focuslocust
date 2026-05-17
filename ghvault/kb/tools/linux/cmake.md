---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cmake

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cmake` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmake` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for cmake covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/cmake.md)
- Source verification: [source record](../../sources/gtfobins/cmake.md)

## Aliases

- `cmake`

## Source Verification

[source record](../../sources/gtfobins/cmake.md)

## Evidence Excerpt

```text
_body: ''
_name: cmake
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cmake
functions:
file-read:
- code: cmake -E cat /path/to/input-file
contexts:
sudo: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gdb

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gdb` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gdb` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for gdb covering file-write, inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/gdb.md)
- Source verification: [source record](../../sources/gtfobins/gdb.md)

## Aliases

- `gdb`

## Source Verification

[source record](../../sources/gtfobins/gdb.md)

## Evidence Excerpt

```text
_body: ''
_name: gdb
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gdb
functions:
file-write:
- code: gdb -nx -ex 'dump value /path/to/output-file "DATA"' -ex quit
contexts:
sudo: null
```

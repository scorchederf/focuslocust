---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cpio

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cpio` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpio` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for cpio covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/cpio.md)
- Source verification: [source record](../../sources/gtfobins/cpio.md)

## Aliases

- `cpio`

## Source Verification

[source record](../../sources/gtfobins/cpio.md)

## Evidence Excerpt

```text
_body: ''
_name: cpio
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpio
functions:
file-read:
- binary: false
code: echo /path/to/input-file | cpio -o
comment: The content of the file is printed to standard output, between the `cpio` archive format header and footer.
```

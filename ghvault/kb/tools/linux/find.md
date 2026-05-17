---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# find

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `find` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/find` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for find covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/find.md)
- Source verification: [source record](../../sources/gtfobins/find.md)

## Aliases

- `find`

## Source Verification

[source record](../../sources/gtfobins/find.md)

## Evidence Excerpt

```text
_body: ''
_name: find
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/find
functions:
file-read:
- code: find /path/to/input-file -exec cat {} \;
comment: This uses `cat` to actually read the file, but since permissions are not dropped, it's executed with the same
privileges as `find`.
```

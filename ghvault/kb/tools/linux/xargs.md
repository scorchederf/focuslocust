---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xargs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xargs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xargs` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for xargs covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/xargs.md)
- Source verification: [source record](../../sources/gtfobins/xargs.md)

## Aliases

- `xargs`

## Source Verification

[source record](../../sources/gtfobins/xargs.md)

## Evidence Excerpt

```text
_body: ''
_name: xargs
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xargs
functions:
file-read:
- binary: false
code: xargs -a /path/to/input-file -0
contexts:
```

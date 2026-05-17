---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# man

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `man` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/man` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for man covering file-read, inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/man.md)
- Source verification: [source record](../../sources/gtfobins/man.md)

## Aliases

- `man`

## Source Verification

[source record](../../sources/gtfobins/man.md)

## Evidence Excerpt

```text
_body: ''
_name: man
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/man
functions:
file-read:
- code: man /path/to/input-file
comment: The file is shown somehow formatted and displayed in the default pager.
contexts:
```

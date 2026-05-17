---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mutt

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mutt` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mutt` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for mutt covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/mutt.md)
- Source verification: [source record](../../sources/gtfobins/mutt.md)

## Aliases

- `mutt`

## Source Verification

[source record](../../sources/gtfobins/mutt.md)

## Evidence Excerpt

```text
_body: ''
_name: mutt
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mutt
functions:
file-read:
- binary: false
code: mutt -F /path/to/input-file
comment: The file is leaked as error messages.
```

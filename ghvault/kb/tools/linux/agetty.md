---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# agetty

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `agetty` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/agetty` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for agetty covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/agetty.md)
- Source verification: [source record](../../sources/gtfobins/agetty.md)

## Aliases

- `agetty`

## Source Verification

[source record](../../sources/gtfobins/agetty.md)

## Evidence Excerpt

```text
_body: ''
_name: agetty
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/agetty
functions:
shell:
- code: agetty -l /bin/sh -o -p -a root tty
contexts:
suid:
```

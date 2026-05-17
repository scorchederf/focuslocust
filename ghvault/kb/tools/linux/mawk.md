---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mawk

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mawk` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mawk` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for mawk covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/mawk.md)
- Source verification: [source record](../../sources/gtfobins/mawk.md)

## Aliases

- `mawk`

## Source Verification

[source record](../../sources/gtfobins/mawk.md)

## Evidence Excerpt

```text
_body: ''
_name: mawk
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mawk
functions:
file-read:
- code: mawk '//' /path/to/input-file
contexts:
sudo: null
```

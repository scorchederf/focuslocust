---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dos2unix

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dos2unix` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dos2unix` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dos2unix covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dos2unix.md)
- Source verification: [source record](../../sources/gtfobins/dos2unix.md)

## Aliases

- `dos2unix`

## Source Verification

[source record](../../sources/gtfobins/dos2unix.md)

## Evidence Excerpt

```text
_body: ''
_name: dos2unix
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dos2unix
functions:
file-read:
- code: dos2unix -f -O /path/to/input-file
contexts:
sudo: null
```

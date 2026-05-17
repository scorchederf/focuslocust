---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# alpine

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `alpine` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/alpine` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for alpine covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/alpine.md)
- Source verification: [source record](../../sources/gtfobins/alpine.md)

## Aliases

- `alpine`

## Source Verification

[source record](../../sources/gtfobins/alpine.md)

## Evidence Excerpt

```text
_body: ''
_name: alpine
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/alpine
functions:
file-read:
- code: alpine -F /path/to/input-file
comment: The file is displayed in the terminal interface. Other options might be available, for example, by pressing `S`
is possible to save the file content elsewhere.
```

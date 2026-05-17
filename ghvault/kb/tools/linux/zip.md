---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for zip covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/zip.md)
- Source verification: [source record](../../sources/gtfobins/zip.md)

## Aliases

- `zip`

## Source Verification

[source record](../../sources/gtfobins/zip.md)

## Evidence Excerpt

```text
_body: ''
_name: zip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zip
functions:
file-read:
- code: 'zip /path/to/temp-file /path/to/input-file
unzip -p /path/to/temp-file'
contexts:
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sed

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sed` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sed` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for sed covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/sed.md)
- Source verification: [source record](../../sources/gtfobins/sed.md)

## Aliases

- `sed`

## Source Verification

[source record](../../sources/gtfobins/sed.md)

## Evidence Excerpt

```text
_body: ''
_name: sed
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sed
functions:
file-read:
- code: sed '' /path/to/input-file
contexts:
sudo: null
```

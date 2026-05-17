---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tic` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tic` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tic covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tic.md)
- Source verification: [source record](../../sources/gtfobins/tic.md)

## Aliases

- `tic`

## Source Verification

[source record](../../sources/gtfobins/tic.md)

## Evidence Excerpt

```text
_body: ''
_name: tic
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tic
functions:
file-read:
- code: tic -C /path/to/input-file
comment: This translates a terminfo file from source format into compiled format. It will attempt to translate an arbitrary
file and output the contents of the file on failure.
```

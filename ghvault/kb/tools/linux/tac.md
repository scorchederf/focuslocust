---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tac

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tac` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tac` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tac covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tac.md)
- Source verification: [source record](../../sources/gtfobins/tac.md)

## Aliases

- `tac`

## Source Verification

[source record](../../sources/gtfobins/tac.md)

## Evidence Excerpt

```text
_body: ''
_name: tac
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tac
functions:
file-read:
- binary: false
code: tac -s 'RANDOM' /path/to/input-file
comment: Make sure that `RANDOM` does not appear into the file to read otherwise the content of the file is corrupted
```

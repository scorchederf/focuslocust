---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dd covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dd.md)
- Source verification: [source record](../../sources/gtfobins/dd.md)

## Aliases

- `dd`

## Source Verification

[source record](../../sources/gtfobins/dd.md)

## Evidence Excerpt

```text
_body: ''
_name: dd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dd
functions:
file-read:
- code: dd if=/path/to/input-file
contexts:
sudo: null
```

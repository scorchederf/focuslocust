---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msguniq

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msguniq` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msguniq` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for msguniq covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/msguniq.md)
- Source verification: [source record](../../sources/gtfobins/msguniq.md)

## Aliases

- `msguniq`

## Source Verification

[source record](../../sources/gtfobins/msguniq.md)

## Evidence Excerpt

```text
_body: ''
_name: msguniq
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msguniq
functions:
file-read:
- binary: false
code: msguniq -P /path/to/input-file
comment: The file is parsed and displayed as a Java `.properties` file.
```

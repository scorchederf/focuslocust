---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# apache2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `apache2` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for apache2 covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/apache2.md)
- Source verification: [source record](../../sources/gtfobins/apache2.md)

## Aliases

- `apache2`

## Source Verification

[source record](../../sources/gtfobins/apache2.md)

## Evidence Excerpt

```text
_body: ''
_name: apache2
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2
functions:
file-read:
- binary: false
code: apache2 -f /path/to/input-file
comment: The first line may be leaked as an error message.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rake

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rake` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rake` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rake covering file-read, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rake.md)
- Source verification: [source record](../../sources/gtfobins/rake.md)

## Aliases

- `rake`

## Source Verification

[source record](../../sources/gtfobins/rake.md)

## Evidence Excerpt

```text
_body: ''
_name: rake
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rake
functions:
file-read:
- code: rake -f /path/to/input-file
comment: The file is actually parsed and the first wrong line is returned in an error message.
contexts:
```

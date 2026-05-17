---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgmerge

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgmerge` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgmerge` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for msgmerge covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/msgmerge.md)
- Source verification: [source record](../../sources/gtfobins/msgmerge.md)

## Aliases

- `msgmerge`

## Source Verification

[source record](../../sources/gtfobins/msgmerge.md)

## Evidence Excerpt

```text
_body: ''
_name: msgmerge
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgmerge
functions:
file-read:
- binary: false
code: msgmerge -P /path/to/input-file /dev/null
comment: The file is parsed and displayed as a Java `.properties` file.
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgattrib

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgattrib` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgattrib` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for msgattrib covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/msgattrib.md)
- Source verification: [source record](../../sources/gtfobins/msgattrib.md)

## Aliases

- `msgattrib`

## Source Verification

[source record](../../sources/gtfobins/msgattrib.md)

## Evidence Excerpt

```text
_body: ''
_name: msgattrib
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgattrib
functions:
file-read:
- binary: false
code: msgattrib -P /path/to/input-file
comment: The file is parsed and displayed as a Java `.properties` file.
```

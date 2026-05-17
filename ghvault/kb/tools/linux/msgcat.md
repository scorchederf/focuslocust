---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgcat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgcat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgcat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for msgcat covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/msgcat.md)
- Source verification: [source record](../../sources/gtfobins/msgcat.md)

## Aliases

- `msgcat`

## Source Verification

[source record](../../sources/gtfobins/msgcat.md)

## Evidence Excerpt

```text
_body: ''
_name: msgcat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgcat
functions:
file-read:
- binary: false
code: msgcat -P /path/to/input-file
comment: The file is parsed and displayed as a Java `.properties` file.
```

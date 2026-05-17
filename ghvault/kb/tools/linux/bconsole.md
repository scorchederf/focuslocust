---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bconsole

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bconsole` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bconsole` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for bconsole covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/bconsole.md)
- Source verification: [source record](../../sources/gtfobins/bconsole.md)

## Aliases

- `bconsole`

## Source Verification

[source record](../../sources/gtfobins/bconsole.md)

## Evidence Excerpt

```text
_body: ''
_name: bconsole
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bconsole
functions:
file-read:
- code: bconsole -c /path/to/file-input
comment: The file is actually parsed and the first wrong line is returned in an error message.
contexts:
```

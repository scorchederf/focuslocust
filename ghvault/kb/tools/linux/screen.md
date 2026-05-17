---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# screen

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `screen` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/screen` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for screen covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/screen.md)
- Source verification: [source record](../../sources/gtfobins/screen.md)

## Aliases

- `screen`

## Source Verification

[source record](../../sources/gtfobins/screen.md)

## Evidence Excerpt

```text
_body: ''
_name: screen
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/screen
functions:
file-write:
- binary: false
code: screen -L -Logfile /path/to/output-file echo DATA
comment: Data is appended to the file and `\n` is converted to `\r\n`.
```

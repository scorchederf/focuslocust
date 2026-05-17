---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# logrotate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `logrotate` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logrotate` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for logrotate covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/logrotate.md)
- Source verification: [source record](../../sources/gtfobins/logrotate.md)

## Aliases

- `logrotate`

## Source Verification

[source record](../../sources/gtfobins/logrotate.md)

## Evidence Excerpt

```text
_body: ''
_name: logrotate
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logrotate
functions:
file-read:
- binary: false
code: logrotate /path/to/input-file
comment: The first word is returned in a error message.
```

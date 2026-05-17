---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_statusfile

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-statusfile` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_statusfile` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for check_statusfile covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/check-statusfile.md)
- Source verification: [source record](../../sources/gtfobins/check-statusfile.md)

## Aliases

- `check-statusfile`
- `check_statusfile`

## Source Verification

[source record](../../sources/gtfobins/check-statusfile.md)

## Evidence Excerpt

```text
_body: ''
_name: check_statusfile
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_statusfile
comment: This is the `check_statusfile` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
file-read:
- code: check_statusfile /path/to/input-file
comment: The read file content is limited to the first line.
```

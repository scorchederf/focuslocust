---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_log

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-log` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_log` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for check_log covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/check-log.md)
- Source verification: [source record](../../sources/gtfobins/check-log.md)

## Aliases

- `check-log`
- `check_log`

## Source Verification

[source record](../../sources/gtfobins/check-log.md)

## Evidence Excerpt

```text
_body: ''
_name: check_log
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_log
comment: This is the `check_log` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
file-read:
- code: check_log -F /path/to/input-file -O /dev/stdout
contexts:
```

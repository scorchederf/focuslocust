---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_raid

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-raid` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_raid` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for check_raid covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/check-raid.md)
- Source verification: [source record](../../sources/gtfobins/check-raid.md)

## Aliases

- `check-raid`
- `check_raid`

## Source Verification

[source record](../../sources/gtfobins/check-raid.md)

## Evidence Excerpt

```text
_body: ''
_name: check_raid
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_raid
comment: This is the `check_raid` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
file-read:
- code: check_raid --extra-opts=@/path/to/input-file
comment: The read file content is limited to the first line.
```

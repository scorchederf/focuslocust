---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_cups

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-cups` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_cups` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for check_cups covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/check-cups.md)
- Source verification: [source record](../../sources/gtfobins/check-cups.md)

## Aliases

- `check-cups`
- `check_cups`

## Source Verification

[source record](../../sources/gtfobins/check-cups.md)

## Evidence Excerpt

```text
_body: ''
_name: check_cups
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_cups
comment: This is the `check_cups` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
file-read:
- binary: false
code: check_cups --extra-opts=@/path/to/input-file
```

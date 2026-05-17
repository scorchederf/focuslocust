---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ntpdate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ntpdate` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ntpdate` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ntpdate covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ntpdate.md)
- Source verification: [source record](../../sources/gtfobins/ntpdate.md)

## Aliases

- `ntpdate`

## Source Verification

[source record](../../sources/gtfobins/ntpdate.md)

## Evidence Excerpt

```text
_body: ''
_name: ntpdate
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ntpdate
functions:
file-read:
- binary: false
code: ntpdate -a x -k /path/to/input-file -d localhost
comment: The file is actually parsed and lines are leaked through error messages.
```

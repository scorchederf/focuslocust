---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# chmod

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `chmod` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chmod` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for chmod covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/chmod.md)
- Source verification: [source record](../../sources/gtfobins/chmod.md)

## Aliases

- `chmod`

## Source Verification

[source record](../../sources/gtfobins/chmod.md)

## Evidence Excerpt

```text
_body: ''
_name: chmod
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chmod
functions:
privilege-escalation:
- code: chmod 6777 /path/to/input-file
comment: This can be run with elevated privileges to change permissions (`6` denotes the SUID bits) and then read, write,
or execute a file.
```

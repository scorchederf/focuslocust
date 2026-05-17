---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# chown

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `chown` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chown` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for chown covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/chown.md)
- Source verification: [source record](../../sources/gtfobins/chown.md)

## Aliases

- `chown`

## Source Verification

[source record](../../sources/gtfobins/chown.md)

## Evidence Excerpt

```text
_body: ''
_name: chown
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chown
functions:
privilege-escalation:
- code: chown $(id -un):$(id -gn) /path/to/input-file
comment: This can be run with elevated privileges to change ownership and then read, write, or execute a file.
contexts:
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# setcap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `setcap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setcap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for setcap covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/setcap.md)
- Source verification: [source record](../../sources/gtfobins/setcap.md)

## Aliases

- `setcap`

## Source Verification

[source record](../../sources/gtfobins/setcap.md)

## Evidence Excerpt

```text
_body: ''
_name: setcap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setcap
functions:
privilege-escalation:
- code: setcap cap_setuid+ep /path/to/command
comment: This can be used to assign capabilities to executable files.
contexts:
```

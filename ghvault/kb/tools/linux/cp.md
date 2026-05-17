---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for cp covering file-read, file-write, privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/cp.md)
- Source verification: [source record](../../sources/gtfobins/cp.md)

## Aliases

- `cp`

## Source Verification

[source record](../../sources/gtfobins/cp.md)

## Evidence Excerpt

```text
_body: ''
_name: cp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cp
functions:
file-read:
- code: cp /path/to/input-file /dev/stdout
contexts:
sudo: null
```

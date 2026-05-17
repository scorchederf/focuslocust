---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# chattr

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `chattr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chattr` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for chattr covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/chattr.md)
- Source verification: [source record](../../sources/gtfobins/chattr.md)

## Aliases

- `chattr`

## Source Verification

[source record](../../sources/gtfobins/chattr.md)

## Evidence Excerpt

```text
_body: ''
_name: chattr
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chattr
functions:
privilege-escalation:
- code: chattr +i /path/to/input-file
comment: Make the target file immutable.
contexts:
```

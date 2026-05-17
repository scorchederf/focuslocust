---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# passwd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `passwd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/passwd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for passwd covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/passwd.md)
- Source verification: [source record](../../sources/gtfobins/passwd.md)

## Aliases

- `passwd`

## Source Verification

[source record](../../sources/gtfobins/passwd.md)

## Evidence Excerpt

```text
_body: ''
_name: passwd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/passwd
functions:
privilege-escalation:
- code: echo -e 'x\nx' | passwd
comment: This changes the root password to `x`, so it's now possible to log in using, for example, `su`.
contexts:
```

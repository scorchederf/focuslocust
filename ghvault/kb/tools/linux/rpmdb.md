---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rpmdb

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rpmdb` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmdb` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rpmdb covering inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rpmdb.md)
- Source verification: [source record](../../sources/gtfobins/rpmdb.md)

## Aliases

- `rpmdb`

## Source Verification

[source record](../../sources/gtfobins/rpmdb.md)

## Evidence Excerpt

```text
_body: ''
_name: rpmdb
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmdb
functions:
inherit:
- code: rpmdb --eval '%{lua:...}'
comment: This allows to run Lua code (`...`).
contexts:
```

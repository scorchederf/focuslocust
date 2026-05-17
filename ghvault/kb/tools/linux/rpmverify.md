---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rpmverify

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rpmverify` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmverify` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rpmverify covering inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rpmverify.md)
- Source verification: [source record](../../sources/gtfobins/rpmverify.md)

## Aliases

- `rpmverify`

## Source Verification

[source record](../../sources/gtfobins/rpmverify.md)

## Evidence Excerpt

```text
_body: ''
_name: rpmverify
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmverify
functions:
inherit:
- code: rpmverify --eval '%{lua:...}'
comment: This allows to run Lua code (`...`).
contexts:
```

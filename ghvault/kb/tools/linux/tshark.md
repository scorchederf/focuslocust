---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tshark

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tshark` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tshark` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tshark covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tshark.md)
- Source verification: [source record](../../sources/gtfobins/tshark.md)

## Aliases

- `tshark`

## Source Verification

[source record](../../sources/gtfobins/tshark.md)

## Evidence Excerpt

```text
_body: ''
_name: tshark
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tshark
functions:
inherit:
- code: 'echo ''...'' >/path/to/temp-file
tshark -Xlua_script:/path/to/temp-file'
comment: This allows to run Lua code (`...`).
```

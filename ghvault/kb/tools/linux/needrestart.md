---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# needrestart

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `needrestart` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/needrestart` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for needrestart covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/needrestart.md)
- Source verification: [source record](../../sources/gtfobins/needrestart.md)

## Aliases

- `needrestart`

## Source Verification

[source record](../../sources/gtfobins/needrestart.md)

## Evidence Excerpt

```text
_body: ''
_name: needrestart
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/needrestart
functions:
inherit:
- code: 'echo ''...'' >/path/to/temp-file
needrestart -c /path/to/temp-file'
comment: This allows to run Perl code (`...`).
```

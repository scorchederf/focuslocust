---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# batcat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `batcat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/batcat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for batcat covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/batcat.md)
- Source verification: [source record](../../sources/gtfobins/batcat.md)

## Aliases

- `batcat`

## Source Verification

[source record](../../sources/gtfobins/batcat.md)

## Evidence Excerpt

```text
_body: ''
_name: batcat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/batcat
functions:
inherit:
- code: batcat --paging always /etc/hosts
comment: '`--paging always` can be omitted provided that the output doesn''t fit the screen.'
contexts:
```

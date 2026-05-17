---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gimp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gimp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gimp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for gimp covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/gimp.md)
- Source verification: [source record](../../sources/gtfobins/gimp.md)

## Aliases

- `gimp`

## Source Verification

[source record](../../sources/gtfobins/gimp.md)

## Evidence Excerpt

```text
_body: ''
_name: gimp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gimp
functions:
inherit:
- code: gimp -idf --batch-interpreter=python-fu-eval -b '...'
comment: This allows to run Python code (`...`). It hangs afterwards and can be terminated by pressing `Ctrl-C`.
contexts:
```

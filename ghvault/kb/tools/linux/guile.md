---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# guile

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `guile` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/guile` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for guile covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/guile.md)
- Source verification: [source record](../../sources/gtfobins/guile.md)

## Aliases

- `guile`

## Source Verification

[source record](../../sources/gtfobins/guile.md)

## Evidence Excerpt

```text
_body: ''
_name: guile
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/guile
functions:
shell:
- code: guile -c '(system "/bin/sh")'
contexts:
sudo: null
```

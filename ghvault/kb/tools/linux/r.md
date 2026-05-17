---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# R

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `r` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/R` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for R covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/r.md)
- Source verification: [source record](../../sources/gtfobins/r.md)

## Aliases

- `R`
- `r`

## Source Verification

[source record](../../sources/gtfobins/r.md)

## Evidence Excerpt

```text
_body: ''
_name: R
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/R
functions:
shell:
- code: R --no-save -e 'system("/bin/sh")'
contexts:
sudo: null
```

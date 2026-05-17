---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dvips

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dvips` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dvips` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dvips covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dvips.md)
- Source verification: [source record](../../sources/gtfobins/dvips.md)

## Aliases

- `dvips`

## Source Verification

[source record](../../sources/gtfobins/dvips.md)

## Evidence Excerpt

````text
_body: ''
_name: dvips
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dvips
functions:
shell:
- code: dvips -R0 texput.dvi
comment: 'The `texput.dvi` output file produced by `tex` can be created offline and uploaded to the target.
```
````

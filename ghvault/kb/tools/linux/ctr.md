---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ctr

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ctr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ctr` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ctr covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ctr.md)
- Source verification: [source record](../../sources/gtfobins/ctr.md)

## Aliases

- `ctr`

## Source Verification

[source record](../../sources/gtfobins/ctr.md)

## Evidence Excerpt

````text
_body: ''
_name: ctr
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ctr
functions:
shell:
- code: ctr run --rm --mount type=bind,src=/,dst=/,options=rbind -t docker.io/library/alpine:latest x
comment: 'An image must be already present, for example:
```
````

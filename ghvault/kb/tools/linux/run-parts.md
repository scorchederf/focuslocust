---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# run-parts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `run-parts` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/run-parts` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for run-parts covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/run-parts.md)
- Source verification: [source record](../../sources/gtfobins/run-parts.md)

## Aliases

- `run-parts`

## Source Verification

[source record](../../sources/gtfobins/run-parts.md)

## Evidence Excerpt

```text
_body: ''
_name: run-parts
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/run-parts
functions:
shell:
- code: run-parts --new-session --regex '^sh$' /bin
contexts:
sudo: null
```

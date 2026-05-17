---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# slsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `slsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/slsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for slsh covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/slsh.md)
- Source verification: [source record](../../sources/gtfobins/slsh.md)

## Aliases

- `slsh`

## Source Verification

[source record](../../sources/gtfobins/slsh.md)

## Evidence Excerpt

```text
_body: ''
_name: slsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/slsh
functions:
shell:
- code: slsh -e 'system("/bin/sh")'
contexts:
sudo: null
```

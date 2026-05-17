---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# perlbug

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `perlbug` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perlbug` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for perlbug covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/perlbug.md)
- Source verification: [source record](../../sources/gtfobins/perlbug.md)

## Aliases

- `perlbug`

## Source Verification

[source record](../../sources/gtfobins/perlbug.md)

## Evidence Excerpt

```text
_body: ''
_name: perlbug
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perlbug
functions:
shell:
- code: 'perlbug -s ''x x x'' -r x -c x -e ''exec /bin/sh #'''
comment: This requires to press `Enter` serveral times before the shell is spawn.
contexts:
```

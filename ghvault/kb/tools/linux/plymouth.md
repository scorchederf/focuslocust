---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# plymouth

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `plymouth` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/plymouth` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for plymouth covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/plymouth.md)
- Source verification: [source record](../../sources/gtfobins/plymouth.md)

## Aliases

- `plymouth`

## Source Verification

[source record](../../sources/gtfobins/plymouth.md)

## Evidence Excerpt

```text
_body: ''
_name: plymouth
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/plymouth
functions:
shell:
- code: plymouth ask-for-password --prompt=x --command=/bin/sh
contexts:
sudo: null
```

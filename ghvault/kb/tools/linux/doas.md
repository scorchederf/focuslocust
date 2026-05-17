---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# doas

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `doas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/doas` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for doas covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/doas.md)
- Source verification: [source record](../../sources/gtfobins/doas.md)

## Aliases

- `doas`

## Source Verification

[source record](../../sources/gtfobins/doas.md)

## Evidence Excerpt

```text
_body: ''
_name: doas
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/doas
functions:
shell:
- code: doas -u root /bin/sh
comment: The user must be allowed to use `doas`.
contexts:
```

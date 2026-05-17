---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nsenter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nsenter` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nsenter` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for nsenter covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nsenter.md)
- Source verification: [source record](../../sources/gtfobins/nsenter.md)

## Aliases

- `nsenter`

## Source Verification

[source record](../../sources/gtfobins/nsenter.md)

## Evidence Excerpt

```text
_body: ''
_name: nsenter
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nsenter
functions:
shell:
- code: nsenter /bin/sh
comment: The shell command can be omitted.
contexts:
```

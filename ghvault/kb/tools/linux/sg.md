---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for sg covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/sg.md)
- Source verification: [source record](../../sources/gtfobins/sg.md)

## Aliases

- `sg`

## Source Verification

[source record](../../sources/gtfobins/sg.md)

## Evidence Excerpt

```text
_body: ''
_name: sg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sg
functions:
shell:
- code: sg $(id -ng)
comment: Commands can be run if the current user's group is specified, therefore no additional permissions are needed.
contexts:
```

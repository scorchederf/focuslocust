---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# setfacl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `setfacl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setfacl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for setfacl covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/setfacl.md)
- Source verification: [source record](../../sources/gtfobins/setfacl.md)

## Aliases

- `setfacl`

## Source Verification

[source record](../../sources/gtfobins/setfacl.md)

## Evidence Excerpt

```text
_body: ''
_name: setfacl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/setfacl
functions:
privilege-escalation:
- code: setfacl -m u:$(id -un):rwx /path/to/input-file
comment: This can be run with elevated privileges to change ownership and then read, write, or execute a file.
contexts:
```

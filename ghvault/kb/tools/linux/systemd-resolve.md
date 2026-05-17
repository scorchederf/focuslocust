---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# systemd-resolve

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `systemd-resolve` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/systemd-resolve` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for systemd-resolve covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/systemd-resolve.md)
- Source verification: [source record](../../sources/gtfobins/systemd-resolve.md)

## Aliases

- `systemd-resolve`

## Source Verification

[source record](../../sources/gtfobins/systemd-resolve.md)

## Evidence Excerpt

```text
_body: ''
_name: systemd-resolve
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/systemd-resolve
functions:
inherit:
- code: systemd-resolve --status
contexts:
sudo: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# busybox

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `busybox` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busybox` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for busybox covering inherit, reverse-shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/busybox.md)
- Source verification: [source record](../../sources/gtfobins/busybox.md)

## Aliases

- `busybox`

## Source Verification

[source record](../../sources/gtfobins/busybox.md)

## Evidence Excerpt

```text
_body: ''
_name: busybox
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busybox
comment: BusyBox may contain many utilities, run `busybox --list-full` to check what other binaries are supported.
functions:
inherit:
- code: busybox ash
contexts:
```

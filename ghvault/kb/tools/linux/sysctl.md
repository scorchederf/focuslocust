---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sysctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sysctl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sysctl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for sysctl covering command, file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/sysctl.md)
- Source verification: [source record](../../sources/gtfobins/sysctl.md)

## Aliases

- `sysctl`

## Source Verification

[source record](../../sources/gtfobins/sysctl.md)

## Evidence Excerpt

```text
_body: ''
_name: sysctl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sysctl
functions:
command:
- blind: true
code: sysctl 'kernel.core_pattern=|/path/to/command'
comment: 'The command is executed by `root` in the background when a core dump occurs.
```

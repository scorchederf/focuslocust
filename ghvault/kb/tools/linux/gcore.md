---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gcore

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gcore` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcore` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for gcore covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/gcore.md)
- Source verification: [source record](../../sources/gtfobins/gcore.md)

## Aliases

- `gcore`

## Source Verification

[source record](../../sources/gtfobins/gcore.md)

## Evidence Excerpt

```text
_body: ''
_name: gcore
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gcore
functions:
file-read:
- code: gcore $PID
comment: It can be used to generate core dumps of running processes (`$PID`). Such files often contains sensitive information
such as open files content, cryptographic keys, passwords, etc. This command produces a binary file named `core.$PID`,
```

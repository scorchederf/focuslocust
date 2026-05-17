---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ksshell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ksshell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ksshell` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ksshell covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ksshell.md)
- Source verification: [source record](../../sources/gtfobins/ksshell.md)

## Aliases

- `ksshell`

## Source Verification

[source record](../../sources/gtfobins/ksshell.md)

## Evidence Excerpt

```text
_body: ''
_name: ksshell
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ksshell
functions:
file-read:
- code: ksshell -i /path/to/input-file
comment: Each line is corrupted by a prefix string. Also consider that lines are actually parsed as `kickstart` scripts
thus some file contents may lead to unexpected results.
```

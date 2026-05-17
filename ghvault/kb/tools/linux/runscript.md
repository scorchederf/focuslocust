---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# runscript

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `runscript` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/runscript` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for runscript covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/runscript.md)
- Source verification: [source record](../../sources/gtfobins/runscript.md)

## Aliases

- `runscript`

## Source Verification

[source record](../../sources/gtfobins/runscript.md)

## Evidence Excerpt

```text
_body: ''
_name: runscript
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/runscript
functions:
shell:
- code: 'echo ''! exec /bin/sh'' >/path/to/temp-file
runscript /path/to/temp-file'
contexts:
```

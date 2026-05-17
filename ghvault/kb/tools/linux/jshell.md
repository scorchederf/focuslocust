---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# jshell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `jshell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jshell` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for jshell covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/jshell.md)
- Source verification: [source record](../../sources/gtfobins/jshell.md)

## Aliases

- `jshell`

## Source Verification

[source record](../../sources/gtfobins/jshell.md)

## Evidence Excerpt

```text
_body: ''
_name: jshell
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jshell
functions:
file-read:
- binary: false
code: 'jshell
jshell> /open /path/to/input-file'
```

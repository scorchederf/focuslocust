---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cobc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cobc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cobc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for cobc covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/cobc.md)
- Source verification: [source record](../../sources/gtfobins/cobc.md)

## Aliases

- `cobc`

## Source Verification

[source record](../../sources/gtfobins/cobc.md)

## Evidence Excerpt

```text
_body: ''
_name: cobc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cobc
functions:
shell:
- code: 'echo ''CALL "SYSTEM" USING "/bin/sh".'' >/path/to/temp-file
cobc -xFj --frelax-syntax-checks /path/to/temp-file'
comment: The `/path/to/temp-file` sill be overwritten after the execution.
```

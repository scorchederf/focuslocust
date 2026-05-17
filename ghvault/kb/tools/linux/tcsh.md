---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tcsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tcsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tcsh covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tcsh.md)
- Source verification: [source record](../../sources/gtfobins/tcsh.md)

## Aliases

- `tcsh`

## Source Verification

[source record](../../sources/gtfobins/tcsh.md)

## Evidence Excerpt

```text
_body: ''
_name: tcsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcsh
functions:
file-write:
- code: tcsh -c 'echo DATA >/path/to/output-file'
contexts:
sudo: null
```

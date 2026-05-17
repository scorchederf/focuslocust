---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# csh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `csh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for csh covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/csh.md)
- Source verification: [source record](../../sources/gtfobins/csh.md)

## Aliases

- `csh`

## Source Verification

[source record](../../sources/gtfobins/csh.md)

## Evidence Excerpt

```text
_body: ''
_name: csh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csh
functions:
file-write:
- code: csh -c 'echo DATA >/path/to/output-file'
contexts:
sudo: null
```

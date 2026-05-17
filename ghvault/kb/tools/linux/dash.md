---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dash

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dash` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dash` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dash covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dash.md)
- Source verification: [source record](../../sources/gtfobins/dash.md)

## Aliases

- `dash`

## Source Verification

[source record](../../sources/gtfobins/dash.md)

## Evidence Excerpt

```text
_body: ''
_name: dash
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dash
functions:
file-write:
- code: dash -c 'echo DATA >/path/to/output-file'
contexts:
sudo: null
```

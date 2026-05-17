---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ash

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ash` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ash` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ash covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ash.md)
- Source verification: [source record](../../sources/gtfobins/ash.md)

## Aliases

- `ash`

## Source Verification

[source record](../../sources/gtfobins/ash.md)

## Evidence Excerpt

```text
_body: ''
_name: ash
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ash
functions:
file-write:
- code: ash -c 'echo DATA >/path/to/output-file'
contexts:
sudo: null
```

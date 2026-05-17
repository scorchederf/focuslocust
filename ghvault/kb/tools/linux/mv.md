---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mv

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mv` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mv` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for mv covering file-write, privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/mv.md)
- Source verification: [source record](../../sources/gtfobins/mv.md)

## Aliases

- `mv`

## Source Verification

[source record](../../sources/gtfobins/mv.md)

## Evidence Excerpt

```text
_body: ''
_name: mv
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mv
functions:
file-write:
- code: 'echo DATA >/path/to/temp-file
mv /path/to/temp-file /path/to/output-file'
contexts:
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# vi

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `vi` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for vi covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/vi.md)
- Source verification: [source record](../../sources/gtfobins/vi.md)

## Aliases

- `vi`

## Source Verification

[source record](../../sources/gtfobins/vi.md)

## Evidence Excerpt

```text
_body: ''
_name: vi
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi
functions:
file-read:
- code: vi /path/to/input-file
contexts:
sudo: null
```

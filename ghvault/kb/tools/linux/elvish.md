---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# elvish

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `elvish` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/elvish` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for elvish covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/elvish.md)
- Source verification: [source record](../../sources/gtfobins/elvish.md)

## Aliases

- `elvish`

## Source Verification

[source record](../../sources/gtfobins/elvish.md)

## Evidence Excerpt

```text
_body: ''
_name: elvish
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/elvish
functions:
file-read:
- code: elvish -c 'print (slurp </path/to/input-file)'
contexts:
sudo: null
```

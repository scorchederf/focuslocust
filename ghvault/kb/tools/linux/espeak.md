---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# espeak

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `espeak` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/espeak` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for espeak covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/espeak.md)
- Source verification: [source record](../../sources/gtfobins/espeak.md)

## Aliases

- `espeak`

## Source Verification

[source record](../../sources/gtfobins/espeak.md)

## Evidence Excerpt

```text
_body: ''
_name: espeak
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/espeak
functions:
file-read:
- binary: false
code: espeak -qXf /path/to/input-file
comment: The file content appears in the middle of other textual information as phonemes.
```

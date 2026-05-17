---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# neofetch

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `neofetch` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/neofetch` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for neofetch covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/neofetch.md)
- Source verification: [source record](../../sources/gtfobins/neofetch.md)

## Aliases

- `neofetch`

## Source Verification

[source record](../../sources/gtfobins/neofetch.md)

## Evidence Excerpt

```text
_body: ''
_name: neofetch
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/neofetch
functions:
file-read:
- binary: false
code: neofetch --ascii /path/to/input-file
comment: The file content is used as the logo while some other information is displayed on its right.
```

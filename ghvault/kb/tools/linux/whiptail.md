---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# whiptail

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `whiptail` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/whiptail` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for whiptail covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/whiptail.md)
- Source verification: [source record](../../sources/gtfobins/whiptail.md)

## Aliases

- `whiptail`

## Source Verification

[source record](../../sources/gtfobins/whiptail.md)

## Evidence Excerpt

```text
_body: ''
_name: whiptail
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/whiptail
functions:
file-read:
- binary: false
code: whiptail --textbox --scrolltext /path/to/input-file 0 0
comment: The file is shown in an interactive TUI dialog made for displaying text, arrows can be used to scroll long content.
```

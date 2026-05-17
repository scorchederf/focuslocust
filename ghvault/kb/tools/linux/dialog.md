---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dialog

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dialog` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dialog` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dialog covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dialog.md)
- Source verification: [source record](../../sources/gtfobins/dialog.md)

## Aliases

- `dialog`

## Source Verification

[source record](../../sources/gtfobins/dialog.md)

## Evidence Excerpt

```text
_body: ''
_name: dialog
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dialog
functions:
file-read:
- code: dialog --textbox /path/to/input-file 0 0
comment: The file is shown in an interactive TUI dialog.
contexts:
```

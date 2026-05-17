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

## Generated Concept Page

- [dialog](../../tools/linux/dialog.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dialog |
| name | dialog |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dialog/ |

## Preserved Source Material

```yaml
_body: ''
_name: dialog
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dialog
functions:
  file-read:
  - code: dialog --textbox /path/to/input-file 0 0
    comment: The file is shown in an interactive TUI dialog.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

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

## Generated Concept Page

- [whiptail](../../tools/linux/whiptail.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | whiptail |
| name | whiptail |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/whiptail/ |

## Preserved Source Material

```yaml
_body: ''
_name: whiptail
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/whiptail
functions:
  file-read:
  - binary: false
    code: whiptail --textbox --scrolltext /path/to/input-file 0 0
    comment: The file is shown in an interactive TUI dialog made for displaying text, arrows can be used to scroll long content.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

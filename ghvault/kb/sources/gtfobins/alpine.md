---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# alpine

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `alpine` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/alpine` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [alpine](../../tools/linux/alpine.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | alpine |
| name | alpine |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/alpine/ |

## Preserved Source Material

```yaml
_body: ''
_name: alpine
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/alpine
functions:
  file-read:
  - code: alpine -F /path/to/input-file
    comment: The file is displayed in the terminal interface. Other options might be available, for example, by pressing `S`
      is possible to save the file content elsewhere.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

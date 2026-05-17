---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sg](../../tools/linux/sg.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sg |
| name | sg |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sg/ |

## Preserved Source Material

```yaml
_body: ''
_name: sg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sg
functions:
  shell:
  - code: sg $(id -ng)
    comment: Commands can be run if the current user's group is specified, therefore no additional permissions are needed.
    contexts:
      sudo:
        code: sg root
      unprivileged: null
```

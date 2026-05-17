---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zathura

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zathura` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zathura` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [zathura](../../tools/linux/zathura.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | zathura |
| name | zathura |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/zathura/ |

## Preserved Source Material

```yaml
_body: ''
_name: zathura
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zathura
comment: This requires a running X server.
functions:
  shell:
  - code: 'zathura

      :! /bin/sh -c ''exec /bin/sh 0<&1'''
    comment: The interaction happens in a GUI window, while the shell is dropped in the terminal.
    contexts:
      sudo: null
      unprivileged: null
```

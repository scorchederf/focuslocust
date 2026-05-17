---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# emacs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `emacs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/emacs` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [emacs](../../tools/linux/emacs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | emacs |
| name | emacs |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/emacs/ |

## Preserved Source Material

```yaml
_body: ''
_name: emacs
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/emacs
comment: All the functions operate in the Emacs terminal interface.
functions:
  file-read:
  - binary: false
    code: emacs /path/to/input-file
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - binary: false
    code: 'emacs /path/to/output-file

      DATA

      C-x C-s'
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: emacs -Q -nw --eval '(term "/bin/sh")'
    contexts:
      sudo: null
      unprivileged: null
```

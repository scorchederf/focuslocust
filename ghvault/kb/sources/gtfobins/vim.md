---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# vim

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `vim` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vim` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [vim](../../tools/linux/vim.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vim |
| name | vim |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/vim/ |

## Preserved Source Material

```yaml
_body: ''
_name: vim
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vim
functions:
  file-read:
  - binary: false
    code: vim -c ':redir! >/path/to/output-file | echo "DATA" | redir END | q'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  inherit:
  - code: vim -c ':py ...'
    comment: This allows to run Python code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: python
  - code: vim -c ':lua ...'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
  - code: vim
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: vi
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pandoc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pandoc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pandoc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pandoc](../../tools/linux/pandoc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pandoc |
| name | pandoc |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pandoc/ |

## Preserved Source Material

```yaml
_body: ''
_name: pandoc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pandoc
functions:
  file-read:
  - binary: false
    code: pandoc -t plain /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - binary: false
    code: echo DATA | pandoc -t plain -o /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  inherit:
  - code: 'echo ''...'' >/path/to/temp-file

      pandoc -L /path/to/temp-file /dev/null'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
```

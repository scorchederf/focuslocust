---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# opencode

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `opencode` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/opencode` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [opencode](../../tools/linux/opencode.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | opencode |
| name | opencode |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/opencode/ |

## Preserved Source Material

```yaml
_body: ''
_name: opencode
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/opencode
functions:
  command:
  - code: 'opencode

      ! /path/to/command'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  inherit:
  - code: opencode db '...'
    comment: This allows to run SQLite queries (`...`) provided that `sqlite3` is installed.
    contexts:
      sudo: null
      unprivileged: null
    from: sqlite3
```

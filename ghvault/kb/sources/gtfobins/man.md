---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# man

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `man` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/man` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [man](../../tools/linux/man.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | man |
| name | man |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/man/ |

## Preserved Source Material

```yaml
_body: ''
_name: man
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/man
functions:
  file-read:
  - code: man /path/to/input-file
    comment: The file is shown somehow formatted and displayed in the default pager.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  inherit:
  - code: man man
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: less
  shell:
  - code: 'man ''-H/bin/sh #'' man'
    comment: This requires GNU `troff` (`groff`) to be installed.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    version: GNU
```

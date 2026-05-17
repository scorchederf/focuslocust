---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ed

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ed` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ed` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ed](../../tools/linux/ed.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ed |
| name | ed |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ed/ |

## Preserved Source Material

```yaml
_body: ''
_name: ed
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ed
functions:
  file-read:
  - binary: false
    code: 'ed /path/to/input-file

      ,p

      q'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - binary: false
    code: 'ed /path/to/output-file

      a

      DATA

      .

      w

      q'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'ed

      !/bin/sh

      q'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

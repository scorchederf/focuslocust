---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ispell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ispell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ispell` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ispell](../../tools/linux/ispell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ispell |
| name | ispell |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ispell/ |

## Preserved Source Material

```yaml
_body: ''
_name: ispell
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ispell
functions:
  shell:
  - code: 'ispell /etc/hosts

      !/bin/sh'
    contexts:
      sudo: null
      suid:
        code: 'ispell /etc/hosts

          !/bin/sh -p'
        shell: false
      unprivileged: null
```

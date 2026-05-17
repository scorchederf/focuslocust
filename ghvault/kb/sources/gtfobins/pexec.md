---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pexec

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pexec` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pexec` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pexec](../../tools/linux/pexec.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pexec |
| name | pexec |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pexec/ |

## Preserved Source Material

```yaml
_body: ''
_name: pexec
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pexec
functions:
  shell:
  - code: pexec /bin/sh
    contexts:
      sudo: null
      suid:
        code: pexec /bin/sh -p
        shell: false
      unprivileged: null
```

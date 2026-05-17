---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# at

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `at` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/at` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [at](../../tools/linux/at.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | at |
| name | at |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/at/ |

## Preserved Source Material

```yaml
_body: ''
_name: at
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/at
functions:
  command:
  - blind: true
    code: echo /path/to/command | at now
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: echo "/bin/sh <$(tty) >$(tty) 2>$(tty)" | at now; tail -f /dev/null
    comment: '`tail` is used to pause the terminal.'
    contexts:
      sudo: null
      unprivileged: null
```

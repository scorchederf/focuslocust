---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# flock

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `flock` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/flock` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [flock](../../tools/linux/flock.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | flock |
| name | flock |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/flock/ |

## Preserved Source Material

```yaml
_body: ''
_name: flock
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/flock
functions:
  shell:
  - code: flock -u / /bin/sh
    contexts:
      sudo: null
      suid:
        code: flock -u / /bin/sh -p
        shell: false
      unprivileged: null
```

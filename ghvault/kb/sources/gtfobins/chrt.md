---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# chrt

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `chrt` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chrt` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [chrt](../../tools/linux/chrt.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | chrt |
| name | chrt |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/chrt/ |

## Preserved Source Material

```yaml
_body: ''
_name: chrt
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chrt
functions:
  shell:
  - code: chrt 1 /bin/sh
    comment: Any number between 1 and 99 will do.
    contexts:
      sudo: null
      suid:
        code: chrt 1 /bin/sh -p
        shell: false
      unprivileged: null
```

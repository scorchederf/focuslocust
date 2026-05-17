---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# iftop

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `iftop` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iftop` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [iftop](../../tools/linux/iftop.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iftop |
| name | iftop |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/iftop/ |

## Preserved Source Material

```yaml
_body: ''
_name: iftop
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iftop
functions:
  shell:
  - code: 'iftop

      !/bin/sh'
    comment: This requires the privilege to capture on some device (specify with `-i` if needed).
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    version: '0.17'
```

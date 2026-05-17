---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# env

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `env` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/env` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [env](../../tools/linux/env.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | env |
| name | env |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/env/ |

## Preserved Source Material

```yaml
_body: ''
_name: env
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/env
functions:
  shell:
  - code: env /bin/sh
    contexts:
      sudo: null
      suid:
        code: env /bin/sh -p
        shell: false
      unprivileged: null
```

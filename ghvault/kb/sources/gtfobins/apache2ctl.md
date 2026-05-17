---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# apache2ctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `apache2ctl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2ctl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [apache2ctl](../../tools/linux/apache2ctl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | apache2ctl |
| name | apache2ctl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/apache2ctl/ |

## Preserved Source Material

```yaml
_body: ''
_name: apache2ctl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2ctl
functions:
  file-read:
  - binary: false
    code: apache2ctl -c 'Include /path/to/input-file'
    comment: The first line only is likely leaked as an error message.
    contexts:
      sudo: null
      unprivileged: null
```

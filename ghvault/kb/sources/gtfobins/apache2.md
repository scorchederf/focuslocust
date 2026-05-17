---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# apache2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `apache2` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [apache2](../../tools/linux/apache2.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | apache2 |
| name | apache2 |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/apache2/ |

## Preserved Source Material

```yaml
_body: ''
_name: apache2
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2
functions:
  file-read:
  - binary: false
    code: apache2 -f /path/to/input-file
    comment: The first line may be leaked as an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - binary: false
    code: apache2 -C 'Define APACHE_RUN_DIR /' -C 'Include /path/to/input-file'
    comment: The first line may be leaked as an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

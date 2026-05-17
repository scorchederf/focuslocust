---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# terraform

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `terraform` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/terraform` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [terraform](../../tools/linux/terraform.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | terraform |
| name | terraform |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/terraform/ |

## Preserved Source Material

```yaml
_body: ''
_name: terraform
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/terraform
functions:
  file-read:
  - binary: false
    code: 'terraform console

      file("/path/to/input-file")'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

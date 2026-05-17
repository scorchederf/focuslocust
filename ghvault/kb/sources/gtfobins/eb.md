---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# eb

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `eb` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/eb` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [eb](../../tools/linux/eb.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | eb |
| name | eb |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/eb/ |

## Preserved Source Material

```yaml
_body: ''
_name: eb
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/eb
comment: For this to work the target must be connected to an AWS instance via EB CLI.
functions:
  inherit:
  - code: eb logs
    contexts:
      sudo: null
      unprivileged: null
    from: journalctl
```

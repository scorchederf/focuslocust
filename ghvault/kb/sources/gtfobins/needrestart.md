---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# needrestart

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `needrestart` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/needrestart` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [needrestart](../../tools/linux/needrestart.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | needrestart |
| name | needrestart |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/needrestart/ |

## Preserved Source Material

```yaml
_body: ''
_name: needrestart
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/needrestart
functions:
  inherit:
  - code: 'echo ''...'' >/path/to/temp-file

      needrestart -c /path/to/temp-file'
    comment: This allows to run Perl code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: perl
```

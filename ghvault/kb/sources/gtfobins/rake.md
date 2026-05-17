---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rake

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rake` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rake` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rake](../../tools/linux/rake.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rake |
| name | rake |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rake/ |

## Preserved Source Material

```yaml
_body: ''
_name: rake
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rake
functions:
  file-read:
  - code: rake -f /path/to/input-file
    comment: The file is actually parsed and the first wrong line is returned in an error message.
    contexts:
      sudo: null
      unprivileged: null
  inherit:
  - code: rake -p '...'
    comment: This allows to run Ruby code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: ruby
```

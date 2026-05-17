---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gem

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gem` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gem` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [gem](../../tools/linux/gem.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | gem |
| name | gem |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/gem/ |

## Preserved Source Material

```yaml
_body: ''
_name: gem
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gem
functions:
  inherit:
  - code: gem open debug
    comment: This requires the name of an installed gem to be provided, e.g., `debug` is usually installed.
    contexts:
      sudo: null
      unprivileged: null
    from: vi
  - code: gem build /path/to/script.rb
    contexts:
      sudo: null
      unprivileged: null
    from: ruby
  - code: gem install --file /path/to/script.rb
    contexts:
      sudo: null
      unprivileged: null
    from: ruby
  shell:
  - code: gem open -e '/bin/sh -s' debug
    comment: This requires the name of an installed gem to be provided, e.g., `debug` is usually installed.
    contexts:
      sudo: null
      unprivileged: null
```

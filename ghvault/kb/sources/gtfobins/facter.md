---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# facter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `facter` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/facter` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [facter](../../tools/linux/facter.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | facter |
| name | facter |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/facter/ |

## Preserved Source Material

```yaml
_body: ''
_name: facter
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/facter
functions:
  inherit:
  - code: FACTERLIB=/path/to/dir/ facter
    comment: The first `.rb` file in the `/path/to/dir/` directory will be executed.
    contexts:
      sudo: null
      unprivileged: null
    from: ruby
  - code: facter --custom-dir=/path/to/dir/ x
    comment: The first `.rb` file in the `/path/to/dir/` directory will be executed.
    contexts:
      sudo: null
      unprivileged: null
    from: ruby
```

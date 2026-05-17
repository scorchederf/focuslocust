---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# vagrant

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `vagrant` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vagrant` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [vagrant](../../tools/linux/vagrant.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vagrant |
| name | vagrant |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/vagrant/ |

## Preserved Source Material

```yaml
_body: ''
_name: vagrant
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vagrant
functions:
  inherit:
  - code: 'echo ''...'' >Vagrantfile

      vagrant up'
    comment: This allows to run Ruby code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: ruby
```

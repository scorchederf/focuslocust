---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cabal

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cabal` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cabal` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cabal](../../tools/linux/cabal.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cabal |
| name | cabal |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cabal/ |

## Preserved Source Material

```yaml
_body: ''
_name: cabal
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cabal
functions:
  shell:
  - code: cabal exec --project-file=/dev/null -- /bin/sh
    contexts:
      sudo: null
      suid:
        code: cabal exec --project-file=/dev/null -- /bin/sh -p
        shell: false
      unprivileged: null
```

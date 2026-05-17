---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nohup

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nohup` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nohup` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nohup](../../tools/linux/nohup.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nohup |
| name | nohup |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nohup/ |

## Preserved Source Material

```yaml
_body: ''
_name: nohup
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nohup
functions:
  command:
  - code: 'nohup /path/to/command

      cat nohup.out'
    comment: The `nohup.out` file contains the standard output and error of the command.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: nohup /bin/sh -c '/bin/sh </dev/tty >/dev/tty 2>/dev/tty'
    comment: This creates a `nohup.out` file in the current working directory.
    contexts:
      sudo: null
      suid:
        code: nohup /bin/sh -p -c '/bin/sh -p </dev/tty >/dev/tty 2>/dev/tty'
        shell: false
      unprivileged: null
```

